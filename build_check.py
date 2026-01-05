# Quick check to ensure files exist before 'commit'
import os
required = [
    "figures/figure1_updated.png",
    "figures/figure2_updated.png",
    "main.tex",
    "CHANGELOG.md",
    "docs/commit_message.txt"
]
missing = [f for f in required if not os.path.exists(f)]
if missing:
    print(f"Missing files: {missing}")
else:
    print("All deliverables present.")