/* Ferreira e Dutra Advogados: comportamento do site. Sem dependências. */
(() => {
  const d = document, w = window;
  const rm = w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* revelações (com reserva: nada fica invisível) */
  const alvos = [...d.querySelectorAll('.rv, [data-final]')];
  if ('IntersectionObserver' in w) {
    const io = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    }), { rootMargin: '0px 0px -6% 0px' });
    alvos.forEach(el => io.observe(el));
  } else alvos.forEach(el => el.classList.add('in'));
  setTimeout(() => alvos.forEach(el => { if (el.getBoundingClientRect().top < innerHeight) el.classList.add('in'); }), 2500);

  /* mapa: desenha quando aparece */
  const mapa = d.querySelector('.mapa');
  if (mapa) {
    if ('IntersectionObserver' in w) {
      const io = new IntersectionObserver(es => { if (es[0].isIntersecting) { mapa.classList.add('ver'); io.disconnect(); } }, { threshold: .3 });
      io.observe(mapa);
    } else mapa.classList.add('ver');
  }

  /* cabeçalho sólido, botão fixo, manifesto palavra a palavra e linha dos passos: tudo num quadro só */
  const topo = d.querySelector('.top'), zap = d.querySelector('.zap');
  const manif = d.querySelector('[data-manifesto]'), palavras = manif ? [...manif.querySelectorAll('span')] : [];
  const passos = [...d.querySelectorAll('[data-passos]')].map(s => [s, s.querySelector('.passos__linha')]);
  let pendente = false, acesas = -1;
  const quadro = () => {
    pendente = false;
    const y = w.scrollY, h = innerHeight;
    topo && topo.classList.toggle('solid', y > 40);
    zap && zap.classList.toggle('ver', y > h * 0.6);
    if (manif) {
      const r = manif.getBoundingClientRect();
      const p = rm ? 1 : Math.min(1, Math.max(0, (h * .85 - r.top) / (r.height + h * .35)));
      const n = Math.round(p * palavras.length);
      if (n !== acesas) { palavras.forEach((s, i) => s.classList.toggle('on', i < n)); acesas = n; }
    }
    passos.forEach(([s, linha]) => {
      if (!linha) return;
      const r = s.getBoundingClientRect();
      const p = rm ? 1 : Math.min(1, Math.max(0, (h * .75 - r.top) / (r.height * .7)));
      linha.style.setProperty('--p', p.toFixed(3));
    });
  };
  const pedir = () => { if (!pendente) { pendente = true; requestAnimationFrame(quadro); } };
  w.addEventListener('scroll', pedir, { passive: true });
  w.addEventListener('resize', pedir, { passive: true });
  quadro();

  /* menu das áreas no computador (abre no toque também) */
  const areas = d.querySelector('.nav__areas'), bt = areas && areas.querySelector('.nav__bt');
  if (bt) {
    bt.addEventListener('click', () => { const ab = areas.classList.toggle('aberto'); bt.setAttribute('aria-expanded', ab); });
    d.addEventListener('click', ev => { if (!areas.contains(ev.target)) { areas.classList.remove('aberto'); bt.setAttribute('aria-expanded', 'false'); } });
  }

  /* menu do celular */
  const mb = d.querySelector('.menu-bt'), menu = d.getElementById('menu');
  if (mb && menu) {
    const fecha = () => { menu.classList.remove('aberto'); d.body.classList.remove('menu-aberto'); mb.setAttribute('aria-expanded', 'false'); mb.setAttribute('aria-label', 'Abrir o menu'); };
    mb.addEventListener('click', () => {
      const ab = menu.classList.toggle('aberto');
      d.body.classList.toggle('menu-aberto', ab); mb.setAttribute('aria-expanded', ab); mb.setAttribute('aria-label', ab ? 'Fechar o menu' : 'Abrir o menu');
    });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', fecha));
    d.addEventListener('keydown', ev => { if (ev.key === 'Escape') fecha(); });
  }

  /* dúvidas: uma aberta por vez */
  const itens = [...d.querySelectorAll('.faq__item')];
  itens.forEach(it => it.addEventListener('toggle', () => { if (it.open) itens.forEach(o => { if (o !== it) o.open = false; }); }));
})();
