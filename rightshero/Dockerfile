# Use the latest Python image
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    gcc libc-dev libffi-dev openssl-dev bash git \
    libtool m4 g++ autoconf automake build-base postgresql-dev

# Upgrade pip and install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy Poetry dependency files first to leverage Docker caching
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the full project
COPY . .

# Expose the application port
EXPOSE 8000

# Default command only starts the server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
