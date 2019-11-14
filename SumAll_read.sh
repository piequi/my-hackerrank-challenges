#!/bin/bash

SUM=0

read -p "Array = " INT_ARRAY

for int in $INT_ARRAY; do
    let "SUM = $SUM + $int"
done

echo $SUM
