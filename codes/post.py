import requests

url = "http://127.0.0.1:5000/submit"

data = {
    "message": "Hello, Flask!"
}

response = requests.post(url, data=data)
print(response.text)