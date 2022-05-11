provider "aws" {
  region = "us-east-1"
  default_tags {
   tags = {
     Terraform = true
     Owner       = "email@domain.com"
     TTL     = 768
   }
 }
}

data "aws_ami" "latest-ubuntu" {
  most_recent = true
  owners = ["099720109477"] # Canonical

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
  instance_type = "t3a.large"
  key_name = "acer-wsl"
  user_data = "${file("userdata.sh")}"
  tags = {
    Name = "dev" 
  }
}

output "public_ip" {
  value       = aws_instance.web.public_ip
}

