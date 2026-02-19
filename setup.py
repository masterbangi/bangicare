# -*- coding: utf-8 -*-
# setup.py - BangiCare first-time setup
# Run once: py setup.py

import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
MEMORY = os.path.join(BASE, "memory")

print("=" * 50)
print("  BangiCare Setup")
print("  by Master Bang-i")
print("=" * 50)

os.makedirs(MEMORY, exist_ok=True)

files = {
    "daily_log.json": [],
    "personal_profile.json": {"name": "", "age": "", "notes": []},
    "schedule.json": [],
    "health_notes.json": []
}

for fname, default in files.items():
    path = os.path.join(MEMORY, fname)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(default, f, ensure_ascii=False, indent=2)

name = input("\nWhat is your name? (press Enter to skip): ").strip()
if name:
    profile_path = os.path.join(MEMORY, "personal_profile.json")
    with open(profile_path, 'r', encoding='utf-8') as f:
        profile = json.load(f)
    profile['name'] = name
    with open(profile_path, 'w', encoding='utf-8') as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
    print(f"Hello, {name}!")

print("\nSetup complete.")
print("Run: py daily_log_manager.py")
print("=" * 50)
