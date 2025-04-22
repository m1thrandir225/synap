#!/bin/bash

is_true() {
  [[ "$1" == "true" ]] || [[ "$1" == "True" ]]
}

is_false() {
  [[ "$1" == "false" ]] || [[ "$1" == "False" ]]
}

if [ -z "$1" ]; then
    echo "Error: please provide a miration message"
    echo "Usage: ./migrate.sh <migration_message> [autogenerate: true|false]"
    exit 1
fi

MESSAGE="$1"
AUTOGENERATE=false


if [ -n "$2" ]; then
  if is_true "$2"; then
    AUTOGENERATE=true
  elif is_false "$2"; then
    AUTOGENERATE=false
  else
    echo "Error: invalid value for autogenerate. Use 'true' or 'false'."
    echo "Usage: ./create_migration.sh <migration_message> [autogenerate: true|false]"
    exit 1
  fi
fi

echo "Generating a new Alembic migration with message: $MESSAGE"
if "$AUTOGENERATE"; then
    alembic revision --autogenerate -m "$MESSAGE"
else 
    alembic revision -m "$MESSAGE"
fi