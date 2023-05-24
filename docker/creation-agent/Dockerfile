# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

RUN /usr/local/bin/python -m pip install --upgrade pip
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download and install the Russian language model
RUN python -m spacy download ru_core_news_sm

# Copy the Python code to the container
COPY ./app.py .

# Expose the port on which the Flask application runs
EXPOSE 5000

# Set the command to run your Python script
CMD [ "python", "app.py" ]
