import requests


def test_request(image_path):
    url = 'http://127.0.0.1:5000/predict'
    files = {'image': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    return response


response = test_request('C:/Users/andre/Beitmodeldeection/Bananass-large.jpg')
print(response.headers)
