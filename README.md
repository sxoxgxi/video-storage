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

Outputs:

```bash
 {'Video size': 573, 'Length': '0:06:18', 'Upload cost': '25$'}
```

If request data is invalid, you will get following error messages with status code 400.

```bash
 # Invalid post request
 {'size': ['This field is required.'], 'duration': ['This field is required.'], 'video_type': ['This field is required.']}

 # Invalid data for fields
 {'size': ['A valid integer is required.']}

 # Invalid video type
 {'video_type': ['This field must be mp4 or mkv.']}
```
