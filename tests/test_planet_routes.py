def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "A vibrant blue and green planet, known for its diverse ecosystems and human inhabitants.",
        "galaxy":"Milky Way"
    }

def test_get_all_planets_returns_all_records(client, two_saved_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Earth",
        "description": "A vibrant blue and green planet, known for its diverse ecosystems and human inhabitants.",
        "galaxy":"Milky Way"
    },
    {
            "id" : 2,
            "name": "Mars",
            "description": "A cold, red planet with a thin atmosphere and known for its high mountains and deep valleys.",
            "galaxy": "Milky Way"
        }
    ]

def test_create_one_planet(client):
    #Act
    response = client.post("/planets", json={
    "name": "Jupiter",
    "description": "A massive gas giant with a prominent red spot and swirling clouds, the largest planet in the Solar System.",
    "galaxy": "Milky Way"
    })
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 201
    assert response_body == {
        "id" : 1,
        "name": "Jupiter",
        "description": "A massive gas giant with a prominent red spot and swirling clouds, the largest planet in the Solar System.",
        "galaxy": "Milky Way"
    }

def test_create_one_planet_with_existing_records(client, two_saved_planets):
    #Act
    response = client.post("/planets", json={
    "name": "Jupiter",
    "description": "A massive gas giant with a prominent red spot and swirling clouds, the largest planet in the Solar System.",
    "galaxy": "Milky Way"
    })
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 201
    assert response_body == {
        "id" : 3,
        "name": "Jupiter",
        "description": "A massive gas giant with a prominent red spot and swirling clouds, the largest planet in the Solar System.",
        "galaxy": "Milky Way"
    }

def test_delete_one_planet_with_two_saved_planets(client, two_saved_planets):
    response = client.delete("/planets/1")
    # count_response = client.get("/planets/count")
    # response_body = count_response.get_
    # print(response_body)
    

    assert response.status_code == 204
    # assert count_response == 1
