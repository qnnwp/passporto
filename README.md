open-house
==========
almond:code cstimmel$ git clone git@github.com:uw-it-aca/passporto.git
almond:code cstimmel$ virtualenv --no-site-packages passporto
almond:code cstimmel$ cd passporto/
almond:passporto cstimmel$ source bin/activate
(passporto)almond:passporto cstimmel$ python bootstrap.py 
(passporto)almond:passporto cstimmel$ buildout

cp passporto/sample.local_settings.py passporto/local_settings.py
edit passporto/local_settings.py
passporto syncdb
passporto runserver
