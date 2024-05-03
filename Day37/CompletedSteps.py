from datetime import datetime as dt

import requests

pixela_username = "ask"
pixela_user_token = "abcdabcdabcdabcd"
graphs = "/graphs/"

# Pixela user creation.
pixela_create_user_endpoint = "https://pixe.la/v1/users/"
pixela_create_user_parameters = {
    "token": pixela_user_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

user_creation_response = requests.post(url=pixela_create_user_endpoint, json=pixela_create_user_parameters)
print(user_creation_response.text)

# Pixela graph creation.
pixela_create_graph_endpoint = pixela_create_user_endpoint + "/" + pixela_username + "/graphs"
graph_id = "cycling"
graph_configuration = {
    "id": graph_id,
    "name": "Cycling",
    "unit": "kilometre",
    "type": "int",
    "color": "momiji",  # Colour for red.
    "timezone": "UTC"
}

headers = {
    "X-USER-TOKEN": pixela_user_token
}

graph_creation_response = requests.post(url=pixela_create_graph_endpoint, json=graph_configuration, headers=headers)
print(graph_creation_response.text)

# Pixela Graph updation.
pixela_update_graph_endpoint = pixela_create_user_endpoint + pixela_username + graphs + graph_id
update_graph_configuration = {
    "name": "Cycling",
    "unit": "kilometre",
    "type": "int",
    "color": "sora",  # Colour for blue.
    "timezone": "UTC"
}

graph_creation_response = requests.put(url=pixela_update_graph_endpoint, json=update_graph_configuration,
                                       headers=headers)
print(graph_creation_response.text)

# Post a pixel
pixela_post_pixel_endpoint = pixela_create_user_endpoint + pixela_username + graphs + graph_id
current_date = dt.now().strftime("%Y%m%d")
post_pixel_configuration = {
    "date": current_date,
    "quantity": "5"
}

graph_creation_response = requests.post(url=pixela_post_pixel_endpoint, json=post_pixel_configuration, headers=headers)
print(graph_creation_response.text)

# Update a pixel.
pixela_update_pixel_endpoint = pixela_create_user_endpoint + pixela_username + graphs + graph_id + "/" + current_date
update_pixel_configuration = {
    "quantity": "10"
}

graph_creation_response = requests.put(url=pixela_update_pixel_endpoint, json=update_pixel_configuration,
                                       headers=headers)
print(graph_creation_response.text)

# Delete a pixel.
pixela_delete_pixel_endpoint = pixela_create_user_endpoint + pixela_username + graphs + graph_id + "/" + current_date

graph_creation_response = requests.delete(url=pixela_delete_pixel_endpoint, headers=headers)
print(graph_creation_response.text)
