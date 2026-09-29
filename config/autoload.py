import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
import socket

load_dotenv()

def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # Menghubungkan ke alamat luar untuk menentukan IP lokal
            s.connect(('10.254.254.254', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()
        return ip


class Settings:
    PROJECT_NAME = os.getenv('PROJECT_NAME')
    PROJECT_VERSION = os.getenv('PROJECT_VERSION')
    PROJECT_DESCRIPTION = os.getenv('PROJECT_DESCRIPTION')
    PROJECT_AUTHOR = os.getenv('PROJECT_AUTHOR')
    TRANSLATE = os.getenv('API_Translate')
    API_GRAMMAR = os.getenv('API_GRAMMAR')


class Alert:
    def Message(self, data, code=200):
        return JSONResponse(content=data, status_code=code)
