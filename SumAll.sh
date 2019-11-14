#!/bin/bash

SUM=0

for int in $@; do
    let "SUM = $SUM + $int"
done

echo $SUM
