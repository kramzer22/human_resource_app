import os
import dotenv

dotenv.load_dotenv()

def get_access_token():
  return os.getenv('ACCESS_TOKEN')

def set_access_token(token) -> None:
  os.environ['ACCESS_TOKEN'] = token
  print(os.environ['ACCESS_TOKEN'])
  
def get_server_url():
  return os.getenv('SERVER_URL')