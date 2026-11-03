/* «Искусство Преображения»: меню, конструктор маникюра, заявка */

document.addEventListener('DOMContentLoaded', function () {
  initMenu();
  initNail();
  initForm();
  initYear();
});

function initMenu() {
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');
  if (!burger || !menu) return;

  function close() {
    menu.hidden = true;
    burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  burger.addEventListener('click', function () {
    var open = menu.hidden;
    menu.hidden = !open;
    burger.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) menu.querySelector('a').focus();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !menu.hidden) { close(); burger.focus(); }
  });

  menu.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') close();
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth > 1080 && !menu.hidden) close();
  });
}

/* Конструктор: форма, длина и покрытие ногтя */
function initNail() {
  var path = document.getElementById('nailPath');
  if (!path) return;

  var clip = document.getElementById('nailClipPath');
  var french = document.getElementById('nailFrench');
  var shine = document.getElementById('nailShine');
  var caption = document.getElementById('ctor-caption');
  var send = document.getElementById('ctor-send');

  var X0 = 118, X1 = 182, CX = 150, TOP = 78;
  var LEN = { s: 54, m: 76, l: 98 };
  var FILL = { nude: '#E3C9B8', milk: '#F2E9DE', pine: '#2C4A3A', french: '#F2E9DE' };

  var state = { shape: 'oval', len: 'm', coat: 'nude' };

  function geometry(shape, len) {
    var tip = TOP + len, mid = TOP + len * 0.5;
    if (shape === 'square') {
      return 'M' + X0 + ' ' + TOP + ' H' + X1 + ' V' + (tip - 10) + ' Q' + X1 + ' ' + tip + ' ' + (X1 - 10) + ' ' + tip +
             ' H' + (X0 + 10) + ' Q' + X0 + ' ' + tip + ' ' + X0 + ' ' + (tip - 10) + ' Z';
    }
    if (shape === 'oval') {
      return 'M' + X0 + ' ' + TOP + ' H' + X1 + ' V' + mid +
             ' C' + X1 + ' ' + (tip - len * 0.1) + ' 170 ' + tip + ' ' + CX + ' ' + tip +
             ' C130 ' + tip + ' ' + X0 + ' ' + (tip - len * 0.1) + ' ' + X0 + ' ' + mid + ' Z';
    }
    if (shape === 'almond') {
      return 'M' + X0 + ' ' + TOP + ' H' + X1 + ' V' + (TOP + len * 0.42) +
             ' C' + X1 + ' ' + (TOP + len * 0.78) + ' 164 ' + (tip - 8) + ' ' + CX + ' ' + tip +
             ' C136 ' + (tip - 8) + ' ' + X0 + ' ' + (TOP + len * 0.78) + ' ' + X0 + ' ' + (TOP + len * 0.42) + ' Z';
    }
    /* stiletto */
    return 'M' + X0 + ' ' + TOP + ' H' + X1 + ' V' + (TOP + len * 0.3) +
           ' C' + X1 + ' ' + (TOP + len * 0.6) + ' 157 ' + (tip - 6) + ' ' + CX + ' ' + tip +
           ' C143 ' + (tip - 6) + ' ' + X0 + ' ' + (TOP + len * 0.6) + ' ' + X0 + ' ' + (TOP + len * 0.3) + ' Z';
  }

  function label(group, value) {
    var el = document.querySelector('.opt[data-group="' + group + '"][data-value="' + value + '"]');
    return el ? el.textContent.trim() : value;
  }

  function render() {
    var len = LEN[state.len];
    var d = geometry(state.shape, len);
    var tip = TOP + len;

    path.setAttribute('d', d);
    if (clip) clip.setAttribute('d', d);

    path.style.fill = FILL[state.coat] || FILL.nude;

    if (state.coat === 'french') {
      french.setAttribute('opacity', '1');
      french.setAttribute('y', String(tip - len * 0.26));
      french.setAttribute('height', String(len * 0.26 + 4));
    } else {
      french.setAttribute('opacity', '0');
    }

    if (shine) {
      shine.setAttribute('d', 'M132 ' + (TOP + len * 0.3) + ' Q128 ' + (TOP + len * 0.6) + ' 140 ' + (TOP + len * 0.78));
      shine.style.strokeWidth = len > 80 ? '10' : '8';
    }

    var text = label('shape', state.shape).toLowerCase() + ' · ' +
               label('len', state.len).toLowerCase() + ' · ' +
               label('coat', state.coat).toLowerCase();
    if (caption) caption.textContent = text;

    return text;
  }

  document.querySelectorAll('.opt').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var group = btn.getAttribute('data-group');
      var value = btn.getAttribute('data-value');

      document.querySelectorAll('.opt[data-group="' + group + '"]').forEach(function (b) {
        var on = b === btn;
        b.classList.toggle('is-on', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
      });

      if (group === 'shape') state.shape = value;
      if (group === 'len') state.len = value;
      if (group === 'coat') state.coat = value;

      render();
    });
  });

  if (send) {
    send.addEventListener('click', function () {
      var text = render();
      var note = document.getElementById('f-note');
      if (note) note.value = 'Хочу: ' + text + '.';
      var form = document.getElementById('lead-form');
      var target = form && !form.hidden ? form : document.getElementById('kontakty');
      if (target) target.scrollIntoView({ block: 'center', behavior: 'smooth' });
      var name = document.getElementById('f-name');
      if (name) setTimeout(function () { name.focus(); }, 450);
    });
  }

  render();
}

function initForm() {
  var form = document.getElementById('lead-form');
  if (!form) return;

  var success = document.getElementById('form-success');
  var waLink = document.getElementById('wa-link');
  var again = document.getElementById('again-btn');
  var nameInput = form.querySelector('[name="name"]');
  var phoneInput = form.querySelector('[name="phone"]');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = true;

    [nameInput, phoneInput].forEach(function (el) {
      var err = document.getElementById('e-' + el.name);
      var valid = el === nameInput ? el.value.trim().length > 1 : digits(el.value).length >= 9;
      el.setAttribute('aria-invalid', valid ? 'false' : 'true');
      if (err) err.textContent = valid ? '' : (el === nameInput ? 'Как к вам обращаться?' : 'Нужен номер для связи');
      if (!valid) ok = false;
    });

    if (!ok) {
      var bad = form.querySelector('[aria-invalid="true"]');
      if (bad) bad.focus();
      return;
    }

    var d = new FormData(form);
    var lines = ['Заявка с сайта: салон маникюра', 'Имя: ' + (d.get('name') || '').trim(), 'Телефон: ' + (d.get('phone') || '').trim()];
    if (d.get('what')) lines.push('Услуга: ' + d.get('what'));
    if (d.get('when')) lines.push('Удобный день: ' + d.get('when').trim());
    if (d.get('note')) lines.push('Комментарий: ' + d.get('note').trim());

    waLink.href = 'https://wa.me/375296210378?text=' + encodeURIComponent(lines.join('\n'));
    form.hidden = true;
    success.hidden = false;
    success.scrollIntoView({ block: 'center', behavior: 'smooth' });
  });

  if (again) {
    again.addEventListener('click', function () {
      success.hidden = true;
      form.hidden = false;
      nameInput.focus();
    });
  }

  function digits(v) { return (v || '').replace(/\D/g, ''); }
}

function initYear() {
  var y = document.getElementById('year');
  if (y) y.textContent = String(new Date().getFullYear());
}
