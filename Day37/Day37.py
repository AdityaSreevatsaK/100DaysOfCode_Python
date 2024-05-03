from datetime import datetime as dt

import requests

pixela_username = "ask"
pixela_user_token = "abcdabcdabcdabcd"
graph_id = "cycling"

pixela_post_pixel_endpoint = "https://pixe.la/v1/users/" + pixela_username + "/graphs/" + graph_id
current_date = dt.now().strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": pixela_user_token
}

post_pixel_configuration = {
    "date": current_date,
    "quantity": input("How many kilometres did you cycle today?\n")
}

while True:
    graph_creation_response = requests.post(url=pixela_post_pixel_endpoint, json=post_pixel_configuration,
                                            headers=headers)
    if graph_creation_response.json()["isSuccess"]:
        break

print("Successfully updated onto profile.")
