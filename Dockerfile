# Dockerfile

FROM python:3.10.0

WORKDIR /app 

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
COPY restAPI_cli.py /app/restAPI_cli.py

EXPOSE 4000
ENV HOST=0.0.0.0

# Run restAPI.py
CMD ["python", "restAPI.py"]

# Define CLI as entrypoint
ENTRYPOINT ["python", "/app/restAPI_cli.py"]