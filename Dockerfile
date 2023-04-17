FROM python:3.10-slim-buster

# Set work directory
WORKDIR /code

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]