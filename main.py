import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from config.routing import router
from config.autoload import Settings
from fastapi.middleware.cors import CORSMiddleware
settings = Settings()

load_dotenv()
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    author=settings.PROJECT_AUTHOR,
)
port = int(os.getenv("PORT", 8080))
host = os.getenv("HOST", "0.0.0.0")
debug = bool(os.getenv("DEBUG", False))
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)


if __name__ == "__main__":
        uvicorn.run(
        "main:app",  # Aplikasi yang akan dijalankan
        host=host,  # Mengizinkan akses dari jaringan luar
        port=port,  # Port yang ingin digunakan
        # ssl_keyfile="C:/xampp/htdocs/ssl/win-acme/file/nahmthaisukibbq.com-key.pem",  # Path ke keyfile SSL
        # ssl_certfile="C:/xampp/htdocs/ssl/win-acme/file/nahmthaisukibbq.com-crt.pem",  # Path ke sertifikat SSL
        log_level="debug"  # Tingkat log untuk debugging
    )

