import os
import hmac
import hashlib
from dotenv import load_dotenv
from fastapi import Request, APIRouter, HTTPException
from starlette.responses import JSONResponse

load_dotenv()
routes = APIRouter()

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

valor_pix_maquina_1 = 0
valor_pix_maquina_2 = 0
ticket = 1

def converter_pix(valor_pix: int) -> str:
    if valor_pix >= ticket:
        creditos = valor_pix // ticket
        pulsos = creditos * ticket
        return f"{pulsos:04}"
    return "0000"

@routes.get("/consulta-Maquina01")
async def consulta_maquina_01():
    global valor_pix_maquina_1
    resposta = converter_pix(valor_pix_maquina_1)
    valor_pix_maquina_1 = 0
    return {"retorno": resposta}

@routes.get("/consulta-maquina-02")
async def consulta_maquina_02():
    global valor_pix_maquina_2
    resposta = converter_pix(valor_pix_maquina_2)
    valor_pix_maquina_2 = 0
    return {"retorno": resposta}

@routes.post("/rota-recebimento")
async def rota_recebimento(request: Request):
    global valor_pix_maquina_1
    try:
        ip = request.client.host
        if ip != "34.193.116.226" and ip != "127.0.0.1": #if ip != "34.193.116.226":
            raise HTTPException(status_code=401, detail="unauthorized")

        EXPECTED_HMAC = "391baafb5d672aafc6eaaa83db10874cdd3360e9819d1a67e335028701fe53ff"

        qy = request.query_params.get("hmac")
        if qy != EXPECTED_HMAC:
            raise HTTPException(status_code=401, detail="unauthorized")


        body = await request.json()

        if "pix" in body:
            print("valor do pix recebido:")
            print(body["pix"][0]["valor"])
            txid = body["pix"][0]["txid"]

            if txid == "V0CRTmog6XdUQtmhDFeoAAA":
                valor_pix_maquina_1 = body["pix"][0]["valor"]
                print("Creditando valor do pix na máquina 1")

            # Aqui daria pra tratar outras máquinas ou ações futuras

        return JSONResponse(content={"ok": "ok"}, status_code=200)
    except Exception as e:
        print("Erro:", e)
        return JSONResponse(content={"error": f"error: {str(e)}"}, status_code=402)