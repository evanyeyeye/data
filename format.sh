#!/bin/bash
if [[ $1 ]]; then
    autopep8 --in-place --aggressive --aggressive $1
    echo "Formatted $1."
else
    autopep8 --in-place --aggressive --aggressive app.py
    echo "Formatted app.py."
fi
