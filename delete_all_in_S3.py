import boto
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.objects.filter(Prefix="dir_path/").delete()
