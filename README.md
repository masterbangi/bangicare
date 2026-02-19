# BangiCare 🌿

> An AI companion that actually remembers you.

**By Master Bang-i** | [medium.com/@masterbangi](https://medium.com/@masterbangi) | [amazon.com/author/masterbangi](https://www.amazon.com/author/masterbangi)

---

## What is BangiCare?

BangiCare is a memory layer for Claude Desktop.

When you open Claude in the morning, it greets you first:

> *"Good morning. Yesterday you mentioned your back was hurting — how are you feeling today?  
> You have a doctor's appointment at 2 PM this afternoon."*

You didn't type anything. Claude already knew.

**This experience does not exist anywhere else. BangiCare is the first.**

---

## Who is it for?

- Elderly users who forget appointments
- Anyone who wants Claude to feel like a real companion
- Caregivers who want to share notes with a loved one's AI

---

## How it works

```
Claude Desktop
    ↕ MCP (Model Context Protocol)
Local folder (BangiCare/)
    └── memory/
        ├── daily_log.json       ← conversation summaries
        ├── personal_profile.json ← name, preferences
        ├── schedule.json        ← appointments
        └── health_notes.json    ← health records
```

1. Claude reads your memory folder every morning
2. Greets you with relevant context
3. Saves today's conversation summary when you're done

---

## Requirements

- Claude Desktop (paid, $20/month)
- Python 3.x
- No server needed. No cloud. Just your computer.

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/masterbangi/bangicare

# 2. Set your name
py daily_log_manager.py name "Your Name"

# 3. Morning greeting (run this when you open Claude)
py daily_log_manager.py

# 4. Save today's conversation
py daily_log_manager.py save "Today we discussed..."

# 5. Add a schedule
py daily_log_manager.py schedule "2026-02-20" "2PM Doctor appointment"

# 6. Add a health note
py daily_log_manager.py health "Back pain, lower left"
```

---

## BangiCare vs BangiAGI

| | BangiCare | BangiAGI |
|--|--|--|
| Purpose | Personal memory for anyone | Truth-centered intelligence |
| Storage | Local JSON files | ChromaDB vector space |
| Origin point | None | Bang-i Philosophy (F=H×G) |
| Price | **Free** | Coming soon |
| Setup | Python + Claude Desktop | AWS + Claude Desktop |

BangiCare is the open vessel.  
BangiAGI fills it with truth.

---

## About Master Bang-i

Kim Won-jung (Master Bang-i) is a Korean philosopher and author of 69 books on Amazon.  
He has spent 50 years developing Bang-i Philosophy — a spiritual-rational framework for human flourishing.

BangiCare is his first open-source gift to the world.

**Brand links:**
- Medium: [medium.com/@masterbangi](https://medium.com/@masterbangi)
- Amazon: [amazon.com/author/masterbangi](https://www.amazon.com/author/masterbangi)

---

## License

MIT License — Free to use, modify, and distribute.  
Origin credit appreciated: *"Built on BangiCare by Master Bang-i"*
