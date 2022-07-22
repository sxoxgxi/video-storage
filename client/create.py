import requests


data = {'uraa': 'Never gonna give you up!', 'descrion': 'Never gonna let you down',
        'size': 30, 'duration': 230, 'video_type': 'mp4'}

res = requests.post('http://localhost:8000/api/create/', json=data)
print(res.json())
print(res.status_code)
