# 1. List All S3 Buckets
# Write a function list_s3_buckets() that:
# Uses boto3 to retrieve and print all S3 bucket names in your AWS account.


# 2. Create an S3 Bucket

# Write a function create_s3_bucket(bucket_name, region) that:
# Creates a new S3 bucket in the specified region (e.g., us-east-1).
# Handles errors gracefully (e.g., if the bucket already exists).


# 3. Delete an S3 Bucket

# Write a function delete_s3_bucket(bucket_name) that:
# Deletes the specified S3 bucket.
# Handles errors if the bucket does not exist or is not empty.

# 4. Bonus Task (Optional):

# Write a function upload_file_to_s3(file_path, bucket_name, object_name) that:
# Uploads a local file to an S3 bucket.
# Use file_path as the path to the file and object_name as the key in the S3 bucket.

# Tips:

# Boto3 Documentation: Use the official Boto3 documentation as a reference.
# S3 Client/Resource: You can use boto3.client('s3') for fine-grained control or boto3.resource('s3') for higher-level abstractions.
# Error Handling: Use try-except to catch common errors like botocore.exceptions.ClientError.


import boto3

def list_s3_buckets() :
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print('Existing Buckets:')
    
    for bucket in response['Buckets']:
        print (f'{bucket ["Name"]}')


list_s3_buckets()


def create_s3_bucket(bucket_name, region):
    s3 = boto3.client('s3')
    try:
        if region == "ap-south-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket (
                Bucket = bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

create_s3_bucket("test12s45", "ap-south-1")


def delete_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully")
    except Exception as e:
        print(f"Error deleting bucket: {e}")

delete_s3_bucket("test12s45")