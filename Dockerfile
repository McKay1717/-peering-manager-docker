FROM python:3.8

####ENV####
ENV DJANGO_SUPERUSER_PASSWORD changeMe
ENV DJANGO_SUPERUSER_EMAIL root@localhost
ENV DJANGO_SUPERUSER_USERNAME root
ENV MY_ASN "DefaultString"
ENV ALLOWED_HOSTS "DefaultString"
ENV DATABASE_NAME ""DefaultString""
ENV DATABASE_USER ""DefaultString""
ENV DATABASE_PASSWORD "DefaultString"
ENV DATABASE_HOST ""DefaultString""
ENV DATABASE_PORT -1
ENV SECRET_KEY "DefaultString"
ENV BASE_PATH "DefaultString"
ENV DEBUG False
ENV CHANGELOG_RETENTION -1
ENV LOGIN_REQUIRED False
ENV EMAIL_SERVER "DefaultString"
ENV EMAIL_PORT -1
ENV EMAIL_USERNAME "DefaultString"
ENV EMAIL_PASSSWORD "DefaultString"
ENV EMAIL_TIMEOUT -1
ENV EMAIL_FROM_ADDRESS "DefaultString"
ENV EMAIL_SUBJECT_PREFIX "DefaultString"
ENV PEERINGDB_USERNAME "DefaultString"
ENV PEERINGDB_PASSWORD "DefaultString"
ENV NAPALM_USERNAME "DefaultString"
ENV NAPALM_PASSWORD "DefaultString"
ENV NAPALM_ARGS "DefaultString"
ENV NAPALM_TIMEOUT -1
ENV PAGINATE_COUNT -1
ENV TIME_ZONE "DefaultString"
ENV BGPQ3_HOST "DefaultString"
ENV BGPQ3_SOURCES "DefaultString"
ENV BGPQ3_ARGS "DefaultString"
ENV NETBOX_API "DefaultString"
ENV NETBOX_API_TOKEN "DefaultString"
ENV NETBOX_DEVICE_ROLES "DefaultString"
##########

###SETUP THE SYSTEM####
RUN apt update && apt install bgpq3 -y

### Get latest version  ####
RUN git clone https://github.com/respawner/peering-manager.git /peering-manager
WORKDIR /peering-manager/
VOLUME /peering-manager/
#Install requierement
RUN pip install --no-cache-dir -r requirements.txt

#Install config file based on ENV
COPY configuration.py /peering-manager/peering_manager/configuration.py
COPY entrypoint.sh /entrypoint.sh

#Prepare Cron
RUN apt-get --no-install-recommends install cron -y
ADD peering-manager.cron /peering-manager.cron
RUN /usr/bin/crontab /peering-manager.cron

#Prepare exec
RUN chmod 755 /entrypoint.sh

#Exec
ENTRYPOINT /entrypoint.sh

EXPOSE 8000/tcp
