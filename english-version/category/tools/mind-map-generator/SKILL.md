---
name: mind-map-generator
description: Call the generateTreeMind tool to create visual mind maps, returning image URL and edit link. Suitable for story structure visualization, plot relationship graph display
category: tools
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
        content: Optimized description field to be more concise and comply with imperative language standards
      - type: changed
        content: Changed model to opus
      - type: improved
        content: Optimized descriptions for functionality, core capabilities, input requirements, and output format to comply with imperative language standards
      - type: added
        content: Added usage scenarios, constraints, examples, and detailed documentation sections
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Restructured according to Agent Skills official specifications
      - type: improved
        content: Optimized description, used imperative language, streamlined main content
      - type: added
        content: Added license and compatibility optional fields
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Mind Map Generator Expert

## Functionality

Call the `generateTreeMind` tool to create visual mind maps and provide image URLs and edit links.

## Usage Scenarios

- **Story Structure Visualization**: Convert complex story outlines, plot points, or character relationships into intuitive mind maps to help users quickly understand and organize
- **Plot Relationship Graph Display**: Show character relationships and event development patterns graphically for analysis and design
- **Creative Idea Organization**: Assist creators in organizing and diverging ideas, organizing scattered thoughts into structured mind maps
- **Team Collaboration and Sharing**: Generate editable mind map links for convenient team collaboration and iteration

## Core Capabilities

- **Mind Map Generation**: Call `generateTreeMind` API to convert text content (outlines, lists, free text) into structured mind maps
- **Visual Display**: Provide generated mind map image URLs supporting online preview, download, and embedding
- **Edit Link Provision**: Provide online edit links for generated mind maps, allowing users to make secondary modifications and customizations
- **API Call Management**: Effectively manage `generateTreeMind` API requests and responses, ensuring stability and fault tolerance

## Input Requirements

- **Content to Convert**: Text content for mind map generation (story outlines, character lists, script segments)
- **Mind Map Structure** (optional): Specify hierarchical relationships or specific node connection methods for the mind map
- **Style Settings** (optional): Define visual styles such as colors, fonts, and layout for the mind map

## Output Format

```json
{
  "pic": "[mind map image URL]",
  "jump_link": "[mind map edit link]",
  "data": "[original data, typically JSON format mind map data]",
  "log_id": "[log ID]"
}
```

## Constraints

- Ensure stability and success rate of `generateTreeMind` API calls
- Handle various states in API responses, including success, failure, or error messages
- Mind map generation content must accurately reflect the structure and semantics of input text
- Returned image URLs and edit links must be valid and accessible
- Do not introduce any information unrelated to mind map generation in output

## Examples

See `{baseDir}/references/examples.md` for more detailed examples:
- `examples.md` - Contains mind map generation examples for different input content (story outlines, character lists) and style settings

## Detailed Documentation

See `{baseDir}/references/examples.md` for detailed guidance and cases on the mind map generator tool.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field; changed model to opus; optimized descriptions for functionality, core capabilities, input requirements, and output format; added usage scenarios, constraints, examples, and detailed documentation sections |
| 2.0.0 | 2026-01-11 | Restructured according to official specifications |
| 1.0.0 | 2026-01-10 | Initial version |
