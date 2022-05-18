provider "namecheap" {
  use_sandbox = false
}

resource "namecheap_record" "foobar" {
  domain     = "theneutral.zone"
  name       = "airflow"
  address    = aws_instance.web.public_ip
  type       = "A"
  ttl        = "60"
  depends_on = [aws_instance.web]
}
