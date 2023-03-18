import requests
r = requests.post('https://api.deepai.org/api/text-generator', data={
    'text': 'hello'
}, headers={
    'api-key': 'a7f95106-5d23-4950-841a-300e39221447'
})
print(r.text)