# Git Collaboration Guide

## Project

M_E1-2: Machine Tool and Vibration Analysis Quiz

## Purpose

This document explains how to contribute to the project
using a separate Git clone and a feature branch.

## Workflow

1. Clone the public repository.
2. Create a dedicated branch.
3. Modify project documentation or source code.
4. Run the automated tests.
5. Commit the changes.
6. Merge the branch into main.
7. Push main to GitHub.
8. Pull the changes into the original repository.

## Commands

    git clone https://github.com/cody26jade/M_E1-2.git
    git checkout -b feature/example
    python -m unittest discover -s tests
    git add .
    git commit -m "Describe the change"
    git checkout main
    git merge --no-ff feature/example
    git push origin main
    git pull --ff-only origin main

## Runtime Data Protection

The local state.json file contains user-created questions,
best scores and play history.

It must not be committed or shared through GitHub.

## Testing

Run the complete unit test suite before merging changes.

Python 3.10 or later is required.
No third-party Python packages are required.
