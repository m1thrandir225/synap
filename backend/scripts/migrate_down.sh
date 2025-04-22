#!/bin/bash 
if [ -z "$1"]; then
    echo "Error: please provide an argument"
    echo "Option 1: ./migrate_down.sh -1 - migrate down 1 version"
    echo "Option 2: ./migrate_down.sh base - migrate down all versions"
    exit 1
fi

TARGET="$1"

alembic downgrade $TARGET