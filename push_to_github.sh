#!/usr/bin/env bash
# Create a GitHub repo on your personal account and push this project to it.
# Usage: ./push_to_github.sh [repo-name]
# Needs a GitHub personal access token:
#   - classic token with the "repo" scope, or
#   - fine-grained token with "Administration: write" + "Contents: write" on your account.
set -euo pipefail

GIT_EMAIL="shikharprakash07@gmail.com"
DEFAULT_REPO="isb-capstone-ai-sentinel"
API="https://api.github.com"

cd "$(dirname "$0")"

for cmd in git curl python3; do
  command -v "$cmd" >/dev/null || { echo "Error: '$cmd' is not installed." >&2; exit 1; }
done

# ---- inputs ---------------------------------------------------------------
REPO_NAME="${1:-}"
if [[ -z "$REPO_NAME" ]]; then
  read -r -p "Repository name [$DEFAULT_REPO]: " REPO_NAME
  REPO_NAME="${REPO_NAME:-$DEFAULT_REPO}"
fi
read -r -p "Make the repository private? [Y/n]: " PRIV
case "${PRIV:-Y}" in [nN]*) PRIVATE=false ;; *) PRIVATE=true ;; esac

read -r -s -p "GitHub personal access token: " GH_TOKEN; echo
[[ -n "$GH_TOKEN" ]] || { echo "Error: no token entered." >&2; exit 1; }

json_field() { python3 -c "import sys,json; print(json.load(sys.stdin).get('$1',''))"; }

RESP_FILE=$(mktemp)
trap 'unset GH_TOKEN; rm -f "$RESP_FILE"' EXIT

gh_api() {  # gh_api METHOD PATH [JSON]; body -> $RESP_FILE, status -> $HTTP_STATUS
  HTTP_STATUS=$(curl -sS -o "$RESP_FILE" -w '%{http_code}' -X "$1" "$API$2" \
        -H "Authorization: Bearer $GH_TOKEN" \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        ${3:+-d "$3"})
}

# ---- who am I -------------------------------------------------------------
gh_api GET /user
if [[ "$HTTP_STATUS" != "200" ]]; then
  echo "Error: token rejected by GitHub (HTTP $HTTP_STATUS)." >&2; exit 1
fi
GH_USER=$(json_field login < "$RESP_FILE")
GH_NAME=$(json_field name < "$RESP_FILE")
echo "Authenticated as: $GH_USER"

# ---- local repository -----------------------------------------------------
if [[ ! -d .git ]]; then
  git init -q
  git checkout -q -b main
fi
git config user.email "$GIT_EMAIL"
git config user.name "${GH_NAME:-$GH_USER}"

if [[ ! -f .gitignore ]]; then
  cat > .gitignore <<'EOF'
.DS_Store
~$*
*.tmp
__pycache__/
*.pyc
.venv/
venv/
*.pdf
EOF
fi

git add -A
if git diff --cached --quiet; then
  echo "No new changes to commit."
else
  git commit -q -m "ISB PCPM capstone: Cisco AI Sentinel product proposal"
  echo "Committed project files."
fi
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# ---- create the GitHub repository ------------------------------------------
BODY=$(python3 -c 'import json,sys; print(json.dumps({"name": sys.argv[1], "private": sys.argv[2] == "true",
  "description": "ISB PCPM capstone: Cisco AI Sentinel product proposal (report + executive deck)"}))' \
  "$REPO_NAME" "$PRIVATE")
gh_api POST /user/repos "$BODY"
case "$HTTP_STATUS" in
  201) echo "Created repository $GH_USER/$REPO_NAME (private=$PRIVATE)." ;;
  422) echo "Repository $GH_USER/$REPO_NAME already exists; pushing to it." ;;
  *)   echo "Error creating repository (HTTP $HTTP_STATUS):" >&2
       json_field message < "$RESP_FILE" >&2; exit 1 ;;
esac

# ---- push (token passed as a one-off header, never stored) ------------------
REMOTE_URL="https://github.com/$GH_USER/$REPO_NAME.git"
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

AUTH=$(printf 'x-access-token:%s' "$GH_TOKEN" | base64 | tr -d '\n')
git -c credential.helper= -c http.extraHeader="Authorization: Basic $AUTH" \
    push -u origin "$BRANCH"
unset AUTH

echo
echo "Done: https://github.com/$GH_USER/$REPO_NAME"
