#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сайт салона маникюра «Искусство Преображения», Минск."""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://romjjjke.github.io/preobrazhenie"
PHONE = "+375 (29) 621-03-78"
PHONE_H = "+375296210378"
WA = "375296210378"
ADDRESS = "пер. Козлова, 4А, Минск"
MAPS = "https://maps.google.com/?q=%D0%BF%D0%B5%D1%80.%20%D0%9A%D0%BE%D0%B7%D0%BB%D0%BE%D0%B2%D0%B0%204%D0%90%2C%20%D0%9C%D0%B8%D0%BD%D1%81%D0%BA"

JSONLD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"NailSalon","name":"Искусство Преображения","description":"Салон маникюра в Минске: маникюр, покрытие гель-лаком, укрепление, наращивание, педикюр, дизайн","telephone":"+375296210378","url":"%s/","image":"%s/assets/img/hero.jpg","address":{"@type":"PostalAddress","streetAddress":"переулок Козлова, 4А","addressLocality":"Минск","addressCountry":"BY"},"areaServed":"Минск"}
</script>""" % (SITE, SITE)

HEAD = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}/{slug}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{slug}">
<meta property="og:image" content="{site}/assets/img/hero.jpg">
<meta name="theme-color" content="#FAF7F2">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Nunito+Sans:wght@300;400;600&display=swap" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">
{jsonld}
</head>
<body>
<a class="skip" href="#main">К содержанию</a>

<header class="head">
  <div class="wrap head-in">
    <a class="brand" href="index.html">
      <span class="brand__name">Искусство Преображения</span>
      <span class="brand__sub">салон маникюра · Минск</span>
    </a>
    <nav class="nav" aria-label="Разделы">
      <a href="#salon">Салон</a>
      <a href="#constructor">Форма и цвет</a>
      <a href="#uslugi">Услуги</a>
      <a href="#visit">Визит</a>
      <a href="#kontakty">Адрес</a>
    </nav>
    <a class="head-phone" href="tel:{phone_h}">{phone}</a>
    <button class="burger" id="burger" aria-expanded="false" aria-controls="menu" aria-label="Меню"><span></span><span></span><span></span></button>
  </div>
</header>

<div class="menu" id="menu" hidden>
  <nav class="menu__nav" aria-label="Меню">
    <a href="#salon">Салон</a>
    <a href="#constructor">Форма и цвет</a>
    <a href="#uslugi">Услуги</a>
    <a href="#visit">Визит</a>
    <a href="#kontakty">Адрес</a>
  </nav>
  <div class="menu__foot">
    <a class="btn btn--fill" href="tel:{phone_h}">{phone}</a>
    <a class="btn btn--line" href="https://wa.me/{wa}">WhatsApp</a>
    <p>{address}</p>
  </div>
</div>

<main id="main">
"""

FOOT = """
</main>

<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      <p class="foot__name">Искусство Преображения</p>
      <p class="foot__about">Салон маникюра в Минске. Маникюр, покрытие гель-лаком, укрепление и наращивание, педикюр, дизайн. Работа по записи.</p>
    </div>
    <nav class="foot__nav" aria-label="Разделы">
      <a href="#salon">Салон</a>
      <a href="#constructor">Форма и цвет</a>
      <a href="#uslugi">Услуги</a>
      <a href="#visit">Визит</a>
      <a href="#kontakty">Адрес</a>
      <a href="politika.html">Политика обработки данных</a>
    </nav>
    <div class="foot__contact">
      <a class="foot__phone" href="tel:{phone_h}">{phone}</a>
      <a href="https://wa.me/{wa}">WhatsApp</a>
      <p>{address}</p>
    </div>
  </div>
  <div class="wrap foot-bottom">
    <p>© <span id="year">2026</span> ООО «Искусство Преображения»</p>
    <p>Информация на сайте не является публичной офертой</p>
  </div>
</footer>

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

FORMS = [("oval", "Овал"), ("almond", "Миндаль"), ("square", "Квадрат"), ("stiletto", "Стилет")]
LENGTHS = [("s", "Короткая"), ("m", "Средняя"), ("l", "Длинная")]
COATS = [("nude", "Нюд"), ("milk", "Молочный"), ("pine", "Тёмная зелень"), ("french", "Френч")]


def opts(items, group, active=0):
    return "".join(
        '<button class="opt%s" type="button" data-group="%s" data-value="%s" aria-pressed="%s">%s</button>'
        % (" is-on" if i == active else "", group, v, "true" if i == active else "false", label)
        for i, (v, label) in enumerate(items))


SERVICES = [
    ("Маникюр аппаратный", "форма и кутикула без воды: кожа не размокает, покрытие ложится ровнее"),
    ("Маникюр комбинированный", "аппарат плюс классика, для чувствительной кожи и тонких ногтей"),
    ("Покрытие гель-лаком", "цвет и глянец, которые не надо подкрашивать к концу недели"),
    ("Укрепление гелем или базой", "для ногтей, которые слоятся и гнутся от любой работы"),
    ("Наращивание", "когда нужна длина и форма под вашу руку, а не «как получится»"),
    ("Педикюр", "стопы и пальцы, покрытие по желанию"),
    ("Дизайн", "тонкая линия, френч, втирка, рисунок по вашему фото"),
    ("Снятие покрытия", "аккуратно, без спиливания своей пластины"),
    ("Уход за кожей рук", "масло, крем, массаж кистей в конце визита"),
]

SERVICE_HTML = "".join(
    '<li><span class="srv__name">%s</span><span class="srv__desc">%s</span></li>' % (n, d) for n, d in SERVICES)

VISIT = [
    ("Запись", "Скажите услугу и удобное время: подтвердим и подскажем, сколько закладывать."),
    ("Форма", "Смотрим ногти и длину, обсуждаем форму и цвет. Можно прийти со своим фото."),
    ("Работа", "Одно кресло и одно время: мастер занят только вами, без прыжков между клиентами."),
    ("Уход", "Показываем, чем поддерживать дома, и записываем на следующий визит, если удобно."),
]
VISIT_HTML = "".join(
    '<li><span class="vstep__n">%02d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, t, d) for i, (t, d) in enumerate(VISIT))

INDEX_BODY = """
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero__copy">
      <p class="hero__kicker">Минск · пер. Козлова, 4А</p>
      <h1 class="hero__title">Маникюр, к которому<br>не хочется возвращаться<br><em>через три дня</em></h1>
      <p class="hero__lede">Салон маникюра «Искусство Преображения». Форма по вашей руке, ровное покрытие без пузырей и отслоек, работа строго по записи. Одно кресло, одно время: мастер занят только вами.</p>
      <div class="hero__actions">
        <a class="btn btn--fill" href="tel:PHONE">Записаться: PHONE</a>
        <a class="btn btn--line" href="https://wa.me/WA">Написать в WhatsApp</a>
      </div>
      <dl class="hero__meta">
        <div><dt>Адрес</dt><dd>пер. Козлова, 4А</dd></div>
        <div><dt>Приём</dt><dd>по записи</dd></div>
        <div><dt>Связь</dt><dd>звонок или WhatsApp</dd></div>
      </dl>
    </div>
    <figure class="hero__media">
      <img src="assets/img/hero.jpg" alt="Рабочее место в салоне: каменный стол, зелёное кресло, лампа" width="520" height="606" fetchpriority="high" decoding="async">
      <figcaption>Одно из двух рабочих мест</figcaption>
    </figure>
  </div>
</section>

<section class="sec" id="salon">
  <div class="wrap salon">
    <div class="salon__text">
      <p class="sec-num">01 / Салон</p>
      <h2 class="h2">Два места, большое окно<br>и <em>никакой суеты</em></h2>
      <p class="lede">Светлый зал на Козлова: каменные столы с вытяжкой, зелёный велюр, белый кирпич и полки с лаками. Окно выходит на улицу, поэтому света хватает даже в пасмурный день, а это важно, когда подбираешь цвет.</p>
      <p class="lede">Второе место в глубине зала: если вы не любите разговоры и хотите просто посидеть в тишине, скажите при записи, посадим там.</p>
      <ul class="salon__facts">
        <li><b>2</b><span>рабочих места</span></li>
        <li><b>1</b><span>мастер на время визита</span></li>
        <li><b>0</b><span>ожидания в очереди</span></li>
      </ul>
    </div>
    <div class="salon__pics">
      <figure class="salon__pic salon__pic--big"><img src="assets/img/station.jpg" alt="Маникюрный стол с зелёным креслом и лампой" width="520" height="606" loading="lazy" decoding="async"></figure>
      <figure class="salon__pic salon__pic--small"><img src="assets/img/room.jpg" alt="Второй зал салона: диван и проход в соседнюю комнату" width="560" height="378" loading="lazy" decoding="async"></figure>
    </div>
  </div>
</section>

<section class="sec sec--dark" id="constructor">
  <div class="wrap">
    <div class="ctor">
      <div class="ctor__view">
        <svg class="nail" viewBox="0 0 300 420" role="img" aria-labelledby="nail-t">
          <title id="nail-t">Предпросмотр формы, длины и покрытия ногтя</title>
          <defs><clipPath id="nailClip"><path id="nailClipPath" d=""></path></clipPath></defs>
          <rect class="nail__bg" x="0" y="0" width="300" height="420"></rect>
          <path class="nail__finger" d="M96 40 h108 a18 18 0 0 1 18 18 v300 a54 54 0 0 1 -108 0 v-300 a18 18 0 0 1 18 -18 z"></path>
          <path class="nail__cuticle" d="M118 92 q32 -14 64 0"></path>
          <path id="nailPath" class="nail__plate" d=""></path>
          <g clip-path="url(#nailClip)"><rect id="nailFrench" class="nail__french" x="0" y="0" width="300" height="0" opacity="0"></rect></g>
          <path id="nailShine" class="nail__shine" d="" opacity="0"></path>
        </svg>
        <p class="ctor__caption">Выбрано: <span id="ctor-caption">овал · средняя · нюд</span></p>
      </div>

      <div class="ctor__side">
        <p class="sec-num sec-num--light">02 / Форма и цвет</p>
        <h2 class="h2 h2--light">Соберите свой маникюр<br><em>до записи</em></h2>
        <p class="ctor__lede">Форма, длина и покрытие. Покажем примерно то же самое, что мастер нарисует на консультации: чтобы вы пришли не с «сделайте красиво», а с понятной картинкой в голове.</p>

        <div class="ctor__groups">
          <div class="ctor__group">
            <p class="ctor__lab">Форма</p>
            <div class="opts" role="group" aria-label="Форма ногтя">""" + opts(FORMS, "shape") + """</div>
          </div>
          <div class="ctor__group">
            <p class="ctor__lab">Длина</p>
            <div class="opts" role="group" aria-label="Длина ногтя">""" + opts(LENGTHS, "len", 1) + """</div>
          </div>
          <div class="ctor__group">
            <p class="ctor__lab">Покрытие</p>
            <div class="opts" role="group" aria-label="Покрытие">""" + opts(COATS, "coat") + """</div>
          </div>
        </div>

        <button class="btn btn--light" type="button" id="ctor-send">Записаться с этим вариантом</button>
        <p class="ctor__note">Предпросмотр условный: цвет на экране всегда чуть отличается от баночки. Точный оттенок выберем на месте по выкрасам.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="uslugi">
  <div class="wrap">
    <div class="uslugi__head">
      <div>
        <p class="sec-num">03 / Услуги</p>
        <h2 class="h2">Что делаем</h2>
      </div>
      <p class="uslugi__note">Стоимость и свободное время присылаем в WhatsApp: напишите услугу и желаемый день, ответим ценой и ближайшим окном. В прайсе на сайте смысла нет: он меняется вместе с материалами и длиной.</p>
    </div>
    <ul class="srv-list">""" + SERVICE_HTML + """</ul>
    <p class="sec-link"><a class="link" href="https://wa.me/WA">Спросить цену в WhatsApp</a></p>
  </div>
</section>

<section class="sec sec--tint" id="visit">
  <div class="wrap">
    <p class="sec-num">04 / Визит</p>
    <h2 class="h2">Как проходит час у мастера</h2>
    <ol class="vsteps">""" + VISIT_HTML + """</ol>
  </div>
</section>

<section class="sec">
  <div class="wrap two">
    <figure class="two__media"><img src="assets/img/detail.jpg" alt="Полки с лаками на стене из белого кирпича" width="560" height="404" loading="lazy" decoding="async"></figure>
    <div>
      <p class="sec-num">05 / Вопросы</p>
      <h2 class="h2">О чём спрашивают чаще всего</h2>
      <div class="faq">
        <details open><summary>Сколько держится покрытие?</summary><p>Зависит от ваших ногтей, длины и бытовых нагрузок. Если покрытие поднялось в первые дни, скажите об этом: это решается коррекцией, а не отращиванием.</p></details>
        <details><summary>Можно прийти со своим фото или идеей?</summary><p>Да, и так даже проще: покажите картинку, обсудим, что реально повторить на вашей длине и форме.</p></details>
        <details><summary>Снимаете покрытие из другого салона?</summary><p>Да. Снимаем аккуратно, без спиливания своей пластины, и сразу говорим, в каком состоянии ногти.</p></details>
        <details><summary>Нужно ли записываться заранее?</summary><p>Да, работаем по записи: так у каждого клиента своё время и мастер не отвлекается. Напишите в WhatsApp, подберём ближайшее окно.</p></details>
        <details><summary>Что делать, если опаздываю?</summary><p>Предупредите звонком или сообщением. Если опоздание большое, визит может сократиться или перенестись, чтобы не сдвинуть следующую запись.</p></details>
        <details><summary>Как вас найти?</summary><p>Переулок Козлова, 4А в Минске. Если не получается найти вход, позвоните: подскажем, куда заходить и на какой этаж подниматься.</p></details>
      </div>
    </div>
  </div>
</section>
"""

KONTAKTY = """
<section class="sec sec--dark" id="kontakty">
  <div class="wrap contact">
    <div>
      <p class="sec-num sec-num--light">06 / Адрес и запись</p>
      <h2 class="h2 h2--light">Переулок Козлова, 4А</h2>
      <p class="contact__lede">Минск. Работаем по записи, поэтому перед визитом лучше позвонить или написать: подтвердим время и подскажем, как зайти.</p>
      <dl class="facts">
        <div><dt>Телефон</dt><dd><a href="tel:PHONE">PHONE</a></dd></div>
        <div><dt>WhatsApp</dt><dd><a href="https://wa.me/WA">PHONE</a></dd></div>
        <div><dt>Адрес</dt><dd>ADDRESS</dd></div>
        <div><dt>Приём</dt><dd>по записи, без очереди</dd></div>
      </dl>
      <p class="contact__map"><a class="link link--light" href="MAPS" rel="noopener" target="_blank">Открыть адрес на карте</a></p>
    </div>
    <div class="contact__form">
      <h3 class="contact__form-title">Оставить заявку</h3>
      <form class="form" id="lead-form" novalidate>
        <div class="field"><label for="f-name">Как к вам обращаться</label><input id="f-name" name="name" type="text" autocomplete="name" aria-describedby="e-name"><span class="field__error" id="e-name"></span></div>
        <div class="field"><label for="f-phone">Телефон</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="+375" aria-describedby="e-phone"><span class="field__error" id="e-phone"></span></div>
        <div class="grid-2">
          <div class="field"><label for="f-what">Услуга</label><select id="f-what" name="what"><option>Маникюр аппаратный</option><option>Маникюр комбинированный</option><option>Покрытие гель-лаком</option><option>Укрепление</option><option>Наращивание</option><option>Педикюр</option><option>Дизайн</option><option>Снятие покрытия</option></select></div>
          <div class="field"><label for="f-when">Удобный день</label><input id="f-when" name="when" type="text" placeholder="например, суббота после 14"></div>
        </div>
        <div class="field"><label for="f-note">Комментарий</label><textarea id="f-note" name="note" rows="3" placeholder="Хочу миндаль средней длины, тёмно-зелёный"></textarea></div>
        <button class="btn btn--light" type="submit">Отправить заявку</button>
        <p class="form__note form__note--light">Нажимая «Отправить», вы соглашаетесь с <a href="politika.html">обработкой персональных данных</a>.</p>
      </form>
      <div class="form-success" id="form-success" hidden>
        <p class="form-success__title">Заявка собрана</p>
        <p>Откройте WhatsApp: сообщение уже заполнено. Или позвоните, если удобнее голосом.</p>
        <div class="form-success__actions">
          <a class="btn btn--light" id="wa-link" href="https://wa.me/WA">Открыть WhatsApp</a>
          <button class="btn btn--ghost" type="button" id="again-btn">Изменить данные</button>
        </div>
      </div>
    </div>
  </div>
</section>
"""

POL_BODY = """
<section class="sec">
  <div class="wrap legal">
    <p class="sec-num">Политика</p>
    <h1 class="h2">Обработка персональных данных</h1>
    <p>Политика описывает, какие данные получает сайт салона «Искусство Преображения», зачем они нужны и как их удалить.</p>
    <h2>Какие данные собираем</h2>
    <p>Только то, что человек указал сам: имя, телефон, услуга, удобный день и комментарий к записи. Документы и сведения о третьих лицах через сайт не запрашиваются.</p>
    <h2>Зачем они нужны</h2>
    <p>Чтобы перезвонить, подтвердить запись, назвать стоимость услуги и согласовать время визита. Для рассылок данные не используются.</p>
    <h2>Кто имеет доступ</h2>
    <p>Сотрудники салона, которые работают с записями. Данные не продаются и не передаются рекламным сетям.</p>
    <h2>Сколько храним</h2>
    <p>Пока заявка нужна для работы с обращением. По запросу данные удаляются, об удалении сообщаем ответным звонком или сообщением.</p>
    <h2>Как отозвать согласие</h2>
    <p>Позвоните по номеру PHONE или напишите в WhatsApp. Обработка прекращается в тот же день.</p>
    <h2>Файлы cookie</h2>
    <p>Рекламных трекеров на сайте нет. Браузер может сохранять технические данные для корректной работы страниц.</p>
    <h2>Изменения</h2>
    <p>Новая редакция публикуется на этой странице.</p>
    <p class="legal__meta">Редакция от 3 ноября 2026 года. Оператор: ООО «Искусство Преображения», г. Минск, пер. Козлова, 4А.</p>
  </div>
</section>
"""

PAGES = [
    dict(slug="index.html",
         title="Салон маникюра «Искусство Преображения» в Минске: маникюр, гель-лак, педикюр",
         desc="Салон маникюра в Минске на переулке Козлова, 4А: маникюр, покрытие гель-лаком, укрепление и наращивание, педикюр, дизайн. Работа по записи. Тел. +375 (29) 621-03-78.",
         body=INDEX_BODY + KONTAKTY),
    dict(slug="politika.html",
         title="Политика обработки данных: ООО «Искусство Преображения»",
         desc="Какие данные получает сайт салона, зачем они нужны, сколько хранятся и как отозвать согласие. Оператор: ООО «Искусство Преображения», Минск.",
         body=POL_BODY),
]


def build():
    for pg in PAGES:
        slug = "" if pg["slug"] == "index.html" else pg["slug"]
        doc = HEAD.format(title=pg["title"], desc=pg["desc"], site=SITE, slug=slug, jsonld=JSONLD,
                          phone=PHONE, phone_h=PHONE_H, wa=WA, address=ADDRESS, maps=MAPS)
        doc += pg["body"] + FOOT.format(phone=PHONE, phone_h=PHONE_H, wa=WA, address=ADDRESS)
        doc = (doc.replace("tel:PHONE", "tel:" + PHONE_H)
                  .replace("https://wa.me/WA", "https://wa.me/" + WA)
                  .replace('href="MAPS"', 'href="%s"' % MAPS)
                  .replace("ADDRESS", ADDRESS)
                  .replace("PHONE", PHONE))
        (ROOT / pg["slug"]).write_text(doc, encoding="utf-8")
        print("built", pg["slug"], len(doc))


if __name__ == "__main__":
    build()
