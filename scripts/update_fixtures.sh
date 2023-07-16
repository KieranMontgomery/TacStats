#!/bin/bash

for file in tests/file/fixtures/*.json; do
    cat $file | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["input"][:-1])' > /tmp/input.acmi
    poetry run python src/main.py --fixture-insert /tmp/input.acmi > dev/null
done
echo "Done"
