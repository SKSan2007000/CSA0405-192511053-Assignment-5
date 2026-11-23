#!/usr/bin/env bash
set -euo pipefail
LOG_FILE="${1:-logs/access.log}"
if [[ ! -r "$LOG_FILE" ]]; then echo "Cannot read $LOG_FILE" >&2; exit 1; fi
echo "Requests per status code:"
awk '{print $7}' "$LOG_FILE" | sort -n | uniq -c | awk '{printf "  %s %s\n",$2,$1}'
echo "Busiest client:"
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -rn | awk 'NR==1 {printf "  %s %s\n",$2,$1}'
echo "Total bytes sent: $(awk '{s += $8} END {print s+0}' "$LOG_FILE")"
