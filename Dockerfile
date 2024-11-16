# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory's contents to the container's /app directory
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir flask pandas scikit-learn xgboost

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]