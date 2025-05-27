terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}
module "vpc" {
  source = "./modules/vpc"
}

module "my_eni" {
  source = "./modules/eni"
  subnet_id = module.vpc.subnet_id
  security_groups = module.sg.security_group_id
}
module "my_eip" {
  source = "./modules/eip"
  network_interface_id = module.my_eni.network_interface_id
}
module "sg" {
  source = "./modules/sg"
  vpc_id = module.vpc.vpc_id
}

module "ec2" {
  source            = "./modules/ec2"
  ami               = var.ami
  instance_type     = var.instance_type
  subnet_id         = module.vpc.subnet_id
  security_group_id = module.sg.security_group_id
  key_name          = var.key_name
  network_interface_id = module.my_eni.aws_eni_id
}

# Example Terraform configuration to create an ENI, multiple EIPs, and an EC2 instance using the same ENI

# # 1) Create a single ENI
# module "eni" {
#   source          = "../modules/eni"   # path to ENI module
#   subnet_id       = var.subnet_id
#   security_groups = var.security_groups
# }

# # 2) Create multiple EIPs on the same ENI
# module "eips" {
#   source    = "../modules/eip"        # path to EIP module
#   for_each  = toset(var.eip_names)     # e.g. ["primary","secondary","tertiary"]

#   network_interface_id = module.eni.eni_id  # attach all to this one ENI
#   # (optional) name = each.key             # tag each EIP if you like
# }

# # 3) Spin up EC2 using the same ENI
# module "ec2" {
#   source               = "../modules/ec2"  # path to EC2 module
#   ami                  = var.ami
#   instance_type        = var.instance_type
#   network_interface_id = module.eni.eni_id  # use ENI as eth0
# }

# # Outputs
# output "eni_public_ips" {
#   description = "Map of all Elastic IPs on the ENI"
#   value = {
#     for name, e in module.eips : name => e.public_ip
#   }
# }
