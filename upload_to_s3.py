import boto3
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load environment variables
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

def upload_to_s3():
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        file_name = "hello.txt"
        s3_key = "uploads/hello.txt"  # Destination path in S3

        s3_client.upload_file(file_name, BUCKET_NAME, s3_key)
        print(f"✅ File uploaded successfully to https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}")
    
    except Exception as e:
        print(f"❌ Failed to upload: {str(e)}")

if __name__ == "__main__":
    print(BUCKET_NAME)
    upload_to_s3()
