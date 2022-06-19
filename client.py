#!/bin/python3
import requests

def main():
    """
    """
    response = requests.post("http://127.0.0.1:5000/rest/login", json={'username': 'test', 'password': 'password'})
    output = response.json()
    access_token = output['access_token']

    headers = {"Authorization": "Bearer {}".format(access_token)}
    response = requests.post("http://127.0.0.1:5000/rest/cities", json={}, headers=headers)
    print(response.text)

    headers = {"Authorization": "Bearer {}".format(access_token)}
    response = requests.post("http://127.0.0.1:5000/rest/places", json={"city": "ANK"}, headers=headers)
    print(response.text)

if __name__ == "__main__":
    main()
