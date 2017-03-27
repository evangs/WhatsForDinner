# WhatsForDinner
A webapp to help decide where to eat for dinner.

## How to Run
- Install Docker(https://www.docker.com/get-docker)
- Clone project
- Create secrets.env file in WhatsForDinner/wfd/ with the following keys. Get a google api key here (https://developers.google.com/maps/documentation/geocoding/get-api-key). Environment when set to PROD will set DEBUG to False in the django settings file, otherwise DEBUG will be True.
```
GOOGLE_API_KEY=
ENVIRONMENT=
```
- docker build -t wfd .
- docker run -it --rm -p 80:80 --env-file secrets.env --name wfdapp wfd
