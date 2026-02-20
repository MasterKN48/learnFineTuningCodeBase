from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Mount the codebase directory at the root to serve all files (html, css, js)
# html=True allows serving index.html at the root path /
app.mount("/", StaticFiles(directory="codebase", html=True), name="static")

if __name__ == "__main__":
    import uvicorn

    # In a real environment, you'd run this via the command line
    # but providing it here for completeness or local testing.
    uvicorn.run(app, host="0.0.0.0", port=8001)
