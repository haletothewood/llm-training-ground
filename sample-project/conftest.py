import sys
from pathlib import Path

# Allow tests to import modules from sample-project when run from the repo root
sys.path.insert(0, str(Path(__file__).parent))
