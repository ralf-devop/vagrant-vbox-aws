# Configure the AWS provider
provider "aws" {
  region = "eu-central-1"
}

# Create private key for ssh connection
resource "tls_private_key" "training_key" {
  algorithm = "ED25519"
}

# Create AWS key pair
resource "aws_key_pair" "training_key_pair" {
  key_name   = "training-ssh-key"
  public_key = tls_private_key.training_key.public_key_openssh
}

# Write the private key to the hard drive so that the trainee can connect later
resource "local_sensitive_file" "local_training_key" {
  content  = tls_private_key.training_key.private_key_openssh
  filename = "${path.module}/${aws_key_pair.training_key_pair.key_name}"
}

# Create own training environment for each trainee
resource "aws_instance" "training-env" {
  ami = "ami-0de6934e87badb694"
  instance_type = "t2.micro"
  key_name = aws_key_pair.training_key_pair.key_name
  count = "${var.number_trainees}"

  user_data = templatefile("${path.module}/user_data.sh.tpl", {
    key = aws_key_pair.training_key_pair.public_key
    key_name = "${aws_key_pair.training_key_pair.key_name}"
    user = "trainee_${count.index}"
  })

  tags = {
    Name = "training-machines"
  }
}

# Output variable: Public IP address
output "trainee_public_ip" {
   value = {
    for k, v in aws_instance.training-env : k => {
      ip = v.public_ip
      user = "trainee_${k}"
      connection_string = "ssh -i ${aws_key_pair.training_key_pair.key_name} trainee_${k}@${v.public_ip}"
    }
  }
}
