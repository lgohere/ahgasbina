from ahgasbina.accounts.models import User
from ahgasbina.accounts.tests import fixtures
from ahgasbina.core.models import Chamada


def test_criar_chamada_sem_login(client):
    resp = client.post("/api/core/chamadas/add", {"new_chamada": "walk the dog"})
    assert resp.status_code == 401


def test_criar_chamada_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.post("/api/core/chamadas/add", {"new_chamada": "walk the dog"})
    assert resp.status_code == 200


def test_criar_chamada_com_login(client, db):
    fixtures.user_jon()
    Chamada.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/core/chamadas/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"chamadas": [{"description": "walk the dog", "done": False, "id": 1}]}
