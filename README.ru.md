# Ownership Tracer

Кто владеет российской публичной компанией — по официальным открытым источникам, со ссылкой на
первоисточник у каждого факта. Скилл для Claude и для ChatGPT.

**Туториал (англ.):** [How to Trace the Owners of a Russian Public Company](TUTORIAL_URL)

## Скачать

Скачайте **один** файл — для того ассистента, которым пользуетесь:

| Вы пользуетесь | Скачать | Установить |
|---|---|---|
| **Claude** (Claude Code) | [e-disclosure-shareholders.zip](https://github.com/Ru-Pro/ownership-tracer/releases/latest/download/e-disclosure-shareholders.zip) | Claude → Customize → Skills → + → Upload a skill ([инструкция](https://support.claude.com/en/articles/12512180-use-skills-in-claude)) |
| **ChatGPT** (Business, Enterprise, Edu, Healthcare) | [e-disclosure-chatgpt.zip](https://github.com/Ru-Pro/ownership-tracer/releases/latest/download/e-disclosure-chatgpt.zip) | ChatGPT → Plugins → Skills → Create → Upload from your computer ([инструкция](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)) |

Зелёная кнопка **Code → Download ZIP** скачивает исходный код, а не скилл — она не подойдёт.

## Что умеет

- Собирает раскрытия компании о долях с e-disclosure.ru и других аккредитованных агентств (AK&M, Прайм,
  СКРИН, Азипи).
- Разбирает каждую долю: держатель, прямое или косвенное владение, доля до и после, дата, цепочка контроля.
- Продолжает цепочки по ЕГРЮЛ: участники ООО, залоги долей, директора.
- Добавляет бухотчётность компаний из цепочек (ГИР БО) и данные Мосбиржи: число акций, стоимость пакетов,
  крупные договорные сделки.
- Проверяет всех в структуре по санкционным спискам (OpenSanctions).
- Отвечает на русском или английском, со ссылкой на источник у каждого факта.

## Устройство репозитория

| Путь | Что там |
|---|---|
| `scripts/` | все скрипты — в одном экземпляре, общие для обоих скиллов |
| `skills/claude/` | скилл для Claude: `SKILL.md`, описание на русском и английском |
| `skills/chatgpt/` | скилл для ChatGPT: `SKILL.md`, `references/METHOD.md` |
| `tutorial/` | туториал и SEO-тексты для сайта |
| `build.py` | собирает оба ZIP в `dist/` |

## Как выпустить новую версию

1. Собрать архивы: `python3 build.py` (они появятся в `dist/`).
2. На GitHub: **Releases → Draft a new release**, создать новый тег (например `v1.1`), вставить текст из
   `RELEASE_NOTES.md`, приложить оба ZIP из `dist/` и опубликовать.

Ссылки на скачивание выше всегда ведут на последний релиз, поэтому README и туториал менять не нужно.

## Данные и лицензии

В репозитории только код, собранных данных нет. Инструмент использует открытую информацию: раскрытия
эмитентов, ЕГРЮЛ и бухотчётность ФНС, рыночные данные Мосбиржи. Санкционные данные — OpenSanctions по
лицензии CC BY-NC 4.0: некоммерческое использование, в публикациях указывать OpenSanctions.

English version: [README.md](README.md)
