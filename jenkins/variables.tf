# var region
variable "region" {
    description = "aws beginner tutorial"
    type = string
    default = "us-east-1"
}

# list port of SG
variable "ingressrules" {
    type = list(number)
    default = [8080,22]
}

# AMI EC2 Linux
variable "jenkins_ami" {
    default = "ami-0c2b8ca1dad447f8a"
}