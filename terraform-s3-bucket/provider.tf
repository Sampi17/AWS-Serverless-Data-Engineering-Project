terraform {
	required_providers {
	 aws = {
	  source = "hashicorp/aws"
	 
	 }
	}
}
    
provider "aws" {
	#configuration options
	region ="us-east-2"
	profile = "default"
	}
