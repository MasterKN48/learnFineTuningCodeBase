from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

port = os.getenv("WEBSITE_PORT") or 8001
# Mount the codebase directory at the root to serve all files (html, css, js)
# html=True allows serving index.html at the root path /
app.mount("/", StaticFiles(directory="codebase", html=True), name="static")

if __name__ == "__main__":
    import uvicorn

    # In a real environment, you'd run this via the command line
    # but providing it here for completeness or local testing.
    uvicorn.run(app, host="0.0.0.0", port=port)
