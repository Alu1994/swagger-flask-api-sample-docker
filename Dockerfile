# Use the official Python image from the Docker Hub
FROM python:3.13.0-alpine3.20

# Set the working directory in the container
WORKDIR /src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
