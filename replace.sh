#!/bin/bash

# sed -i 's/multi_region = false/multi_region = true/' main.tf
# sed -i '/primary_bucket_region = "REPLACE_PRIMARY_REGION_VALUE"/a\  secondary_bucket_region = "REPLACE_SECONDARY_REGION_VALUE"' main.tf

# echo "========"
# cat main.tf


#sed -i 's/app_dir: src/app_dir: mahendra\/src/' workflows/replace-cicd.yml
#sed -i 's/test_dir: src/tests/test_dir: mahendra\/src\/tests/' workflows/replace-cicd.yml
#sed -i -e 's|app_dir: src|app_dir: mahendra/src|' -e 's|test_dir: src/tests|test_dir: mahendra/src/tests|' workflows/replace-cicd.yml

PROJECT_NAME="MAHENDRA"

sed -i -e "s|app_dir: src|app_dir: $PROJECT_NAME/src|" -e "s|test_dir: src/tests|test_dir: $PROJECT_NAME/src/tests|" workflows/replace-cicd.yml

cat workflows/replace-cicd.yml