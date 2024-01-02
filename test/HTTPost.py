import requests

url = "http://127.0.0.1:8000/api/upload/"
data = {'stringa': 'La_tua_stringa_da_inviare'}
try:
    response = requests.post(url, data=data)

    print("Status Code:", response.status_code)
    print("Response Content:", response.text)
except Exception as E:
    print(E)
