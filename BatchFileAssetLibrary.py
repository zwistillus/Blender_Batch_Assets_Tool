# Author: Sarah Jiang (ZWIST)
# Blender 4.2+ — Batch mark objects as Assets in every .blend file in a folder (and subfolders).
# How to use:
# 1) Blender → Scripting workspace
# 2) Paste this into a new text block
# 3) Set ROOT folder path below
# 4) Run Script
#
# IMPORTANT:
# - BACK UP your .blend files first (this script will SAVE changes).
# - Prints progress/errors to the system console / terminal.

import bpy
import os
import traceback

# ✅ CHANGE THIS:
ROOT = r"/ABSOLUTE/PATH/TO/YOUR/BLEND_FOLDER"

# Mark these object types as assets. Common useful default is MESH only.
MARK_TYPES = {"MESH"}  # other options: {"MESH","CURVE","FONT","SURFACE","META","GPENCIL","EMPTY"}


SKIP_NAME_CONTAINS = {"_COL", "COLLIDER", "collision", "proxy", "helper", "low", "LOD"}

GENERATE_PREVIEWS = False


def should_skip(obj: bpy.types.Object) -> bool:
    n = obj.name
    for token in SKIP_NAME_CONTAINS:
        if token in n:
            return True
    return False


def mark_objects_as_assets() -> int:
    marked = 0
    for obj in bpy.data.objects:
        if obj.type not in MARK_TYPES:
            continue
        if should_skip(obj):
            continue
        try:
            # Mark as asset (id-type function)
            obj.asset_mark()
            marked += 1
        except Exception:
            pass
    return marked


def generate_previews_if_requested():
    if not GENERATE_PREVIEWS:
        return
    try:
        bpy.ops.ed.lib_id_load_custom_preview()
    except Exception:
        pass


def is_real_blend_file(path: str) -> bool:
    # Skip autosaves/backups
    low = path.lower()
    if not low.endswith(".blend"):
        return False
    if low.endswith(".blend1") or low.endswith(".blend2"):
        return False
    return True


ok_files = 0
fail_files = 0
total_marked = 0

for dirpath, _, filenames in os.walk(ROOT):
    for fname in sorted(filenames):
        path = os.path.join(dirpath, fname)
        if not is_real_blend_file(path):
            continue

        try:
            bpy.ops.wm.open_mainfile(filepath=path)

            marked = mark_objects_as_assets()
            generate_previews_if_requested()

            bpy.ops.wm.save_mainfile()
            ok_files += 1
            total_marked += marked
            print(f"[OK] {path}  | marked {marked} objects")

        except Exception as e:
            fail_files += 1
            print(f"[FAIL] {path}  | {repr(e)}")
            traceback.print_exc()

print("\n=== DONE ===")
print(f"Files processed OK: {ok_files}")
print(f"Files failed:       {fail_files}")
print(f"Total objects marked as assets: {total_marked}")
