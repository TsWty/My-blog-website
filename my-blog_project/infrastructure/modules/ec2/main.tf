resource "aws_instance" "ec2" { 
  ami                         = var.ami
  instance_type               = var.instance_type
  subnet_id                   = var.subnet_id
  vpc_security_group_ids      = [var.security_group_id]
  associate_public_ip_address = true
  key_name                    = var.key_name
  network_interface {
    network_interface_id = var.network_interface_id
    device_index         = 0
    
  }
  tags = {
    Name        = "blog-ec2"
    Environment = "dev"
  }
}


