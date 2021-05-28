from flask import Flask
import logging
import sys
from dotenv import load_dotenv

load_dotenv()
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

flaskAppInstance = Flask(__name__)
if __name__ == '__main__':
    logging.debug("Starting Flask Server")
    from api import *
    #flaskAppInstance.run(port=8080)
    flaskAppInstance.run(host="0.0.0.0",port=8080,debug=True,use_reloader=True)
