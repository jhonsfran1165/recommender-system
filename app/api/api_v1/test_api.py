from fastapi.testclient import TestClient
from app.main import app
from app.api.api_v1.constants import CLUSTERS, COPIES, COPY, COPY_TITLE_65

client = TestClient(app)


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

    assert response.status_code == 200


def test_get_copy_no_found():
    response = client.get(
        "/api/v1/copies/copy?id=123232"
    )

    assert response.status_code == 200
    assert response.json() == None


def test_get_copy_found():
    response = client.get(
        "/api/v1/copies/copy?id=65"
    )

    copy = response.json()

    assert response.status_code == 200
    assert copy["copy_title"] == COPY_TITLE_65


def test_get_copy_by_titles_no_found():
    response = client.get(
        "/api/v1/copies/copies-by-title?id=34"
    )

    assert response.status_code == 200
    assert response.json() == []


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

    assert response.status_code == 200
    assert response.json() == []


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

    assert response.status_code == 200
    assert response.json() == []


def test_get_kmeans_found():
    response = client.get(
        "/api/v1/rules/kmeans?prog=3743&jor=DIU&sede=0"
    )

    assert response.status_code == 200
    assert response.json() == CLUSTERS
