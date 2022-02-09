s3_client = boto3.client('s3')
response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="issuer_settlement_files/temp_files/")
for object in response['Contents']:
    print('Deleting', object['Key'])
    s3_client.delete_object(Bucket=bucket_name, Key=object['Key'])
