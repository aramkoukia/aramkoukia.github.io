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

  /* Skip the hero animation for people who prefer reduced motion */
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.hero-graph animate, .hero-graph animateMotion').forEach(function (n) { n.remove(); });
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

  /* Filter the post index */
  var f = document.getElementById('filter');
  if (f) {
    var items = [].slice.call(document.querySelectorAll('.entry'));
    var years = [].slice.call(document.querySelectorAll('.year'));
    var empty = document.getElementById('empty');
    f.addEventListener('input', function () {
      var q = f.value.trim().toLowerCase();
      var shown = 0;
      items.forEach(function (it) {
        var match = !q || it.dataset.search.indexOf(q) > -1;
        it.hidden = !match;
        if (match) shown++;
      });
      years.forEach(function (y) { y.hidden = !y.querySelector('.entry:not([hidden])'); });
      if (empty) {
        empty.hidden = shown > 0;
        var s = empty.querySelector('span');
        if (s) s.textContent = f.value;
      }
    });
  }
})();
