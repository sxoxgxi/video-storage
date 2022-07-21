# video storing and validation

## Video Charging:

Endpoint: http://localhost:8000/api/charge/

Send request to the endpoint with requests:

```python
 import requests

 res = requests.post('http://localhost:8000/api/charge/',
                    json={'size': 573, 'duration': 378, 'video_type': 'mp4'})

 print(res.json())
```

> Note: Don't miss the trailing slash in the endpoint.

Success response with status code 200:

```bash
 {'Video size': 573, 'Length': '0:06:18', 'Upload cost': '25$'}
```

If request data is invalid: You will get following error messages with status code 400.

```bash
 # Invalid post request
 {'size': ['This field is required.'], 'duration': ['This field is required.'], 'video_type': ['This field is required.']}

 # Invalid data for fields
 {'size': ['A valid integer is required.']}

 # Invalid video type
 {'video_type': ['This field must be mp4 or mkv.']}
```

# Creating Videos

Endpoint: http://localhost:8000/api/create/

Send post request to endpoint with requets:

```python
 import requests

 data = {'title': 'Never gonna give you up!', 'description': 'Never gonna let you down',
         'size': 30, 'duration': 230, 'video_type': 'mp4'}

 res = requests.post('http://localhost:8000/api/create/', json=data)
 print(res.json())
```

> Note: Don't miss the trailing slash in the endpoint.

Success response with status code 201:

```bash
 {'id': 6, 'title': 'Never gonna give you up!', 'description': 'Never gonna let you down', 'size': 30, 'duration': 230, 'video_type': 'mp4'}
```

If post request data dosen't match the parameters: You will get following error messages with status code 400.

```bash
 {'size': ['This field is required.'], 'duration': ['This field is required.'], 'video_type': ['This field is required.']}
```
