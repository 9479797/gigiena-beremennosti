---
name: methodical-review
description: >-
  Независимая методическая экспертиза образовательных, просветительских и
  научно-популярных текстов: соответствие цели и аудитории, педагогическая
  логика, порядок объяснения, когнитивная нагрузка, ясность и выполнимость
  рекомендаций, границы применимости и риск неверного толкования. Использовать,
  когда пользователь просит «проверить методику», «подходит ли текст
  аудитории», «оценить структуру объяснения», «нет ли риска, что читатель
  поймёт неправильно». Навык не переписывает текст; не заменяет научную
  рецензию, фактчекинг и медицинскую экспертизу.
---

# Methodical Review

## Purpose

Провести независимую методическую экспертизу готового текста.

Основной вопрос:

> Насколько текст методически правильно построен для своей предполагаемой аудитории и цели?

Skill не должен превращать проверку в обычную корректуру и не должен автоматически переписывать текст.

Он должен сначала определить:
1. для кого написан текст;
2. какую задачу он решает;
3. чему должен научить / что должен объяснить;
4. какие действия или выводы читатель должен сделать после чтения.

После этого проверить, действительно ли содержание и структура текста обеспечивают достижение этой цели.

---

# Project integration — «Гигиена беременности»

**В маршруте книги «Гигиена беременности» (Editorial v1.7) этот этап между Checkpoint 4 и Checkpoint 5 заменён живой экспертизой применимости акушерки-редактора** (`editorial/human-review-roles-v1.0.md`, раздел 3; `editorial/pregnancy-book-editorial-v1.7.md`, раздел 8). Живой специалист с практикой проверяет ту же педагогическую логику плюс реальность применения. Модельный `methodical-review` в закреплённой точке маршрута больше не запускается и `USER GATE` в маршруте сам по себе не создаёт.

Навык остаётся доступен **для разовой проверки по прямому запросу пользователя** («проверь методику», «подходит ли текст аудитории», «оцени структуру объяснения», «нет ли риска неверного прочтения»), а также как справочный методический слой внутри prepress-аудита.

При разовом вызове:

1. Проводить независимую проверку аудитории, педагогической логики, применимости, cognitive load и риска неверного толкования.
2. Не переписывать текст и не исправлять найденные дефекты молча. Отчёт описывает проблему, её влияние на читателя и маршрут возврата в ответственный этап.
3. Дефекты маршрутизировать в этапы v1.7: медицинский или содержательный пробел → Checkpoint 2; разбавленность, композиция, списки, ритм → Checkpoint 4; дефект reader job или архитектуры → Checkpoint 0 или 1 по масштабу; AI-шаблонность → Checkpoint 3.
4. Не запускать `$russian-book-editor`. Не принимать за пользователя архитектурные, медицинские или содержательные решения и не изменять approved canon.

При конфликте правил внутри проекта использовать приоритет:

`явные решения пользователя → медицинская безопасность и заключение врача-рецензента → approved canon → content map → pregnancy-book-editorial-v1.7 → независимые проверки → исходный текст`.

---

# Scope

Skill применяется прежде всего к:

- образовательным статьям;
- просветительским материалам;
- учебно-методическим текстам;
- памяткам;
- инструкциям;
- научно-популярным материалам;
- patient education materials;
- материалам для родителей;
- материалам для пациентов;
- профессиональным текстам, предназначенным для обучения.

Для научных статей skill не заменяет научное peer review.

Для медицинских текстов skill не определяет самостоятельно медицинскую истинность утверждений. Медицинские утверждения должны рассматриваться с точки зрения:
- понятности;
- корректности подачи;
- границ применимости;
- риска неправильной интерпретации;
- необходимости обращения к специалисту.

---

# Core Principles

## 1. Do not confuse methodical quality with language quality

Grammar, spelling, punctuation and stylistic polish are secondary.

A grammatically perfect text can be methodically poor.

A stylistically simple text can be methodically excellent.

Prioritize:
1. purpose;
2. audience;
3. learning / informational outcome;
4. logical progression;
5. usability;
6. safety and interpretation;
7. evidence-to-recommendation transition;
8. language.

---

# 2. Identify audience and purpose

Before reviewing, explicitly infer or extract:

- target audience;
- expected prior knowledge;
- context of use;
- intended outcome;
- expected reader action.

If these are not stated, mark:

`AUDIENCE_UNCLEAR`

or

`PURPOSE_UNCLEAR`

Do not silently invent the author's intended audience.

If the audience can only be inferred from the text, label it:

`INFERRED_AUDIENCE`

---

# 3. Check alignment

Evaluate alignment between:

`Purpose → Content → Structure → Explanation → Recommendation → Conclusion`

Ask:

- Does every major section contribute to the stated purpose?
- Are there sections that are interesting but unnecessary?
- Are important elements missing?
- Does the conclusion actually follow from the material?
- Does the text promise more than it delivers?
- Are recommendations supported by the preceding explanation?

Classify problems as:

- `ALIGNMENT_ERROR`
- `ALIGNMENT_WEAK`
- `ALIGNMENT_OK`

---

# 4. Check pedagogical progression

Evaluate whether information appears in a cognitively useful order.

Look for progression such as:

`Context → Problem → Explanation → Principle → Example → Application → Limitations → Summary`

The exact structure may differ by genre.

Do not force one universal structure.

Check for:

- unexplained concepts before prerequisites;
- abrupt jumps;
- excessive detail before the main idea;
- conclusions appearing before explanation;
- recommendations without rationale;
- examples that appear before the principle they illustrate;
- repeated explanation of the same concept;
- missing transitions.

Mark:

`SEQUENCE_PROBLEM`

when the order makes comprehension unnecessarily difficult.

---

# 5. Check information hierarchy

Determine whether the text clearly distinguishes:

- essential information;
- secondary information;
- optional detail;
- exceptions;
- warnings;
- professional/specialist information.

Check whether critical information is visually and logically prominent.

Examples of problems:

- minor detail receives more attention than the main recommendation;
- safety warning appears too late;
- exception is hidden inside a long paragraph;
- key action is buried among background information;
- several recommendations have no priority.

Mark:

`PRIORITY_PROBLEM`

---

# 6. Check cognitive load

Evaluate whether the reader can reasonably process the material.

Check:

- sentence complexity;
- number of concepts introduced simultaneously;
- density of numbers;
- unexplained abbreviations;
- unnecessary terminology;
- long enumerations;
- excessive cross-references;
- repeated switching between topics.

Do not equate "simple language" with "good pedagogy".

The goal is appropriate cognitive load for the intended audience.

Classify:

- `LOW_LOAD`
- `APPROPRIATE_LOAD`
- `HIGH_LOAD`

---

# 7. Check explanation quality

For each important concept ask:

1. Is it introduced?
2. Is it explained?
3. Is its relevance explained?
4. Is the reader told what to do with this information?

A text should not merely provide facts.

Identify transitions of the form:

`Fact → Meaning → Practical implication`

If the text repeatedly stops at:

`Fact → Fact → Fact`

mark:

`EXPLANATION_GAP`

---

# 8. Check recommendation quality

For every important recommendation evaluate:

- What is being recommended?
- To whom?
- Under what conditions?
- Why?
- How should it be applied?
- Are there exceptions?
- When should the reader consult a professional?

Avoid recommendations that are:

- absolute without qualification;
- context-free;
- impossible to implement;
- inconsistent with previous sections;
- too vague to act upon.

For medical or safety-sensitive material pay special attention to:

- universal statements;
- dosage;
- thresholds;
- contraindications;
- exceptions;
- escalation criteria.

---

# 9. Check boundaries of applicability

A methodically strong text tells the reader when a recommendation does NOT apply.

Look for:

- population limitations;
- contraindications;
- special conditions;
- severity thresholds;
- exceptions;
- need for professional assessment.

Mark:

`BOUNDARY_MISSING`

when a recommendation is presented as universal but the text itself suggests that applicability depends on conditions.

Do not infer medical contraindications from general knowledge unless external verification is explicitly requested.

---

# 10. Check reader interpretation risk

This is especially important for medical, educational and safety-related texts.

Ask:

> Could a reasonable reader interpret this sentence in a way that leads to an incorrect or unsafe action?

Potential problems include:

- false reassurance;
- excessive alarm;
- interpreting general advice as personal medical advice;
- treating an example as a universal rule;
- treating a threshold as a guaranteed safety boundary;
- interpreting "usually" as "always";
- interpreting "not necessary" as "never necessary".

Mark:

`MISINTERPRETATION_RISK`

and explain the likely interpretation.

Do not rewrite the medical recommendation unless explicitly asked.

---

# 11. Check terminology

Evaluate whether terminology is appropriate for the audience.

For every specialist term ask:

- Is it necessary?
- Is it explained at first use?
- Is the explanation understandable?
- Is the same term used consistently?

Classify:

`TERM_UNEXPLAINED`
`TERM_INCONSISTENT`
`TERM_TOO_TECHNICAL`

Do not replace specialist terminology merely to make the text simpler if the term is necessary.

---

# 12. Check examples and practicalization

Examples should clarify principles rather than introduce unrelated information.

Check:

- Is the example representative?
- Is it clearly identified as an example?
- Could readers mistake it for a universal prescription?
- Does it actually illustrate the preceding concept?
- Are examples balanced against exceptions?

Mark:

`EXAMPLE_MISLEADING`

when an example may be interpreted as a general rule.

---

# 13. Check internal consistency

Compare statements across the entire document.

Look for:

- different recommendations for the same issue;
- inconsistent terminology;
- inconsistent thresholds;
- conflicting classifications;
- contradiction between introduction and conclusion;
- contradiction between general rule and later exception;
- recommendations that conflict with the text's own stated principles.

Every finding must cite both relevant passages.

Classify:

`INTERNAL_CONTRADICTION`

or

`INTERNAL_TENSION`

Use `INTERNAL_TENSION` when statements can be reconciled but the text does not explain how.

---

# 14. Check conclusion and retention

The conclusion should answer:

- What should the reader remember?
- What should the reader do?
- What are the limits of the advice?

Check whether the conclusion:

- introduces new information;
- merely repeats headings;
- contains recommendations absent from the main text;
- omits the most important practical points;
- accurately reflects the body.

Mark:

`CONCLUSION_MISALIGNED`

when the conclusion does not accurately represent the body.

---

# 15. Check actionability

For practical texts, determine whether the reader can answer:

- What should I do?
- How should I do it?
- How often / when?
- What should I avoid?
- When should I stop?
- When should I seek professional help?

A text can be informative but not actionable.

Mark:

`ACTIONABILITY_GAP`

when important information cannot be translated into a reasonable action.

---

# 16. Separate methodological findings from factual findings

This skill must NOT silently decide whether a scientific or medical claim is true.

For example:

Bad finding:

> "The statement about vitamin D is incorrect."

Preferred finding:

> "The text presents a specific vitamin D dosage as a general recommendation. The methodological issue is that the conditions under which this recommendation applies are not specified. Medical validity of the dosage requires external verification."

Use:

`FACTUAL_VERIFICATION_NEEDED`

when factual correctness cannot be established from the supplied material.

---

# 17. Medical and safety-sensitive texts

For medical content, add a dedicated safety layer.

Check:

### A. False reassurance
Could the text cause a reader to delay necessary medical attention?

### B. Overgeneralization
Is advice presented as universally applicable?

### C. Personalization risk
Could general educational information be mistaken for individualized medical advice?

### D. Escalation
Does the text clearly identify situations requiring professional evaluation where the text itself discusses severity or risk?

### E. Numerical thresholds
Are numerical values presented with enough context?

### F. Dosage
Are doses presented as general information or as individualized prescriptions?

Do not determine medical correctness without appropriate sources.

---

# Project routing of findings

В проекте «Гигиена беременности» Methodical review не устраняет дефект самостоятельно. Для каждого `Critical`, `Major` и любого другого замечания, которое требует изменения текста, указывать ответственный маршрут.

Использовать следующую логику:

- новое, спорное или неподтверждённое медицинское утверждение, вопрос фактической корректности, доказательности, числа, дозы или медицинской границы, а также недостающее объяснение, практическое действие, следующий шаг, условие применимости или safety boundary → `Checkpoint 2 — Медицинская сверка и расширение` (в v1.7 бывшие Checkpoint 2 и 2A объединены);
- дефект reader job, обещания темы, границ или базовой архитектуры → `Checkpoint 0 — Спина темы`;
- крупный дефект книжного черновика или содержательной последовательности, требующий пересборки блока в рамках уже утверждённой архитектуры → `Checkpoint 1 — Черновик`;
- шаблонная AI-подача, искусственная риторика или humanize-дефект → `Checkpoint 3 — Анти-шаблон и человечность`;
- разбавленность, плотность, расплющивание, списки, информационная иерархия, фрагментация, композиция, расположение уже объяснённого материала → `Checkpoint 4 — Плотность, композиция и подача`;
- если требуется выбор пользователя между несколькими содержательно различными вариантами → `USER CHOICE REQUIRED`.

`FACTUAL_VERIFICATION_NEEDED` всегда является маршрутом на медицинскую/доказательную проверку, а не основанием для самостоятельного исправления этим skill.

Не возвращать текст в более ранний Checkpoint без необходимости: локальный дефект направлять только в тот этап, который отвечает за его причину. После исправления повторять Methodical review только тогда, когда изменение затрагивает педагогическую функцию, применимость, интерпретацию, информационную иерархию или другое качество, которое этот gate уже проверял.

Это маршрутизация для разового вызова. В самом маршруте книги (v1.7) методический слой между Checkpoint 4 и Checkpoint 5 ведёт живая акушерка-редактор, а не этот навык.

---

# Severity

Use four levels:

## Critical

Potentially dangerous interpretation, fundamental methodological failure, or major mismatch between purpose and content.

## Major

A problem that materially reduces educational usefulness, creates significant ambiguity, or undermines the text's intended purpose.

## Moderate

A problem that makes comprehension or application harder but does not fundamentally invalidate the material.

## Minor

A local improvement that would increase clarity or usability.

---

# Output format

Produce the following sections.

## 1. Executive summary

Include:

- inferred audience;
- inferred purpose;
- overall methodological assessment;
- 3–7 most important findings.

## 2. Audience and purpose

| Element | Assessment | Evidence |
|---|---|---|
| Audience | ... | ... |
| Purpose | ... | ... |
| Expected reader outcome | ... | ... |

Clearly distinguish stated vs inferred elements.

## 3. Methodological findings

For each finding:

### [SEVERITY] [CODE] — Short title

**Location:** section / paragraph

**Problem:**  
Describe the methodological issue.

**Why it matters:**  
Explain its effect on comprehension, learning, application or safety.

**Evidence from text:**  
Quote only the minimum necessary text.

**Suggested direction:**  
Describe what should be changed conceptually.

**Route:**  
For the Pregnancy Book project, name the responsible Checkpoint or `USER CHOICE REQUIRED`. Outside the project, describe the responsible type of revision without inventing a workflow.

Do not rewrite the passage unless requested.

## 4. Pedagogical structure

Evaluate:

- sequence;
- hierarchy;
- transitions;
- explanation;
- examples;
- conclusion.

## 5. Actionability

List important recommendations and assess:

`Clear / Partially clear / Unclear / Potentially misleading`

## 6. Safety and interpretation

List:

- false reassurance risks;
- overgeneralizations;
- missing boundaries;
- ambiguous thresholds;
- personalization risks.

## 7. Internal consistency

Use:

| Statement A | Statement B | Relationship | Issue |
|---|---|---|---|

## 8. What works well

Do not produce only criticism.

Identify 3–7 concrete methodological strengths.

## 9. Priority revision plan

Separate into:

### Must fix
Problems affecting safety, correctness of interpretation, purpose or major pedagogical structure.

### Should fix
Problems affecting comprehension, hierarchy or actionability.

### Could improve
Editorial and optimization improvements.

## 10. Final assessment

Provide:

- Methodological quality: Excellent / Good / Mixed / Weak / Poor
- Audience fit: Excellent / Good / Mixed / Weak / Poor
- Actionability: Excellent / Good / Mixed / Weak / Poor
- Safety of interpretation: Excellent / Good / Mixed / Weak / Poor

Then provide a concise rationale.

For the Pregnancy Book project, add one non-acceptance handoff line:

- `METHODICAL GATE: READY FOR USER DECISION` — findings are reported and no unresolved methodological issue prevents the user from deciding whether to proceed;
- `METHODICAL GATE: REVISION RECOMMENDED BEFORE CP5` — one or more findings should be routed back before Checkpoint 5;
- `METHODICAL GATE: USER CHOICE REQUIRED` — the next step depends on an unresolved choice between materially different options, to be made by the user.

These statuses do not replace Checkpoint 5 and never authorize automatic transition past the USER GATE.

---

# Important restrictions

1. Do not turn the review into proofreading.
2. Do not rewrite the entire text.
3. Do not silently correct factual claims.
4. Do not invent an audience or purpose.
5. Do not treat general medical knowledge as evidence unless external verification was requested.
6. Do not use the output of another review skill as evidence.
7. Do not penalize a text merely because it does not follow the structure of a scientific paper.
8. Do not require citations for every statement unless the genre or task requires them.
9. Distinguish methodological problems from factual uncertainty.
10. Always explain why a finding matters to the reader.
11. In the Pregnancy Book project this skill runs only on direct request (the route's methodical step is the live midwife-editor); a one-off report does not by itself authorise advancing any Checkpoint.
12. Do not invoke `$russian-book-editor` from Methodical review.
13. Route defects to the responsible Checkpoint instead of silently repairing them inside this skill.