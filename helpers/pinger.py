import ping3
import time
import os
import dotenv

dotenv.load_dotenv()

class Pinger:
  _PING_URL = os.getenv('PING_URL')
  
  @staticmethod
  def test_server_response() -> bool:
    result = False
    
    time.sleep(0.5)
    for i in range(3):
      response_time = ping3.ping(Pinger._PING_URL)
      if response_time:
        print(f"Ping successful. Round-trip time: {response_time} seconds")
        result = True
        break
      else:
        print(f"Ping successful. Round-trip time: {response_time} seconds")
        time.sleep(2)
      
    return result