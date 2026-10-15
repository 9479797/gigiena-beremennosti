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
колонки «Рабочая ссылка».

**Статус редакции:** «действует», «пересмотр истёк» (срок «не позднее» прошёл —
утверждения из документа получают `QUALIFIED`), «заменён» (указать чем).

---

## А. Российские клинические рекомендации

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | КР «Нормальная беременность», РОАГ, 2023, ред. 15.02.2024, ID 288 (288_2) | пересмотр истёк (не позднее 2025) | https://cr.minzdrav.gov.ru — карточка 288_2 | https://congress-med.ru/assets/files/2024/2024-normalnaya-beremennost.pdf | закрыт (с 15.10.2026; 14.10.2026 открывался) | `sources/russian-guidelines/normalnaya-beremennost.pdf`; файл пользователя 15.10.2026 — совпадает | 1–11 | 15.10.2026 | — |
| R-002 | КР «Преэклампсия. Эклампсия. Отеки, протеинурия и гипертензивные расстройства…», РОАГ, 2024, ID 637 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — ID 637 | https://base.garant.ru/409626439/ | частично (обрыв на 2.5, без приложений) | `sources/russian-guidelines/preeklampsiya-2024.pdf` (официальный, 74 с.) | 8, 11; сверка 1, 7 | 15.10.2026 | — |
| R-003 | КР «Венозные осложнения во время беременности и послеродовом периоде. Акушерская тромбоэмболия», 2025 | действует; поле «пересмотр» на титуле нет | https://roag-portal.ru/recommendations_obstetrics | — | закрыт (портал РОАГ) | `sources/russian-guidelines/venoznye-oslozhneniya-akusherskaya-tromboemboliya.pdf`; файл пользователя 15.10.2026 — идентичен | 2, 11 | 15.10.2026 | прямой адрес файла на портале |
| R-004 | КР «Признаки внутриутробной гипоксии плода, требующие предоставления медицинской помощи матери», 2023, ID 774 | пересмотр истёк (не позднее 2025) | https://cr.minzdrav.gov.ru — ID 774 | https://base.garant.ru/407548979/ | частично (разделы 1–2.4 читаются) | онлайн-копия | 11 | 15.10.2026 | Приложение В; копия PDF — https://pericentr.gosuslugi.ru/netcat_files/8/9/KR774_Priznaki_vnutriutrobnoy_gipoxii_ploda.pdf (не открывалась) |
| R-005 | КР «Чрезмерная рвота беременных», 2024, ID 802 (802_1) | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — ID 802 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/304617; Прил. В — https://base.garant.ru/410598052/7dede6ac8f25be619ed07c17ed1c62c9/ | частично | онлайн-копии | 1, 11 | 15.10.2026 | страницы цитат — по копии без пагинации |
| R-006 | КР «Преждевременная отслойка нормально расположенной плаценты», ID 800 | не установлен | https://cr.minzdrav.gov.ru — ID 800 | https://base.garant.ru/410576556/c9c989f1e999992b41b30686f0032f7d/; https://pravo.ppt.ru/klinicheskie-rekomendatsii/304478 | частично | онлайн-копии | 11 | 15.10.2026 | год утверждения; страницы |
| R-007 | КР «Преждевременные роды», 2024, ID 331 | действует | https://cr.minzdrav.gov.ru — ID 331 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/303408 | частично (нет Прил. В) | онлайн-копия | 9, 11 | 15.10.2026 | Приложение В |
| R-008 | КР «Выкидыш», ID 670 | не установлен | https://cr.minzdrav.gov.ru — ID 670 | — | закрыт | — | (11 — не используется в тексте) | 15.10.2026 | Приложение В — запись 77 `skachat-vruchnuyu.md` |
| R-009 | КР «Роды одноплодные, родоразрешение путём кесарева сечения», 2024, ID 639 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — ID 639 | https://pravo.ppt.ru/klinicheskie-rekomendatsii/302238 | частично | `sources/russian-guidelines/rody-kesarevo-sechenie-2024.pdf` | 10 | 14.10.2026 | — |
| R-010 | КР «Инфекция мочевых путей при беременности», ID 719 | см. запись 16 `skachat-vruchnuyu.md` | https://cr.minzdrav.gov.ru — ID 719 | — | закрыт | файл пользователя 09.10.2026 | 7, 9 | 09.10.2026 | ссылка на полный текст |
| R-011 | КР «Привычный выкидыш», 2022, ID 721 | пересмотр истёк (2024) | https://cr.minzdrav.gov.ru — ID 721 | — | закрыт | файл пользователя 09.10.2026 | 7 | 09.10.2026 | ссылка на полный текст |
| R-012 | КР «Депрессивный эпизод, рекуррентное депрессивное расстройство», 2024, ID 301_3 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — 301_3 | — | закрыт | `sources/russian-guidelines/kr-depressivnyj-epizod-rdr-2024.txt` (выгрузка пользователя) | 10 | 14.10.2026 | — |
| R-013 | КР «Генерализованное тревожное расстройство», 2024, ID 457_3 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — 457_3 | — | закрыт | `sources/russian-guidelines/kr-generalizovannoe-trevozhnoe-rasstrojstvo-2024.txt` | 10 | 09.10.2026 | — |
| R-014 | КР «Тревожно-фобические расстройства», 2024, ID 455_3 | действует (пересмотр 2026) | https://cr.minzdrav.gov.ru — 455_3 | — | закрыт | `sources/russian-guidelines/kr-trevozhno-fobicheskie-rasstrojstva-2024.txt` | 10 | 09.10.2026 | — |
| R-015 | КР «Обсессивно-компульсивное расстройство», 2025, ID 650_2 | действует (пересмотр 2027) | https://cr.minzdrav.gov.ru — 650_2 | — | закрыт | `sources/russian-guidelines/kr-obsessivno-kompulsivnoe-rasstrojstvo.txt` | 10 | 09.10.2026 | — |

## Б. Российские нормативные документы

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| N-001 | Приказ Минздрава России от 19.12.2025 № 747н, Порядок по профилю «акушерство и гинекология» | действует с 10.01.2026 | http://publication.pravo.gov.ru — поиск «747н» | https://ppt.ru/obzory/vstupaet-v-silu/prikaz-minzdrava-rossii-19-12-2025-747n (обзор) | частично (обзор, не текст) | `sources/russian-guidelines/prikaz-747n-2025-akusherstvo-ginekologiya.pdf` (скан, распознан машинно) | 10, 11 | 15.10.2026 | текстовая официальная публикация |
| N-002 | Приказ Минздрава России от 14.10.2022 № 668н, Порядок при психических расстройствах | действует | http://publication.pravo.gov.ru | — | закрыт | `sources/russian-guidelines/prikaz-668n-2022-psihicheskie-rasstrojstva.pdf` (скан) | 10 | 14.10.2026 | — |
| N-003 | Приказ Минздравсоцразвития России от 23.07.2010 № 541н, ЕКС, «Здравоохранение» | действует | http://publication.pravo.gov.ru | — | закрыт | `sources/russian-guidelines/prikaz-541n-2010-eks-zdravoohranenie.rtf` | 10 | 14.10.2026 | — |
| N-004 | Федеральный закон от 21.11.2011 № 323-ФЗ «Об основах охраны здоровья граждан…», ст. 11 | действует | http://publication.pravo.gov.ru | https://www.consultant.ru/document/cons_doc_LAW_121895/8e8caa29efb42dd54e3924ee7441f06d469f4a80/ | открыт | онлайн | 11 | 15.10.2026 | — |
| N-005 | МЧС России, «Порядок вызова экстренных служб», 29.07.2022 | — | — | https://ngc.organizations.mchs.gov.ru/export/pdf/News/4237396 | открыт | онлайн | 10, 11 | 15.10.2026 | — |

## В. Международные руководства и официальные материалы

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| I-001 | RCOG, Reduced Fetal Movements, Green-top Guideline No. 57, 2-е изд., BJOG 2026;133(8):e70–e92 | действует (пересмотр 2029); 1-е изд. 2011 заменено | https://doi.org/10.1111/1471-0528.70198 | https://www.rcog.org.uk/guidance/browse-all-guidance/green-top-guidelines/reduced-fetal-movements-green-top-guideline-no-57/ | закрыт (Wiley) | `sources/who-international/rcog-gtg57-reduced-fetal-movements-2026.pdf` | 11 | 15.10.2026 | — |
| I-002 | NICE NG133, Hypertension in pregnancy, 2019 | действует | https://www.nice.org.uk/guidance/ng133 | https://www.nice.org.uk/guidance/ng133/chapter/Recommendations | открыт | онлайн | 11 | 15.10.2026 | — |
| I-003 | NICE CG192, Antenatal and postnatal mental health, 2014, обновл. 2020 | действует | https://www.nice.org.uk/guidance/cg192 | — | открыт | `sources/who-international/nice-cg192-2014-updated-2020.pdf` | 10 | 14.10.2026 | — |
| I-004 | WHO, Guide for integration of perinatal mental health…, 2022 | действует | — | — | — | `sources/who-international/who-perinatal-mental-health-guide-2022.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-005 | WHO, Responding to intimate partner violence and sexual violence against women, 2013 | действует | — | — | — | `sources/who-international/who-ipv-sv-guidelines-2013.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-006 | WHO, Doing What Matters in Times of Stress, 2020 (рус.) | действует | — | — | — | `sources/who-international/who-doing-what-matters-2020-ru.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-007 | COPE, Australian Clinical Practice Guideline, Mental health care in the perinatal period, 2023 | действует | — | — | — | `sources/who-international/cope-australia-perinatal-mental-health-2023.pdf` | 10 | 14.10.2026 | канонический адрес |
| I-008 | ACOG Committee Opinion No. 569, Oral Health Care During Pregnancy…, 2013, переподтверждён 2025 | действует | https://www.acog.org/-/media/project/acog/acogorg/clinical/files/committee-opinion/articles/2013/08/oral-health-care-during-pregnancy-and-through-the-lifespan.pdf | — | закрыт (ACOG, код 402) | `sources/who-international/Oral Health Care During Pregnancy and Through the Lifespan.pdf` | 6 | 12.09.2026 | — |
| I-009 | Oral Health Care During Pregnancy: A National Consensus Statement, ред. 2026 | действует | https://www.mchoralhealth.org/PDFs/OralHealthPregnancyConsensus.pdf | там же | открыт | `sources/who-international/OralHealthPregnancyConsensus.pdf` | 6 | 12.09.2026 | — |
| I-010 | AAPD, Oral Health Care for the Pregnant Patient, 2025 | действует | https://www.aapd.org/globalassets/media/policies_guidelines/bp_pregnancy25.pdf | там же | открыт | `sources/who-international/bp_pregnancy25.pdf` | 6 | 12.09.2026 | — |
| I-011 | FDA, Ultrasound Imaging (раздел для беременных), актуально на 19.09.2024 | действует | https://www.fda.gov/radiation-emitting-products/medical-imaging/ultrasound-imaging (по пути навигации) | — | закрыт | `sources/who-international/fda-ultrasound-imaging.pdf` (снимок страницы) | 11 | 15.10.2026 | подтвердить точный адрес страницы |
| I-012 | STRIDE BP, Validated devices for BP measurement in pregnancy / preeclampsia | обновляется постоянно; выгрузка 15.10.2026 | https://www.stridebp.org | — | не проверялся | `sources/who-international/stridebp-monitors-pregnancy-2026-10-15.pdf` | 11 | 15.10.2026 | прямой адрес списка |

## Г. Пациентские материалы (только навигация и вопросы читательниц; утверждения — с оговоркой о применимости к РФ)

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| P-001 | NHS, Your baby's movements | проверена 08.07.2024 | https://www.nhs.uk/pregnancy/keeping-well/your-babys-movements/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-002 | NHS, Pre-eclampsia | проверена 23.03.2026 | https://www.nhs.uk/conditions/pre-eclampsia/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-003 | NHS, Pregnancy symptoms you need to get help for | проверена 24.06.2026 | https://www.nhs.uk/pregnancy/common-symptoms/pregnancy-symptoms-you-need-to-get-help-for/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-004 | NHS, Vomiting and morning sickness | проверена 17.04.2024 | https://www.nhs.uk/pregnancy/common-symptoms/vomiting-and-morning-sickness/ | там же | открыт | онлайн | 11 | 15.10.2026 | — |
| P-005 | South West Maternal Medicine Network (NHS England), Breathlessness in Pregnancy | дата не указана (адрес 2024/05) | https://southwestmaternalmedicinenetwork.nhs.uk/wp-content/uploads/2024/05/Breathlessness-in-Pregnancy.pdf | там же | частично | онлайн | (11 — не используется в тексте) | 15.10.2026 | сверка формулировки — запись 81 `skachat-vruchnuyu.md` |

## Д. Научные статьи

| Код | Документ | Статус редакции | Каноническая ссылка | Рабочая ссылка (полный текст) | Доступ | Где сверено | Темы | Проверено | Чего не хватает |
|---|---|---|---|---|---|---|---|---|---|
| S-001 | Louwen F. et al. Paracetamol use during pregnancy and autism risk. Int J Gynecol Obstet 2025;171(3):915–919 | — | https://doi.org/10.1002/ijgo.70577 | — | закрыт (Wiley) | `sources/reviews/louwen-2025-paracetamol-autism-ijgo.pdf` | 7 | 07.10.2026 | — |

---

Темы 1–10 внесены частично — только документы, которые лежат в `sources/` или
открывались в последних сессиях. Остальные источники этих тем вносятся при их
проверке на источники (по одной теме за раз).
