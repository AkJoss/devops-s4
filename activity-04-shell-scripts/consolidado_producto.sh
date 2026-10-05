#!/bin/bash
# Activity 04 — split eventos.txt into one CSV per product id
# Usage: ./consolidado_producto.sh   (requires eventos.txt in cwd)
# @author José Alberto Rocha Munguía

if [ ! -f "eventos.txt" ]; then
    echo "Error: El archivo 'eventos.txt' no existe."
    exit 1
fi

# Extract numeric product ids, then dump matching lines per product
egrep -o '[0-9]+' eventos.txt | sort | uniq | while read producto; do
    grep "$producto" eventos.txt > "producto_$producto.csv"
done

echo "Archivos CSV generados por producto"
