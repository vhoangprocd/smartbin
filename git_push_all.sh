#!/usr/bin/env bash
# Git push helper for Unix (run from repo root)
set -euo pipefail

echo
echo "================================================="
echo "  SmartBin - Git Push All (Unix)
echo "================================================="

echo "Working dir: $(pwd)"

# Check git
if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git not found"
  exit 1
fi

read -p "Enter Git user.name (leave empty to keep existing): " GIT_NAME
if [ -n "$GIT_NAME" ]; then
  git config user.name "$GIT_NAME"
  echo "Set user.name = $GIT_NAME"
fi

read -p "Enter Git user.email (leave empty to keep existing): " GIT_EMAIL
if [ -n "$GIT_EMAIL" ]; then
  git config user.email "$GIT_EMAIL"
  echo "Set user.email = $GIT_EMAIL"
fi

read -p "Enter remote URL to add/set (leave empty to use existing origin): " REMOTE_URL
if [ -n "$REMOTE_URL" ]; then
  git remote remove origin 2>/dev/null || true
  git remote add origin "$REMOTE_URL"
  echo "Remote origin set to $REMOTE_URL"
fi

echo
echo "--- Git status ---"
git status --porcelain || true

# If no commits, create initial commit
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  echo "No commits found. Creating initial commit..."
  git add .
  git commit -m "Initial commit"
else
  echo "Commits exist."
fi

# Ensure branch main
git branch -M main || true

# Push
echo "Pushing to origin main..."
git push -u origin main

echo "SUCCESS: Pushed to origin main."
