#!/usr/bin/env bash
# install-skills.sh — Install or remove the ToolShed skills in this folder.
# Usage:
#   ./skills/install-skills.sh               # Install into ./.claude/skills
#   ./skills/install-skills.sh --global      # Install into ~/.claude/skills
#   ./skills/install-skills.sh --target DIR  # Install into a custom folder
#   ./skills/install-skills.sh --dry-run     # Show what would happen without changing files
#   ./skills/install-skills.sh --remove      # Remove the skills from the target folder

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS=("intent-mirror" "claim-to-chart" "design-system-from-notes" "learning-capture")

TARGET_DIR="$(pwd)/.claude/skills"
DRY_RUN=0
REMOVE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --global)
      TARGET_DIR="${HOME}/.claude/skills"
      shift
      ;;
    --target)
      if [[ $# -lt 2 ]]; then
        echo "Error: --target requires a folder path." >&2
        exit 1
      fi
      TARGET_DIR="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --remove|--uninstall)
      REMOVE=1
      shift
      ;;
    -h|--help)
      echo "ToolShed Skills Installer"
      echo ""
      echo "Usage:"
      echo "  ./skills/install-skills.sh               Install into ./.claude/skills"
      echo "  ./skills/install-skills.sh --global      Install into ~/.claude/skills"
      echo "  ./skills/install-skills.sh --target DIR  Install into DIR"
      echo "  ./skills/install-skills.sh --dry-run     Preview actions without changing files"
      echo "  ./skills/install-skills.sh --remove      Remove the installed skills"
      exit 0
      ;;
    *)
      echo "Unknown option: $1 (run with --help for usage)" >&2
      exit 1
      ;;
  esac
done

TIMESTAMP="$(date +%Y%m%d-%H%M%S)"

if [[ "$REMOVE" -eq 1 ]]; then
  echo "Removing ToolShed skills from: ${TARGET_DIR}"
  for skill in "${SKILLS[@]}"; do
    dest="${TARGET_DIR}/${skill}"
    if [[ -d "$dest" ]]; then
      if [[ "$DRY_RUN" -eq 1 ]]; then
        echo "  [dry-run] Would remove ${dest}"
      else
        rm -rf "$dest"
        echo "  Removed ${skill}"
      fi
    else
      echo "  Skipped ${skill} (not present)"
    fi
  done
  exit 0
fi

echo "Installing ToolShed skills into: ${TARGET_DIR}"
if [[ "$DRY_RUN" -eq 0 ]]; then
  mkdir -p "$TARGET_DIR"
else
  echo "  [dry-run] Would ensure folder exists: ${TARGET_DIR}"
fi

for skill in "${SKILLS[@]}"; do
  src="${SCRIPT_DIR}/${skill}"
  dest="${TARGET_DIR}/${skill}"

  if [[ ! -f "${src}/SKILL.md" ]]; then
    echo "Error: Missing ${src}/SKILL.md" >&2
    exit 1
  fi

  if [[ -d "$dest" ]]; then
    backup="${dest}.backup-${TIMESTAMP}"
    if [[ "$DRY_RUN" -eq 1 ]]; then
      echo "  [dry-run] Found existing ${skill}; would back up to ${backup}"
    else
      mv "$dest" "$backup"
      echo "  Backed up existing ${skill} to $(basename "$backup")"
    fi
  fi

  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "  [dry-run] Would copy ${skill} -> ${dest}"
  else
    mkdir -p "$dest"
    cp -R "${src}/." "$dest/"
    echo "  Installed ${skill}"
  fi
done

echo ""
echo "Done. Installed skills: ${SKILLS[*]}"
echo "To remove them later, run: ./skills/install-skills.sh --remove --target \"${TARGET_DIR}\""
