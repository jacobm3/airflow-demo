provider "namecheap" {
  use_sandbox = false
}

resource "namecheap_record" "airflow" {
  domain     = "theneutral.zone"
  name       = "airflow"
  address    = aws_instance.airflow.public_ip
  type       = "A"
  ttl        = "60"
  depends_on = [aws_instance.airflow]
}

resource "namecheap_record" "vault" {
  domain     = "theneutral.zone"
  name       = "vault"
  address    = aws_instance.vault.public_ip
  type       = "A"
  ttl        = "60"
  depends_on = [aws_instance.vault]
}
