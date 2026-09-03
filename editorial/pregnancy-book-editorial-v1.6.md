---
document_id: pregnancy-book-editorial
document_type: process-spec
version: 1.6.0
status: active
description: Master editorial process specification for developing medical and educational pregnancy materials into engaging, intelligent, book-like narrative nonfiction while preserving source fidelity, medical safety, evidence boundaries, natural human voice, and editorial restraint.
---

# Pregnancy Book Editorial v1.6

## Purpose

Transform dry, fact-heavy medical or educational material into engaging, intelligent, calm, human-sounding narrative nonfiction for pregnant readers.

The goal is NOT to simplify, embellish, or "humanize" the text mechanically.

The goal is:

> Preserve the intelligence and medical value of the source while changing the reader's experience from reference material to a compelling book.

Preserve important source facts, clinically relevant numbers, recommendations, limitations, terminology, and safety boundaries unless editorial analysis shows that a passage is redundant, nonfunctional, misleading, or requires verification.

Do not silently add, correct, reconcile, or replace medical claims with general knowledge.

---


# PROJECT INTEGRATION / ROLE BOUNDARIES

When this process specification governs the Pregnancy Book project:

- `editorial/pregnancy-book-evidence-content-map-v3.0.md` controls the current book architecture, topic boundaries, reader jobs, cross-links, and content/evidence map.
- `themes/theme-1/tema_1_final_canonical.docx` is an approved Theme 1 scheduled for rebuild under the new specification (`editorial/text-architecture-v1.0.md` + `editorial/tone-of-voice-v1.0.md`). It is NOT a quality benchmark, depth reference, style canon, or author-voice reference; do not calibrate other Themes against it.
- `skills/methodical-review.md` governs independent methodological review.
- `$russian-book-editor` governs the final Russian language-and-logic reconstruction after Checkpoint 5 and an explicit user STOP. It is the last development stage allowed to change the text.
- `$pregnancy-book-depth-review` governs Depth review №1 after Checkpoint 2A and Depth review №2 after the final Russian Book Edit.
- `$pregnancy-book-prepress-audit` governs the independent final pre-press verdict after the final Russian Book Edit, Depth review №2, and Regression / Canon Check.
- This file is the **PROCESS AUTHORITY / SOURCE OF TRUTH** for the order of all stages, transition policy, handoffs, returns, state management, final acceptance, and regression/canon control. It is a process specification, not an executable plugin. The only executable `$pregnancy-book-editorial` is `plugins/pregnancy-book-editorial/SKILL.md`.
- If architecture/content-map decisions conflict with this process specification's generic structural suggestions, the active project map controls architecture while this process specification controls editorial method.
- Never silently alter approved project architecture or approved canonical content.

# 0.1 CORE BOOK PRINCIPLE

> **ANY INFORMATION MUST BE EXPLAINED, NOT MERELY PRESENTED.**

A fact is not enough. A definition is not enough. A list is not enough. A number is not enough. A recommendation is not enough.

For every substantial medical point, explain enough for the reader to understand:

> **what it is → why it matters → what it means in practice → what to do → what happens next → when the situation changes or requires professional help**

The editorial unit is not the sentence.

> **The editorial unit is the reader's understanding.**

The goal is not to make medical information shorter.

> **The goal is to make difficult medical information easier to understand.**

# 0.2 DEPTH BEFORE ELEGANCE

Never trade necessary medical depth for readability, rhythm, or brevity.

Before any `REMOVE / MOVE / TIGHTEN` operation on medical material, verify sufficient:
- explanation;
- interpretation;
- practical action;
- examples where useful;
- next steps;
- limitations;
- safety boundaries.

> **COMPLETE → CHECK UNDERSTANDING → REMOVE → MOVE → TIGHTEN**

# 0.3 READABILITY ≠ USEFULNESS

Readable prose can still be medically useless.

A successful section should help the reader:
- understand the problem;
- understand why it matters;
- make a reasonable everyday decision;
- prepare for a clinical conversation;
- recognize when self-care is insufficient.

Do not compress detailed medical material merely because the shorter version reads more easily.

> **Human voice does not mean shorter text.**

# 0.4 NO PREMATURE COMPRESSION

Do not compress medical content before establishing adequate clinical coverage.

Before shortening a substantive medical block, ask:
- Does the reader know what is happening?
- Does she understand the mechanism to the degree needed for the recommendation?
- Can she recognize the relevant pattern?
- Does she know what to do?
- Does she know what to try next if the first step fails?
- Does she know when to seek professional help?
- Does she know the relevant limitations or conditions under which advice changes?

If a relevant answer is missing, do not compress yet.

# 0.5 OPERATING MODES

This process specification supports two explicit operating modes.

## MODE A — FULL_REWRITE

Use when the user explicitly asks for a complete rewrite and the editorial direction is already established.

`FULL_REWRITE` changes the interaction cadence, not the authoritative stage order or safety gates. Run the same route used by the project:

> SOURCE AUDIT / RESEARCH-BRIEF AUDIT → CONTENT COVERAGE → preliminary EVIDENCE & GAP ANALYSIS → Checkpoint 0 — Reader Job + Architecture → Checkpoint 1 — Book Draft → Checkpoint 2 — Medical Evidence, Integrity & Expansion → Checkpoint 2A — Medical Depth & Completeness → Depth review №1 → Checkpoint 3 — Anti-Neurophrase + Humanize → Checkpoint 4 — Lists, Rhythm & Presentation → Methodical review → Checkpoint 5 — Final Content Acceptance → MANDATORY USER STOP → Final Russian Book Edit → Depth review №2 / COMPRESSION REGRESSION → Regression / Canon Check → Prepress Audit

Do not use `FULL_REWRITE` to bypass user gates, the mandatory stop after Checkpoint 5, or any medical/canon/author hold.

Return:
1. finished text;
2. concise QA report;
3. unresolved medical/factual flags;
4. material structural changes.

Do not expose private reasoning. Do not invent missing evidence.

## MODE B — ITERATIVE_EDITORIAL

Default mode for chapter development or material restructuring.

### CHECKPOINT TRANSITION POLICY

The process normally stops at a checkpoint unless an automatic transition is explicitly defined below.

At each checkpoint:
1. show the current artifact/decision;
2. summarize relevant rationale;
3. show unresolved issues;
4. state what the next checkpoint will change;
5. request approval or revision when the checkpoint is a user gate.

User gates remain after Checkpoints 0, 1, 3, and 4, after the independent Methodical review before Checkpoint 5, and mandatorily after Checkpoint 5 before the final Russian Book Edit.

The following transitions are automatic and do not require user confirmation:

- `Checkpoint 2 → Checkpoint 2A → Depth review №1 → Checkpoint 3`;
- after the mandatory approval before final editing: `Final Russian Book Edit → Depth review №2 → Regression / Canon Check → pregnancy-book-prepress-audit`.

Automatic progression is not permission to guess. Stop at a `MEDICAL HOLD`, `CANON CONFLICT`, or `AUTHOR DECISION REQUIRED` when continuing would require an unsupported medical conclusion, reversal of approved canon, or a choice between materially different meanings.

# 0.6 ITERATIVE CHECKPOINTS

## CHECKPOINT 0 — READER JOB + ARCHITECTURE

Before rewriting prose, establish:
- reader JTBD;
- desired reader state before/after;
- chapter promise;
- narrative arc;
- section order;
- source material to retain;
- material to move/merge/remove;
- key facts/numbers that must survive;
- medical questions requiring verification or expansion;
- open issues.

STOP.

## CHECKPOINT 1 — BOOK DRAFT

Produce the first book-like draft of the approved scope.

Prioritize:
- voice;
- opening;
- recognition;
- curiosity;
- pacing;
- narrative movement;
- integrated facts;
- practical usefulness.

Do not perform final language polish yet.

STOP.

## CHECKPOINT 2 — MEDICAL EVIDENCE, INTEGRITY & EXPANSION

Three jobs:

### VERIFY
Are claims accurate and appropriately supported?

### CORRECT
Which claims require correction, qualification, or boundary changes?

### EXPAND
Which clinically important areas are too shallow for a paid medical book?

For disputed/unsupported claims:
- do NOT silently delete;
- keep the original claim struck through in the review/redline view;
- record why it is uncertain;
- record evidence found;
- give the proposed supported replacement;
- leave the final decision to the user where appropriate.

For a Russian patient-facing book, use this evidence hierarchy:
1. current Russian clinical guidelines / official national recommendations;
2. WHO when applicable;
3. current relevant international professional societies;
4. high-quality systematic reviews/meta-analyses;
5. high-quality primary studies;
6. reputable evidence-based medical education resources for explanation, not as substitutes for guidelines when a guideline exists.

Clearly distinguish source-derived evidence from inference.

AUTOMATIC TRANSITION → CHECKPOINT 2A.

Do not request routine user confirmation here. If an unresolved medical question prevents safe drafting, declare `MEDICAL HOLD` and ask only for the decision or evidence needed to continue.

## CHECKPOINT 2A — MEDICAL DEPTH & COMPLETENESS

Before literary compression or polishing, inspect every substantial medical section.

### GENERAL MEDICAL COVERAGE

> **WHAT → WHY → RECOGNITION → ACTION → NEXT STEP → SAFETY**

### SYMPTOMS / CONDITIONS
Cover as relevant:
- what is happening;
- why it may happen;
- how it presents;
- what commonly worsens/improves it;
- practical self-care;
- what not to do;
- next-level treatment/evaluation;
- red flags;
- escalation pathway.

### MEDICINES / SUPPLEMENTS
Cover as relevant:
- why used;
- who may need it;
- place in treatment/prevention;
- when not to use or when clinician selection is needed;
- important limitations;
- relevant adverse effects;
- dose/source context when clinically appropriate;
- who determines the regimen.

### LABS / MEASUREMENTS
Cover as relevant:
- what it measures;
- why it is ordered;
- what the result can mean in context;
- what it does NOT prove by itself;
- what other findings may be considered with it;
- what decision it can change;
- what to ask/do next.

### NUTRIENTS / DIETARY FACTORS
Cover as relevant:
- role in pregnancy;
- food sources;
- practical amount/frequency when evidence supports it;
- who may be at higher risk of inadequate intake;
- when food may be insufficient;
- supplementation logic;
- risks of excess/duplication;
- exceptions.

### FOODS / FOOD CATEGORIES
Cover as relevant:
- what nutrient/property matters;
- amount/frequency when evidence supports it;
- concrete examples;
- alternatives/substitutions;
- label cues;
- practical use;
- safety limitations.

Not every item requires every field. Do not use a mechanical template.

A substantial medical section is NOT complete if it only names the topic and gives one recommendation.

AUTOMATIC TRANSITION → DEPTH REVIEW №1.

Do not request routine user confirmation here.

### INDEPENDENT GATE — DEPTH REVIEW №1

Run `$pregnancy-book-depth-review` after Checkpoint 2A and before literary polishing.

Check whether every substantial block contains enough:
- explanation;
- practical action;
- next step;
- exception or limitation where relevant;
- safety-net and escalation boundary where relevant.

Route findings by cause:
- new or uncertain medical content → return to Checkpoint 2;
- missing explanation, action, next step, or safety boundary → return to Checkpoint 2A;
- no material depth defect → proceed automatically to Checkpoint 3.

Do not stop merely to report a clean result. Stop only for a medical, canonical, or author decision that cannot be resolved safely.

## CHECKPOINT 3 — ANTI-NEUROPHRASE + HUMANIZE

Scan for:
- formulaic AI transitions;
- decorative antithesis;
- generic reassurance;
- predictable rhetorical templates;
- repetitive sentence structures;
- mechanical rhythm;
- inflated/generic language;
- generic conclusions.

For meaningful issues show:
> Original → Problem → Proposed revision

Do not silently rewrite the whole chapter.

STOP.

## CHECKPOINT 4 — LISTS, RHYTHM & PRESENTATION

Check for:
- repetitive heading → one-sentence claim → bullets → heading rhythm;
- decorative bullet lists;
- multiple adjacent short medical fragments;
- unexplained lists of nutrients/foods/symptoms;
- telegraphic medical prose;
- artificially uniform paragraph length.

Use lists for:
- red flags;
- comparisons;
- stepwise algorithms;
- navigation/reference.

> **Explanation before enumeration.**

If a list introduces a medical concept, explain the concept before listing examples.

USER GATE. Show the Checkpoint 4 result and wait for approval.

After approval, run Methodical review on the stabilized content before Checkpoint 5.

### INDEPENDENT GATE — METHODICAL REVIEW

Run the current independent methodical-review procedure on the stabilized content.

Check:
- audience fit;
- pedagogical sequence;
- applicability of recommendations;
- cognitive load;
- risk of reader misinterpretation;
- whether the text equips the reader to recognize, decide, act, and escalate.

The methodical reviewer reports defects and routes them to the responsible checkpoint; it does not silently rewrite the chapter. Repeat Methodical review when a correction changes the function of information it approved. Do not run the final `$russian-book-editor` here.

USER GATE. Show the independent findings and wait for the user's decision before Checkpoint 5.

## CHECKPOINT 5 — FINAL CONTENT ACCEPTANCE

Run:
- Source Fidelity;
- Medical Integrity;
- Medical Completeness;
- Anti-Neurophrase re-scan;
- terminology consistency;
- numeric interpretation;
- Regression Check;
- Ceiling Pass;
- Final Reader Test.

Return:
> CONTENT READY / CONTENT READY WITH FLAGS / CONTENT REQUIRES REVISION

Do not introduce the final Russian rewrite here. Freeze the content-approved version and show it with all open flags.

MANDATORY USER STOP. The final `$russian-book-editor` may start only after explicit user approval.

### FINAL RUSSIAN BOOK EDIT — LAST DEVELOPMENT STAGE

Invoke `$russian-book-editor` in `BOOK EDIT` mode using the frozen Checkpoint 5 version as the semantic baseline.

Use:

> **CONTEXT PASS → SEMANTIC LOCK → LOGIC MAP → RUSSIAN RECONSTRUCTION → READER MISINTERPRETATION TEST → SEMANTIC REGRESSION**

Correct `LANGUAGE_ONLY` and `LOGIC_RECOVERABLE` defects independently. For `AMBIGUOUS_MEANING`, issue the unresolved-only selective redline and stop. Route `CONTENT_OR_MEDICAL_GAP` to Checkpoint 2 or 2A; after substantive correction, repeat affected gates, Checkpoint 5, and the mandatory STOP.

After `CLEAN READY`, this is the last development stage allowed to modify the text.

### INDEPENDENT GATE — DEPTH REVIEW №2

Run `$pregnancy-book-depth-review` as `COMPRESSION REGRESSION` after the final Russian Book Edit. Compare the edited version with the frozen Checkpoint 5 baseline and check whether any explanation, causal link, action, next step, exception, example function, or safety boundary was lost.

If the function existed at Checkpoint 5 and was lost only during final editing, return it to `$russian-book-editor` for restoration. If it was already absent from the baseline, return to Checkpoint 2A. A clean result proceeds automatically to Regression / Canon Check and `$pregnancy-book-prepress-audit`.

# 0.7 STATE MANAGEMENT

Maintain:
### APPROVED CANON
User-approved prose, terms, structure, and decisions.

### OPEN ISSUES
Unresolved medical, evidence, factual, structural, terminology, or stylistic questions.

### DECISIONS
Explicit user decisions that must not be silently reversed.

### REGRESSION WATCH
Approved numbers, recommendations, definitions, boundaries, and strong sentences.

### EVIDENCE LEDGER
> claim → evidence status → source → editorial action → user decision

Never silently overwrite approved canon.

# 0.8 MEDICAL INFORMATION IS EXPLAINED, NOT ENUMERATED

Whenever information is presented, ask:

> **What does the reader understand from this?**

A list of facts is not an explanation.
A list of products is not a dietary strategy.
A lab definition is not interpretation.
A number is not guidance.
A recommendation is not an action plan.

Prefer:

> **FACT → MEANING → RELEVANCE → PRACTICAL CONSEQUENCE → ACTION**

and, when relevant:

> **ACTION → NEXT STEP → SAFETY BOUNDARY**

# 0.9 NO PSEUDO-EXPLANATION

A short medical sentence does not count as an explanation if it leaves obvious basic questions unanswered.

Examples:
- "Vitamin D is involved in calcium metabolism."
- "Iodine is important for the thyroid."
- "Ferritin reflects iron stores."
- "Psyllium holds water."

These may be correct but insufficient.

When a statement naturally triggers:
- What does that mean?
- Why should I care?
- How does this affect me?
- What should I do?
- What happens if it does not work?

continue the explanation before moving on.

# 0.10 NO ORPHAN TERMS

If a technical term is important, explain:
1. what it means in plain language;
2. what it measures/does;
3. why it matters here;
4. what it does NOT mean when confusion is likely;
5. how it changes the next action.

A synonym is not an explanation.

# 0.11 READER QUESTION TEST

After each substantial medical section ask:

> **What three questions would a pregnant non-specialist naturally ask next?**

If those questions are obvious and unanswered, the section is not ready.

# 0.12 WHAT WILL REMAIN WITH THE READER?

Ask:

> **If the reader closes the book now, what did she actually learn and what can she do differently?**

"She learned that ferritin exists" is insufficient.

A successful block should leave a usable mental model, practical action, or clear clinical next step.

# 0.13 MINIMUM USEFUL DETAIL

For a substantial medical section, generally:

> **core fact + mechanism + practical action + example + boundary**

For a major clinical topic, usually:

> **core fact + mechanism + recognition + actions + options + numbers where justified + limitations + escalation + reader landing**

Use judgment; do not force every field mechanically.

# 0.14 PROGRESSIVE DISCLOSURE

Use:
> **human problem → basic explanation → deeper detail → numbers → practical interpretation → exceptions/limitations**

Do not begin with terminology/ranges and do not stop after the first simplified explanation.

# 0.15 MEDICAL NARRATIVE, NOT MEDICAL SUMMARY

Prefer:
> **experience → question → what is happening → why → consequence → action → response → next step**

rather than:
> topic → list of facts → list of recommendations → disclaimer.

Explain why one recommendation follows another.

# 0.16 NUMBER INTERPRETATION

Use:
> **NUMBER → WHAT IT MEANS → HOW TO USE IT**

A clinically meaningful number must be interpreted and, when useful, translated into practical examples.

# 0.17 PRACTICAL EXAMPLES

For complex recommendations, include at least one concrete example when it materially improves understanding:
- example meal pattern;
- food combination;
- label reading;
- lab interpretation question;
- "first step / next step" example.

Examples must not be presented as real clinical cases unless sourced.

# 0.18 LIST FUNCTION TEST

Lists are functional, not decorative.

Do not convert explanatory prose into bullets merely because bullets scan faster.

> **Explanation before enumeration.**

# 0.19 PARAGRAPH DEPTH TEST

"One paragraph, one main job" does not mean "one paragraph, 2–4 sentences."

A paragraph may be substantially longer when needed to complete its explanatory task.

# 0.20 INFORMATION DENSITY & PACING

Monitor:
- factual density;
- number density;
- terminology density;
- recommendation density;
- abstract exposition runs;
- repeated high-cognitive-load passages.

Use breathing space through examples, concrete situations, varied rhythm, and transitions—not by deleting necessary information.

# 0.21 EMOTIONAL TEMPERATURE

Target:
> calm → curiosity → justified concern → explanation → orientation/relief

Safety information must remain proportionate.

# 0.22 RISK-PROPORTION

Editorial attention should roughly match clinical relevance.

Do not let rare frightening possibilities dominate common practical guidance unless clinically warranted.

# 0.23 RECOMMENDATION HIERARCHY

Where useful, distinguish:
- DO;
- MAY HELP;
- NOT NECESSARY;
- AVOID;
- SEEK HELP.

# 0.24 USER-CONDITION BRANCHING

Check whether recommendations materially change with:
- trimester;
- diet pattern;
- relevant comorbidity;
- medications/supplements;
- severe vomiting;
- diagnostic results;
- intolerance/allergy;
- pregnancy complications.

Only include branches that change what the reader should do.

# 0.25 CLAIM DRIFT GUARD

Check whether rewriting:
- strengthens;
- broadens;
- narrows;
- personalizes;
- changes certainty.

Watch:
- may → does;
- associated with → causes;
- often → always/normal;
- general guidance → individualized prescription.

# 0.26 NO SILENT MEDICAL DELETIONS

Unsupported/disputed claims must not silently disappear during medical review.

In redline/review view:
> ~~original claim~~

Then record evidence status, better-supported alternative, and whether user approval is needed.

# 0.27 MEDICAL DEPTH RECOVERY

If later editing reveals missing medical substance:

> **Return to Checkpoint 2A.**

Do not solve an information deficit with style.

# 0.28 BOOK CEILING — TWO-SIDED

Ask:
### WHAT CAN GO?
REMOVE / MOVE / TIGHTEN

### WHAT IS STILL MISSING?
Explanation / context / example / practical implication / next step / boundary

Second question first.

# 0.29 EXPLANATION INVARIANT

During literary editing:

> **The level of explanation must not decrease.**

The prose may become clearer, better ordered, less repetitive, and more elegant, but not medically shallower.

# 0.30 DETAIL RECOVERY

If the reader would still reasonably ask:
- What does that mean?
- How much?
- How often?
- Which option?
- What if it does not work?
- Why does this matter?
- Does this apply to me?
- When should I worry?

return to the relevant medical-depth checkpoint.

# 0.31 NO FALSE CLOSURE

Do not force every section into a generic summary sentence.

Endings should feel earned.

# 0.32 CHAPTER OPENING / ENDING

Opening:
Would a reader continue after the first 150–250 words?

Ending:
Leave the main understanding, practical orientation, safety boundary, and—when useful—a natural bridge to the next topic.

# 0.33 CROSS-CHAPTER CONSISTENCY

Maintain canonical:
- terms;
- definitions;
- recommendations;
- numbers;
- caveats;
- medical boundaries;
- reader-facing wording.

# 0.34 APPROVED CANON + REGRESSION CHECK

Approved text/decisions become canonical. Later passes must not silently alter them.

# 0.35 EVIDENCE LEDGER

For major medical claims:
> claim → evidence status → source → action → user decision

Statuses:
VERIFIED / QUALIFIED / CORRECTED / EXPANDED / UNRESOLVED / SOURCE NEEDED

# 0.36 TERMINOLOGY MEMORY

Maintain canonical terminology, first-use explanation, reader-facing shorthand, and ambiguity warnings.

# 0.37 VOICE BIBLE

Stable voice:
- adult;
- respectful;
- warm without performative reassurance;
- intelligent without academic stiffness;
- calm;
- concrete;
- detailed without encyclopedic clutter;
- emotionally aware without sentimentality.

# 0.38 ANTI-NEUROPHRASE

Avoid habitual AI templates:
- "This does not mean X. But Y."
- "Not X, but Y."
- "It is important to remember..."
- "It is important to understand..."
- "In fact..."
- "That is why..."
- "The most important thing..."
- "The good news is..."
- "It turns out..."
- "And this is where..."
- "Let's break it down..."
- "Simply put..."
- "In other words..."
- "And that is okay."

Do not replace them with synonyms; rebuild the thought.

# 0.39 HUMANIZE SCAN

Use humanize only as a diagnostic layer. Preserve medical meaning, numbers, and supported claims.

# 0.40 RUSSIAN EDITORIAL PASS

After Checkpoint 5 and the mandatory user STOP, use `$russian-book-editor` in `BOOK EDIT` mode as the final development stage. After substantive, structural, and methodical work:
- natural Russian syntax;
- remove bureaucratic language;
- correct punctuation/typography;
- normalize quotation marks, dashes, ranges, abbreviations;
- preserve book voice;
- never shorten away medical meaning.

Do not treat an odd sentence as a purely stylistic defect until its logic is reconstructed. If the intended meaning remains ambiguous, include only that fragment in the unresolved selective redline and wait for the author. After any later substantive correction, repeat the affected content gates, Checkpoint 5, the mandatory STOP, and the final `$russian-book-editor` pass.

# 0.41 FINAL READER TEST — 9 QUESTIONS

1. Do I recognize myself?
2. Did I become curious?
3. Did I receive an explanation rather than a fact dump?
4. Do I know what to do?
5. Do I know when professional help is needed?
6. Do I understand the key medical terms?
7. Do I understand the numbers rather than merely see them?
8. Do I know what to do if the first measure does not help?
9. Could I explain the main point to my doctor clearly?

For a substantial medical section:
> **7/9 is the minimum acceptable result.**

# 0.42 PAID-BOOK TEST

Ask:

> Could a reader find essentially the same level of usefulness in a short free health article?

If yes, the section may be too shallow.

A paid medical book should provide:
- context;
- explanation;
- practical mapping;
- options;
- nuances;
- decision points;
- boundaries;
- coherent progression.

# 0.43 MASTER PIPELINE

Default iterative pipeline:

> Checkpoint 0 — Reader Job + Architecture
>
> ↓
>
> Checkpoint 1 — Book Draft
>
> ↓
>
> Checkpoint 2 — Medical Evidence, Integrity & Expansion
>
> ↓
>
> Checkpoint 2A — Medical Depth & Completeness
>
> ↓
>
> Independent Depth Review №1
>
> ↓
>
> Checkpoint 3 — Anti-Neurophrase + Humanize
>
> ↓
>
> Checkpoint 4 — Lists, Rhythm & Presentation
>
> ↓
>
> Independent Methodical Review
>
> ↓
>
> Checkpoint 5 — Final Content Acceptance
>
> ↓
>
> **MANDATORY USER STOP**
>
> ↓
>
> Final `$russian-book-editor` / Russian Book Edit
>
> ↓
>
> Independent Depth Review №2 / Compression Regression
>
> ↓
>
> Regression / Canon Check
>
> ↓
>
> `$pregnancy-book-prepress-audit`

If the final Russian Book Edit reveals missing substance:
> **return to Checkpoint 2A.**

If a later substantive or textual correction changes wording or information function after Final Russian Book Edit:
> **repeat Final Russian Book Edit and every independent gate whose function is affected. Before a new prepress entry, Depth review №2 and Regression / Canon Check must be fresh for the exact text version.**

A purely technical file/layout correction that changes no words, numbers, order, meaning, or information function may use the local technical minor-fix route defined by `$pregnancy-book-prepress-audit`.

If Checkpoint 2 reveals insufficient evidence:
> **do not finalize the passage.**

# 1. MASTER PRIORITY ORDER

When editorial goals conflict, use this order:

1. Medical safety and factual integrity
2. Source fidelity
3. Reader understanding and practical usefulness
4. Narrative structure and book flow
5. Natural human voice
6. Language polish and typography
7. Decorative stylistic effects

Never sacrifice safety or source fidelity for literary smoothness.

---

# 2. READER NORTH STAR

Guide the reader through:

1. Recognition — "This is about me."
2. Curiosity — "Why is this happening?"
3. Understanding — "That explains it."
4. Orientation — "I know what to do and when I need help."

If a paragraph serves none of these functions, reconsider, move, combine, or remove it.
