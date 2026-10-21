(function () {
  var root = document.documentElement;

  /* Theme toggle */
  var btn = document.querySelector('.theme-toggle');
  function label() {
    if (btn) btn.setAttribute('aria-label', root.dataset.theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
  }
  label();
  if (btn) btn.addEventListener('click', function () {
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
    label();
  });

  /* Hairline under the sticky header once the page scrolls */
  var header = document.querySelector('.site-header');
  if (header) {
    var edge = function () { header.classList.toggle('scrolled', scrollY > 8); };
    addEventListener('scroll', edge, { passive: true });
    edge();
  }

  /* Reading progress */
  var bar = document.getElementById('progress');
  if (bar) {
    var tick = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, h.scrollTop / max) : 0) + ')';
    };
    addEventListener('scroll', tick, { passive: true });
    tick();
  }

  /* Table of contents */
  var body = document.querySelector('.post-body');
  var toc = document.getElementById('toc');
  if (body && toc) {
    var heads = [].slice.call(body.querySelectorAll('h2[id], h3[id]'));
    if (heads.length >= 3) {
      var list = document.createElement('ol');
      var links = {};
      heads.forEach(function (h) {
        var li = document.createElement('li');
        if (h.tagName === 'H3') li.className = 'sub';
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        list.appendChild(li);
        links[h.id] = a;
      });
      var title = document.createElement('p');
      title.className = 'toc-title';
      title.textContent = 'On this page';
      toc.appendChild(title);
      toc.appendChild(list);
      toc.hidden = false;
      if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (e) {
            if (!e.isIntersecting) return;
            Object.keys(links).forEach(function (k) { links[k].removeAttribute('aria-current'); });
            links[e.target.id].setAttribute('aria-current', 'true');
          });
        }, { rootMargin: '0px 0px -70% 0px' });
        heads.forEach(function (h) { io.observe(h); });
      }
    }
  }

  /* Copy buttons on code blocks */
  document.querySelectorAll('.prose pre').forEach(function (pre) {
    var wrap = document.createElement('div');
    wrap.className = 'code-block';
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'copy';
    b.textContent = 'Copy';
    b.addEventListener('click', function () {
      var done = function (msg) { b.textContent = msg; setTimeout(function () { b.textContent = 'Copy'; }, 1600); };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(pre.innerText).then(function () { done('Copied'); }, function () { done('Copy failed'); });
      } else {
        done('Copy failed');
      }
    });
    wrap.appendChild(b);
  });

  /* Collapse every year except the most recent one */
  var yearList = document.querySelector('.years');
  [].slice.call(document.querySelectorAll('.year')).forEach(function (y, n) {
    var b = y.querySelector('.year-toggle');
    if (!b) return;
    var set = function (open) { y.classList.toggle('collapsed', !open); b.setAttribute('aria-expanded', String(open)); };
    set(n === 0);
    b.addEventListener('click', function () {
      if (yearList && yearList.classList.contains('filtering')) return;
      set(y.classList.contains('collapsed'));
    });
  });

  /* Filter the post index by text and topic */
  var f = document.getElementById('filter');
  if (f) {
    var items = [].slice.call(document.querySelectorAll('.entry'));
    var years = [].slice.call(document.querySelectorAll('.year'));
    var empty = document.getElementById('empty');
    var chips = [].slice.call(document.querySelectorAll('.tag-filter .tag'));
    var tag = new URLSearchParams(location.search).get('tag') || '';
    if (tag && !chips.some(function (c) { return c.dataset.tag === tag; })) tag = '';

    var apply = function () {
      var q = f.value.trim().toLowerCase();
      var shown = 0;
      items.forEach(function (it) {
        var match = (!q || it.dataset.search.indexOf(q) > -1) &&
          (!tag || (' ' + it.dataset.tags + ' ').indexOf(' ' + tag + ' ') > -1);
        it.hidden = !match;
        if (match) shown++;
      });
      years.forEach(function (y) { y.hidden = !y.querySelector('.entry:not([hidden])'); });
      if (yearList) yearList.classList.toggle('filtering', !!(q || tag));
      chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c.dataset.tag === tag)); });
      if (empty) {
        empty.hidden = shown > 0;
        var s = empty.querySelector('span');
        if (s) s.textContent = q || (chips.filter(function (c) { return c.dataset.tag === tag; })[0] || {}).textContent || '';
      }
    };

    f.addEventListener('input', apply);
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        tag = c.dataset.tag === tag ? '' : c.dataset.tag;
        var url = new URL(location.href);
        if (tag) url.searchParams.set('tag', tag); else url.searchParams.delete('tag');
        history.replaceState(null, '', url);
        apply();
      });
    });
    if (tag) apply();
  }
})();
