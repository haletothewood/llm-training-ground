```python
# sample-project/tasks.py

"""
Business logic for task management.
"""

import uuid
from datetime import datetime, timezone

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
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
```
