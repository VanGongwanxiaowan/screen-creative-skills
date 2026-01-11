# Text Truncation Tool (Novel Version) - Detailed Examples

## Example 1: Truncate at Period

### Input

```
Novel text="This is an example novel text content. This is the second sentence. This is the third sentence.", Maximum length=20
```

### Output

```
[Text Truncation Result]

Original length: 32
Truncated length: 10
Truncation position: At the first period

Truncated text:
This is an example novel text content.
```

## Example 2: Truncate at Line Break

### Input

```
Novel text="Chapter One begins

Chapter Two continues

Chapter Three develops", Maximum length=30
```

### Output

```
[Text Truncation Result]

Original length: 29
Truncated length: 15
Truncation position: At the end of Chapter One line break

Truncated text:
Chapter One begins

Chapter Two continues
```

## Example 3: Truncate Longer Novel Paragraph

### Input

```
Novel text="This is a very long novel text content that needs intelligent truncation processing. It contains multiple sentences, each with its complete meaning. We need to truncate at the most appropriate position to ensure the truncated text maintains semantic completeness and coherence.", Maximum length=50
```

### Output

```
[Text Truncation Result]

Original length: 107
Truncated length: 50
Truncation position: At the second sentence period

Truncated text:
This is a very long novel text content that needs intelligent truncation processing. It contains multiple sentences, each with its complete meaning.
```

## Example 4: With Truncation Marker

### Input

```
Novel text="This is a very long novel text content that needs to be truncated. This is the second paragraph content that also needs to be truncated. This is the third paragraph content that also needs to be truncated.", Maximum length=60, Truncation marker="...[To be continued]"
```

### Output

```
[Text Truncation Result]

Original length: 67
Truncated length: 72
Truncation position: At the second paragraph period

Truncated text:
This is a very long novel text content that needs to be truncated. This is the second paragraph content that also needs to be truncated....[To be continued]
```

## Example 5: Intelligent Truncation Maintaining Semantics

### Input

```
Novel text="The story tells the growth journey of a young girl coming from the countryside to the city. She experienced many difficulties and setbacks but never gave up on her dream. Finally, through her own effort and persistence, she achieved life's value and goals. This story tells us that as long as we persist unremittingly, we will definitely succeed.", Maximum length=80, Intelligent truncation=true
```

### Output

```
[Text Truncation Result]

Original length: 102
Truncated length: 81
Truncation position: At the third sentence period

Truncated text:
The story tells the growth journey of a young girl coming from the countryside to the city. She experienced many difficulties and setbacks but never gave up on her dream. Finally, through her own effort and persistence, she achieved life's value and goals.
```
