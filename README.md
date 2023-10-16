# partyProject
a simple story generator

## HOW TO RUN PROJECT
- `cd randomparty`
- build project `docker-compose up -d --build`
- create super user `docker exec -it party_app python3 manage.py createsuperuser`
- and app is available in http://0.0.0.0:8006/
  
- http://0.0.0.0:8006/api/newparty/ - new random party
- http://0.0.0.0:8006/api/login/ - user authorization
- http://0.0.0.0:8006/api/register/ - user registration
- http://0.0.0.0:8006/api/token/refresh/ - refresh token

