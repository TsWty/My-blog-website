output "ec2_id"      { value = module.my_ec2.instance_id }
output "ec2_public"  { value = module.my_eip.public_ip }

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "subnet_id" {
  description = "Subnet ID"
  value       = module.vpc.subnet_id
}
