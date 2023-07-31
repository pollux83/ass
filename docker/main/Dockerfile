# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /main

# Copy the local requirements.txt into the container's working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container's working directory
COPY .. .

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# Run the Streamlit app when the container starts
CMD ["streamlit", "run", "main.py"]
