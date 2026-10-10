#!/usr/bin/env bash
# Restore only the assignment database from its saved baseline.
set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
baseline="$project_dir/backups/baseball-baseline.sql"

if [[ ! -s "$baseline" || ! -r "$baseline" ]]; then
    echo "Missing, empty, or unreadable backup: $baseline" >&2
    exit 1
fi
command -v mariadb >/dev/null

echo "This erases baseball and restores backups/baseball-baseline.sql."
echo "Stop assignment programs before continuing."
read -r -p "Type baseball to continue: " answer
if [[ "$answer" != "baseball" ]]; then
    echo "Cancelled."
    exit 0
fi

# The restricted account can recreate baseball but cannot modify flask_app.
# MariaDB prompts for the password; the script never stores it.
if {
    printf '%s\n' 'DROP DATABASE IF EXISTS `baseball`;' \
        'CREATE DATABASE `baseball` CHARACTER SET utf8mb4;' 'USE `baseball`;'
    cat -- "$baseline"
} | mariadb --user=baseball_user --password; then
    echo "Baseline restored."
else
    echo "Restore failed. baseball may be incomplete; fix the error and rerun." >&2
    exit 1
fi
