module "infra" {
  source = "../../modules/infra"

  base_name    = "REPLACE_APP_NAME"
  multi_region = false

  primary_bucket_region = "REPLACE_PRIMARY_REGION_VALUE"
}
