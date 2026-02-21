"""
Unit tests for tasks.py business logic.
"""

import pytest
import tasks as task_lib


# --- create_task ---

def test_create_task_returns_required_fields():
    task = task_lib.create_task("Write docs")
    assert task["title"] == "Write docs"
    assert task["status"] == "open"
    assert task["priority"] == "medium"
    assert "id" in task
    assert "created_at" in task


def test_create_task_accepts_custom_priority():
    task = task_lib.create_task("Deploy", priority="high")
    assert task["priority"] == "high"


# --- filter_by_status ---

def test_filter_by_status_returns_matching():
    tasks = [
        task_lib.create_task("A", status="open"),
        task_lib.create_task("B", status="done"),
        task_lib.create_task("C", status="open"),
    ]
    result = task_lib.filter_by_status(tasks, "open")
    assert len(result) == 2
    assert all(t["status"] == "open" for t in result)


# --- filter_by_priority ---

def test_filter_by_priority_returns_only_matching():
    tasks = [
        task_lib.create_task("A", priority="low"),
        task_lib.create_task("B", priority="medium"),
        task_lib.create_task("C", priority="high"),
    ]
    result = task_lib.filter_by_priority(tasks, "high")
    # Should return only the high-priority task.
    # This test passes even with the bug — "high" happens to work with >=.
    assert len(result) == 1
    assert result[0]["title"] == "C"


def test_filter_by_priority_medium_excludes_high():
    tasks = [
        task_lib.create_task("A", priority="medium"),
        task_lib.create_task("B", priority="high"),
    ]
    result = task_lib.filter_by_priority(tasks, "medium")
    # Should return only medium tasks.
    # This test currently fails due to the bug in filter_by_priority.
    assert len(result) == 1
    assert result[0]["title"] == "A"


# --- sort_by_priority ---

def test_sort_by_priority_descending():
    tasks = [
        task_lib.create_task("Low", priority="low"),
        task_lib.create_task("High", priority="high"),
        task_lib.create_task("Medium", priority="medium"),
    ]
    result = task_lib.sort_by_priority(tasks)
    assert result[0]["priority"] == "high"
    assert result[1]["priority"] == "medium"
    assert result[2]["priority"] == "low"


# --- update_task ---

def test_update_task_changes_allowed_fields():
    task = task_lib.create_task("Original")
    task_lib.update_task(task, {"title": "Updated", "status": "done"})
    assert task["title"] == "Updated"
    assert task["status"] == "done"


def test_update_task_ignores_id_changes():
    task = task_lib.create_task("Original")
    original_id = task["id"]
    task_lib.update_task(task, {"id": "hacked-id"})
    assert task["id"] == original_id
