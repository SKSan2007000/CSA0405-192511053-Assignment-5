#!/usr/bin/env bash
set -euo pipefail
THRESHOLD="${1:-80}"
USE=$(df -P / | awk 'NR==2 {gsub("%","",$5); print $5}')
printf "Root filesystem usage: %s%% (alert threshold: %s%%)\n" "$USE" "$THRESHOLD"
if (( USE >= THRESHOLD )); then echo "ALERT: disk usage threshold exceeded"; else echo "OK: disk usage below threshold"; fi
