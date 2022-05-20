output "airflow_public_ip" {
  value = aws_instance.airflow.public_ip
}

output "airflow_instance_id" {
  value = aws_instance.airflow.id
}

output "vault_public_ip" {
  value = aws_instance.vault.public_ip
}

output "vault_instance_id" {
  value = aws_instance.vault.id
}

output "bucket" {
  value = aws_s3_bucket.site_bucket.bucket
}

output "bucket_domain_name" {
  value = aws_s3_bucket.site_bucket.bucket_domain_name
}

