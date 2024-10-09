#!/bin/bash

sed -i 's/multi_region = false/multi_region = true/' main.tf
sed -i '/primary_bucket_region = "REPLACE_PRIMARY_REGION_VALUE"/a\  secondary_bucket_region = "REPLACE_SECONDARY_REGION_VALUE"' main.tf

echo "========"
cat main.tf
