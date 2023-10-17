# Dockerfile

FROM python:3.10.0

WORKDIR /app 

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 4000

ENV HOST=0.0.0.0

# Run restAPI.py instead of app.py
CMD ["python", "restAPI.py"]