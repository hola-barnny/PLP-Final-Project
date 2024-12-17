# Use the official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY backend/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code from the backend folder to /app
COPY backend /app

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=3500

# Expose the port Flask will run on
EXPOSE 3500

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=3500"]
