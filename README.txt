# task
we want to show list of places that are worth to see in our country for tourists and need your help to develop a mobile app with Flutter.
the app will interact with the pre-developed small-sized (76 lines) backend server by REST API --the source code is available in hello.py and a reference client code is available in client.py

## expected application
the app should have 'login-page', 'cities-list-page', 'city-places-list-page' and 'place-details-page' which we describe below.

1) login-page: app should have a login page. user inputs (username and password) should be passed to backend by calling "http://URL/rest/login"". upon unsuccessful login response, user should be notified. upon successful response, user should be routed to 'cities-list-page'
2) cities-list-page: app should fetch list of cities that have places worth to see by calling  "http://URL/rest/cities". upon getting response, user should see the list of cities, and have ability to tap one of them to route 'city-places-list-page'
3) city-places-list-page: app should fetch list of places by calling "http://URL/rest/places" with city code as data. upon getting response, user should see the list of places (only 'landing' image and 'intro' text). user should have ability to tap one of them to route 'place-details-page'. user should also have ability to return 'cities-list-page'
4) place-details-page: app should show 'landing' image and 'alternative' images if any (preferably as sliding images, as in Instagram) with 'full' text. user should have ability to route back to 'city-places-list' page.

## remarks 
- successful login response will contain json-web-token. this should be used for all further API calls for authentication.
- I don't recommend, but you're free to modify pre-developed backend code. the single restriction is, all API calls (except /rest/login) have to use json-web-tokens.

## bonus points
1) handle disconnection: if the mobile device does not have an internet connection at login, or lost it after the login phase, just notify her as in today's modern mobile applications.
2) develop auto-login and log-out: once user enters correct credentials, just auto-login her on her second application launching. besides, develop log-out option, in which if user log-outs, route her to login page on her second application running  --as in most modern applications we've been using such as Instagram, Twitter, Gmail etc.
hint: https://pub.dev/packages/shared_preferences
3) show distance: get user's longitude and latitude informatin, then show calculate her distance to show far she is to the place in 'place-details-page'.
hint: https://pub.dev/packages/geolocator

# install server

## prerequisities
- install python
- install virtualenv

## run server
cd tourism
. bin/activate
export FLASK_APP=hello.py
flask run --host=127.0.0.1 --port=5000

## test server
cd tourism
. bin/activate
python3 client.py
