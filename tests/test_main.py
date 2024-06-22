from fastapi.testclient import TestClient
from fast.main import app
def test_root_path(): # passed test
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello":"world"}

def test_piaic_description(): # passed test
    client = TestClient(app=app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"organization":"piaic"}

def test_third_checck(): # failed test
    client = TestClient(app=app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"organization":"ABC"}
    
