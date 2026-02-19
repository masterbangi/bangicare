# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# daily_log_manager.py - 방이구조체1 핵심 엔진
# 대화 요약 저장 + 아침 인사 생성

import json
import os
from datetime import datetime, timedelta

BASE = r"F:\BangiCare"
MEMORY_DIR  = os.path.join(BASE, "memory")
DAILY_LOG   = os.path.join(MEMORY_DIR, "daily_log.json")
PROFILE     = os.path.join(MEMORY_DIR, "personal_profile.json")
SCHEDULE    = os.path.join(MEMORY_DIR, "schedule.json")
HEALTH      = os.path.join(MEMORY_DIR, "health_notes.json")

def init_dirs():
    os.makedirs(MEMORY_DIR, exist_ok=True)
    defaults = {
        DAILY_LOG: [],
        PROFILE: {"name": "", "age": "", "notes": []},
        SCHEDULE: [],
        HEALTH: []
    }
    for path, default in defaults.items():
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(default, f, ensure_ascii=False, indent=2)

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def dump(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_today(summary: str, keywords: list = None):
    logs = load(DAILY_LOG)
    logs.append({
        "date": datetime.now().strftime('%Y-%m-%d'),
        "time": datetime.now().strftime('%H:%M'),
        "summary": summary,
        "keywords": keywords or []
    })
    dump(DAILY_LOG, logs)
    print(f"저장완료: {summary[:40]}")

def save_schedule(date: str, content: str):
    schedules = load(SCHEDULE)
    schedules.append({"date": date, "content": content,
                       "added": datetime.now().strftime('%Y-%m-%d %H:%M')})
    dump(SCHEDULE, schedules)
    print(f"일정저장: {date} {content}")

def save_health(note: str):
    notes = load(HEALTH)
    notes.append({"date": datetime.now().strftime('%Y-%m-%d'), "note": note})
    dump(HEALTH, notes)
    print(f"건강메모저장: {note}")

def set_user_name(name: str):
    profile = load(PROFILE)
    profile['name'] = name
    dump(PROFILE, profile)
    print(f"이름 설정완료: {name}")

def get_yesterday_summary():
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    entries = [e for e in load(DAILY_LOG) if e['date'] == yesterday]
    return entries[-1]['summary'] if entries else None

def get_today_schedule():
    today = datetime.now().strftime('%Y-%m-%d')
    return [s for s in load(SCHEDULE) if s['date'] == today]

def get_recent_health(days=2):
    cutoff = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    return [n for n in load(HEALTH) if n['date'] >= cutoff]

def morning_greeting():
    profile = load(PROFILE)
    name = profile.get('name') or '선생님'
    yesterday = get_yesterday_summary()
    today_schedules = get_today_schedule()
    health_notes = get_recent_health()

    lines = [f"{name}, 안녕하세요."]
    if yesterday:
        lines.append(f"어제는 '{yesterday[:30]}' 이야기를 나눴습니다.")
    if health_notes:
        lines.append(f"최근 '{health_notes[-1]['note']}' 말씀하셨는데, 오늘은 어떠세요?")
    if today_schedules:
        for s in today_schedules:
            lines.append(f"오늘 {s['content']} 있습니다.")
    else:
        lines.append("오늘 특별한 일정은 없습니다.")
    lines.append("오늘 무엇을 도와드릴까요?")
    return '\n'.join(lines)

def show_status():
    logs = load(DAILY_LOG)
    sched = load(SCHEDULE)
    health = load(HEALTH)
    print(f"대화기록: {len(logs)}개 | 일정: {len(sched)}개 | 건강메모: {len(health)}개")
    if logs:
        last = logs[-1]
        print(f"마지막기록: {last['date']} {last['time']} — {last['summary'][:50]}")

if __name__ == '__main__':
    import sys
    init_dirs()
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''

    if not cmd:
        print(morning_greeting())
    elif cmd == 'save' and len(sys.argv) > 2:
        save_today(sys.argv[2])
    elif cmd == 'schedule' and len(sys.argv) > 3:
        save_schedule(sys.argv[2], sys.argv[3])
    elif cmd == 'health' and len(sys.argv) > 2:
        save_health(sys.argv[2])
    elif cmd == 'name' and len(sys.argv) > 2:
        set_user_name(sys.argv[2])
    elif cmd == 'status':
        show_status()
    else:
        print("사용법:")
        print("  py daily_log_manager.py")
        print("  py daily_log_manager.py name '이름'")
        print("  py daily_log_manager.py save '오늘 대화 요약'")
        print("  py daily_log_manager.py schedule '2026-02-20' '오후2시 정형외과'")
        print("  py daily_log_manager.py health '허리 통증'")
        print("  py daily_log_manager.py status")
