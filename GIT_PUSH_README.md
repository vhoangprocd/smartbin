# Git Push Helper

This folder contains helper scripts to set git identity, create an initial commit (if none), ensure `main` branch, and push to the remote origin.

Files:
- `git_push_all.bat` — Windows interactive batch script (run from repo root)
- `git_push_all.sh` — Unix shell script (run from repo root)
- `push_repo.py` — Python helper script (cross-platform)

Usage examples:

Windows (double-click or run in CMD from repo root):
```bat
git_push_all.bat
```

Unix / macOS:
```bash
# make executable once
chmod +x git_push_all.sh
./git_push_all.sh
```

Python (cross-platform):
```bash
python push_repo.py --remote https://github.com/vhoangprocd/smartbin.git --name "Your Name" --email you@example.com
```

Notes:
- If using HTTPS, Git will prompt for credentials unless you have a credential helper configured.
- For GitHub, consider using Git Credential Manager or SSH keys to avoid repeated password prompts.
