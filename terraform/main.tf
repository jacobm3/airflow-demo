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
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.latest-ubuntu.id

  # t3a.large; 2 vcpu, 8GB ram, ebs = $1.80/day
  # m5d.large; 2 vcpu, 8GB ram, nvme = $2.70/day
  # m6a.large; 2 vcpu, 8GB ram, ebs = $2.07/day

  instance_type = "m5d.large"
  key_name      = "acer-wsl"
  user_data     = file("userdata.sh")
  iam_instance_profile = aws_iam_instance_profile.airflow.name
  tags = {
    Name = "airflow"
  }
}

resource "aws_iam_instance_profile" "airflow" {
  name = "airflow-instance-profile"
  role        = aws_iam_role.instance_role.name
}

resource "aws_iam_role" "instance_role" {
  name        = "airflow-iam-role"
  assume_role_policy = data.aws_iam_policy_document.instance_role.json
  managed_policy_arns = [aws_iam_policy.s3_uploader_policy.arn]
}

resource "aws_iam_policy" "s3_uploader_policy" {
  name = "s3_uploader_policy"
  policy = data.aws_iam_policy_document.s3_uploader.json
}

#resource "aws_iam_role_policy_attachment" "test-attach" {
#  role       = aws_iam_role.instance_role.name
#  policy_arn = aws_iam_policy.s3_uploader_policy.arn
#}

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


data "aws_iam_policy_document" "s3_uploader" {
  statement {
    effect = "Allow"

    actions = [
      "s3:Get*",
      "s3:List*",
      "s3:PutObject",
      "s3:DeleteObject",
    ]

    resources = [
      aws_s3_bucket.site_bucket.arn,
      "${aws_s3_bucket.site_bucket.arn}/*",
    ]
  }
}




