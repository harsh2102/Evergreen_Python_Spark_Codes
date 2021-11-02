import boto3
import s3fs
fs=s3fs.S3FileSystem(anon=False)
s3=boto3.resource('s3')
fs.ls(bucket_path)
