# Upload a File to an S3 Bucket:

# Write a function upload_file_to_s3(file_path, bucket_name, object_name) that:

# Uploads a local file to a specified S3 bucket.
# Uses file_path as the path to the file on your local machine.
# Uses object_name as the key (name of the file) in the S3 bucket.


# List Objects in an S3 Bucket:

# Write a function list_objects_in_bucket(bucket_name) that:

# Lists all objects (files) in a specified S3 bucket.
# Prints the name and size of each object.

# Download a File from an S3 Bucket:

# Write a function download_file_from_s3(bucket_name, object_name, download_path) that:

# Downloads a file (object_name) from an S3 bucket to a specified local path (download_path).

import boto3

def upload_file_to_s3(file_path, bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}' as '{object_name}'.")
    except Exception as e:
        print(f"Error uploading the file: {e}")


upload_file_to_s3("/Users/Tanmoy/Development/Python/log.txt", "test12s45", "log.txt")

def list_objects_in_bucket(bucket_name):
    s3 = boto3.client('s3')

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"Object Name: {obj['Key']}, Size: {obj['Size']} bytes")
        else:
            print(f"No objects found in bucket'{bucket_name}'")
    except Exception as e:
        print(f"Error fetching objects in the bucket: {e} ")

list_objects_in_bucket("test12s45")

def download_file_from_s3(bucket_name, object_name, download_path):
    s3 = boto3.client('s3')

    try:
        s3.download_file(bucket_name, object_name, download_path)
        print(f"File '{object_name}' downloaded from bucket '{bucket_name}' to '{download_path}'.")
    except Exception as e:
        print(f"Error downloading file: {e} ")

download_file_from_s3("test12s45", "log.txt", "/Users/Tanmoy/Development/Python/log_downloaded.txt" )
