# Text Truncation Tool - Detailed Examples

## Example 1: Truncate at Period

### Input

```
Text="This is an example text. This is the second sentence. This is the third sentence.", Maximum length=20
```

### Output

```
Original length: 32
Truncated length: 10
Truncation position: At the first sentence period

Truncated text:
This is an example text.
```

## Example 2: Truncate at Line Break

### Input

```
Text="First paragraph content
Second paragraph content
Third paragraph content", Maximum length=30
```

### Output

```
Original length: 29
Truncated length: 15
Truncation position: At the first paragraph line break

Truncated text:
First paragraph content
```

## Example 3: Truncate at Specified Length

### Input

```
Text="This is a very very long sentence with no punctuation inside so it can only be truncated at the specified length", Maximum length=25
```

### Output

```
Original length: 43
Truncated length: 25
Truncation position: Truncated at specified length

Truncated text:
This is a very very long se
```

## Example 4: With Truncation Marker

### Input

```
Text="This is a very long text content that needs to be truncated. This is the second paragraph content that also needs to be truncated. This is the third paragraph content that also needs to be truncated.", Maximum length=50, Truncation marker="..."
```

### Output

```
Original length: 59
Truncated length: 53
Truncation position: At the second paragraph period

Truncated text:
This is a very long text content that needs to be truncated. This is the second paragraph content that also needs to be truncated....
```

## Example 5: Paragraph Text Truncation

### Input

```
Text="The story tells the story of a young girl coming from the countryside to the city to struggle. She experienced many difficulties and setbacks but never gave up on her dream. Finally, through her own effort and persistence, she achieved life's value. This story tells us that as long as we persist unremittingly, we will definitely succeed.", Maximum length=100
```

### Output

```
Original length: 125
Truncated length: 100
Truncation position: At the third sentence period

Truncated text:
The story tells the story of a young girl coming from the countryside to the city to struggle. She experienced many difficulties and setbacks but never gave up on her dream. Finally, through her own effort and persistence, she achieved life's value.
```
