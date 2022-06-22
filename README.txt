# install server

## prerequisities
- install python
- install virtualenv

## run server
cd tourism
. bin/activate
export FLASK_APP=hello.py
flask run --host=192.168.111.14 --port=5000

## test server
cd tourism
. bin/activate
python3 client.py
