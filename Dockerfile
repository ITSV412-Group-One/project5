# Use an official Python runtime as a parent image
FROM python:3.10.0

# Set the working directory inside the container
WORKDIR /app

# copy the current directory 
# COPY . /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install slack_sdk
RUN pip install -r requirements.txt
RUN pip install requests

# make port 4000 available 
EXPOSE 4000

# define environment variable
ENV NAME API 

# Copy all the local code into the container
# COPY restAPI.py .

# Define the command to run your application
CMD ["python", "restAPI.py"]
