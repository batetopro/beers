import json


def test_login(users, beers, orders):
    resp = users.get('/api/users/exists', query_string={'username': 'testuser'})
    assert resp.status_code == 404

    # TODO: input validation of register

    data = {'username': 'testuser', 'mail': 'test@example.com', 'first_name': 'Test', 'last_name': 'User', 'password': '4csTJdx4'}
    resp = users.post('/api/users/register', data=data)
    print(resp.data)
    assert resp.status_code == 200
    
    resp = users.get('/api/users/exists', query_string={'username': 'testuser'})
    assert resp.status_code == 200
    
    resp = users.post('/api/users/login', data={'username': 'testuser', 'password': '4csTJdx4'})
    data = json.loads(resp.data)
    token = data['token']
    
    resp = users.post('/api/users/check_token', data={'token': token})
    assert resp.status_code == 200
    
    resp = users.post('/api/users/check_token', data={'token': token + '@@@'})
    assert resp.status_code == 404
    
    resp = users.post('/api/users/logout', data={'token': token})
    assert resp.status_code == 200
    
    resp = users.post('/api/users/logout', data={'token': token})
    assert resp.status_code == 404
    
    resp = users.post('/api/users/check_token', data={'token': token})
    assert resp.status_code == 404

