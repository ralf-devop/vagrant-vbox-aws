# Configure the AWS provider
provider "aws" {
  region = "eu-central-1"
}

# Create own training environment for each trainee
resource "aws_instance" "training-env" {
  ami = "ami-0de6934e87badb694"
  instance_type = "t2.micro"
  key_name = "myawskey"
  count = 3

  user_data = <<-EOF
        #!/bin/bash
        sudo useradd trainee_${count.index}
    EOF

  tags = {
    Name = "training-machines"
  }
}

# Output variable: Public IP address
output "public_ip" {
  value = "${aws_instance.training-env[*].public_ip}"
}
