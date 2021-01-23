# Base Image
FROM python:3.9.1

# Install dependencies
RUN apt-get update && apt-get install -y netcat


# Setting working directory
WORKDIR /app


# Dealing with requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# Coping project
COPY . /app


# Add entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# Running server
CMD ["/app/entrypoint.sh"]