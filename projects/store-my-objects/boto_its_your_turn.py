import boto3

TARGET_BUCKET_PREFIX = "aws-s3-example-bucket"

s3 = boto3.resource('s3')

buckets = s3.buckets.all()
bucket_iter = iter(buckets)
bucket_list = list(bucket_iter)

if not bucket_list:
   print("No buckets found")
   quit()

selected_bucket = None

for bucket in bucket_list:
   if(bucket.name.startswith(TARGET_BUCKET_PREFIX)):
      selected_bucket = bucket;
      break

if not selected_bucket:
   print(TARGET_BUCKET_PREFIX + " not found")
   quit()

print("Pick S3 bucket: " + selected_bucket.name)

# Store test objects
with open('resources/images/test.jpg', 'rb') as data:
           s3.Bucket(selected_bucket.name).put_object(Key='test.jpg', Body=data)
with open('resources/datasets/list_of_names.json', 'rb') as data:
           s3.Bucket(selected_bucket.name).put_object(Key='list_of_names.json', Body=data)

# Print the contents of the bucket
for my_bucket_object in selected_bucket.objects.all():
    print(my_bucket_object)
