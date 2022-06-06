import requests
import datetime as dt

time = dt.datetime.now()
today = time.strftime("%Y%m%d")

USERNAME = "aliuj"
TOKEN = "7rh4pi3bo35ynj"
GRAPH_ID = "julichka7249"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#responce = requests.post(url=pixela_endpoint, json=user_params)
#print(responce.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Min",
    "type": "int",
    "color": "ajisai",
    "timezone": "Europe/Istanbul"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

#responce = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(responce.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_data = {
    "date": today,
    "quantity": input("How many minutes did you learn coding today? ")
}

responce = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(responce.text)

#update_endpoint = f"{pixel_endpoint}/{today}"

#update_data = {"quantity": "210"}

#responce = requests.put(url=update_endpoint, json=update_data, headers=headers)
#print(responce.text)

#responce = requests.delete(url=update_endpoint, headers=headers)
#print(responce.text)