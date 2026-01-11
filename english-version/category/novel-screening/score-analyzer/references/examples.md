# Score Analysis Agent - Detailed Examples

## Example 1: Analyze Multiple Round Evaluation Results

### Input

```
Please analyze the following multiple round evaluation results:

[First Round Evaluation]
Ideological: Positive, 8.0 points
Artistry: Detail portrayal 7.5 points, Narrative logic 8.0 points
Viewability: Audience base 8.0 points, Character portrayal 7.5 points

[Second Round Evaluation]
Ideological: Positive, 8.2 points
Artistry: Detail portrayal 7.8 points, Narrative logic 8.3 points
Viewability: Audience base 8.3 points, Character portrayal 7.8 points

[Third Round Evaluation]
Ideological: Positive, 7.9 points
Artistry: Detail portrayal 7.6 points, Narrative logic 8.1 points
Viewability: Audience base 8.1 points, Character portrayal 7.6 points
```

### Output

```
[Score Analysis Report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. Evaluation Overview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Evaluation times: 3 times
- Valid scores: 3 times
- Rating level: A Grade (Recommended attention)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. Score Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- First score: 8.0 points
- Highest score: 8.3 points (Second round Viewability-Audience base)
- Lowest score: 7.5 points (First round Artistry-Detail portrayal)
- Average score: 8.0 points

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. Score Sequence
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 8.0 points (First round)
2. 8.3 points (Second round)
3. 8.0 points (Third round)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV. High Score Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- 8.5 points and above: 0 times
- 8.0-8.4 points: 12 times
- 7.5-7.9 points: 9 times
- 7.4 points and below: 0 times

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V. Comprehensive Rating
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

According to rating standards:
- **A Grade (Recommended attention)**: Appeared 5 times 8.0 points
Meets A Grade standards, recommend attention and follow-up.
```

## Example 2: Statistical Indicators

### Input

```
Please statistics the indicators of the following evaluation:

[1st Evaluation] 8.2 points
[2nd Evaluation] 7.9 points
[3rd Evaluation] 8.1 points
[4th Evaluation] 8.0 points
[5th Evaluation] 8.3 points
[6th Evaluation] 7.8 points
[7th Evaluation] 8.1 points
[8th Evaluation] 8.0 points
[9th Evaluation] 7.9 points
[10th Evaluation] 8.2 points
```

### Output

```
[Score Statistics Indicator Report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. Evaluation Overview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Evaluation times: 10 times
- Valid scores: 10 times
- Total score: 80.5 points
- Average score: 8.05 points

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. Score Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Highest score: 8.3 points
- Lowest score: 7.8 points
- Median: 8.05 points
- Mode: 8.0 points (appeared 2 times)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. Score Distribution
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- 8.5 points and above: 0 times (0%)
- 8.0-8.4 points: 10 times (100%)
- 7.5-7.9 points: 0 times (0%)
- 7.4 points and below: 0 times (0%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV. Trend Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Score trend: Relatively stable, fluctuating between 7.8-8.3
- Overall evaluation: High quality, stable scores

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V. Rating Result
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

According to rating standards:
- **S Grade (Strong attention)**: ≥1 time 8.5 points or ≥8 times 8.0 points
- **A Grade (Recommended attention)**: ≥5 times 8.0 points

Rating result: **A Grade (Recommended attention)**

Note: Appeared 10 times 8.0 points, far exceeding A Grade standard (5 times), approaching S Grade standard
```
