resource "aws_eip" "this" {
  vpc = true

  tags = {
    Name        = "blog-eip"
    Environment = "dev"
  }
}
resource "aws_eip_association" "this" {
  allocation_id   = aws_eip.eip.id
  network_interface_id = var.network_interface_id
}