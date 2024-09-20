#!/bin/bash
ls -la
pwd
ls -la workflows
python3.8 ./update-files.py
cat workflows/cicd-output.yaml