# Blender_Batch_Assets_Tool
Batch script for converting large folders of .blend files into Blender Asset Browser for Blender 4.2+. No more manual asset marking.

## Requirements

- Blender **4.2 or newer**
- Python access via Blender’s **Scripting** workspace
- Write access to the `.blend` files (the script saves changes)

---

## Installation

1. Clone this repository or download the script file:
   ```bash
   git clone https://github.com/zwistillus/Blender_Batch_Assets_Tool.git
2. Open Blender → Scripting workspace
3. Paste or open the script into a new text block
4. Set ROOT folder path below
5. Run Script

# IMPORTANT:
BACK UP your .blend files first (this script will SAVE changes).
Prints progress/errors to the system console / terminal.

---

## Features

- Opens every `.blend` file in a folder (recursively)
- Marks mesh objects as Asset Browser assets
- Saves files automatically
- Skips backup files (`.blend1`, `.blend2`)
- Optional filtering to avoid helper / collision objects
- Compatible with **Blender 4.2+**

---

## Use Case

If you have:
- 50–500+ `.blend` files
- Environment packs, props, scans, or kitbash assets
- Files that are **not already marked as assets**

This script batch-processes them so they appear correctly in Blender’s **Asset Browser**.

---
