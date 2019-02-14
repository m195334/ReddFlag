#!/bin/bash
for path in ./*; do
    for inter in $path/*; do
	[ -d "${path}" ] || continue # if not a directory, skip
	dirname="$(basename "${inter}")"
	imgdir="${dirname}_img"
	echo $inter
	mkdir "${imgdir}"
	for pdfile in $path/"${dirname}"/*.pdf ; do
	    echo $pdfile
    	    pdftoppm -l 2 -f 2 -png "${pdfile}" > "$(basename "${imgdir}")"/"$(basename "${pdfile%.*}")".png
	done
    done
    
done
