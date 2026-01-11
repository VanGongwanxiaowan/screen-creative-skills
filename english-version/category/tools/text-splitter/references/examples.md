# Text Splitter Tool - Detailed Examples

## Example 1: Split by Character Count

### Input

```
Text="This is a long text content that needs to be split. This is the second paragraph content. This is the third paragraph content. This is the fourth paragraph content.", Split size=20, Split unit=characters
```

### Output

```
[Text Splitting Result]

Original length: 47
Split unit: Characters
Split size: 20
Number of chunks after splitting: 3

Chunk 1:
This is a long text content that needs to be split.

Chunk 2:
This is the second paragraph content. This is the thi

Chunk 3:
rd paragraph content. This is the fourth paragraph content.
```

## Example 2: Split by Paragraphs

### Input

```
Text="First paragraph content
Second paragraph content
Third paragraph content
Fourth paragraph content", Split size=2, Split unit=paragraphs
```

### Output

```
[Text Splitting Result]

Original number of paragraphs: 4
Split unit: Paragraphs
Split size: 2
Number of chunks after splitting: 2

Chunk 1:
First paragraph content
Second paragraph content

Chunk 2:
Third paragraph content
Fourth paragraph content
```

## Example 3: Split by Sentences

### Input

```
Text="This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence. This is the fifth sentence.", Split size=2, Split unit=sentences
```

### Output

```
[Text Splitting Result]

Original number of sentences: 5
Split unit: Sentences
Split size: 2
Number of chunks after splitting: 3

Chunk 1:
This is the first sentence.
This is the second sentence.

Chunk 2:
This is the third sentence.
This is the fourth sentence.

Chunk 3:
This is the fifth sentence.
```

## Example 4: Smart Splitting (Maintain Semantic Completeness)

### Input

```
Text="The story tells the growth journey of a young girl. She experienced many difficulties and setbacks but never gave up. Finally, she achieved her dream through her own effort.", Split size=30, Smart splitting=true
```

### Output

```
[Text Splitting Result]

Original length: 56
Split mode: Smart splitting (maintain semantic completeness)
Target size: 30
Number of chunks after splitting: 2

Chunk 1:
The story tells the growth journey of a young girl. She experienced many difficulties and setbacks but never gave up.

Chunk 2:
Finally, she achieved her dream through her own effort.
```
