from app import app
import unittest

class FlaskappTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tests_users_status_code(self):
        result = self.app.get('/api/v1/users')
        self.assertEqual(result.status_code, 200)

    def test_tweets_status_code(self):
        result = self.app.get('/api/v2/tweets')
        self.assertEqual(result.status_code, 200)
    
    def test_addusers_status_code(self):
        result = self.app.post('/api/v1/users', data='{ "username":"Ovestint", "email": "ronaldrvera@jourrapide.com", "password": "juzahpei6e", "name":"Ronald R. Vera"}', content_type='application/json')
        print(result)
        self.assertEquals(result.status_code, 201)

    def test_updusers_status_code(self):
        result = self.app.put('/api/v1/users/16', data='{"username":"CindyB", "password": "Dallaire123"}', content_type='application/json')
        self.assertEquals(result.status_code, 200)

    def test_addtweets_status_code(self):
       result = self.app.post('/api/v2/tweets', data='{"username":"CindyB", "body": "It Works!#Awesome"}', content_type='application/json')
       self.assertEqual(result.status_code, 201)

    def test_delusers_status_code(self):
        result = self.app.delete('/api/v1/users', data='{"username":"Ovestint"}', content_type='application/json')
        print(result)
        self.assertEquals(result.status_code, 200)