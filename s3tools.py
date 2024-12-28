import boto3

s3 = boto3.resource('s3')
#s3.Bucket("webscrape123").upload_file("./myfile.jpg", "myfile.jpg")
s3.Bucket("webscrape123").download_file("myfile.jpg", "./myfile.jpg")
