#!/bin/bash
echo "Hello Container!"

poetry install --no-dev

echo "Install DONE!!"

echo "Show packages!"

sleep 3

poetry show