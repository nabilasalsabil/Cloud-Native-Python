from app import app
import unittest

class FlaskappTests(unittest.TestCase):
  def setUp(self):
    # creates a test client
    self.app = app.test_client()
    # propagate the exceptions to the test client
    self.app.testing = True
  def test_users_status_code(self):
    # sends HTTP GET request to the application
    result = self.app.get('/api/v1/users')
    # assert the status code of the response
    self.assertEqual(result.status_code, 200)
  def test_tweets_status_code(self):
     # sends HTTP GET request to the application
     # on the specified path
     result = self.app.get('/api/v2/tweets')
     # assert the status code of the response
     self.assertEqual(result.status_code, 200)

  def test_addusers_status_code(self):
     # sends HTTP POST request to the application
     # on the specified path
     result = self.app.post('/api/v1/users', data='{ "username":"nabila", "email": "nabila@gmail.com", "password": "test123", "name":"Nabila Salsabil"}', content_type='application/json')
     print (result)
     # assert the status code of the response
     self.assertEquals(result.status_code, 201)

  def test_updusers_status_code(self):
     # sends HTTP PUT request to the application
     # on the specified path
     result = self.app.put('/api/v1/users/1', data='{"password": "salsa123"}', content_type='application/json')
     # assert the status code of the response
     self.assertEquals(result.status_code, 200)
  def test_addtweets_status_code(self):
     # sends HTTP GET request to the application
     # on the specified path
     result = self.app.post('/api/v2/tweets', data='{"username":"nabilasalsabil", "body": "Wow! Is it working#testing"}', content_type='application/json')

     # assert the status code of the response
     self.assertEqual(result.status_code, 201)

  def test_delusers_status_code(self):
     # sends HTTP Delete request to the application
     # on the specified path
     result = self.app.delete('/api/v1/users', data='{"username":"nabila"}', content_type='application/json')
     print (result)
     # assert the status code of the response
     self.assertEquals(result.status_code, 200)
