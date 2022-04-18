**从一个bucket移动文件到另一个bucket**
```
import boto3
s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'mybucket',   #要复制的bucket名
    'Key': 'mykey'    #要复制的文件名 
 }
s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')   #otherbucket：目标bucket  otherkey：复制文件的名字，前面可以接文件夹名
```

**在bucket下创建文件夹**
```
bucket = s3.Bucket('bucket_name')
k = bucket.new_key('abc/123/')      #文件夹名必须以/结尾
k.set_contents_from_string('')
```
**判断bucket是否存在某文件**
```
bucket_name = 'your_want_check_bucket'
KEY = 'file_name'
try:
    obj = s3.get_object(Bucket=bucket_name,Key=KEY)     #该语句会上bucket检查是否存在该文件，若不存在则会报错！
except Exception as e:
    print('fail')
```

**从S3下载文件到指定目录**
```
s3 = boto3.client('s3')
s3.download_file(bucket_name, KEY, FILE_PATH)   #bucket_name:想要下载文件所在的bucket KEY：想要下载的文件名 FILE_PATH：下载的目标地址，需要指定到文件名
```
