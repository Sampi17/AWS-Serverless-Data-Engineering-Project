resource  "aws_s3_bucket" "b" {
 bucket = "my-data-lake-17"
 
 
 tags = {
  Name = "My bucket"
  Environment = "Dev"
 }
}
