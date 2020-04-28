#!/bin/bash
old_prefix=.rng
new_prefix=.txt
for f in *$old_prefix; do 
    mv -- "$f" "${f%$old_prefix}$new_prefix"
done
