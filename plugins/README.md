# Plugins проекта

В этой папке хранятся полноценные пакеты специализированных навыков проекта «Гигиена беременности».

Каждый plugin сохраняется целиком вместе с `SKILL.md`, папками `agents/`, `references/`, `assets/` и другими входящими в пакет файлами. Если какая-либо из этих папок отсутствует в исходном пакете, создавать её искусственно не нужно.

Структура пакета не должна изменяться при загрузке в репозиторий.

## Текущие plugins

- `pregnancy-book-editorial/` — **единственный executable** `$pregnancy-book-editorial`, исполняющий оркестратор редакционного workflow. `editorial/pregnancy-book-editorial-v1.6.md` остаётся неисполняемой PROCESS SPEC / PROCESS AUTHORITY / SOURCE OF TRUTH.
- `pregnancy-book-depth-review/` — независимая проверка глубины: Depth review №1 и Depth review №2 / COMPRESSION REGRESSION.
- `russian-book-editor/` — финальная русская книжная редактура после Checkpoint 5 и обязательного подтверждения пользователя; последний этап разработки, имеющий право менять текст.
- `pregnancy-book-prepress-audit/` — независимый финальный pre-press аудит и издательский вердикт.

Одиночные Markdown-skills, не оформленные как полноценные plugin-пакеты, хранятся в `skills/`.
