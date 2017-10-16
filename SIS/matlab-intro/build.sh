#!/bin/bash
pids=()
for svgfile in *.svg; do
    file_name=$(echo $svgfile | sed -r 's/(.+)\..+|(.*)/\1\2/')
    pids+=$(inkscape -z -e $file_name.png -h 1024 $svgfile &)
done

for pid in $pids; do
    wait pid
done
pdflatex sprawozdanie.tex
mkdir -p out
mv sprawozdanie.pdf out

rm *log *aux
