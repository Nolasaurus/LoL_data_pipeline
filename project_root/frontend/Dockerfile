# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install necessary packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Install Python dependencies
COPY ./frontend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Copy the frontend and backend directories
COPY ./frontend /code/frontend
COPY ./backend /code/backend

# Set the working directory to /code/frontend where your app.py is located
WORKDIR /code/frontend

# Run the Flask application
CMD ["flask", "run"]
