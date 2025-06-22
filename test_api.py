import requests

#Sample Test case 1
def test_dog_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        print ("Success")
    else:
        print ("Error")

#Get response URL
def test_get_user():
    headers = {
        "x-api-key": "reqres-free-v1",  # Replace with your actual key if needed
        "Content-Type": "application/json"
    }
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    assert response.status_code == 200
    assert response.json().get("data", {}).get("first_name") == "Janet"

#Post
def test_create_user():
    payload = {"name": "John", "job": "Engineer"}
    headers = {
        "x-api-key": "reqres-free-v1",
        "Content-Type": "application/json"
    }
    response = requests.post("https://reqres.in/api/users", json=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 201
    assert response.json().get("name") == "John"

#Put
def test_update_user():
    payload = {"name": "John", "job": "Manager"}
    headers = {
        "x-api-key": "reqres-free-v1",
        "Content-Type": "application/json"
    }
    response = requests.put("https://reqres.in/api/users/2", json=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200
    assert response.json()["job"] == "Manager"

#Delete
def test_delete_user():
    headers = {
        "x-api-key": "reqres-free-v1",
        "Content-Type": "application/json"
    }
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 204

#Edge case
def test_get_user_invalid_id():
    headers = {
        "x-api-key": "reqres-free-v1",
        "Content-Type": "application/json"
    }
    response = requests.get("https://reqres.in/api/users/9999", headers=headers)
    print("Status Code:", response.status_code)
    assert response.status_code == 404


#Error handling
def test_create_user_missing_fields():
    payload = {}  # Intentionally missing required fields
    headers = {
        "x-api-key": "reqres-free-v1",
        "Content-Type": "application/json"
    }
    response = requests.post("https://reqres.in/api/users", json=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    # Adjust based on expected behavior — mock APIs often return 201 anyway
    assert response.status_code not in [500], "Server error on invalid input"  # Depending on API behavior