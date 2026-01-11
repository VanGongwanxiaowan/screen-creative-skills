# File Reference Parsing Expert - Detailed Examples

## Example 1: Parse Single File Reference

### Input

```
Please parse the following file reference:

@file://data/stories/story1.txt
```

### Output

```
[File Reference Parsing Result]

File path: data/stories/story1.txt
Reference type: Local file reference

Suggested operations:
1. Read file content
2. Check if file exists
3. Verify file format is correct
```

## Example 2: Parse Multiple File References

### Input

```
Please parse the following file references:

First story: @file://data/stories/story1.txt
Second story: @file://data/stories/story2.txt
Background material: @file://data/background/info.md
```

### Output

```
[File Reference Parsing Result]

Identified 3 file references:

1. File path: data/stories/story1.txt
   Reference type: Story text

2. File path: data/stories/story2.txt
   Reference type: Story text

3. File path: data/background/info.md
   Reference type: Background material

Suggested operations:
1. Read all files in order
2. Verify completeness of each file
3. Integrate file content for analysis
```

## Example 3: Parse URL Reference

### Input

```
Please parse the following reference:

@url://https://example.com/article/how-to-write-drama
```

### Output

```
[File Reference Parsing Result]

URL: https://example.com/article/how-to-write-drama
Reference type: Web resource reference

Suggested operations:
1. Use WebFetch tool to get URL content
2. Extract core content of article
3. Integrate into analysis
```

## Example 4: Parse Mixed References

### Input

```
Please parse the following references:

Story text: @file://project/stories/main_story.txt
Reference material: @url://https://drama-guide.com/techniques
User notes: @file://project/notes/user_notes.md
```

### Output

```
[File Reference Parsing Result]

Identified 3 references:

1. Local file: project/stories/main_story.txt (story text)
2. Web resource: https://drama-guide.com/techniques (reference material)
3. Local file: project/notes/user_notes.md (user notes)

Suggested operations:
1. Prioritize reading main story file
2. Get web reference material as auxiliary
3. Read user notes to understand special requirements
4. Integrate all content for analysis
```
