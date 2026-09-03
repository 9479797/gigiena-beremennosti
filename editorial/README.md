# Редакционные правила проекта

В этой папке хранятся управляющие документы проекта «Гигиена беременности»: редакционный workflow, архитектура книги, правила переходов, приоритеты и критерии принятия решений.

## Активные документы

- `project-instructions-v1.8.md` — активная GitHub-first инструкция проекта: постоянный SOURCE OF TRUTH, связь Project ↔ GitHub, стандартные команды, правила состояния тем, действующий стилевой ориентир и политика дубликатов skills/files.
- `pregnancy-book-editorial-v1.6.md` — **PROCESS SPEC / PROCESS AUTHORITY / SOURCE OF TRUTH** для маршрута разработки, Checkpoint'ов, остановок, автоматических переходов, возвратов и финального принятия тем. Это управляющий документ, а не executable skill.
- `pregnancy-book-evidence-content-map-v3.0.md` — активная архитектура книги: reader jobs, границы тем, coverage, cross-links, evidence priorities и правила глубины.
- `text-architecture-v1.0.md` — активная спецификация устройства текста темы: единицы текста, право информации на объём, критерий пустого объёма.
- `tone-of-voice-v1.0.md` — активная спецификация голоса книги: регистр, обращение к читательнице, модальность, словарь, режимы речи, присутствие автора.
- `templates/evidence-ledger-template.md` — обязательный шаблон evidence ledger темы; копируется в `themes/theme-N/evidence-ledger.md`.
- `canonical-style-corpus-v1.0.md` — выведен из обращения (status: retired); стиль задаётся `tone-of-voice-v1.0.md`.

`project-instructions-v1.6.md` и `project-instructions-v1.7.md` являются историческими версиями и не управляют новой работой после активации v1.8.

Единственный executable `$pregnancy-book-editorial` хранится в `.claude/skills/pregnancy-book-editorial/SKILL.md` и обязан следовать активной process spec. Все навыки проекта лежат в `.claude/skills/` (каждый — папка с `SKILL.md` и внутренними файлами).

При конфликте версий семантические номера значимы: для текущей работы используются Project Instructions v1.8, Editorial v1.6 и Content Map v3.0. Исторические версии не должны управлять активной разработкой.
