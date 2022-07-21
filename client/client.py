import requests

res = requests.post('http://localhost:8000/api/post',
                    json={'size': 573956800, 'duration': 378, 'video_type': 'mp4'})

print(res.json())
print(res.status_code)
