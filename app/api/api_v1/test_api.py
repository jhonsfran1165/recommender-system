from fastapi.testclient import TestClient
from app.main import app
from app.api.api_v1.constants import CLUSTERS, COPIES, COPY, COPY_TITLE_65

client = TestClient(app)


def test_sessioninfo_no_login():
    response = client.get(
        "/sessioninfo"
    )

    data = response.json()
    assert response.status_code == 401
    assert data["message"] == "unauthorised"


def test_get_copy_no_login():
    response = client.get(
        "/api/v1/copies/copy?id=123232"
    )

    data = response.json()
    assert response.status_code == 401
    assert data["message"] == "unauthorised"


def test_get_copie_by_title_no_login():
    response = client.get(
        "/api/v1/copies/copies-by-title?id=58"
    )

    data = response.json()
    assert response.status_code == 401
    assert data["message"] == "unauthorised"


def test_get_rules_no_login():
    response = client.get(
        "/api/v1/rules/rules?id=422662&confidence=0.5&lift=1"
    )

    data = response.json()
    assert response.status_code == 401
    assert data["message"] == "unauthorised"


def test_get_kmeans_no_login():
    response = client.get(
        "/api/v1/rules/kmeans?prog=3743&jor=DIU&sede=0"
    )

    data = response.json()
    assert response.status_code == 401
    assert data["message"] == "unauthorised"


def test_email_no_valid_login():
    email = "jhonsfran"
    password = "jhoan"

    res = client.post('/api/v1/auth/signin', json={
        "formFields": [
            {
                "id": "email",
                "value": email
            },
            {
                "id": "password",
                "value": password
            }
        ]
    })

    data = res.json()

    assert data["formFields"][0]["error"] == "Email is not valid"
    assert data["status"] == "FIELD_ERROR"


def test_password_no_valid_login():
    email = "jhonsfran@gmail.com"
    password = "jhoan"

    res = client.post('/api/v1/auth/signin', json={
        "formFields": [
            {
                "id": "email",
                "value": email
            },
            {
                "id": "password",
                "value": password
            }
        ]
    })

    data = res.json()

    assert data["status"] == "WRONG_CREDENTIALS_ERROR"


def test_email_no_exist_login():
    email = "jhonsfran11@gmail.com"
    password = "jhoan"

    res = client.post('/api/v1/auth/signin', json={
        "formFields": [
            {
                "id": "email",
                "value": email
            },
            {
                "id": "password",
                "value": password
            }
        ]
    })

    data = res.json()

    assert data["status"] == "WRONG_CREDENTIALS_ERROR"


def test_login():
    email = "jhonsfran@gmail.com"
    password = "jhoan123"

    res = client.post('/api/v1/auth/signin', json={
        "formFields": [
            {
                "id": "email",
                "value": email
            },
            {
                "id": "password",
                "value": password
            }
        ]
    })

    data = res.json()

    assert data["user"]["email"] == email
    assert data["status"] == "OK"


def test_sessioninfo():
    response = client.get(
        "/sessioninfo"
    )

    data = response.json()

    assert data["userId"] == "1713f346-edee-4743-964d-5f78662e1e7c"
    assert response.status_code == 200


def test_get_copy_no_found():
    response = client.get(
        "/api/v1/copies/copy?id=123232"
    )

    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Copy not found"


def test_get_copy_found():
    response = client.get(
        "/api/v1/copies/copy?id=65"
    )

    copy = response.json()

    assert response.status_code == 200
    assert copy["copy_title"] == COPY_TITLE_65


def test_get_copy_by_titles_no_found():
    response = client.get(
        "/api/v1/copies/copies-by-title?id=31234234"
    )

    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Copies not found"


def test_get_copy_by_titles_found():
    response = client.get(
        "/api/v1/copies/copies-by-title?id=58"
    )

    copies = response.json()

    assert response.status_code == 200
    assert copies[0] == COPY


def test_get_rules_no_found():
    response = client.get(
        "/api/v1/rules/rules?id=2334123123&confidence=0.5&lift=1"
    )

    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Rules not found"


def test_get_rules_found():
    response = client.get(
        "/api/v1/rules/rules?id=422662&confidence=0.5&lift=1"
    )

    assert response.status_code == 200
    assert response.json() == COPIES


def test_get_kmeans_not_found():
    response = client.get(
        "/api/v1/rules/kmeans?prog=37443&jor=DIU&sede=0"
    )

    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Clusters not found"


def test_get_kmeans_found():
    response = client.get(
        "/api/v1/rules/kmeans?prog=3743&jor=DIU&sede=0"
    )

    assert response.status_code == 200
    assert response.json() == CLUSTERS
