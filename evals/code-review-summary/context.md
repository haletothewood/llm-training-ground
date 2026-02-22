```diff
--- a/sample-project/tasks.py
+++ b/sample-project/tasks.py
@@ -29,6 +29,4 @@ def filter_by_status(tasks, status):
 def filter_by_priority(tasks, priority):
-    # BUG: uses >= instead of ==, so "low" returns everything,
-    # "medium" returns medium + high, and only "high" works correctly.
-    target = PRIORITY_ORDER.get(priority, -1)
-    return [t for t in tasks if PRIORITY_ORDER.get(t["priority"], -1) >= target]
+    return [t for t in tasks if t["priority"] == priority]
```
