## Define base image
FROM python:3.11

## Using bash 
SHELL ["/bin/bash", "-c"]

## Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

## Upgrade pip
RUN pip install --upgrade pip

## Install other libs


## Add user shex
#RUN useradd -rms /bin/bash shex && chmod 777 /opt /run

## Work directory
WORKDIR /swaphub
COPY . /swaphub/

## Create folders for static and media
#RUN mkdir /swaphub/static && mkdir /swaphub/media && chown -R shex:shex /swaphub && chmod 755 /swaphub

## Copy project files to image
#COPY --chown=shex:shex ../ .

RUN apt-get update \
    && apt-get install -y curl \
    && apt-get clean

## Install libs
RUN pip install -r requirements.txt

## Select user
#USER shex

## Define application-server (gunicorn)
# CMD ["gunicorn", "-b", "0.0.0.0:8001", "swaphub.config.wsgi:application"]
# CMD gunicorn swaphub.config.wsgi:application

# CMD python .\swaphub\manage.py runserver 0.0.0.0:8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" \
    && python manage.py collectstatic --no-input \
    #&& python manage.py runserver 0.0.0.0:8000
    && gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --log-level info
