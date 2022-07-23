# Video Charging:

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

If request data is invalid: You will get the following error messages with status code 400.

```bash
 # Invalid post request
 {'size': ['This field is required.'], 'duration': ['This field is required.'], 'video_type': ['This field is required.']}

 # Invalid data for fields
 {'size': ['A valid integer is required.']}

 # Invalid video type
 {'video_type': ['This field must be mp4 or mkv.']}
```

# Uploading Videos

Endpoint: http://localhost:8000/api/create/

Send post request to endpoint with requets:

```python
 import requests

 data = {'title': 'Never gonna give you up!', 'description': 'Never gonna let you down',
         'video_file': 'file.mp4', 'thumbnail': 'thumbnail.jpg'}

 res = requests.post('http://localhost:8000/api/create/', json=data)
 print(res.json())
```


> Note: Don't miss the trailing slash in the endpoint.

Success response with status code 201:

```bash
 {'id': 61a1a375-2c6e-49c1-b1b1-gerr4, 'title': 'Never gonna give you up!', 'description': 'Never gonna let you down', 'video_file': 'media/file.mp4', 'thumbnail': 'media/thumbnails/thumbnail.jpg'}
```

If post request data dosen't match the parameters: You will get the following error message with status code 400.

```bash
 {'title': ['This field is required.'], 'video_file': ['No file was submitted.'], 'thumbnail': ['No file was submitted.']}
```

# Videos

For list view of all the videos endpoint is http://localhost:8000/api/videos/
Example:
![Alt text](https://i.ibb.co/pWMgTMM/listview.png "List View")

# Uploading videos

Endpoint: http://localhost:8000/api/create

### Validation Errors:

Video length is above the maximum allowed:
![Alt text](https://i.ibb.co/gZwyj22/uploadvalidation1.png "Length error")

Video Size is above the maximum allowed:
![Alt text](https://i.ibb.co/whKXMBZ/validation2.png "Size error")

>  Extension Allowed: mp4, mkv.
