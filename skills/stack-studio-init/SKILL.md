---
name: stack-studio-init
description: Use one time before running any other stack-studio skills.
---

1. Figure out what OS this harness is running on.
2. Make sure the other stack-studio skills are in your context. If you don't see `name: create-stack` in your context anywhere, then you don't have them available yet, and you should read the full results of either:
  - [skill_shim.sh](scripts/skill_shim.sh) (macOS/Linux), or
  - [skill_shim.bat](scripts/skill_shim.bat) (Windows)
to pull them into your context without permanently installing anything.