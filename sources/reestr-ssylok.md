# Реестр ссылок на источники

Одна строка — один документ. Реестр отвечает на три вопроса: **где документ
открывается**, **может ли его прочитать Claude или агент** и **какие темы на нём
стоят**. По нему видно, что ещё надо найти и что пользователь должен открыть сам.

Решение пользователя 15.10.2026: новые PDF в GitHub не загружаются. Репозиторий
хранит ссылки и сведения о документах, а не сами документы: источники обновляются,
а файлы в Git остаются навсегда. Файлы, уже лежащие в `sources/`, остаются (удаление
не освобождает место в истории). Копии документов пользователь хранит у себя; если
документ закрыт для агента, пользователь открывает его сам и присылает в чат цитату,
снимок страницы или разовый файл — в репозиторий такой файл не коммитится.

## Как пользоваться

- **Перед поиском источника** — найти документ здесь. Если строка есть и доступ
  «открыт», читать по рабочей ссылке; если «закрыт» — не тратить время на обходы,
  а сразу ставить задачу пользователю (`sources/skachat-vruchnuyu.md`, со ссылкой на код).
- **После проверки темы на источники** — добавить новые документы, обновить дату
  проверки, доступ и колонку «Темы». Новые строки добавляются в конец своей группы;
  коды не переиспользуются.
- **Колонка «Чего не хватает»** — то, что нельзя было проверить: приложение не
  открылось, год не установлен, нужна сверка по официальному файлу. По ней строится
  список задач пользователю.

Ведут реестр источниковед (`.claude/agents/istochnikoved.md`) и основная сессия.
Связанные файлы: `sources/README-inventory.md` — подробные карточки файлов, уже
лежащих в `sources/`; `sources/skachat-vruchnuyu.md` — очередь задач пользователю.

## Обозначения

**Доступ для агента** (WebFetch и шелл из рабочей среды):

- **открыт** — полный текст читается напрямую;
- **частично** — текст обрывается, нет приложений или таблиц, либо страница
  отдаёт только пересказ;
- **закрыт** — капча, отказ в доступе, скриптовая страница или блокировка
  сети; нужен пользователь.

**Где сверено:** `sources/…` — файл в репозитории; «файл пользователя» — пользователь
прислал в чат, в репозиторий не положен; «онлайн-копия» — сверено по зеркалу из
колонки «Рабочая ссылка»; «Google Диск» — папка пользователя «Источники гигиена беременности»
(ID `12xqpIS-KBjibp8YrECL0d8ublx1aCnCP`): только чтение через коннектор Google Drive, файлы в репозиторий
не копируются; в скобках — имя файла на Диске, если оно отличается от названия документа. Перечень файлов
папки на 15.10.2026 — `editorial/reports/istochniki-2026-10-15-google-disk.md`.

**Статус редакции:** «действует», «пересмотр истёк» (срок «не позднее» прошёл —
утверждения из документа получают `QUALIFIED`), «заменён» (указать чем).

---

## А. Российские клинические рекомендации

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | КР «Нормальная беременность», РОАГ, 2023, ред. 15.02.2024, ID 288 (288_2) | пересмотр истёк (не позднее 2025) | https://cr.minzdrav.gov.ru — карточка 288_2 | https://congress-med.ru/assets/files/2024/2024-normalnaya-beremennost.pdf | закрыт (с 15.10.2026; 14.10.2026 открывался) | `sources/russian-guidelines/normalnaya-beremennost.pdf`; файл пользователя 15.10.2026 — совпадает; Google Диск — 2 копии («Нормальная беременность. Клин. рек-и.», «2024-normalnaya-beremennost») | 1–11 | 15.10.2026 | — |
| R-002 | КР «Преэклампсия. Эклампсия. Отеки, протеинурия и гипертензивные расстройства…», РОАГ, 2024, ID 637 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — ID 637 | https://base.garant.ru/409626439/ | частично (обрыв на 2.5, без приложений) | `sources/russian-guidelines/preeklampsiya-2024.pdf` (официальный, 74 с.); Google Диск — 2 одинаковые копии («Преэклампсия», «Преэклампсия. Эклампсия») | 8, 11; сверка 1, 7 | 15.10.2026 | — |
| R-003 | КР «Венозные осложнения во время беременности и послеродовом периоде. Акушерская тромбоэмболия», 2025 | действует; поле «пересмотр» на титуле нет | https://roag-portal.ru/recommendations_obstetrics | — | закрыт (портал РОАГ) | `sources/russian-guidelines/venoznye-oslozhneniya-akusherskaya-tromboemboliya.pdf`; файл пользователя 15.10.2026 — идентичен; Google Диск | 2, 11 | 15.10.2026 | прямой адрес файла на портале |
| R-004 | КР «Признаки внутриутробной гипоксии плода, требующие предоставления медицинской помощи матери», 2023, ID 774 | пересмотр истёк (не позднее 2025) | https://cr.minzdrav.gov.ru — ID 774 | https://base.garant.ru/407548979/ | частично (разделы 1–2.4 читаются) | онлайн-копия; Google Диск — полный текст с Приложением В (о шевелениях в нём ничего нет, только о КТГ) | 11 | 15.10.2026 | — |
| R-005 | КР «Чрезмерная рвота беременных», 2024, ID 802 (802_1) | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — ID 802 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/304617; Прил. В — https://base.garant.ru/410598052/7dede6ac8f25be619ed07c17ed1c62c9/ | частично | онлайн-копии; Google Диск — Прил. В сверено | 1, 11 | 15.10.2026 | на титуле файла нет ID и срока пересмотра; страниц в выгрузке нет |
| R-006 | КР «Преждевременная отслойка плаценты», 2024, ID 800 | действует (пересмотр не позднее 2026) | https://cr.minzdrav.gov.ru — ID 800 | https://base.garant.ru/410576556/c9c989f1e999992b41b30686f0032f7d/; https://pravo.ppt.ru/klinicheskie-rekomendatsii/304478 | частично | онлайн-копии; Google Диск — титул и Прил. В | 11 | 15.10.2026 | страниц в выгрузке нет |
| R-007 | КР «Преждевременные роды», 2024, ID 331 | действует (пересмотр не позднее 2026) | https://cr.minzdrav.gov.ru — ID 331 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/303408 | частично (нет Прил. В) | онлайн-копия; Google Диск — Прил. В | 9, 11 | 15.10.2026 | — |
| R-008 | КР «Выкидыш (самопроизвольный аборт)», 2024, ID 670 (670_2) | действует (пересмотр не позднее 2026) | https://cr.minzdrav.gov.ru — ID 670 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/300215 (без приложений) | частично | Google Диск — Прил. В | 11 (реестр, строка 46; в списке источников нет) | 15.10.2026 | — |
| R-009 | КР «Роды одноплодные, родоразрешение путём кесарева сечения», 2024, ID 639 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — ID 639 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/302238 | частично | `sources/russian-guidelines/rody-kesarevo-sechenie-2024.pdf`; Google Диск | 10 | 14.10.2026 | — |
| R-010 | КР «Инфекция мочевых путей при беременности», ID 719 | на Диске — редакция 2025 (РОАГ, РОУ; ID на титуле не указан); Темы 7 и 9 сверены по прежней (ID 719) | https://cr.minzdrav.gov.ru — ID 719 | — | закрыт | файл пользователя 09.10.2026; Google Диск — редакция 2025 | 7, 9 | 15.10.2026 | сверить 7.15 и 9.15 с редакцией 2025 |
| R-011 | КР «Привычный выкидыш», ID 721 (ред. 2022); на Диске — ред. 2025 | ред. 2022 — пересмотр истёк; на Диске — ред. 2025 (файл от 28.03.2025, ID на титуле не указан) | https://cr.minzdrav.gov.ru — ID 721 | — | закрыт | файл пользователя 09.10.2026; Google Диск — ред. 2025 | 7 | 15.10.2026 | сверить 7.16 с редакцией 2025 |
| R-012 | КР «Депрессивный эпизод, рекуррентное депрессивное расстройство», 2024, ID 301_3 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — 301_3 | — | закрыт | `sources/russian-guidelines/kr-depressivnyj-epizod-rdr-2024.txt` (выгрузка пользователя) | 10 | 14.10.2026 | — |
| R-013 | КР «Генерализованное тревожное расстройство», 2024, ID 457_3 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — 457_3 | — | закрыт | `sources/russian-guidelines/kr-generalizovannoe-trevozhnoe-rasstrojstvo-2024.txt` | 10 | 09.10.2026 | — |
| R-014 | КР «Тревожно-фобические расстройства», 2024, ID 455_3 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — 455_3 | — | закрыт | `sources/russian-guidelines/kr-trevozhno-fobicheskie-rasstrojstva-2024.txt` | 10 | 09.10.2026 | — |
| R-015 | КР «Обсессивно-компульсивное расстройство», 2025, ID 650_2 | действует (пересмотр 2027) | https://cr.minzdrav.gov.ru — 650_2 | — | закрыт | `sources/russian-guidelines/kr-obsessivno-kompulsivnoe-rasstrojstvo.txt` | 10 | 09.10.2026 | — |
| R-016 | КР «Роды одноплодные, самопроизвольное родоразрешение в затылочном предлежании (нормальные роды)», 2024, ID 636 (636_2) | действует (пересмотр не позднее 2026); заменила ред. 2021 | https://cr.minzdrav.gov.ru — ID 636 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/251870 (ред. 2021) | частично | Google Диск — ред. 2024 | 7 | 15.10.2026 | 7.15 сверялась по ред. 2021 (запись 15 `skachat-vruchnuyu.md`) — сверить с ред. 2024 |
| R-017 | КР «Инфекции амниотической полости и плодных оболочек (хориоамнионит)», 2023, ID 776 | пересмотр истёк (не позднее 2025) | https://cr.minzdrav.gov.ru — ID 776 | — (открытой копии не найдено) | закрыт | Google Диск | 9, 11 | 15.10.2026 | — |
| R-018 | КР «Патологическое прикрепление плаценты (предлежание и врастание плаценты)», 2023, ID 767 | пересмотр истёк (не позднее 2025) | https://cr.minzdrav.gov.ru — ID 767 | https://www.consultant.ru/document/cons_doc_LAW_447855/ (карточка) | частично | Google Диск — определение предлежания сверено | 8 | 15.10.2026 | — |
| R-019 | КР «Гестационный сахарный диабет», 2024, РАЭ и РОАГ | действует | https://cr.minzdrav.gov.ru | — | не проверялся | Google Диск | кандидат: 1, 3, 11 | 15.10.2026 | ID на титуле не указан |
| R-020 | КР «Внутрипечёночный холестаз при беременности», 2024, ID 289 | действует (пересмотр не позднее 2026) | https://cr.minzdrav.gov.ru — ID 289 | — | не проверялся | Google Диск | кандидат: 5 (зуд), 11 | 15.10.2026 | — |
| R-021 | КР «Многоплодная беременность», 2024, ID 638 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — ID 638 | — | не проверялся | Google Диск | кандидат: оговорки о двойне в любой теме | 15.10.2026 | — |
| R-022 | КР «Истмико-цервикальная недостаточность», 2024, ID 671 | действует | https://cr.minzdrav.gov.ru — ID 671 | — | не проверялся | Google Диск («Истимико-цервикальная…») | кандидат: 3, 4 | 15.10.2026 | — |
| R-023 | КР «Тазовое предлежание плода», 2024, ID 626 | действует (пересмотр не позднее 2026) | https://cr.minzdrav.gov.ru — ID 626 | — | не проверялся | Google Диск | кандидат: 3 | 15.10.2026 | — |
| R-024 | КР «Резус-изоиммунизация. Гемолитическая болезнь плода», 2024 | действует | https://cr.minzdrav.gov.ru | — | не проверялся | Google Диск | кандидат: ориентационный раздел | 15.10.2026 | ID на титуле не указан |
| R-025 | КР «Аномалии объёма амниотической жидкости», 2024 | действует | https://cr.minzdrav.gov.ru | — | не проверялся | Google Диск | кандидат: 11 | 15.10.2026 | ID на титуле не указан |
| R-026 | КР «Недостаточный рост плода, требующий предоставления медицинской помощи матери (задержка роста плода)», 2025, ID 722 (722_2) | действует (пересмотр не позднее 2027) | https://cr.minzdrav.gov.ru — ID 722 | — | не проверялся | Google Диск | кандидат: 11 (11.2) | 15.10.2026 | — |
| R-027 | КР «Послеоперационный рубец на матке…», 2024, ID 635 | действует | https://cr.minzdrav.gov.ru — ID 635 | — | не проверялся | Google Диск | кандидат: ориентационный раздел | 15.10.2026 | полное название — по титулу |
| R-048 | КР «Воспалительные заболевания челюстей. Одонтогенный остеомиелит челюсти», 2026, ID 1049_1 | действует (пересмотр не позднее 2028) | https://cr.minzdrav.gov.ru — ID 1049 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/341391 | частично | Google Диск | 6 | 15.10.2026 | — |
| R-049 | КР «Кариес зубов» (взрослые), 2025, ID 1021_1 | действует (пересмотр не позднее 2027) | https://cr.minzdrav.gov.ru — ID 1021 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/324363 | частично | Google Диск («Кариес зубов»). Файл «Клинические_рекомендации_Кариес_зубов» (2 с.) — НЕ текст КР, не использовать | 6 | 15.10.2026 | — |
| R-050 | КР «Острые респираторные вирусные инфекции (ОРВИ) у взрослых», 2025, ID 724_2 | действует (пересмотр не позднее 2027) | https://cr.minzdrav.gov.ru — ID 724 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/316824 | частично | Google Диск — страница рубрикатора | 7, 9 | 15.10.2026 | — |
| R-051 | КР «Токсическое действие окиси углерода. Токсическое действие других газов, дымов и паров», 2024 | действует (пересмотр каждые 3 года) | https://cr.minzdrav.gov.ru | — | не проверялся | Google Диск (3 копии) | 8 | 15.10.2026 | ID на титуле не указан |


### А2. Лежат на Google Диске, вне границ книги

Роды, послеродовый период и гинекология вне беременности — в темы 1–11 не входят. Строки заведены, чтобы
не искать эти документы повторно; если тема начнёт на них опираться, строку переносят в группу А.

| Код | Документ | Статус редакции | Где сверено | Проверено |
|---|---|---|---|---|
| R-028 | КР «Аномалии родовой деятельности», 2024 | пересмотр 2026 | Google Диск | 15.10.2026 |
| R-029 | КР «Неудачная попытка стимуляции родов (подготовка шейки матки к родам и родовозбуждение)», 2024 | — | Google Диск | 15.10.2026 |
| R-030 | КР «Затруднённые роды [дистоция] вследствие предлежания плечика», 2024, ID 595 | пересмотр не позднее 2026 | Google Диск | 15.10.2026 |
| R-031 | КР «Медицинская помощь матери при установленном или предполагаемом несоответствии размеров таза и плода. Лицевое, лобное или подбородочное предлежание плода», 2024 | — | Google Диск | 15.10.2026 |
| R-032 | КР «Оперативные влагалищные роды», 2023, ID 775 | пересмотр истёк (не позднее 2025) | Google Диск | 15.10.2026 |
| R-033 | КР «Разрывы промежности при родоразрешении и другие акушерские травмы (акушерский травматизм)», 2023, ID 768 — 2 копии | пересмотр истёк (не позднее 2025) | Google Диск | 15.10.2026 |
| R-034 | КР «Послеродовое кровотечение», 2025 | — | Google Диск | 15.10.2026 |
| R-035 | КР «Эмболия амниотической жидкостью», 2025 | — | Google Диск | 15.10.2026 |
| R-036 | КР «Послеродовые инфекционные осложнения», 2024, ID 791 | пересмотр не позднее 2026 | Google Диск | 15.10.2026 |
| R-037 | КР «Нормальный послеродовой период (послеродовая помощь и обследование)», 2024 | — | Google Диск | 15.10.2026 |
| R-038 | КР «Воспалительные заболевания молочных желёз» | год на титуле не читается | Google Диск | 15.10.2026 |
| R-039 | КР «Искусственный аборт (медицинский аборт)», 2024 | — | Google Диск | 15.10.2026 |
| R-040 | КР «Контрацепция. Наблюдение за применением противозачаточных средств», 2024 | — | Google Диск | 15.10.2026 |
| R-041 | «Национальные медицинские критерии приемлемости методов контрацепции», РОАГ, 2023 (адаптация ВОЗ, 5-е изд., 2015) | — | Google Диск | 15.10.2026 |
| R-042 | КР «Воспалительные болезни женских тазовых органов» | год на титуле не читается | Google Диск | 15.10.2026 |
| R-043 | КР «Полипы эндометрия», 2024 | — | Google Диск | 15.10.2026 |
| R-044 | КР «Вагинальные интраэпителиальные неоплазии», 2024 | — | Google Диск | 15.10.2026 |
| R-045 | КР «Болезни бартолиновой железы», 2024 | — | Google Диск | 15.10.2026 |
| R-046 | КР «Врождённые аномалии (пороки развития) влагалища и матки у детей и подростков», 2024 | — | Google Диск | 15.10.2026 |
| R-047 | КР «Спайки вульвы», 2024 | — | Google Диск | 15.10.2026 |

На Диске лежит также форма FDA 2877 (декларация на ввоз электронных изделий) — не источник, в реестр не внесена.

## Б. Российские нормативные документы

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| N-001 | Приказ Минздрава России от 19.12.2025 № 747н, Порядок по профилю «акушерство и гинекология» | действует с 10.01.2026 | http://publication.pravo.gov.ru — поиск «747н» | https://ppt.ru/obzory/vstupaet-v-silu/prikaz-minzdrava-rossii-19-12-2025-747n (обзор) | частично (обзор, не текст) | `sources/russian-guidelines/prikaz-747n-2025-akusherstvo-ginekologiya.pdf` (скан, распознан машинно) | 10, 11 | 15.10.2026 | текстовая официальная публикация |
| N-002 | Приказ Минздрава России от 14.10.2022 № 668н, Порядок при психических расстройствах | действует | http://publication.pravo.gov.ru | — | закрыт | `sources/russian-guidelines/prikaz-668n-2022-psihicheskie-rasstrojstva.pdf` (скан) | 10 | 14.10.2026 | — |
| N-003 | Приказ Минздравсоцразвития России от 23.07.2010 № 541н, ЕКС, «Здравоохранение» | действует | http://publication.pravo.gov.ru | — | закрыт | `sources/russian-guidelines/prikaz-541n-2010-eks-zdravoohranenie.rtf` | 10 | 14.10.2026 | — |
| N-004 | Федеральный закон от 21.11.2011 № 323-ФЗ «Об основах охраны здоровья граждан…», ст. 11 | действует | http://publication.pravo.gov.ru | https://www.consultant.ru/document/cons_doc_LAW_121895/8e8caa29efb42dd54e3924ee7441f06d469f4a80/ | открыт | онлайн | 11 | 15.10.2026 | — |
| N-005 | МЧС России, «Порядок вызова экстренных служб», 29.07.2022 | — | — | https://ngc.organizations.mchs.gov.ru/export/pdf/News/4237396 | открыт | онлайн | 10, 11 | 15.10.2026 | — |
| N-006 | СанПиН 2.6.4115-25 (постановление Главного санитарного врача от 27.03.2025 № 6) | действует с 01.09.2025 до 01.09.2031 | http://publication.pravo.gov.ru/document/0001202504220013 | https://www.consultant.ru/document/cons_doc_LAW_503722/ | частично | Google Диск (выгрузка КонсультантПлюс, 2 копии) | 6 | 15.10.2026 | — |
| N-007 | Постановление Правительства РФ от 29.12.2025 № 2188 (Программа госгарантий 2026–2028) | действует (ред. от 02.04.2026) | http://publication.pravo.gov.ru | — | закрыт | Google Диск (выгрузка КонсультантПлюс; текст читается до с. 79 из 864) | 6 | 15.10.2026 | — |
| N-008 | Приказ Минздрава России от 13.11.2025 № 666н (порядок по профилю «психиатрия-наркология») | в силе с 01.09.2026 | http://publication.pravo.gov.ru/document/0001202512230030 | — | закрыт | Google Диск | 8 | 15.10.2026 | — |
| N-009 | Приказ Минздрава России от 12.01.2026 № 10н (диспансерное наблюдение, ПАВ) | в силе 01.09.2026–01.09.2032 | http://publication.pravo.gov.ru | https://rulaws.ru/acts/Prikaz-Minzdrava-Rossii-ot-12.01.2026-N-10n/ | частично | Google Диск (официальный текст, скан) | 8 | 15.10.2026 | — |
| N-010 | Приказ Минздрава России от 15.04.2026 № 286н (справки и медицинские заключения) | в силе 01.09.2026–01.09.2032 | http://publication.pravo.gov.ru/document/0001202605290025 | https://rulaws.ru/acts/Prikaz-Minzdrava-Rossii-ot-15.04.2026-N-286n/ | частично | Google Диск (официальный текст, скан) | 8 | 15.10.2026 | — |
| N-011 | Приказ Минздрава РФ от 23.08.1999 № 327 (анонимное лечение в наркологии) | действует (подтверждение пользователя 16.10.2026) | http://publication.pravo.gov.ru | https://base.garant.ru/12116904 | частично | Google Диск (выгрузка Гаранта .odt) | 8 | 16.10.2026 | — |
| N-012 | Приказ Минздрава России от 23.11.2021 № 1089н (листки нетрудоспособности) | действует; изменён приказом от 10.11.2025 № 657н (только п. 1) | http://publication.pravo.gov.ru | https://legalacts.ru/doc/prikaz-minzdrava-rossii-ot-23112021-n-1089n-ob-utverzhdenii/ | закрыт | Google Диск — скан без текста, не прочитан; сроки 140/194 дня — sfr.gov.ru (07.10.2026) | 8 | 16.10.2026 | текст п. 57 (по желанию) |
| N-013 | Социальный фонд России, отделение по Волгоградской области: новость о пособии по беременности и родам, 07.10.2026 | — | https://sfr.gov.ru/branches/volgograd/news/~2026/10/07/285366 | https://sfr.gov.ru/branches/penza/news/~2026/02/20/278993 | открыт | — | 8 | 16.10.2026 | — |

## В. Международные руководства и официальные материалы

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| I-001 | RCOG, Reduced Fetal Movements, Green-top Guideline No. 57, 2-е изд., BJOG 2026;133(8):e70–e92 | действует (пересмотр 2029); 1-е изд. 2011 заменено | https://doi.org/10.1111/1471-0528.70198 | https://www.rcog.org.uk/guidance/browse-all-guidance/green-top-guidelines/reduced-fetal-movements-green-top-guideline-no-57/ | закрыт (Wiley) | `sources/who-international/rcog-gtg57-reduced-fetal-movements-2026.pdf`; Google Диск | 11 | 15.10.2026 | — |
| I-002 | NICE NG133, Hypertension in pregnancy, 2019 | действует | https://www.nice.org.uk/guidance/ng133 | https://www.nice.org.uk/guidance/ng133/chapter/Recommendations | открыт | онлайн | 11 | 15.10.2026 | — |
| I-003 | NICE CG192, Antenatal and postnatal mental health, 2014, обновл. 2020 | действует | https://www.nice.org.uk/guidance/cg192 | — | открыт | `sources/who-international/nice-cg192-2014-updated-2020.pdf` | 10 | 14.10.2026 | — |
| I-004 | WHO, Guide for integration of perinatal mental health…, 2022 | действует | — | — | — | `sources/who-international/who-perinatal-mental-health-guide-2022.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-005 | WHO, Responding to intimate partner violence and sexual violence against women, 2013 | действует | — | — | — | `sources/who-international/who-ipv-sv-guidelines-2013.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-006 | WHO, Doing What Matters in Times of Stress, 2020 (рус.) | действует | — | — | — | `sources/who-international/who-doing-what-matters-2020-ru.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-007 | COPE, Australian Clinical Practice Guideline, Mental health care in the perinatal period, 2023 | действует | — | — | — | `sources/who-international/cope-australia-perinatal-mental-health-2023.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-008 | ACOG Committee Opinion No. 569, Oral Health Care During Pregnancy…, 2013, переподтверждён 2025 | действует | https://www.acog.org/-/media/project/acog/acogorg/clinical/files/committee-opinion/articles/2013/08/oral-health-care-during-pregnancy-and-through-the-lifespan.pdf | — | закрыт (ACOG, код 402) | `sources/who-international/Oral Health Care During Pregnancy and Through the Lifespan.pdf` | 6 | 12.09.2026 | — |
| I-009 | Oral Health Care During Pregnancy: A National Consensus Statement, ред. 2026 | действует | https://www.mchoralhealth.org/PDFs/OralHealthPregnancyConsensus.pdf | там же | открыт | `sources/who-international/OralHealthPregnancyConsensus.pdf` | 6 | 12.09.2026 | — |
| I-010 | AAPD, Oral Health Care for the Pregnant Patient, 2025 | действует | https://www.aapd.org/globalassets/media/policies_guidelines/bp_pregnancy25.pdf | там же | открыт | `sources/who-international/bp_pregnancy25.pdf` | 6 | 12.09.2026 | — |
| I-011 | FDA, Ultrasound Imaging (раздел для беременных), актуально на 19.09.2024 | действует | https://www.fda.gov/radiation-emitting-products/medical-imaging/ultrasound-imaging (адрес подтверждён поиском 16.10.2026) | — | закрыт | `sources/who-international/fda-ultrasound-imaging.pdf` (снимок страницы); Google Диск | 11 | 15.10.2026 | подтвердить точный адрес страницы |
| I-012 | STRIDE BP, Validated devices for BP measurement in pregnancy / preeclampsia | обновляется постоянно; выгрузка 15.10.2026 | https://www.stridebp.org | — | не проверялся (адрес главной; список для беременных — через раздел приборов) | `sources/who-international/stridebp-monitors-pregnancy-2026-10-15.pdf`; Google Диск | 11 | 15.10.2026 | прямой адрес списка |
| I-013 | FIGO, Fetal Growth Initiative: лучшие практические рекомендации по скринингу, диагностике и лечению задержки роста плода, 2021 (рус. перевод) | действует | — | — | не проверялся | Google Диск | кандидат: 11 | 15.10.2026 | канонический адрес |
| I-014 | ISSVD, Recommendations for the Diagnosis and Treatment of Vaginitis (рус. перевод; ред. Vieira-Baptista, Stockdale, Sobel) | действует | — | — | не проверялся | Google Диск | кандидат: 4, 5 | 15.10.2026 | год и канонический адрес |
| I-015 | FDA, Marketing Clearance of Diagnostic Ultrasound Systems and Transducers. Guidance for Industry and FDA Staff, 21.02.2023 (1-я ред. 27.06.2019) | действует | https://www.fda.gov | — | закрыт | Google Диск («Guidance-Diagnostic-Ultrasound-Systems-Transducers») | (11 — не используется в тексте) | 15.10.2026 | — |
| I-016 | NICE NG192, Caesarean birth | опубл. 31.03.2021, обновл. 10.06.2025 | https://www.nice.org.uk/guidance/ng192 | там же | открыт | Google Диск | 10 | 15.10.2026 | — |
| I-017 | NICE PH50, Domestic violence and abuse: multi-agency working | опубл. 26.02.2014, действует | https://www.nice.org.uk/guidance/ph50 | — | частично | Google Диск | 10 | 15.10.2026 | — |
| I-018 | USPSTF, Screening for Depression and Suicide Risk in Adults, 2023 | действует | https://uspreventiveservicestaskforce.org/uspstf/recommendation/screening-depression-suicide-risk-adults | там же | открыт | Google Диск | 10 | 15.10.2026 | — |
| I-019 | USPSTF, Interventions to Prevent Perinatal Depression, 2019 | обновляется | https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/perinatal-depression-preventive-interventions | там же | открыт | Google Диск | 10 | 15.10.2026 | — |
| I-020 | USPSTF, Screening for IPV, Elder Abuse, and Abuse of Vulnerable Adults. JAMA 2018;320(16):1678–1687 | действует | https://doi.org/10.1001/jama.2018.14741 | — | закрыт (JAMA) | Google Диск | 10 | 15.10.2026 | — |
| I-021 | ACOG Committee Opinion No. 518, Intimate Partner Violence, 2012 | пометки о переподтверждении в PDF нет | https://doi.org/10.1097/AOG.0b013e318249ff74 | — | закрыт (ACOG) | Google Диск | 10 | 15.10.2026 | статус на acog.org |
| I-022 | ACOG Committee Opinion No. 825, Caring for Patients Who Have Experienced Trauma, 2021 | действует | https://doi.org/10.1097/AOG.0000000000004326 | — | закрыт (ACOG) | Google Диск | 10 | 15.10.2026 | — |
| I-023 | ACOG Committee Opinion No. 711, Opioid Use and Opioid Use Disorder in Pregnancy, 2017 | — | https://doi.org/10.1097/AOG.0000000000002235 | — | закрыт (ACOG) | Google Диск | 8 | 15.10.2026 | — |
| I-024 | ACOG Clinical Consensus No. 10, Cannabis Use During Pregnancy and Lactation, 2025 | действует | https://doi.org/10.1097/AOG.0000000000006053 | — | закрыт (ACOG) | Google Диск | 8 | 15.10.2026 | — |
| I-025 | ESHRE, Routine psychosocial care in infertility and medically assisted reproduction, март 2015 | — | https://doi.org/10.1093/humrep/dev177 | — | закрыт | Google Диск | 10 | 15.10.2026 | — |
| I-026 | NHTSA, If You’re Pregnant — Seat Belt Recommendations for Drivers and Passengers (11426-021126-v8) | действует | https://www.nhtsa.gov/seatbelts | — | частично | Google Диск; страница Air Bags — онлайн (WebFetch) | 8 | 15.10.2026 | — |
| I-027 | Canver B.R., Gomez A.E. Alcohol Withdrawal Syndrome. StatPearls, NBK441882, обновл. 14.02.2024 | — | https://www.ncbi.nlm.nih.gov/books/NBK441882/ | там же | закрыт (CAPTCHA) | Google Диск | 8 | 15.10.2026 | — |
| I-028 | МЧС России. ФГБУ «Центр экстренной психологической помощи МЧС России» — страница учреждения (телефон +7 (495) 989-50-50) | — | https://mchs.gov.ru/ministerstvo/uchrezhdeniya-mchs-rossii/federalnye-gosudarstvennye-byudzhetnye-uchrezhdeniya/fku-centr-ekstrennoy-psihologicheskoy-pomoshchi-mchs-rossii | https://psi.mchs.gov.ru/ | открыт | — | 10 | 16.10.2026 | режим работы, регионы |
| I-029 | НМИЦ им. В.А. Алмазова. Экстренные службы психологической поддержки (перечень), 12.2025 | — | https://education.almazovcentre.ru/wp-content/uploads/2025/12/ekstrennye-sluzhby-psihologicheskoj-podderzhki.pdf | — | открыт | — | 10 | 16.10.2026 | операторы линий не названы |
| I-030 | UKTIS. Use of loratadine in pregnancy (монография), Version 4, March 2026 — раздел Summary | — | https://uktis.org/monographs/use-of-loratadine-in-pregnancy/ | — | открыт (цитаты частями) | — | 7 | 16.10.2026 | — |
| I-031 | ACOG Committee Opinion No. 554: Reproductive and sexual coercion. Obstet Gynecol 2013;121(2 Pt 1):411–415; PMID 23344307 | не установлен (Reaffirmed?) | https://doi.org/10.1097/01.AOG.0000426427.79586.3b | PubMed 23344307 | реферат; PDF закрыт | — | 10 | 16.10.2026 | статус |

## Г. Пациентские материалы (только навигация и вопросы читательниц; утверждения — с оговоркой о применимости к РФ)

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| P-001 | NHS, Your baby's movements | проверена 08.07.2024 | https://www.nhs.uk/pregnancy/keeping-well/your-babys-movements/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-002 | NHS, Pre-eclampsia | проверена 23.03.2026 | https://www.nhs.uk/conditions/pre-eclampsia/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-003 | NHS, Pregnancy symptoms you need to get help for | проверена 24.06.2026 | https://www.nhs.uk/pregnancy/common-symptoms/pregnancy-symptoms-you-need-to-get-help-for/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-004 | NHS, Vomiting and morning sickness | проверена 17.04.2024 | https://www.nhs.uk/pregnancy/common-symptoms/vomiting-and-morning-sickness/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-005 | South West Maternal Medicine Network (NHS England), Breathlessness in Pregnancy | дата не указана (адрес 2024/05) | https://southwestmaternalmedicinenetwork.nhs.uk/wp-content/uploads/2024/05/Breathlessness-in-Pregnancy.pdf | там же | частично | Google Диск | (11 — не используется в тексте) | 15.10.2026 | — |
| P-006 | UKTIS / Bumps, Loratadine (листок для пациенток), май 2025, v4.0 | действует | https://www.medicinesinpregnancy.org/ | — | открыт | Google Диск | 7 (только навигация) | 15.10.2026 | нужна монография UKTIS, раздел Summary |

## Д. Научные статьи

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| S-001 | Louwen F. et al. Paracetamol use during pregnancy and autism risk. Int J Gynecol Obstet 2025;171(3):915–919 | — | https://doi.org/10.1002/ijgo.70577 | — | закрыт (Wiley) | `sources/reviews/louwen-2025-paracetamol-autism-ijgo.pdf` | 7 | 07.10.2026 | — |
| S-002 | Савинова Т.Л., Грудкин А.А., …, Сухих Г.Т. Дистанционный мониторинг беременных: опыт Оренбурга. Акушерство и гинекология. 2024;(11):162–172 | — | https://dx.doi.org/10.18565/aig.2024.212 | https://roag-portal.ru/science-articles (№ 93) | не проверялся | Google Диск («ДИСТАНЦИОННЫЙ МОНИТОРИНГ БЕРЕМЕННЫХ») | 11 — контекст для врача (DISPUTED 48, 54), в списке источников нет | 15.10.2026 | — |
| S-003 | Тысячный О.В., Баев О.Р. Современная тенденция частоты гестационного сахарного диабета и макросомии плода по данным перинатального центра третьего уровня. Акушерство и гинекология. 2026;(7):58–65 | — | https://dx.doi.org/10.18565/aig.2026.116 | https://roag-portal.ru/science-articles (№ 147) | не проверялся | Google Диск («Тенденция частоты гестационного диабета…») | кандидат: 1 (частота ГСД — одно учреждение, авторы сами пишут, что на популяцию не переносится) | 15.10.2026 | — |
| S-004 | Батрак Н.В., Малышкина А.И., Ткаченко А.С. Оценка качества жизни… у беременных с ранним и поздним выявлением гестационного сахарного диабета. Акушерство и гинекология. 2023;(2):64–70 | — | https://dx.doi.org/10.18565/aig.2022.230 | — | не проверялся | Google Диск («Оценка состояния с выявлением гестационного диабета») | вне книги (малая выборка, ассоциации без причинных выводов) | 15.10.2026 | — |
| S-005 | O’Connell M.A. et al. Interventions for fear of childbirth including tocophobia. Cochrane CD013321.pub2, 2021 | — | https://doi.org/10.1002/14651858.CD013321.pub2 | — | закрыт | Google Диск | 10 | 15.10.2026 | — |
| S-006 | Yaacob M. et al. Powered versus manual toothbrushing. Cochrane CD002281.pub3, 2014 | — | https://doi.org/10.1002/14651858.CD002281.pub3 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7133541/ | частично | Google Диск | 6 | 15.10.2026 | — |
| S-007 | Badahdah A. … Natto Z.S. Dental Water Jet… Healthcare (Basel) 2025;13(4):396 | — | https://doi.org/10.3390/healthcare13040396 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11855567/ | закрыт (лимит) | Google Диск | 6 | 15.10.2026 | — |
| S-008 | Gamba T.O. et al. Impact of dental imaging on pregnant women… Imaging Sci Dent 2024;54(1):1–11 | — | https://doi.org/10.5624/isd.20230177 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10985525/ | частично | Google Диск | 6 | 15.10.2026 | — |
| S-009 | Langa G.P.J. et al. Bristle stiffness and end-shape… interproximal surfaces. J Evid Based Dent Pract 2021;21(2):101548 | — | https://doi.org/10.1016/j.jebdp.2021.101548 | — | закрыт | Google Диск — снимок страницы с рефератом | 6 | 15.10.2026 | полный текст |
| S-010 | Ranzan N. et al. Bristle stiffness and end-shape and adverse effects on soft tissues. Int Dent J 2019;69(3):171–182 | — | https://doi.org/10.1111/idj.12421 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9379007/ | частично | Google Диск | 6 | 15.10.2026 | — |
| S-011 | MacDonald L.A. et al. Clinical guidelines for occupational lifting in pregnancy. Am J Obstet Gynecol 2013;209(2):80–88 | — | https://doi.org/10.1016/j.ajog.2013.02.047 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4552317/ | закрыт (CAPTCHA) | Google Диск — рисунок 2 просмотрен | 8 | 15.10.2026 | — |
| S-012 | Чибисова М.А., Гурджи М.Я., Водоватов А.В. Радиационная безопасность при рентгеностоматологических исследованиях у беременных. Клиническая стоматология 2026;29(1):205–208 | — | https://doi.org/10.37988/1811-153X_2026_1_205 | https://www.kstom.ru/ks/article/view/0117-27 | частично | Google Диск | 6 | 15.10.2026 | — |
| S-013 | Parimi M., Marshall C., Prata N. Matrescence: A Critical and Sensitive Period in the Maternal and Child Health (MCH) Life Course Perspective. Women’s Health Issues, 2025 (комментарий; принят 27.10.2025) | — | https://doi.org/10.1016/j.whi.2025.10.009 | https://www.whijournal.com | не проверялся | Google Диск | 10 (DISPUTED 55) | 16.10.2026 | том, страницы |
| S-014 | Trinko et al. Improving maternal well-being: a matrescence education pilot study. Maternal Health, Neonatology and Perinatology 2025;11:18 | — | https://doi.org/10.1186/s40748-025-00203-0 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12220242 | открыт | Google Диск | 10 (DISPUTED 55) | 15.10.2026 | — |
| S-015 | Athan A.M. A critical need for the concept of matrescence in perinatal psychiatry. Frontiers in Psychiatry 2024;15:1364845 | — | https://doi.org/10.3389/fpsyt.2024.1364845 | — | не проверялся (по ссылке у Parimi) | — | 10 (DISPUTED 55) | 16.10.2026 | открыть |
| S-016 | Ravanelli N., Casasola W., English T., Edwards K.M., Jay O. Heat stress and fetal risk. Environmental limits for exercise and passive heat stress during pregnancy: a systematic review with best evidence synthesis. Br J Sports Med 2019;53(13):799–805; PMID 29496695 | — | https://doi.org/10.1136/bjsports-2017-097914 | PubMed 29496695 | реферат | — | 5 (5.5), 8 (8.9) — кандидат | 16.10.2026 | полный текст |
| S-017 | Moretti M.E., Bar-Oz B., Fried S., Koren G. Maternal hyperthermia and the risk for neural tube defects in offspring. Epidemiology 2005;16(2):216–219; PMID 15703536 | — | https://doi.org/10.1097/01.ede.0000152903.55579.15 | PubMed 15703536 | реферат | — | 8 | 16.10.2026 | — |


## Е. Инструкции лекарственных препаратов

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| L-001 | Артикаин, раствор для инъекций 40 мг/мл (ПРОМОМЕД РУС / Биохимик), инструкция | действующая на 15.10.2026 | https://grls.rosminzdrav.ru | — | закрыт | Google Диск | 6 | 15.10.2026 | регистрационный номер |
| L-002 | Артикаин ИНИБСА 40 мг/мл + эпинефрин 0,010 мг/мл, листок-вкладыш | действующий | https://grls.rosminzdrav.ru | — | закрыт | Google Диск | 6 | 15.10.2026 | — |
| L-003 | Азота закись, газ сжатый (АО «Линде Газ Рус»), инструкция | действующая | https://grls.rosminzdrav.ru | — | закрыт | Google Диск | 6 | 15.10.2026 | — |
| L-004 | Никоретте, спрей 1 мг/доза (ДжейТНЛ), листок-вкладыш | действующий | https://grls.rosminzdrav.ru | — | закрыт | Google Диск | 8 | 15.10.2026 | — |
| L-005 | Никоретте, резинка жевательная 2 и 4 мг (ДжейТНЛ), листок-вкладыш | действующий | https://grls.rosminzdrav.ru | — | закрыт | Google Диск | 8 | 15.10.2026 | — |
| L-006 | Никоретте, пластырь трансдермальный 10/15/25 мг/16 ч, инструкция | действующая | https://grls.rosminzdrav.ru | — | закрыт | Google Диск | 8 | 15.10.2026 | — |
| L-007 | Никоретте, таблетки для рассасывания 2 и 4 мг, инструкция | действующая | https://grls.rosminzdrav.ru | — | закрыт | Google Диск | 8 | 15.10.2026 | — |

---

Темы 1–10 внесены частично (документы с Google Диска пользователя внесены все — 15.10.2026) — только документы, которые лежат в `sources/` или
открывались в последних сессиях. Остальные источники этих тем вносятся при их
проверке на источники (по одной теме за раз).
