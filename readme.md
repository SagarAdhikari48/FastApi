## Steps - cd to the project directory and

# 1. python3 -m venv venv - This will install virtual environment

# 2. source venv/bin/activate  - THis will activate the virtual environment and in terminal (venv) appears

# 3. pip3 install fastapi uvicorn - this will install fast api and uvicorn -Uvicorn is a lightweight, high-performance ASGI (Asynchronous Server Gateway Interface) server for Python.Without Uvicorn, your FastAPI code is just Python code—it won't be accessible through a web browser or API client.When a request comes in:
# Uvicorn receives the request.
# Uvicorn passes it to FastAPI.
# FastAPI processes the request.
# Uvicorn sends the response back to the client.

#   python3 -c "import fastapi; print(fastapi.__version__)" -version check


# 4.uvicorn main:app --reload    -> This will start the server with main:app