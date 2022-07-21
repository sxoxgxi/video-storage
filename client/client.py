import requests

res = requests.post('http://localhost:8000/api/charge',
                    json={'size': 400, 'duration': 378, 'video_type': 'mp4'})
# res = requests.post('http://localhost:8000/api/post',
#                     json={'hellow': 598})

print(res.json())
print(res.status_code)
