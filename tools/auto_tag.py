#!/usr/bin/env python3
"""
Add `tags:` to posts in _posts/ based on keywords in the title, description and body.

Usage:
    python3 tools/auto_tag.py            # tag posts that have no tags yet
    python3 tools/auto_tag.py --force    # re-tag every post
    python3 tools/auto_tag.py --dry-run  # print what would change

Posts that already have a `tags:` line are left alone unless --force is passed,
so hand-edited tags are safe (--force overwrites them). Edit TAGS below to change the categories.
"""
import re
import sys
from pathlib import Path

# Tag -> keywords. Matched case-insensitively on word boundaries.
TAGS = {
    "Leadership": [
        "leadership", "leader", "leaders", "engineering manager", "engineering managers",
        "mentor", "mentoring", "teams", "team's", "hire", "hiring", "culture", "1:1", "one-on-one",
        "star players", "fulfillment", "sdm", "velocity", "greatness", "taste",
    ],
    "Product & Agile": [
        "agile", "lean", "scrum", "estimation", "product development", "roadmap",
        "product", "products", "backlog", "sprint", "project funding", "budgeting",
        "anti-patterns", "build less", "mcnamara",
    ],
    "Architecture": [
        "architecture", "microservices", "microservice", "distributed", "design pattern",
        "designpattern", "cache-aside", "caching", "event sourcing", "cqrs", "soa",
        "scalable", "scalability", "sre", "reliability", "aop", "interceptor", "single sign-on",
    ],
    "AI": [
        "ai", "generative", "llm", "llms", "machine learning", "agent", "agents",
        "chatbot", "chatbots", "bot framework", "cortana",
    ],
    "Azure": [
        "azure", "cosmos", "cosmosdb", "documentdb", "application insights", "webjobs",
        "logic app", "service fabric", "arm templates", "vsts", "azure devops", "aks",
    ],
    "AWS": [
        "aws", "amazon sqs", "amazon sns", "s3", "ec2", "lambda", "api gateway", "opensearch",
    ],
    ".NET": [
        ".net", "net core", "c#", "asp.net", "aspnet", "entity framework", "dapper",
        "visual studio", "f#", "giraffe", "blazor", "wcf", "postsharp", "unity",
        "xamarin", "uwp", "quartz.net", "string interpolation", "nameof",
    ],
    "JavaScript": [
        "javascript", "js", "node", "nodejs", "node.js", "angular", "angular2", "react",
        "vue", "vuejs", "jquery", "es6", "typescript", "web components", "css", "domparser",
        "express",
    ],
    "Data": [
        "sql", "t-sql", "tsql", "database", "databases", "nosql", "redis", "power bi",
        "kusto", "data store", "opensearch", "scrapy", "dataannotations",
    ],
    "Containers": [
        "docker", "kubernetes", "container", "containers", "swarm", "service fabric", "aks",
        "dev spaces",
    ],
    "Career": ["career", "books", "what to read", "top paying", "stay curious"],
    "Python": ["python", "scrapy", "django", "flask"],
    "Git": ["git", "gitignore", "commit", "commits", "branch"],
    "Blockchain": [
        "blockchain", "ethereum", "smart contract", "smart contracts", "bitcoin", "crypto",
        "cryptocurrency", "iota",
    ],
    "Personal": [
        "iran", "revolution", "niece", "christmas", "grouse mountain", "goal in life",
        "paradoxes", "hey, i'm aram", "oh hey", "income tax", "remote jobs",
    ],
}

MAX_TAGS = 3
HEAD_WEIGHT = 4   # a keyword in the title, slug or description
BODY_WEIGHT = 1   # each keyword hit in the body (capped per keyword)
BODY_CAP = 3
BODY_THRESHOLD = 6  # body-only score needed when the title/description doesn't match


def patterns():
    out = {}
    for tag, words in TAGS.items():
        out[tag] = [re.compile(r"(?<![\w.])" + re.escape(w) + r"(?![\w])", re.I) for w in words]
    return out


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else (None, text)


def field(front, name):
    m = re.search(r"^" + name + r":\s*(.*)$", front, re.M)
    return m.group(1).strip().strip('"') if m else ""


def score(head, body, pats):
    body = re.sub(r"```.*?```", " ", body, flags=re.S)       # skip code blocks
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)|https?://\S+", " ", body)  # skip images and URLs
    scores = {}
    for tag, regs in pats.items():
        h = sum(HEAD_WEIGHT for r in regs if r.search(head))
        b = sum(min(len(r.findall(body)), BODY_CAP) * BODY_WEIGHT for r in regs)
        if h or b >= BODY_THRESHOLD:
            scores[tag] = h + b
    return [t for t, _ in sorted(scores.items(), key=lambda kv: -kv[1])][:MAX_TAGS]


def main():
    force = "--force" in sys.argv
    dry = "--dry-run" in sys.argv
    root = Path(__file__).resolve().parent.parent / "_posts"
    pats = patterns()
    untagged = []
    for path in sorted(root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        front, body = split_front_matter(text)
        if front is None:
            continue
        has_tags = re.search(r"^tags:", front, re.M)
        if has_tags and not force:
            continue
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem).replace("-", " ")
        head = " ".join([field(front, "title"), field(front, "description"), slug])
        tags = score(head, body, pats)
        if not tags:
            untagged.append(path.name)
            continue
        line = "tags: [" + ", ".join('"%s"' % t for t in tags) + "]"
        front = re.sub(r"^tags:.*\n?", "", front, flags=re.M).rstrip("\n")
        new = "---\n" + front + "\n" + line + "\n---\n" + body
        print("%-70s %s" % (path.name[:70], ", ".join(tags)))
        if not dry:
            path.write_text(new, encoding="utf-8")
    if untagged:
        print("\nNo tag matched (add one by hand):")
        for n in untagged:
            print("  " + n)


if __name__ == "__main__":
    main()
