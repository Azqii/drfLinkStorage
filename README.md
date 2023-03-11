# LinkStorage

LinkStorage is a simple DRF app that allows you to store your links with its descriptions

## Setup

1. Clone this repo to your desktop with `git clone https://github.com/Azqii/drfLinkStorage.git`
2. Configure **.env** file
3. Run `docker-compose up`

Site should be available on the **NGINX_PORT** (**.env**) port (default: 80)

## Technologies

- Python 3
- Django Rest Framework 3.14
- PostgreSQL
- Nginx + Gunicorn
- Celery + RabbitMQ

## Docs

Swagger-ui docs are available on **/api/schema/swagger-ui/** page