---
name: output-formatter
description: Integrate agent output results into structured final output, support multiple formats. Suitable for integrating analysis reports, generating structured reports
category: result-processing
version: 2.1.0
last_updated: 2026-01-11
license: MIT
compatibility: Claude Code 1.0+
maintainer: Gong Fan
allowed-tools: []
model: opus
changelog:
  - version: 2.1.0
    date: 2026-01-11
    changes:
      - type: improved
        content: Optimized description field to be more concise and comply with imperative language specifications
      - type: changed
        content: Changed model to opus
      - type: improved
        content: Optimized descriptions of functionality, use cases, core capabilities, core steps, input requirements, and output format to comply with imperative language specifications
      - type: added
        content: Added constraints, examples, and detailed documentation sections
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Refactored according to Agent Skills official specifications
      - type: improved
        content: Optimized description, using imperative language, simplified main content
      - type: added
        content: Added license and compatibility optional fields
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Output Formatting Expert

## Functionality

Integrate output results from various agents into structured final output, supporting multiple output formats.

## Use Cases

- Integrate analysis results from multiple agents, generate unified structured reports.
- Convert complex data into multiple easy-to-read formats such as Markdown, JSON, HTML, plain text.
- Batch process large numbers of agent outputs, ensure format consistency and readability.
- Automate report generation process, improve work efficiency.

## Core Capabilities

- **Result Integration**: Efficiently integrate all agent output results, ensure data integrity.
- **Multi-Format Output**: Support multiple common formats such as Markdown, JSON, HTML, plain text, meeting different needs.
- **Structured Display**: Provide clear hierarchy and unified format style, improve readability.
- **Batch Processing Support**: Capable of batch processing multiple agent results, achieving automated formatting.
- **Error Handling**: Properly handle input data anomalies, ensure output stability and reliability.

## Core Steps

```
Receive agent output results
    ↓
Format according to specified output format
    ↓
Integrate all result data
    ↓
Generate structured final output
    ↓
Return formatted results
```

## Input Requirements

- **Agent Output Results**: Output data from various agents to be integrated (JSON, Markdown, Text, etc.).
- **Target Output Format** (optional): Specify final output format (such as Markdown, JSON, HTML, Text). Default is Markdown.
- **Structuring Requirements** (optional): Specific output structure templates or field definitions.

## Output Format

Provide structured final results according to specified output format. For example, in Markdown format, may contain the following content:

```
# Comprehensive Report Title

## Story Outline
[Complete story outline content]

## Major Plot Points
- Plot point 1: [Description]
- Plot point 2: [Description]

## Mind Map
![Mind Map](Image URL)
[Mind map edit link]

## Detailed Plot Points
### Plot Point 1
[Detailed description]

## Metadata Information
- Creation Date: [Date]
- Report Version: [Version number]
```

## Constraints

- Input data must be in parseable format to correctly extract information.
- Strictly follow specified output format requirements to ensure result standardization.
- Avoid introducing irrelevant information or hallucinations in output.

## Examples

See `{baseDir}/references/examples.md` directory for more detailed examples:
- `examples.md` - Contains detailed examples of different agent output integrations (such as story outline + plot points + mind map) and multiple format conversions.

## Detailed Documentation

See `{baseDir}/references/examples.md` for detailed guidance and cases on output formatting.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field to be more concise and comply with imperative language specifications; changed model to opus; optimized descriptions of functionality, use cases, core capabilities, core steps, input requirements, and output format to comply with imperative language specifications; added constraints, examples, and detailed documentation sections. |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications |
| 1.0.0 | 2026-01-10 | Initial version |
