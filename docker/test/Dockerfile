# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /test

# Copy the local requirements.txt into the container's working directory
COPY requirements.txt .

#RUN apt-get update && apt-get install -y \
#    build-essential \
#    curl \
#    software-properties-common \
#    git \
#    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y
# Create and activate a virtual environment
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

#RUN git clone https://github.com/streamlit/streamlit-example.git .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Change the user to a non-root user
RUN useradd -m myuser
USER myuser

# Copy the rest of the application code into the container's working directory
COPY .. .

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app when the container starts
#ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
