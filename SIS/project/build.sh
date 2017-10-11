#!/bin/bash
pids=()

for svgfile in *.svg; do
    file_name=$(echo $svgfile | sed -r 's/(.+)\..+|(.*)/\1\2/')
    svg_part="--file=$svgfile"
    pdf_part="--export-pdf=$file_name.pdf"
    pids+=$(inkscape -D -z $svg_part $pdf_part --export-latex &)
done

for pid in $pids; do
    wait pid
done

pdflatex sprawozdanie.tex > /dev/null
mkdir -p out
mv sprawozdanie.pdf out

rm *pdf *pdf_tex *log *aux
