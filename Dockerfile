# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY ./src /usr/src/app
COPY ./.env /usr/src/app/.env

# Poetry installation
RUN pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml poetry.lock* /usr/src/app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Expose the port the app runs on
EXPOSE 8501

# Healthcheck to verify the container is running correctly
HEALTHCHECK CMD curl --fail http://localhost:8501 || exit 1

# Command to run the app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
