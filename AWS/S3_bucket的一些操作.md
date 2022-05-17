**从一个bucket移动文件到另一个bucket**
```
import boto3
s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'mybucket',   #要复制的bucket名
    'Key': 'mykey'    #要复制的文件名 
 }
s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')   #otherbucket：目标bucket  otherkey：复制文件的名字，前面可以接文件夹名
s3.Object(bucket_name, KEY).delete()    #可以把原bucket下的文件删掉来实现文件移动的目的
```

**在bucket下创建文件夹**
```
s3 = boto3.client('s3')
s3.put_object(Bucket='mybucket', Key='mykey')   #mybucket:想要创建文件夹的bucket名   Key：创建的文件夹名，必须要以'/'结尾，例如：ABC/
```

**判断bucket是否存在某文件**
```
bucket_name = 'your_want_check_bucket'
KEY = 'file_name'
try:
    obj = s3.get_object(Bucket=bucket_name,Key=KEY)     #该语句会上bucket检查是否存在该文件，若不存在则会报错！ 该key不要用/开头，例abc/123。
except Exception as e:
    print('fail')
```

**从S3下载文件到指定目录**
```
s3 = boto3.client('s3')
s3.download_file(bucket_name, KEY, FILE_PATH)   #bucket_name:想要下载文件所在的bucket KEY：想要下载的文件名 FILE_PATH：下载的目标地址，需要指定到文件名
```

**上传文件到s3指定目录**
```
s3 = boto3.client('s3')
s3_client.upload_file(Filename = file_path, Bucket=bucket, Key = (dir_path + file) )
#file_path:本地文件的地址  bucket：想要上传到的bucket名    Key：为上传到s3的地址，为bucket后的地址，例：abc/ABC,ABC为上传到s3上后想要的文件名。
```
