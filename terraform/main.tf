provider "aws" {
  region = "us-east-1"
  default_tags {
    tags = {
      Terraform = true
      Owner     = "jacobm3@gmail.com"
      TTL       = 768
    }
  }
}

data "aws_ami" "latest-ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "web" {
  ami = data.aws_ami.latest-ubuntu.id

  # t3a.large; 2 vcpu, 8GB ram, ebs = $1.80/day
  # m5d.large; 2 vcpu, 8GB ram, nvme = $2.70/day
  # m5d.xlarge; 4 vcpu, 16GB ram, nvme = $5.42/day
  # m6a.large; 2 vcpu, 8GB ram, ebs = $2.07/day

  instance_type        = "m5d.large"
  key_name             = "acer-wsl"
  user_data            = file("userdata.sh")
  iam_instance_profile = aws_iam_instance_profile.airflow.name
  security_groups      = [aws_security_group.airflow.name]
  lifecycle {
    ignore_changes = [user_data]
  }
  tags = {
    Name = "airflow"
  }
}

resource "aws_iam_instance_profile" "airflow" {
  name = "airflow-instance-profile"
  role = aws_iam_role.instance_role.name
}

resource "aws_iam_role" "instance_role" {
  name               = "airflow-iam-role"
  assume_role_policy = data.aws_iam_policy_document.instance_role.json
  managed_policy_arns = [aws_iam_policy.s3_uploader_policy.arn,
  aws_iam_policy.rekognition_policy.arn]
}

resource "aws_iam_policy" "s3_uploader_policy" {
  name   = "s3_uploader_policy"
  policy = data.aws_iam_policy_document.s3_uploader.json
}


data "aws_iam_policy_document" "s3_uploader" {
  statement {
    effect = "Allow"

    actions = [
      "s3:*",
    ]

    resources = [
      aws_s3_bucket.site_bucket.arn,
      "${aws_s3_bucket.site_bucket.arn}/*",
    ]
  }
}


resource "aws_iam_policy" "rekognition_policy" {
  name   = "rekognition_policy"
  policy = data.aws_iam_policy_document.rekognition_policy_doc.json
}

data "aws_iam_policy_document" "rekognition_policy_doc" {
  statement {
    effect    = "Allow"
    actions   = ["rekognition:*"]
    resources = ["*"]
  }
}

data "aws_iam_policy_document" "instance_role" {
  statement {
    effect = "Allow"
    actions = [
      "sts:AssumeRole",
    ]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_security_group" "airflow" {
  name        = "airflow"
  description = "Allow airflow inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["73.166.0.0/16"]
  }

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["73.166.0.0/16"]
    #cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "airflow"
  }
}


