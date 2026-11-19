# Проверка ссылок списка источников Темы 3 (редакция автора от 19.11.2026)

Дата: 2026-11-19. Задача 5 («Проверка ссылок»). Файл: `work/tema3-2026-11-19-v2.docx` (в репозиторий не коммитится), раздел «Клинические и научные источники», 38 записей, все 38 — гиперссылки в `word/_rels/document.xml.rels`. Пары «запись → адрес» получены скриптом из `word/document.xml` (w:hyperlink r:id → Target), порядок гиперссылок совпадает с нумерацией записей [1]–[38].

## Итоги

- Работает: 21 (адрес открыт агентом, документ на месте); ещё 8 подтверждены по PubMed (страницы PubMed, bjsm.bmj.com и OUP агенту закрыты: сверены название, журнал, год, том, страницы, pii, DOI).
- Заменено: 0. Мёртвых адресов и адресов, ведущих на другой документ, нет.
- Закрыто агенту и передано пользователю: 9 (записи ручной проверки 120–128 в `sources/skachat-vruchnuyu.md`): [1], [3], [4], [8], [15], [23], [25], [28], [32]. Из них по-настоящему не подтверждены два адреса: [8] (СП 2.1.4284-26, файл на сайте Роспотребнадзора) и [15] (ACSM, DOMS).

Пять главных находок:

1. Запись [21]: адрес верный, название нет. PDF `gtg-37b-1.pdf` называется «Thromboembolic Disease in Pregnancy and the Puerperium: Acute Management» (GTG 37b, 3-е издание, апрель 2015); названия из записи («Diagnosis and treatment of venous thrombosis in pregnancy and after birth») на странице RCOG нет. На странице RCOG: «reviewed in 2022 – an update is in development».
2. Запись [35]: PDF называется «Exercise in Pregnancy» (C-Obs 62, действует с марта 2020), в записи — «Exercise During Pregnancy»; следующий пересмотр был назначен на март 2023 — срок истёк.
3. Запись [8]: СП 2.1.4284-26 существует (постановление № 20 от 02.06.2026, Минюст 02.06.2026 № 86856, с 01.09.2026, срок 6 лет), но адрес файла на 02.rospotrebnadzor.ru подтвердить не удалось, а температуры приложения 4 (25–28, 26–29, 35–39 °C) по тексту не сверены.
4. Запись [10]: в PubMed (PMID 32022807) статья вышла в 2019 году (Acta Bioeng Biomech 2019;21(4):93–99), в записи указан 2020. Это исследование посадки на велосипеде, не беременных.
5. Записи [1] и [32] (ACOG), [23] (NICE NG127), [15] (ACSM) агенту закрыты: содержание, приписанное им в списке, по самим документам не сверено. Для [1] проверен только реферат PubMed; PMID 33481513 в PubMed — комментарий к заключению, а не оно само.

## Отмены и замены документов, замеченные попутно

- СП 2.1.3678-20 утрачивает силу с 01.09.2026 (заменён СП 2.1.4284-26; «Гарант», hotlaw/2116371). В репозитории (`*.md`) упоминаний СП 2.1.3678-20 нет.
- RANZCOG C-Obs 62: срок пересмотра (март 2023) истёк; более нового издания специально не искал (решение 07.10.2026).
- RCOG GTG 37b (2015): страница сообщает «reviewed in 2022 – an update is in development».

## Таблица

Способ проверки: WebFetch открывает адреса, которые перед этим вернула выдача WebSearch; остальные получают «адрес не разрешён». Командная строка в интернет не выходит и не использовалась.

| Тема | Запись | Адрес | Итог | Что сделать |
|---|---|---|---|---|
| 3 | [1] ACOG CO 804, 2020 | https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2020/04/physical-activity-and-exercise-during-pregnancy-and-the-postpartum-period | закрыт агенту, передан пользователю. WebFetch: ошибка запроса. Адрес с тем же названием вернул поиск по acog.org; PubMed 32217980 (Obstet Gynecol 2020;135(4):e178–e188), DOI 10.1097/AOG.0000000000003772 | запись 122 |
| 3 | [2] Mottola et al., BJSM 2018 (2019 Canadian guideline) | https://bjsm.bmj.com/content/52/21/1339 | работает (подтверждён по PubMed). Страница bjsm.bmj.com агенту не разрешена; PubMed 30337460: название, BJSM 2018;52(21):1339–1346, pii 52/21/1339 (совпадает с адресом), DOI 10.1136/bjsports-2018-100056 | оставить; запасной адрес https://doi.org/10.1136/bjsports-2018-100056 |
| 3 | [3] WHO, Guidelines on physical activity and sedentary behaviour, 2020 | https://www.ncbi.nlm.nih.gov/books/NBK566046/ | закрыт агенту, передан пользователю. NBK566046 отдаёт агенту reCAPTCHA. Документ на месте: https://www.who.int/publications-detail-redirect/9789240015128 открыт («WHO guidelines on physical activity and sedentary behaviour», 2020) | запись 124 |
| 3 | [4] WHO, Guideline on haemoglobin cutoffs, 2024 | https://www.who.int/publications/i/item/9789240088542 | закрыт агенту, передан пользователю. Точный адрес агенту не разрешён; страница того же ISBN 9789240088542 открыта по https://www.who.int/publications-detail-redirect/9789240088542: название и 5 марта 2024 совпали | запись 125 |
| 3 | [5] SMFM Consult Series 50, 2020 (reaffirmed 2025) | https://publications.smfm.org/publications/326-society-for-maternal-fetal-medicine-consult-series-50/ | работает. открыта: название, №50, 2020, «Reaffirmed 2025» | — |
| 3 | [6] CDC, How to Measure Physical Activity Intensity | https://www.cdc.gov/physical-activity-basics/measuring/index.html | работает. открыта: относительная интенсивность 0–10, умеренная 5–6, разговорный тест | — |
| 3 | [7] Ravanelli et al., BJSM 2019;53:799–805 | https://pubmed.ncbi.nlm.nih.gov/29496695/ | работает (подтверждён по PubMed). PMID 29496695: название, авторы, BJSM 2019;53(13):799–805, DOI 10.1136/bjsports-2017-097914; в реферате: погружение ≤33,4 °C до 45 мин | оставить |
| 3 | [8] СП 2.1.4284-26 (постановление № 20 от 02.06.2026), приложение 4 | https://02.rospotrebnadzor.ru/upload/iblock/749/td3cen07sl6tt5sp3z9kpc09onwb10br/SP_2.1.4284_26.pdf | закрыт агенту, передан пользователю. Адрес на 02.rospotrebnadzor.ru агенту не разрешён и в выдаче не найден. Документ существует: Гарант (hotlaw/2116371) — постановление № 20 от 02.06.2026, Минюст 02.06.2026 № 86856, с 01.09.2026, срок 6 лет, СП 2.1.3678-20 утрачивает силу | запись 123 |
| 3 | [9] CDC, Chloramines and Pool Operation | https://www.cdc.gov/healthy-swimming/toolkit/chloramines-and-pool-operation.html | работает. открыта: хлорамины, вентиляция (материал для операторов бассейнов) | — |
| 3 | [10] Millour et al., saddle height in cycling, PMID 32022807 | https://pubmed.ncbi.nlm.nih.gov/32022807/ | работает (подтверждён по PubMed). PMID 32022807: название совпадает; Acta Bioeng Biomech 2019;21(4):93–99. В записи списка год 2020, в PubMed — 2019; реферат: Holmes 25–35° в статике | оставить; год в записи проверить (в PubMed 2019) |
| 3 | [11] AHA, Warm Up, Cool Down | https://www.heart.org/en/healthy-living/exercise-and-physical-activity/fitness-basics/warm-up-cool-down | работает. открыта | — |
| 3 | [12] HSE, Dizziness and fainting in pregnancy | https://www2.hse.ie/conditions/dizziness-and-fainting-pregnancy/ | работает. открыта (www2.hse.ie) | — |
| 3 | [13] CDC, Heat and Pregnancy; Clinical Overview of Heat and Pregnancy | https://www.cdc.gov/heat-health/hcp/clinical-overview/heat-and-pregnant-women.html | работает. открыта страница Clinical Overview; вторая страница из названия (Heat and Pregnancy) гиперссылкой не снабжена | — |
| 3 | [14] AHA и Красный Крест, 2024 Guidelines for First Aid | https://cpr.heart.org/en/resuscitation-science/2024-first-aid-guidelines | работает. открыта (cpr.heart.org) | — |
| 3 | [15] ACSM, Delayed Onset Muscle Soreness | https://www.acsm.org/docs/default-source/files-for-resource-library/delayed-onset-muscle-soreness-%28doms%29.pdf | закрыт агенту, передан пользователю. WebFetch: адрес не разрешён, в выдаче по названию не найден (в той же папке acsm.org найден другой файл) | запись 126 |
| 3 | [16] Aldabe et al., relaxin и PGP, 2012, PMID 22310881 | https://pubmed.ncbi.nlm.nih.gov/22310881/ | работает (подтверждён по PubMed). PMID 22310881: название, Eur Spine J 2012;21(9):1769–76, DOI 10.1007/s00586-012-2162-x; PMC3459115 есть | оставить |
| 3 | [17] Theodorsen et al., J Physiother 2024, PMID 38472049 | https://pubmed.ncbi.nlm.nih.gov/38472049/ | работает (подтверждён по PubMed). PMID 38472049: название совпадает; J Physiother 2024;70(2):142–148 | оставить |
| 3 | [18] Cabral et al., J Physiother 2025;71:254–259, PMID 41006087 | https://pubmed.ncbi.nlm.nih.gov/41006087/ | работает (подтверждён по PubMed). PMID 41006087: J Physiother 2025;71(4):254–259 совпадает; название в PubMed «Transversus abdominis and rectus abdominis activation exercises do not alter inter-recti distance in pregnant women», в записи — русское описание | оставить; в записи можно дать оригинальное название |
| 3 | [19] NICE NG201, Antenatal care, 2021 | https://www.nice.org.uk/guidance/ng201/chapter/Recommendations | работает. открыта (chapter/Recommendations); п. 1.3 физическая активность, п. 1.4 физиотерапия при PGP | — |
| 3 | [20] RCOG, Pelvic girdle pain and pregnancy | https://www.rcog.org.uk/for-the-public/browse-our-patient-information/pelvic-girdle-pain-and-pregnancy/ | работает. открыта; «Published: June 2015» | — |
| 3 | [21] RCOG GTG 37b (в записи — «Diagnosis and treatment of venous thrombosis…») | https://www.rcog.org.uk/media/wj2lpco5/gtg-37b-1.pdf | работает; название записи не совпадает. PDF gtg-37b-1.pdf открыт: название «Thromboembolic Disease in Pregnancy and the Puerperium: Acute Management», GTG 37b, 3-е изд., апрель 2015. Страница RCOG: «reviewed in 2022 – an update is in development»; названия из записи на странице нет | адрес верный; название записи привести к названию документа (предложение в основную сессию) |
| 3 | [22] ACOG Clinical Consensus No. 4, UTI, 2023 | https://www.acog.org/clinical/clinical-guidance/clinical-consensus/articles/2023/08/urinary-tract-infections-in-pregnant-individuals | работает. открыта: «Urinary Tract Infections in Pregnant Individuals», Clinical Consensus No. 4, август 2023 | — |
| 3 | [23] NICE NG127, Suspected neurological conditions | https://www.nice.org.uk/guidance/ng127/chapter/recommendations-for-adults-aged-over-16 | закрыт агенту, передан пользователю. WebFetch: ошибка запроса. Адрес с этим названием дала выдача nice.org.uk; карточка https://www.nice.org.uk/guidance/ng127 открыта (проверена в сентябре 2021) | запись 120 |
| 3 | [24] NICE NG210, Pelvic floor dysfunction, 2021 | https://www.nice.org.uk/guidance/ng210/chapter/Recommendations | работает. открыта: профилактика и нехирургическое лечение; обучение мышц тазового дна, контроль под наблюдением | — |
| 3 | [25] IUGA, Pelvic Floor Exercises | https://www.yourpelvicfloor.org/conditions/pelvic-floor-exercises/ | закрыт агенту, передан пользователю. Страница агенту не разрешена. Адрес приведён в оглавлении yourpelvicfloor.org/conditions (открыто) под названием «Pelvic Floor Exercises» | запись 127 |
| 3 | [26] Woodley et al., Cochrane CD007471.pub4, 2020 | https://www.cochrane.org/evidence/CD007471_how-effective-pelvic-floor-muscle-training-undertaken-during-pregnancy-or-after-birth-preventing-or | работает. открыта: Woodley SJ и др., выпуск 5, 07.05.2020, DOI 10.1002/14651858.CD007471.pub4 | — |
| 3 | [27] Sobhgol et al., Int Urogynecol J 2020, PMID 32506232 | https://pubmed.ncbi.nlm.nih.gov/32506232/ | работает (подтверждён по PubMed). PMID 32506232: «The effect of antenatal pelvic floor muscle exercises on labour and birth outcomes…», 2020;31(11):2189–2203, DOI 10.1007/s00192-020-04298-1 | оставить |
| 3 | [28] NHS Forth Valley, Electrical Muscle Stimulator | https://nhsforthvalley.com/health-services/az-of-services/maternity/pelvic-health-physiotherapy/physiotherapy-leaflets-aftercare/electrical-muscle-stimulator/ | закрыт агенту, передан пользователю. Адрес записи агенту не разрешён; тот же листок открыт по https://nhsforthvalley.com/?p=3812218 («Electrical Muscle Stimulator User Information», противопоказания в листке есть) | запись 128 |
| 3 | [29] CDC NIOSH, Physical Job Demands and Reproductive Health | https://www.cdc.gov/niosh/reproductive-health/prevention/physical-demands.html | работает. открыта; название страницы «About Physical Job Demands and Reproductive Health» (в записи «About Physical Demands…») | — |
| 3 | [30] RCOG, Air travel and pregnancy | https://www.rcog.org.uk/for-the-public/browse-our-patient-information/air-travel-and-pregnancy/ | работает. открыта; издание 2016, обновлено январь 2026 | — |
| 3 | [31] CDC HEAR HER, Urgent Maternal Warning Signs | https://www.cdc.gov/hearher/maternal-warning-signs/index.html | работает. открыта; дата на странице 15.05.2024 | — |
| 3 | [32] ACOG, Preterm Labor and Birth (FAQ) | https://www.acog.org/womens-health/faqs/preterm-labor-and-birth | закрыт агенту, передан пользователю. WebFetch: ошибка запроса. Адрес с этим названием дала выдача acog.org | запись 121 |
| 3 | [33] RCOG, When your waters break prematurely | https://www.rcog.org.uk/for-the-public/browse-our-patient-information/when-your-waters-break-prematurely/ | работает. открыта; «Published: June 2019» | — |
| 3 | [34] RCOG, Your baby's movements in pregnancy | https://www.rcog.org.uk/for-the-public/browse-our-patient-information/your-babys-movements-in-pregnancy/ | работает. открыта; «Published: February 2019» | — |
| 3 | [35] RANZCOG, C-Obs 62 (в записи — «Exercise During Pregnancy») | https://ranzcog.edu.au/wp-content/uploads/Exercise-During-Pregnancy-Guidance.pdf | работает; название записи не совпадает. PDF открыт: название «Exercise in Pregnancy», C-Obs 62, действует с марта 2020, следующий пересмотр был назначен на март 2023 | адрес верный; название записи привести к «Exercise in Pregnancy»; срок пересмотра истёк (записать как «пересмотр истёк») |
| 3 | [36] NHS, Exercising in pregnancy (Best Start in Life) | https://www.nhs.uk/best-start-in-life/pregnancy/exercising-in-pregnancy/ | работает. открыта; изменена 26.01.2026 | — |
| 3 | [37] European Hernia Society, rectus diastasis, 2021 | https://academic.oup.com/bjs/article/108/10/1189/6378260 | работает (подтверждён по PubMed). Страница OUP агенту не разрешена; PMID 34595502: Br J Surg 2021;108(10):1189–1191, pii 6378260 (совпадает с адресом), DOI 10.1093/bjs/znab128; PMC10364860 есть | оставить; запасной https://doi.org/10.1093/bjs/znab128 |
| 3 | [38] CDC NIOSH, Heat-related Illnesses | https://www.cdc.gov/niosh/heat-stress/about/illnesses.html | работает. открыта; рассмотрена 03.03.2026 | — |

## Машиночитаемый список замен

Формат: `старый адрес → новый адрес`, старый — точно как в rels. Заменять нечего: каждый адрес либо открыт агентом, либо подтверждён по PubMed, либо оставлен как канонический для закрытого сайта.

```
(замен нет)
```

Предложения по тексту записей (не адреса, текст не правился; решает основная сессия и автор):

```
[21] название записи -> «Thromboembolic Disease in Pregnancy and the Puerperium: Acute Management; Green-top Guideline 37b, 2015» (адрес без изменений)
[35] название записи -> «Exercise in Pregnancy. C-Obs 62, 2020» (адрес без изменений); отметить «пересмотр, назначенный на март 2023, не выполнен»
[10] год записи -> 2019 по PubMed (PMID 32022807)
[1], [3], [4], [8], [15], [23], [25], [28], [32] -> до проверки записей 120–128 сведения, приписанные этим записям, считать не сверенными по документу
```

## Ход работы

Сделано (19.11.2026):
- прочитаны AGENTS.md (начало), `format-spiska-istochnikov-v2.0.md` (раздел 6), `sources/reestr-ssylok.md`, `sources/skachat-vruchnuyu.md` (нумерация, до 119);
- извлечены 38 пар «запись → адрес»;
- проверены все 38: 21 страница открыта, 8 по PubMed, 9 переданы пользователю;
- внесены записи 120–128 в `sources/skachat-vruchnuyu.md`, группа «Тема 3» (T3-01–T3-38) в `sources/reestr-ssylok.md`.

Осталось: ответы пользователя по записям 120–128; сверка содержания записей по самим документам (задача 4 / реестр доказательств Темы 3) этим отчётом не выполнялась — здесь проверены только адрес и опознание документа.

Ограничения: страницы PubMed и NCBI Bookshelf отдают агенту reCAPTCHA; acog.org и nice.org.uk (NG127) вернули ошибку запроса; многие адреса WebFetch не разрешал без предварительной выдачи поиска. Обходов не делалось.
