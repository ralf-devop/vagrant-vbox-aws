import boto3

s3 = boto3.resource('s3')

buckets = s3.buckets.all()
bucket_iter = iter(buckets)
bucket_list = list(bucket_iter)

if not bucket_list:
   print("No buckets found")
   quit()

first_bucket = bucket_list[0]
print("Pick first S3 bucket: " + first_bucket.name)

# Store test objects
with open('resources/images/test.jpg', 'rb') as data:
           s3.Bucket(first_bucket.name).put_object(Key='test.jpg', Body=data)
with open('resources/datasets/list_of_names.json', 'rb') as data:
           s3.Bucket(first_bucket.name).put_object(Key='list_of_names.json', Body=data)

# Print the contents of the bucket
for my_bucket_object in first_bucket.objects.all():
    print(my_bucket_object)
