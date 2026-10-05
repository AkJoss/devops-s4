#!/bin/bash
# Activity 05 — hello world + append argv into vim.txt
# @author José Alberto Rocha Munguía

echo "Hello World"

echo "Estoy usando vim" > vim.txt

echo "$1" >> vim.txt
