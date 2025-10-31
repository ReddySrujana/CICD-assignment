from app import app


# ⬆one empty line here
# and another one here

def test_get_message():
    with app.test_client() as client:
        response = client.get('/api/message')
        assert response.status_code == 200
        assert response.json == {'message': 'Hello from Flask!'}
