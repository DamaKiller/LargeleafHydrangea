```
import boto3
s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'mybucket',   #要复制的bucket名
    'Key': 'mykey'    #要复制的文件名 
 }
s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')   #otherbucket：目标bucket  otherkey：复制文件的名字
```
