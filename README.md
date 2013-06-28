passporto
=========

$ git clone git@github.com:uw-it-aca/passporto.git

$ virtualenv --no-site-packages passporto
$ cd passporto/
$ source bin/activate

(passporto)$ python bootstrap.py 
(passporto)$ buildout

(passporto)$ cp passporto/sample.local_settings.py passporto/local_settings.py

edit passporto/local_settings.py

(passporto)$ passporto syncdb
(passporto)$ passporto runserver
