#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ~/data/list.txt | cut -d' ' -f3 | cut -d'/' -f3)

for i in $files; do
	if test -e ~/data/$i; then
		echo $HOME/data/$i >> oldFiles.txt
	fi
done

