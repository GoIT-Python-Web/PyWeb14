from fastapi import FastAPI

from app.api.router import router

from fastapi_sso.sso.google import GoogleSSO
from starlette.requests import Request




CLIENT_ID = "1013771678336-ruv0j3d6qhvj8gppapati22jq1mc1fjn.apps.googleusercontent.com"  # <-- paste your client id here
CLIENT_SECRET = "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" # <-- paste your client secret here

google_sso = GoogleSSO(CLIENT_ID, CLIENT_SECRET, "http://localhost:8000/google/callback")


app = FastAPI()
app.router.include_router(router)




@app.get("/google/login")
async def google_login():
    with google_sso:
        return await google_sso.get_login_redirect()

@app.get("/google/callback")
async def google_callback(request: Request):
    with google_sso:
        user = await google_sso.verify_and_process(request)
    return user

@app.get("/")
def read_root():
    return {"message": "REST APP v1.0"}
