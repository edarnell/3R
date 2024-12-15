#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "No .tex file specified."
    exit 1
fi

# Define paths based on provided filename
TEX_FILE="$1"
BUILD_DIR="./build"
PDF_DIR="./pdf"
AI_DIR="./ai"

# Extract base filename without extension for use with pdflatex
BASE_FILE=$(basename "$TEX_FILE" .tex)

# Clear the build directory
rm -rf $BUILD_DIR/*
echo "Cleared build directory."

# Create the build, PDF, and AI directories if they don't exist
mkdir -p $BUILD_DIR
mkdir -p $PDF_DIR
mkdir -p $AI_DIR

# Run pdflatex multiple times, outputting files to the build directory
pdflatex -output-directory=$BUILD_DIR $TEX_FILE && \
pdflatex -output-directory=$BUILD_DIR $TEX_FILE && \
pdflatex -output-directory=$BUILD_DIR $TEX_FILE

# Check if PDF was generated and move it to the PDF directory
if [ -f "$BUILD_DIR/${BASE_FILE}.pdf" ]; then
    cp "$BUILD_DIR/${BASE_FILE}.pdf" "$PDF_DIR/"
    echo "PDF moved to $PDF_DIR"
else
    echo "PDF generation failed."
fi

# Copy and rename relevant files for AI analysis to the AI directory
cp "$BUILD_DIR/${BASE_FILE}.log" "$AI_DIR/${BASE_FILE}_log.txt"

echo "debug copied to AI directory as .txt"