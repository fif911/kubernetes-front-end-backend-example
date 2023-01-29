FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app/

# Install dependencies
COPY ./app/requirements.txt /app/
# RUN bash -c "ls"
RUN bash -c "pip install -r ./requirements.txt"

EXPOSE 80

COPY ./app /app
ENV PYTHONPATH=/app
