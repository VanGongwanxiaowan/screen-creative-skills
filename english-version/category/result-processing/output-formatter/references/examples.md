# Output Formatting Expert - Detailed Examples

## Example 1: Format as Markdown Report

### Input

```
Please format the following analysis results as a structured Markdown report:

Analysis results:
Story type: Urban emotional drama
Protagonist: Lin Qian, 28-year-old planning manager
Male lead: Lu Yuan, creative director
Plot: From competition to romance
Ending: Finally together
```

### Output

```
# Story Analysis Report

## I. Basic Information

| Item | Content |
|------|---------|
| Story Type | Urban Emotional Drama |
| Story Background | Workplace Environment |
| Story Style | Light and Warm |

## II. Character Design

### Protagonist: Lin Qian
- **Age**: 28 years old
- **Occupation**: Planning Manager
- **Personality**: Independent and strong, cold outside warm inside

### Male Lead: Lu Yuan
- **Occupation**: Creative Director
- **Personality**: Brilliant and talented, sincere and devoted

## III. Plot Development

1. **First Meeting Stage**: Competitors
2. **Development Stage**: Cooperation and getting to know
3. **Climax Stage**: Facing tests
4. **Ending Stage**: Finally together

## IV. Story Ending

Lin Qian and Lu Yuan overcame all obstacles and got together.

---

*Report generated time: 2026-01-11*
```

## Example 2: Format as JSON Output

### Input

```
Please format the following character information as JSON:

Character: Lin Qian
Age: 28 years old
Occupation: Planning Manager
Personality: Independent and strong, cold outside warm inside
```

### Output

```json
{
  "character": {
    "name": "Lin Qian",
    "age": 28,
    "occupation": "Planning Manager",
    "personality": ["Independent and strong", "Cold outside warm inside"],
    "background": "Came to Beijing from small city to struggle"
  }
}
```

## Example 3: Format as List Output

### Input

```
Please format the following plot points as a structured list:

Plot 1: Lin Qian and Lu Yuan meet in bidding
Plot 2: Two forced to cooperate
Plot 3: Develop appreciation during cooperation
Plot 4: Establish romantic relationship
Plot 5: Ex-girlfriend appears
Plot 6: Overcome obstacles
Plot 7: Finally together
```

### Output

```
[Plot Development List]

Stage 1: First Meeting and Competition
1. Lin Qian and Lu Yuan meet in bidding
2. Two compete as rivals

Stage 2: Cooperation and Getting to Know
3. Two forced to cooperate on project
4. Develop appreciation during cooperation

Stage 3: Tests and Fulfillment
5. Establish romantic relationship
6. Ex-girlfriend appears, creates obstacles
7. Overcome obstacles, finally together
```

## Example 4: Format as Table Output

### Input

```
Please format the following character relationships as a table:

Lin Qian and Lu Yuan: Romantic relationship
Lin Qian and Supervisor: Superior-subordinate relationship
Lu Yuan and Ex-girlfriend: Former lover relationship
```

### Output

```
[Character Relationship Table]

| Character A | Character B | Relationship Type | Relationship Description |
|-------------|-------------|-------------------|-------------------------|
| Lin Qian | Lu Yuan | Romantic relationship | From competitors to lovers |
| Lin Qian | Supervisor | Superior-subordinate | Workplace superior-subordinate |
| Lu Yuan | Ex-girlfriend | Former lover | Past emotional entanglement |
```
