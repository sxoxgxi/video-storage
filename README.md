# video storing and validation

## Video Charging:

Endpoint: http://localhost:8000/api/post

Send request to the endpoint with requests:

```python
 import requests

 res = requests.post('http://localhost:8000/api/post',
                    json={'size': 573, 'duration': 378, 'video_type': 'mp4'})

 print(res.json())


```

outputs:

```bash
 {'Video size': 573, 'Length': '0:06:18', 'Upload cost': '25$'}
```
