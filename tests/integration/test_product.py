"""
def test_start(config):
  response = requests.get(f'{config.base_url}/product', timeout=config.TIMEOUT)
  assert response.status_code == 200
  assert response.json() == [{"id":3,"name":"Screwdriver","price":79},{"id":2,"name":"Nail","price":99},{"id":1,"name":"Hammer","price":199}]
"""
