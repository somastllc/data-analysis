# Somali Lesson Writing Guide

This guide defines the approved style for rewriting the course lessons in Somali. Read it before creating, auditing, or editing a Somali lesson.

## Core principle

The Somali lesson is a rewrite, not a sentence-by-sentence translation. It must teach the same concepts, examples, distinctions, calculations, and conclusions as the English source, but it should sound like a clear lesson originally written in simple Somali.

The goal is not to remove all English. The goal is to make Somali the language of explanation while preserving the English business and technical terms learners will encounter in study and work.

## Language balance

Use these rules in order:

1. Write the explanation in natural Somali.
2. Introduce a useful English business or technical term after the Somali term.
3. After introducing the term, use the Somali wording unless repeating the English term helps connect an example to the definition.
4. Keep actual product, platform, role, interface, file-format, and industry names in English when that is how learners will encounter them.
5. Do not force an English word into an ordinary Somali sentence when a clear Somali word already exists.

| Type | Preferred treatment | Example |
|---|---|---|
| Foundational term | Somali first, then English | `xog (data)` |
| Technical concept | Somali first, then English | `tayada xogta (data quality)` |
| Business concept | Somali first, then English | `faaʼiido tartan (competitive advantage)` |
| Common problem label | Somali first, then English | `qiimeyaal maqan (missing values)` |
| File format or technology | Keep its recognized name | `CSV`, `JSON`, `Excel`, `SQL database` |
| Product or platform | Keep its recognized name | `Facebook`, `mobile money` |
| Common industry role | Keep or introduce the recognized role | `data scientist`, `business owners` |
| Interface term learners will see | Somali explanation with the English label where useful | `safaf (rows)`, `tiirar (columns)` |

Hybrid forms such as `website-yada`, `apps-ka`, `sensors-ka`, and `devices-ka` are acceptable when they reflect terms learners commonly use. Forms such as `data-du`, `data-da`, `problem-ka`, `numbers-ka`, and `file-kii` should be replaced with `xogtu`, `xogta`, `dhibaatada`, `tirooyinka`, and `faylkii`.

There is no fixed Somali-to-English ratio. Keep only the English that improves recognition or technical understanding.

## Terms that must remain distinct

Do not use `data process` and `data processing` as though they mean the same thing.

| English term | Approved Somali term | Meaning |
|---|---|---|
| **Data process** | **hab-socodka xogta** | The ordered work from defining a problem through collecting, cleaning, analyzing, communicating, and making a decision |
| **Data processing** | **farsamaynta xogta** | Operations that calculate, transform, organize, or otherwise process data |
| **Data pipeline** | Keep **data pipeline** and explain it in Somali | The system that moves data from its source through storage and preparation to use |

Use `habka xogta loo maareeyo` only as a plain-language explanation when the context needs it, not as the canonical course term for `data process`. Avoid using `habaynta xogta` for `data processing` when it could be confused with formatting, organization, or structured data.

## Titles and headings

The main title is Somali first, followed by the useful English title or term in parentheses.

```markdown
# Noocyada Xogta (Types of Data)
# Ilaha iyo Qaababka Xogta (Data Sources and Formats)
# Tayada Xogta (Data Quality)
# Maxay Xogtu Muhiim u Tahay? (Why Data Matters)
```

Section headings should normally be Somali. Add English when the heading introduces an important named business or technical concept, such as `Faaʼidada Tartan (Competitive Advantage)` or `Xirfadaha Xogta (Data Skills)`. Generic headings do not need an English translation.

Do not add words such as `Aasaaska` or `Basics` unless the lesson genuinely needs that distinction. Prefer the shortest title that names the subject accurately.

## Lesson opening

Every Somali lesson begins with this structure:

```markdown
# Cinwaanka Soomaaliga (English Title)

**Cutubka:** 1aad - Waa maxay xog (data)?  
**Casharka:** N-aad ee 5-ta cashar  
**Dhammaadka casharkan:** Hal jumlad oo sheegaysa waxa ardaygu awoodi doono.

## Dulmar
```

The learning outcome should be specific and observable. Use verbs such as `sharaxdo`, `kala garato`, `aqoonsato`, or `hubiso`. Avoid vague promises about understanding everything.

The overview should begin with a concrete situation whenever the source supports one. A shop, school, mobile money account, customer list, website, or workplace request is easier for a beginner to enter than an abstract definition.

## Lesson structure

A typical lesson uses this sequence:

1. A short real-world overview
2. A clear definition of the central concept
3. The important categories, steps, or distinctions
4. A table when exact comparisons or repeated fields are easier to scan
5. One concrete example that applies the concept
6. A final consequence, decision, or responsibility when it belongs to the source

This is a content-driven structure, not a rigid page template. Use only the sections the lesson needs.

Define vocabulary where it is first taught. Do not add a separate Key Terms section. Important English terms belong next to their Somali explanation, not in an isolated glossary at the end of the lesson.

## Simplicity and clarity

- Prefer short, direct sentences.
- Keep one main teaching idea in each paragraph.
- Use familiar Somali before a formal or rare synonym.
- Explain a technical term once, then apply it.
- Keep a short explanation that a beginner needs, even if an expert would infer it.
- Remove a sentence that merely repeats the sentence before it.
- Do not expand a simple point into several abstract paragraphs.
- Do not translate an English idiom literally when a natural Somali explanation is clearer.

For example, explain **Garbage In, Garbage Out (GIGO)** by its meaning:

> Xog xun oo la geliyo (input) waxay keentaa natiijo xun (output).

Do not translate `garbage` word by word if that makes the lesson sound unnatural.

The Lesson 1 sentence `Xogtu badanaa sheekadoo dhan ma sheegto` is intentional. Do not change it to `sheeko dhan` or another shortened form.

## Content fidelity

The Somali rewrite must preserve the instructional substance of the English source:

- Keep every concept needed by the learning outcome.
- Keep meaningful contrasts, such as primary versus secondary data.
- Keep numerical examples and verify their results.
- Keep important qualifications, such as a problem mattering differently depending on the question.
- Keep callbacks when they complete an earlier example. A return to the same two shops is useful if it reveals the competitive advantage created by recording and reviewing the data.
- Keep ethical consequences involving privacy, bias, fairness, and responsibility.

Sentences may be combined, split, reordered within a section, or simplified. Do not silently remove a teaching point or add a new claim merely to make the Somali version shorter or longer.

## Examples and localization

Examples should feel familiar to Somali learners:

- mobile money
- local shops and market prices
- school attendance and grades
- Somali names and cities
- Facebook and other commonly used platforms
- workplace datasets and customer records

Prefer an unnamed actor such as a shop owner or manager unless names make the example easier to follow. When names or locations are needed, use Somali ones.

The setting may be Somali while the technical interface terms remain English. A Somali shop example can still use `Customer ID`, `CSV`, `stock`, or `shopping cart` when those are the labels learners are likely to see.

## Grammar and orthography

- Use U+02BC `ʼ` for the Somali glottal stop.
- Do not use the ASCII apostrophe (U+0027) or right single quotation mark (U+2019) inside Somali words.
- Write `goʼaan`, `suʼaal`, `daʼda`, `faaʼiido`, `masʼuuliyad`, and `hayʼad` with the approved character.
- Do not use em dashes.
- Check noun and pronoun agreement after rewriting a sentence.
- Prefer `xogtu`, `xogta`, and `xogtii` over attaching Somali endings to `data`.
- Use `maamule` when the source means one manager. Use `maamulka` only when it means management as a group or institution.
- Keep terminology consistent with earlier approved lessons unless the user deliberately changes it.

Use `/home/sharafdin/Documents/Goobo-Labs/somali-language-standard/` when a spelling, punctuation, or grammar point needs verification. Treat the reviewed lesson wording and the user's corrections as the final authority for this course when multiple valid Somali variants exist.

## Review workflow

Complete the Somali source before designing its presentation:

1. Read the full English lesson and identify every teaching point.
2. Rewrite it in simple Somali using this guide.
3. Compare it with the approved Somali lessons for terminology and tone.
4. Audit grammar, agreement, spelling, repetition, and unnecessary English.
5. Give the Markdown to the user for corrections and approval.
6. Lock the Markdown lesson.
7. Only then analyze the required pages and SVGs from the final Somali content.
8. Build the HTML, assets, and PDF under `exports/somali/`.

Do not update an existing Somali export while its Markdown is still being reviewed unless the user explicitly requests it.

Page and SVG counts are content-driven. A lesson may naturally need eight pages, fewer than eight, or more than eight. Eight is neither required nor forbidden. The same rule applies to SVGs.

## Final checklist

Before asking for approval, confirm:

- The Somali lesson teaches the same content as the English source.
- Somali carries the explanation.
- English appears only where it improves recognition or technical accuracy.
- The title and learning outcome match the lesson.
- Definitions appear before or where their terms are used.
- Examples are concrete and locally understandable.
- No section is duplicated or unnecessarily expanded.
- Numerical examples are correct.
- Subject agreement is clear.
- All Somali glottal stops use `ʼ`.
- No em dash is present.
- No export was changed before Markdown approval.

Useful checks:

```bash
rg -n -P "[\x{27}\x{2019}\x{2014}]" path/to/somali-lesson.md
git diff --check -- path/to/somali-lesson.md
```
