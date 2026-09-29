import datetime

from fastapi import APIRouter, Form, Query

from config.autoload import Alert
from controllers.akmadnudin_ai import AiService
from typing import Annotated

router = APIRouter()
alert = Alert()
ai_service = AiService()

@router.get('/')
async def host():
    return "Hello World"
@router.post("/ai", summary="Ai Request")
async def ai_def(message: Annotated[str, Form()] = None):
    if not all([message]):
        return alert.Message({
            'message': "Please Add All Field",
            "status": False
        }, 404)
    return ai_service.Aigenerated(message)


@router.post("/cek-grammar", summary="Ai Request")
async def ai_grammary_def(message: Annotated[str, Form()] = None):
    if not all([message]):
        return alert.Message({
            'message': "Please Add All Field",
            "status": False
        }, 404)
    return ai_service.AiGrammary(message)


@router.post('/translate', summary="Translate data")
async def translates(language_from: Annotated[str, Form()] = None, language_target: Annotated[str, Form()] = None,
                     message: Annotated[str, Form()] = None):
    if not all([language_from, language_target, message]):
        return alert.Message({
            'message': "Please Add All Field",
            "status": False
        }, 404)
    return ai_service.translate(language_from, language_target, message)
