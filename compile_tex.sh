#!/bin/bash

# Define paths
TEX_FILE="3R.tex"
BUILD_DIR="./build"
PDF_DIR="./pdf"
AI_DIR="./ai"
BIB_FILE="3R"

# Clear the build directory
rm -rf $BUILD_DIR/*
echo "Cleared build directory."

# Create the build, PDF, and AI directories if they don't exist
mkdir -p $BUILD_DIR
mkdir -p $PDF_DIR
mkdir -p $AI_DIR

# Run pdflatex, bibtex, and pdflatex again twice, outputting files to the build directory
pdflatex -output-directory=$BUILD_DIR $TEX_FILE && \
bibtex $BUILD_DIR/$BIB_FILE && \
pdflatex -output-directory=$BUILD_DIR $TEX_FILE && \
pdflatex -output-directory=$BUILD_DIR $TEX_FILE

# Check if PDF was generated and move it to the PDF directory
if [ -f "$BUILD_DIR/${TEX_FILE%.tex}.pdf" ]; then
    mv "$BUILD_DIR/${TEX_FILE%.tex}.pdf" "$PDF_DIR/"
    echo "PDF moved to $PDF_DIR"
else
    echo "PDF generation failed."
fi

# Copy and rename relevant files for AI analysis to the AI directory
# Adjust the file names and extensions as needed
cp "$BUILD_DIR/${TEX_FILE%.tex}.log" "$AI_DIR/${TEX_FILE%.tex}_log.txt"
cp "$BUILD_DIR/${TEX_FILE%.tex}.bbl" "$AI_DIR/${TEX_FILE%.tex}_bbl.txt"

# Add any additional files you need to copy and rename below
# Example: cp "$BUILD_DIR/otherfile.blg" "$AI_DIR/otherfile_blg.txt"

echo "Relevant files copied to AI directory."
