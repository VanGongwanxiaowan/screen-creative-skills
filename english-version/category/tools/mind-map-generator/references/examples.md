# Mind Map Generator Expert - Detailed Examples

## Description

This skill calls the `generateTreeMind` tool to generate mind maps, returning a JSON response containing image URL and edit link.

## Example 1: Story Five Elements Mind Map

### Input

```
Generate a five elements mind map for the following story:

The story of Lin Qian and Lu Yuan developing from competitors to lovers at an advertising company. Lin Qian is a 28-year-old planning manager, independent and strong. Lu Yuan is the creative director, brilliant and talented. The two first met during a bidding competition, got to know each other during cooperation, and finally got together.
```

### Output

```json
{
  "pic": "https://api.example.com/mindmap/images/abc123.png",
  "jump_link": "https://mindmap.example.com/edit/abc123",
  "data": {
    "root": "Lin Qian and Lu Yuan's Love Story",
    "children": [
      {
        "title": "Genre Type",
        "children": ["Urban Emotion", "Workplace Romance", "Growth Inspiration"]
      },
      {
        "title": "Story Synopsis",
        "children": ["First meeting in bidding", "Getting to know in cooperation", "Ex-girlfriend test", "Finally together"]
      },
      {
        "title": "Character Biographies",
        "children": [
          {
            "title": "Lin Qian",
            "children": ["28-year-old planning manager", "Independent and strong", "Cold outside warm inside"]
          },
          {
            "title": "Lu Yuan",
            "children": ["Creative director", "Brilliant and talented", "Sincere and devoted"]
          }
        ]
      },
      {
        "title": "Character Relationships",
        "children": ["Lin Qian↔Lu Yuan: Romance line", "Lin Qian↔Supervisor: Superior-subordinate", "Lu Yuan↔Ex-girlfriend: Former lover"]
      },
      {
        "title": "Major Plot Points",
        "children": ["First meeting in bidding", "Getting to know in cooperation", "Affection buds", "External obstacles", "Finally together"]
      }
    ]
  },
  "log_id": "req_20250111_abc123"
}
```

## Example 2: Character Relationship Mind Map

### Input

```
Generate a character relationship mind map for the following story:

After Su Wan entered the palace, she developed complex relationships with the Emperor, Empress, and deposed Tai Fei. Su Wan gained favor, and the Empress was jealous and framed her. Su Wan was sent to the Cold Palace and met the deposed Tai Fei. The Tai Fei taught Su Wan palace struggle techniques. Finally, Su Wan successfully counterattacked.
```

### Output

```json
{
  "pic": "https://api.example.com/mindmap/images/def456.png",
  "jump_link": "https://mindmap.example.com/edit/def456",
  "data": {
    "root": "Palace Character Relationship Network",
    "children": [
      {
        "title": "Su Wan (Center)",
        "children": ["With Emperor: Favored concubine", "With Empress: Hostile", "With Tai Fei: Mentor-disciple"]
      },
      {
        "title": "Emperor",
        "children": ["With Su Wan: Favor", "With Empress: Husband and wife"]
      },
      {
        "title": "Empress",
        "children": ["With Su Wan: Jealousy and frame-up", "With Emperor: Surface husband and wife"]
      },
      {
        "title": "Deposed Tai Fei",
        "children": ["With Su Wan: Teach techniques", "With Emperor: Old love", "With Empress: Former enemy"]
      }
    ]
  },
  "log_id": "req_20250111_def456"
}
```

## Example 3: Plot Development Mind Map

### Input

```
Generate a plot development mind map for the following story:

Lin Wan was killed by Gu Cheng and Su Fei, reborn back to three years ago. She began collecting criminal evidence, while approaching Fu Sihan. Finally, Lin Wan exposed the conspiracy, Gu Cheng and Su Fei were punished, and Lin Wan and Fu Sihan got together.
```

### Output

```json
{
  "pic": "https://api.example.com/mindmap/images/ghi789.png",
  "jump_link": "https://mindmap.example.com/edit/ghi789",
  "data": {
    "root": "Lin Wan's Rebirth Revenge Story",
    "children": [
      {
        "title": "Past Life: Harmed",
        "children": ["Lin Wan married Gu Cheng", "Best friend Su Fei betrayed", "Conspired to kill Lin Wan", "Reborn back to three years ago"]
      },
      {
        "title": "Present Life: Layout",
        "children": ["Surface maintain relationship", "Secretly collect evidence", "Approach Fu Sihan", "Develop feelings"]
      },
      {
        "title": "Climax: Expose",
        "children": ["Publicly expose conspiracy", "Fu Sihan provides evidence", "Gu Cheng and Su Fei disgraced", "Legal punishment"]
      },
      {
        "title": "Ending: New Life",
        "children": ["Revenge successful", "Confirm relationship with Fu Sihan", "Start new life"]
      }
    ]
  },
  "log_id": "req_20250111_ghi789"
}
```

## API Return Description

```json
{
  "pic": "Access URL of the mind map image, can be directly used for display or download",
  "jump_link": "Online edit link, users can open editor through this link to modify the mind map",
  "data": "Original data structure of the mind map, containing root node and all child nodes' hierarchical information",
  "log_id": "Request log ID, used for issue tracking and debugging"
}
```
