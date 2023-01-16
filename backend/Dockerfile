FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/

# Allow installing dev dependencies to run tests
COPY ./app/requirements.txt /app/
# RUN bash -c "ls"
RUN bash -c "pip install -r ./requirements.txt"

COPY ./app /app
ENV PYTHONPATH=/app
