# Память Claude по проекту — резервная копия от 30.10.2026

Дословный перенос памяти claude.ai-проекта «Гигиена беременности» в репозиторий,
чтобы она не пропала при отключении аккаунта. Метка `[stated]` — сказано
пользователем. Если пункт расходится с `AGENTS.md` или файлами `editorial/`,
главный — репозиторий. Часть ранних пунктов (раздел «Обзор проекта») относится
к сентябрю 2026 и могла устареть.

---

## Обзор проекта (overview)

- [stated] Dima is the author and project owner of *Гигиена беременности* ("Pregnancy Hygiene"), a Russian-language book for pregnant women
- [stated] The book's audience: pregnant women and those planning pregnancy; for relatives, the Introduction highlights relevant chapters
- [stated] The book is organized into thematic chapters (Themes 1–4 currently in progress) covering nutrition, daily routine/sleep, physical activity, and intimate health
- [stated] Repository: `9479797/gigiena-beremennosti` on GitHub
- [stated] Dima makes all final decisions and manually applies changes
- [stated] Claude serves as primary writing and editorial partner in browser chat
- [stated] Claude Code acts as a terminal agent for repository operations (commits, file management, spec updates)
- [stated] Yulia Papenkina is the medical consultant, reviewing chapters for clinical accuracy in the Russian healthcare context
- [stated] Yulia's clinical feedback carries weight for removing or restructuring content (e.g. the snoring/sleep apnea section was removed entirely based on her input)
- [stated] Constraint: the GitHub connector in the Project panel is read-only and syncs only manually — after any Claude Code commit session, Dima must press **Sync** in the Context panel on claude.ai
- [stated] Key clinical reference: ACOG Committee Opinion 804 (exercise in pregnancy)
- [stated] Cochrane reviews are referenced for pelvic floor exercise dosing
- [stated] Perplexity has been used for content generation comparison — noted to produce more narrative-flowing prose vs. Claude's structured enumeration tendency

### Состояние (на момент импорта, сентябрь 2026 — перепроверять)
- [stated] Theme 4 (intimate health) has completed both a full prompt-mode pass (language cleanup, terminology unpacking) and a Theme 1–3 mode pass, adding: fetal perception during sex, fear after medical clearance, returning to intimacy after a break, relationship dynamic changes, women without partners, spotting after examination/cervicometry, next-day sensations
- [stated] Theme 3 (physical activity) is substantially revised: contraindications list corrected against ACOG CO 804; pelvic girdle pain section rewritten with a six-step daily protocol and acute pain first-aid block; pelvic floor exercise section built with Cochrane-based dosing; exercise substitution list corrected; supine position threshold set at 20 weeks per ACOG CO 804
- [stated] Themes 1 and 2 have approved edited versions (genuine repetition reduced, not content)
- [stated] Active editorial specs committed to the repository: `text-architecture-v1.1`, `tone-of-voice-v1.1`, `human-review-roles-v1.0`, `theme-reconnaissance-v1.0`, `source-verification-v1.0`, `evidence-ledger-template.md`
- [stated] Editorial process spec is at v1.7

### Впереди
- [stated] Cross-links between chapters are deferred until all themes are written
- [stated] A hydration subsection ("питьевой режим") for Theme 1 is missing and needs to be written
- [stated] Ongoing open questions are tracked in `DISPUTED-CLAIMS.md` for Yulia's review
- [stated] planning a source-verification pass over every theme next; downloaded the ROAG portal clinical guidelines for that (2026-10-15)
- [stated] has a Google storage (Drive) with many obstetrics/gynecology files; plans to share its link so Claude can close sources that otherwise need manual download (2026-10-15)
- [stated] says «тема 0» for Раздел 0 «Быстрая помощь: когда нельзя ждать» (urgent-help navigator); started developing it 2026-10-16 after all Themes 1–11 were drafted
- [stated] the book text will be published as HTML with styling and fast navigation; quick-jump links between parts are to be developed later
- [stated] HTML-версия книги строится по принципу mobile first (2026-10-20)
- [stated] Яна — акушерка, эксперт проекта; консультирует Диму, тексты тем не проверяет; исключение — Введение, которое она читает не как врач, а как эксперт по аудитории книги (2026-10-20)
- [stated] HTML-версию книги делают в самом конце, после правок врача (2026-10-20)
- [stated] оглавление книги — динамический раздел, его не фиксируют: оно меняется вместе с редакцией проекта (2026-10-20)
- [stated] решил добавить новую тему о поездках (будущая Тема 12) — все поездки, включая зарубежные; болезни, опасности и прививки в ней раскладываются по направлениям (странам/регионам); карточки-фразы позже переводятся на языки стран (2026-10-22); 23.10.2026 отложил Тему 12 до выхода книги — в первое издание не входит, вернуться после выхода
- [stated] переработал Тему 8 сам и будет так же сам дорабатывать Темы 9, 10 и 11; проверку его переработок ведут по одному формату — этап «Сверка авторской редакции» (REVIEW THEME N): уточняющие вопросы без ограничения числа, затем правка по разделам редлайном и единый файл редлайна темы (2026-10-27)
- [stated] книга — часть более широкого онлайн-проекта для беременных и мам (платный курс, конкурентный анализ, реклама в Яндекс Директ), не отдельное направление

---

## Как работать с Димой (preferences)

- [stated] запрещает «нейрослоп» — обороты, по которым узнаётся нейросеть: короткие предложения-связки вроде «Разница здесь принципиальная», формулы утешения вроде «это не признак того, что что-то было сделано не так», метафоры-опоры вроде «не тот рычаг, которым стоит пользоваться», клише вроде «терпеть молча»
- [stated] хочет сокращать расход токенов там, где это возможно
- [stated] требует спрашивать разрешения перед рендером PDF (soffice/pdftoppm) для визуальной проверки — не делать это по умолчанию на каждую правку
- [stated] требует спрашивать разрешения перед пересборкой .docx файла — не пересобирать при каждом небольшом изменении текста
- [stated] предпочитает точечные правки (найти фрагмент → заменить) вместо пересборки/перегенерации всей главы или файла целиком
- [stated] резко реагирует на бесполезный расход токенов — не выполнять действия сверх того, что реально нужно для запроса (лишние пересборки zip/архива, повторные проверки, дублирующие вебфетчи одного и того же источника)
- [stated] недоволен, когда Claude передаёт агенту инструкцию с числами/списками/проверками, не сверив их фактически сам — приводило к нескольким лишним раундам правок подряд (2026-09-15, реестр Темы 5); перед отправкой любой инструкции с конкретными числами или проверяемым условием Claude обязан сам проверить это (grep/скрипт), а не полагаться на память или прикидку
- [stated] тексты тем присылать ему только в формате .docx (решение 2026-09-22); оглавление темы оформлять как в Темах 1–2
- [stated] подписи-источники в тексте тем (сквозная привязка/нумерация) не прорабатывать сейчас — собирать после завершения всех тем
- [stated] не хочет сам думать о том, откуда Claude брать материалы проекта (например, текст Темы 1): ожидает, что Claude сам достаёт нужное из репозитория — репозиторий для этого и ведётся; просьбы приложить файл, который уже есть в репозитории, его раздражают
- [stated] список клинических источников во всех темах оформлять ТОЛЬКО как в Теме 5 (окончательное решение 2026-09-30, отменяет вариант «как в Темах 1–4» того же дня): заголовок «Клинические и научные источники», шапка-абзац как в Теме 5, жирные названия групп без строки-пояснения, сквозная нумерация, запись «N. Источник. Название, выходные данные — какое утверждение главы на нём стоит. Оговорка»; стандарт — editorial/format-spiska-istochnikov-v2.0.md
- [stated] 2026-10-07 подтвердил стандарт Темы 5 после сравнения с форматом Тем 1–3: в списке должно быть видно, на чём держится каждое утверждение главы, чтобы врач сразу видел слабые места; формат Тем 1–3 («Организация — Название» без пояснения) не использовать; остальные темы привести к стандарту позже
- [stated] раздражается, когда приходится повторять одно и то же требование несколько раз — эталон оформления брать из уже готовой темы, на которую он указал, а не придумывать свой вариант
- [stated] хочет делегировать часть работы по проекту субагентам, но вводить их по одному — много агентов сразу его запутает (2026-10-07); впереди — сводная проверка всех тем: стиль изложения, логика, кросс-ссылки
- [stated] решил (2026-10-07): один агент «сверщик» отвечает и за сверку между темами, и за репозиторий (SAVE THEME) — «проверяющий, сверяющий и соединяющий»; сводную сверку всех тем отложить, пока не написаны оставшиеся темы
- [stated] если сайт закрыт для машинной проверки, давать ему релевантные рабочие ссылки, чтобы он сам прошёл по ним и скачал или открыл документ (2026-10-07)
- [stated] план (содержание книги, план разделов темы, coverage Content Map) можно менять всегда, когда найдены новые положения или решения: работа над улучшением материала, а не над сохранением плана (2026-10-08, записано в AGENTS.md)
- [stated] тема должна давать читательнице всю нужную информацию на месте: повторы из других тем допустимы с отсылкой «подробнее — Тема N», если нужны для логики темы и не выглядят избыточными (2026-10-08, записано в AGENTS.md)
- [stated] вместо термина «спина темы» писать «основа темы» — так понятнее по-русски (2026-10-08, записано в AGENTS.md)
- [stated] не спрашивать у него доступ к проверенным доказательным сайтам и разрешения на действия агентов: разрешения фиксируются на весь проект для всех агентов, чтобы работа шла в фоне без его постоянного присутствия (2026-10-08)
- [stated] промт «медицинский шеф-редактор» заложен в проект (editorial/prompt-shef-redaktor.md, 2026-10-08): пользователь вызывает его для проверки каждой темы перед отправкой врачу
- [stated] вопросы «проверить врачу» и пометки ПРОВЕРИТЬ сначала прорабатывать самостоятельно — искать доказательные первоисточники; только если не нашлось, ставить пометку врачу и продолжать работу дальше (2026-10-09)
- [stated] статьи и руководства с платным доступом (например, ACOG CPG, журнальные полные тексты) не покупает — в списки на ручное скачивание их не включать; утверждения на таких источниках оставлять «по реферату» (2026-10-14)
- [stated] советы в тексте тем не должны вести «в никуда»: каждое «скажите врачу / попросите / обратитесь» доводить до конкретного шага, чтобы женщина, читая, получала точное решение, что делать; авторские советы без продолжения не оставлять как есть (2026-10-14)
- [stated] не хочет загружать массивные PDF-источники в GitHub (источники обновляются; GitHub не для них): в репозитории вести реестр ссылок на источники, по которому видно, что ещё найти и что Claude не смог открыть; скачанные файлы держит у себя (2026-10-15); впереди — проверка каждой темы на источники
- [stated] правки в его тексты присылать редлайном: удалённое — красным зачёркнутым, новый текст — фиолетовым (2026-10-23; раньше, с 2026-10-18, новый текст был обычного цвета)
- [stated] сделал «Стандарт научной и литературной редактуры» v1.4 (editorial/standart-redaktury-v1.4.md) временно главным документом редактуры, чтобы оценить текст, сделанный по нему; сверка с Разделом 0 и другими темами и список источников по стандарту остаются обязательными (2026-10-23)
- [stated] «необходимо», «следует», «не следует» — часть голоса книги, канцеляритом не считать (2026-10-23, стилистический промпт v1.2)
- [stated] не присылать файлы, которые он не просил (например, отдельный редлайн «дополнений» или промежуточные версии) — только запрошенное (2026-10-21)
- [stated] при стилистической правке тем по промпту Тем 1–4 (Темы 5, 6, 7 по очереди, раздел за разделом) отдавать только чистый файл темы и короткий отчёт; редлайн — только по запросу (2026-10-21)
- [stated] при работе с темами всегда добавлять отсылки к другим темам/разделам (в т.ч. Раздел 0), где это нужно, чтобы сохранять общую собранность книги — не откладывать на общий проход (2026-10-21)
- [stated] не нагружать его в чате подробными отчётами о правках: журнал правок Claude сам записывает в репозиторий (README темы), а в чате — только результат (2026-10-21)
- [stated] в текстах тем не допускает многоабзацных рассуждений о второстепенном (пример — абзацы про отменённые буквенные категории FDA в 7.1): излагать по существу и коротко то, что нужно читательнице (2026-10-21)
- [stated] при любой дальнейшей проработке тем вносить корректировки в содержание книги (editorial/soderzhanie-knigi.md и .docx) вместе с темой; структура всех тем — двухуровневая, как в Темах 1–5 и 11 (2026-10-22, записано в AGENTS.md)
- [stated] после неудачной правки Темы 7 не доверяет Claude «слепо»: правки в его тексты сначала предлагать редлайном, в текст не вносить без его решения (2026-10-22)
- [stated] подробные справочные тексты (например, разбор исследований препаратов) на сайте будут свёрнуты в аккордеоны — их оставлять, если изложение верное, а не вырезать как лишние подробности (2026-10-22)
- [stated] в текстах тем нужна «человечность»: без жёстких выражений, способных испугать женщину (образец тона — его Тема 7); возможный вред — с модальностью источника, без каталога худших исходов, рядом с риском — от чего он зависит (2026-10-23, записано в стандарт v1.4, п. 9.11)
- [stated] в его авторских текстах переписывать только то, что реально необходимо, а не всё подряд; правки идут по разделам, по шагам, редлайном (2026-10-27, записано в AGENTS.md)
- [stated] при расхождении темы с Разделом 0 главный всегда Раздел 0: новый текст писать по Разделу 0, старый оставлять в редлайне и помечать «ПРОВЕРИТЬ»; торговые марки в темах не удалять; подробности оставлять под аккордеонами — книга будет в онлайн-формате (2026-10-27)

---

## Редакционные принципы (editorial-principles)

### Режимы работы
- [stated] Two working modes are explicitly distinguished: "by the prompt" (preserve volume, flag duplicates only) vs. "Theme 1–3 mode" (actively propose cuts and rewrites)
- [stated] Dima specifies which mode applies at the start of each section

### Строение текста
- [stated] Volume is not a quality metric — the goal is eliminating true functional duplicates, not shortening texts
- [stated] Explanatory depth, working techniques, reassurance passages, and reference tables are protected from cuts
- [stated] "Layered repetition" is the core structural failure pattern: the same material presented in prose, then table, then algorithm, then control questions — this is what to watch for and eliminate
- [stated] Unified chapter structure: title → table of contents with subsections → optional intro paragraph → sections → *Коротко о главном (Итоги главы)* → clinical sources
- [stated] All themes must match Themes 1 and 2 in structure and writing style (decided 2026-09-16); Dima does not care about text-architecture / tone-of-voice spec versions or "pilot theme" concepts
- [stated] Project rules that complicate work or block starting themes are to be removed
- [stated] New themes: write the chapter directly without deep pre-verification or lengthy reconnaissance; keep content, mark unconfirmed claims with a "needs confirmation" tag; sources are found later by Dima or Claude
- [stated] The book must be engaging reading, not just a dry reference; listing theme/section numbers up front is bad form ("моветон") — readers will close the book
- [stated] Pregnant readers need simple, plain-language presentation — not specialist-style algorithms or academic checks (e.g. "check the author's credentials"); Dima has had to repeat this requirement (2026-10-20)
- [stated] Heading style "B" — "[Topic]: [what the reader learns]" — is the book-wide standard for chapter/section headings; subsection headings remain short nominal groups

### Источники и пометки
- [stated] Source direction rule: source → claim; never reverse-engineer a source to justify a pre-written claim
- [stated] `[ПРОВЕРИТЬ]` tags explain what was checked and why the question remains open, distinguishing "not found" from "standard doesn't exist"
- [stated] Active tags: `[ПРОВЕРИТЬ]` and `[ОЧЕВИДНОЕ?]`
- [stated] Retired tags: `[ВОПРОС ЮЛИИ]`, `[ОТ РЕДАКТОРА]`, `[ИСТОЧНИК]`, `[ОСПОРЕНО]`
- [stated] `DISPUTED-CLAIMS.md` is the single source of truth for open questions to the medical consultant; other files reference it rather than duplicate content
- [stated] Fact-checking is Dima's responsibility unless delegated — Claude flags items needing verification with `[ПРОВЕРИТЬ]` but does not independently verify inline unless asked

### Порядок работы
- [stated] Standard editorial workflow: upload chapter file → reader-question test (§10 of text-architecture spec: "what questions will a reader have after finishing this section?") → identify gaps, structural issues, claims needing verification → draft insertions and edits in chat → Dima applies changes manually → re-upload updated file → further review
- [stated] Repository operations are handled by Claude Code via terminal prompts drafted by Claude in chat
- [stated] Dima uses the terminal as a "save button" for commits; browser chat is the primary working environment

### Как вести себя с автором
- [stated] When Dima uploads a file for revision, take it as the working text and make requested edits directly — do not cross-reference repository rules or raise structural compliance concerns unless explicitly asked
- [stated] Accuracy over agreement: hold a position until a new argument or fact appears rather than shifting because Dima pushes back
- [stated] When there is a disagreement, explicitly name what is correct and what is not in Dima's objection

### Решения 16.09.2026
- [stated] Themes 1 and 2 are the reference for structure and writing style of all themes; no "pilot theme" concept; rules that block starting themes or complicate the project are to be removed
- [stated] New themes are written directly without deep pre-verification or reconnaissance; unconfirmed claims stay in the text with a verification tag rather than being cut
- [stated] No separate midwife-editor will be sought: the doctor alone reviews themes, combining the medical check with the midwife-applicability check
- [stated] Project working notes and agent prompts (`claude/*.md`) should live in the repository, not only in the claude.ai project knowledge base

### История
- [stated] Theme 3 was incorrectly marked as a style canon prematurely — this error should not be repeated; canon designation requires explicit approval after full review
- [stated] Inline source tags / source attribution per paragraph are deferred book-wide: sources will be assembled after all themes are finished (decided 2026-09-22)

### Решения 21.10.2026
- [stated] Themes 1–4 after the doctor's review are the approved language/style canon for restyling all other themes (Dima: their style is "приемлемый")
- [stated] Chief-editor prompt and the Themes 1–4 style prompt stay as two separate prompts, applied in sequence (content/structure first, then style) — not merged

### Решения 22.10.2026
- [stated] Book contents (editorial/soderzhanie-knigi) are approved; every theme follows the two-level structure of Themes 1–5 and 11, and any further theme work must also update the contents
- [stated] Drug efficacy is not to be judged by Russian clinical recommendations or Russian drug studies (Dima considers them potentially bought by manufacturers); rely on independent international evidence
- [stated] Detailed reference material (e.g. on specific drugs, humidifier care) can stay in the text as accordions on the website rather than being cut
- [stated] Dima does not trust Claude's edits blindly: substantive changes come as redline proposals first; text is changed only on his go-ahead

### Решения 23.10.2026
- [stated] Project rule: don't send the reader to another theme for details — put the needed material (numbers, explanations) in place, under an accordion if large; figures must match the theme where they were already checked
- [stated] Text must stay humane: no harsh phrasing that could frighten a pregnant woman — his own rewrite of Theme 7 is the example of the right tone
- [stated] Editor may add, cut, move or remove medical information for logic and clarity (with targeted verification of new facts); scientific detail goes under accordions, not the main text (added to standard v1.4)

### Решения 27.10.2026
- [stated] In Dima's own rewritten theme text, edit only what is really necessary (factual error, mismatch with Раздел 0/other themes, unclear action, rule violation) — do not rewrite everything; each edit needs a stated reason
- [stated] Раздел 0 always wins on discrepancies: theme text is rewritten per Раздел 0, old text kept struck in redline, marked [ПРОВЕРИТЬ]
- [stated] Full detailed explanations stay (book goes online; accordions keep it compact); all trade/brand names are kept; cross-theme references are checked and kept so they don't get lost
- [stated] Work theme by theme section by section; send only the edited section's redline, not the whole theme file; sources are compiled by the source agent after the theme text is approved

---

## Защита HTML-версии книги (book-protection)

Подробно — `editorial/html-zashchita.md`.

- [stated] 2026-10-20 принял к реализации меры защиты HTML-книги от копирования: помехи в коде страницы (запрет контекстного меню, копирования, горячих клавиш F12/Ctrl+U/Ctrl+S/Ctrl+P, скрытие при печати); постраничная выдача текста с сервера по логину вместо одного файла; персональные водяные знаки читателя (видимые и невидимые); юридическая защита (©, условия использования, фиксация авторства, жалобы на пиратские копии)
- [stated] ограничение скорости выдачи страниц на сервере — не использовать
- [stated] хочет добавить скрытый встроенный текст (невидимый на странице), который попадает в копию, если запрет копирования обойдён
- [stated] 2026-10-20 принял способ реализации скрытого текста: прятать через CSS (position:absolute, 1px, clip-path), а не цветом фона; aria-hidden="true"; случайные разные названия классов; вставки в середину предложений; в скрытый текст подставлять ID читателя (работает как водяной знак); вставки расставлять автоматически скриптом при сборке HTML, а не вручную в текстах тем
- [stated] главное ограничение: меры защиты не должны заметно увеличивать размер файлов и время загрузки книги на устройствах; меры, которые почти не влияют на загрузку, брать в работу
- [stated] 2026-10-20 в работу по этому критерию: подмена части кириллицы латиницей при копировании; подпись-источник к скопированному фрагменту; шрифтовая обфускация только для отдельных ценных фрагментов (таблицы, протоколы); ограничение сеансов на аккаунт (задаётся в настройках GetCourse, в коде книги не делается); ссылки на главы с коротким сроком действия; запрет встраивания в чужие сайты (X-Frame-Options / frame-ancestors); ловушки для парсеров; мониторинг копий
- [stated] не брать: перестановку фрагментов текста в коде с пересборкой через CSS; отдельное шифрование текста главы (выдача глав через сервер уже принята)
- [stated] 2026-10-20 отрисовку фрагментов в canvas/картинками исключил из-за веса картинок; заменил шрифтовой обфускацией тех же фрагментов
- [stated] 2026-10-20 планирует размещать книгу как урок(и) GetCourse с доступом по логину GetCourse, чтобы управлять доступами; книга должна отображаться и в мобильном приложении GetCourse
