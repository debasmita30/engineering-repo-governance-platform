import re
import sys

PATTERN = r"^(feat|fix|chore|docs|refactor|test|ci): .+"

commit_msg_file = sys.argv[1]

with open(commit_msg_file, "r") as f:
    message = f.readline().strip()

if not re.match(PATTERN, message):
    print(
        "Invalid commit message.\n"
        "Use format: type: message\n"
        "Example: feat: add CI pipeline"
    )
    sys.exit(1)
