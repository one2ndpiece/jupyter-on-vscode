# Use the official Python image as the base image
FROM python:3.11.4-slim-bullseye

# Set the working directory
WORKDIR /usr/src/app

# Install Poetry using pip
RUN pip install poetry

# Disable the creation of virtual environments by Poetry
RUN poetry config virtualenvs.create false

# # Copy the project files into the container
# COPY pyproject.toml poetry.lock ./

# # Install the project dependencies
# RUN poetry install --no-dev

# Keep the container running
CMD ["tail", "-f", "/dev/null"]