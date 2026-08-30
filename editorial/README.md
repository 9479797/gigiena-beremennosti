# Редакционные правила проекта

В этой папке хранятся управляющие документы проекта «Гигиена беременности»: редакционный workflow, архитектура книги, правила переходов, приоритеты и критерии принятия решений.

## Активные документы

- `project-instructions-v1.7.md` — активная GitHub-first инструкция проекта: постоянный SOURCE OF TRUTH, связь Project ↔ GitHub, стандартные команды, правила состояния тем и политика дубликатов skills/files.
- `pregnancy-book-editorial-v1.6.md` — **PROCESS SPEC / PROCESS AUTHORITY / SOURCE OF TRUTH** для маршрута разработки, Checkpoint'ов, остановок, автоматических переходов, возвратов и финального принятия тем. Это управляющий документ, а не executable skill.
- `pregnancy-book-evidence-content-map-v3.0.md` — активная архитектура книги: reader jobs, границы тем, coverage, cross-links, evidence priorities и правила глубины.

`project-instructions-v1.6.md` является исторической версией и не управляет новой работой после активации v1.7.

Единственный executable `$pregnancy-book-editorial` хранится в `plugins/pregnancy-book-editorial/SKILL.md` и обязан следовать активной process spec. Полноценные исполняющие plugin-пакеты хранятся отдельно в `plugins/`, а одиночные Markdown-skills — в `skills/`.

При конфликте версий семантические номера значимы: для текущей работы используются Project Instructions v1.7, Editorial v1.6 и Content Map v3.0. Исторические версии не должны управлять активной разработкой.
