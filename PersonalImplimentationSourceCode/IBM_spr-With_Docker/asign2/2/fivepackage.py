#Package 1
from flask import Flask
#Package 2
import time
#Package 3
import random
#Package 4
import os
#Package 5
import socket as s

os.system("pwd")

h='localhost'

ri=random.randint(5,10)
app = Flask(__name__)

@app.route('/')
def hello():
    ht= s.gethostbyname(h)
    time.sleep(ri)
    return "Hello World!" + " ,IP : " + ht + ",Current Directory: " + '/'

if __name__ == "__main__":    
    app.run()

