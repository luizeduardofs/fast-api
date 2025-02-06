from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "user_name": "batatinha",
            "email": "user@example.com",
            "password": "string",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "user_name": "batatinha",
        "email": "user@example.com",
    }


def test_read_uses(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "user_name": "batatinha",
                "email": "user@example.com",
            }
        ]
    }


def test_get_user_by_id(client):
    response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"user_name": "batatinha", "email": "user@example.com", "id": 1}


def test_get_user_by_id_not_found(client):
    response = client.get("/users/999")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User Not Found"}


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "user_name": "Luiz Eduardo",
            "email": "luiz@gmail.com",
            "password": "string",
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"user_name": "Luiz Eduardo", "email": "luiz@gmail.com", "id": 1}


def test_update_user_not_found(client):
    response = client.put(
        "/users/999",
        json={
            "user_name": "Luiz Eduardo",
            "email": "luiz@gmail.com",
            "password": "string",
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User Not Found"}


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}


def test_delete_user_not_found(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User Not Found"}
