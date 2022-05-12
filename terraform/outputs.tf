output "public_ip" {
  value = aws_instance.web.public_ip
}

output "instance_id" {
  value = aws_instance.web.id
}

output "bucket" {
  value = aws_s3_bucket.site_bucket.bucket
}

output "bucket_domain_name" {
  value = aws_s3_bucket.site_bucket.bucket_domain_name
}

