# install python on Mac

## steps

- install python3

本地已经有python2.7，但仍然可以直接装2.7，装完后执行 python3 即可。

- install pip

https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

- install postgre

first use dmg, but can't install requirements.txt. so use brew, because this https://stackoverflow.com/questions/11618898/pg-config-executable-not-found.

```
brew services restart postgresql
```

- install django

```
python3 -m pip install Django
```

- install redis 

https://gist.github.com/tomysmile/1b8a321e7c58499ef9f9441b2faa0aa8

- create user in django
$ python manage.py createsuperuser