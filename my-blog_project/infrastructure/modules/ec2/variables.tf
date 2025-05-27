variable "ami" {
    description = "EC2 AMI ID"
}
variable "instance_type" {
    description = "EC2 instance_type"
}
variable "subnet_id" {
    description = "EC2 subnet_id"
}
variable "security_group_id" {
  description = "Security group"
}
variable "key_name" {
  description = "Name of the SSH key pair"
}
variable "network_interface_id" { type = string }