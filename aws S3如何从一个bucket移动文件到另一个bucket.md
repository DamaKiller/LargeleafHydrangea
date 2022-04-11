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
