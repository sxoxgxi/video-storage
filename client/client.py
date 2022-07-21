import requests

res = requests.post('http://localhost:8000/api/post',
                    json={'video_size': 573956800, 'length': 378, 'video_type': 'mp4'})
print(res.json())
