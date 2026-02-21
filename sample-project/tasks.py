"""
Business logic for task management.
"""

import uuid
from datetime import datetime

PRIORITY_ORDER = {"low": 0, "medium": 1, "high": 2}

VALID_STATUSES = {"open", "in_progress", "done"}
VALID_PRIORITIES = {"low", "medium", "high"}


def create_task(title, description="", priority="medium", status="open"):
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "priority": priority,
        "status": status,
        "created_at": datetime.utcnow().isoformat(),
    }


def filter_by_status(tasks, status):
    return [t for t in tasks if t["status"] == status]


def filter_by_priority(tasks, priority):
    # BUG: uses >= instead of ==, so "low" returns everything,
    # "medium" returns medium + high, and only "high" works correctly.
    # The symptom: GET /tasks?priority=medium returns too many results.
    target = PRIORITY_ORDER.get(priority, -1)
    return [t for t in tasks if PRIORITY_ORDER.get(t["priority"], -1) >= target]


def sort_by_priority(tasks):
    return sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t["priority"], 0), reverse=True)


def get_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task, updates):
    allowed_fields = {"title", "description", "priority", "status"}
    for key, value in updates.items():
        if key in allowed_fields:
            task[key] = value
    return task
