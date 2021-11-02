import boto3
fs=s3fs.S3FileSystem(anon=False)
s3=boto3.resource('s3')
fs.ls(bucket_path)
