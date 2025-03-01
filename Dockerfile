# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
