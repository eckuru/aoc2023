#!/usr/bin/env sh

sed 's/[a-z|A-Z]//g' input  > inputdigits
sed 's/\(^[0-9]\).*\([0-9]\)$/\1\2/' inputdigits > relevant
sed 's/\(^[0-9]$\)/\1\1/' relevant > numbers
awk '{s+=$1} END {print s}' numbers
