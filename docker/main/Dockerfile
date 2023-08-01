# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /main

# Copy the local requirements.txt into the container's working directory
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

#RUN git clone https://github.com/streamlit/streamlit-example.git .

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container's working directory
COPY .. .

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app when the container starts
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
