---
name: russian-prose
description: >-
  Natural Russian prose. Use when writing any Russian text in any repository:
  notes, replies, README, commits, PRs.
---

# Russian prose

Russian written by an agent should read as written by a native speaker. The usual failure is telegraph style and English glue inside Russian sentences, more often than bureaucratic officialese.

## Check before handing text back

Run from this skill's directory. The script checks Markdown files only:

```bash
python3 scripts/russian_prose_check.py FILE.md [FILE.md ...]
```

For a commit message or PR body, save the draft to a temporary Markdown file and check that.

Fix every hit unless it is a quote the user dictated. The script covers patterns 1–8. Reread the text for 9–14 yourself.

## Patterns

Numbers are stable ids shared with the script. Bad examples are real agent text.

### Caught by the script

1. **Dash.** Keep the em dash, the en dash and the spaced hyphen out of prose. End the sentence, use a comma, or add the verb the dash stood for.

   | Before | After |
   | --- | --- |
   | «Колонки на передней панели — тишина.» | «Спереди колонки молчат.» |
   | «Вместо неё — второй remote в Origin.» | «Вместо неё добавим в Origin второй remote.» |

2. **Telegraph symbols.** Symbols such as +, →, =, ≠ and × between words turn prose into a telegram. Write the sentence with a verb. Arrows are fine inside code and UI paths.

   | Before | After |
   | --- | --- |
   | «H1 + рейтинг + УТП + CTA в бот» | «В заголовке название мастерской, под ним рейтинг, преимущества и кнопка, которая ведёт в бот.» |
   | «Симптом → лид, альтернатива прайсу.» | «Блок заменяет прайс: клиент выбирает неисправность и оставляет заявку.» |

3. **Slash lists.** Join the items with commas and the conjunction you mean.

   | Before | After |
   | --- | --- |
   | «Яндекс / 2ГИС / Google» | «Яндекс, 2ГИС и Google» |

4. **Latin words in a Russian sentence.** Descriptive text is Russian. English stays only in keys and identifiers in backticks, URLs, proper nouns, and UI quotes. Section keys, commands, and config names go in backticks. One established term per sentence is fine:

   - «крутить remapping»

   | Before | After |
   | --- | --- |
   | «mid-page норма» | «обычно в середине страницы» |
   | «Реальный first-viewport контент — блок ниже» | «Первый экран на самом деле занимает блок ниже.» |
   | «вне scope» | «в задачу не входит» |
   | «Скоуп» | «Охват» |

5. **Calques.** English idioms translated word for word.

   | Before | After |
   | --- | --- |
   | «Реальная причина: …» | «Причина оказалась простой: …» |
   | «Здесь фокус — передняя панель» | «Эта заметка про переднюю панель.» |
   | «Имеет смысл, когда…» | «Нужен, когда…» |
   | «ок» | «в порядке», «работает», «годится» |

   Rephrase these as well:

   - «по сути», «играет роль», «на основе того, что», «в порядке, чтобы», «делает X легче»

6. **Officialese.** Replace these with plain verbs and words:

   - «является», «осуществлять», «данный», «вышеуказанный», «в рамках», «с целью», «важно отметить», «стоит подчеркнуть»

   | Before | After |
   | --- | --- |
   | «Необходимо осуществить обновление документации» | «Нужно обновить документацию» |

7. **Bold.** At most one bold fragment per paragraph or list item. Bold the one thing the reader must not miss.

8. **Parenthetical asides.** At most one per sentence. An aside that carries a fact becomes its own sentence. An aside that carries nothing is deleted.

   | Before | After |
   | --- | --- |
   | «Над хедером часто sticky-баннер с акцией (не переснимали отдельно).» | «Над шапкой часто висит баннер с акцией. Отдельно его не снимали.» |

### Judgment

9. **Fragments without a verb.** Short inventory lines still need a verb.

   | Before | After |
   | --- | --- |
   | «Блок высокий: на скрине обрезан верх.» | «Блок высокий, поэтому на скриншоте обрезан верх.» |

10. **Hedges and agent notes to self.** Write only the caveats the user stated. Keep notes about the agent's future work out of the text body. The user deleted all of these:

    - «шлейф не был воткнут (или сидел криво)»
    - «Разъём подписан `HD_AUDIO` или `JAUD1`, название может отличаться, смотреть маркировку платы или мануал»
    - «Фото тренажёра в `cover`, когда будет снимок из зала»

11. **Domain terms.** Use the term people in the field use, not a translation. When unsure, search before writing.

    | Before | After |
    | --- | --- |
    | «обратная поверхность бедра» | «задняя поверхность бедра» |
    | «безранговая экипировка» | «безгрейдовая» (Lineage II) |

12. **Semicolon chains.** A semicolon only joins parallel items of one kind. Otherwise split into sentences. A good use:

    - «Не отрывать ягодицы; не бить валиком; не раскачиваться»

13. **English rhythm.** Passive everywhere, long noun stacks, every sentence starting the same way:

    - «Это позволяет…», «Это обеспечивает…»

    | Before | After |
    | --- | --- |
    | «Файл был создан агентом» | «Агент создал файл» |

14. **One register per text.** Neutral by default. The imperative second person is fine in a personal how-to, but then the whole text uses it:

    - «Втыкай по ключу, не переворачивай»

## When English is fine

Leave code, URLs, proper nouns, schema keys, and intentionally bilingual UI strings or template headings alone. Keep repository and project identifiers as they are and put them in backticks in prose, for example:

- `hero`, `MoSCoW`, `callback-cta`

## The letter ё

Write it wherever the word has it:

- «ещё», «всё», «её», «вперёд»
