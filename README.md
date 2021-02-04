
# Fixly-clone

## Start
Przed pierwszym uruchomieniem aplikacji należy stworzyć folder w którym będą przechowywane dane Postgre:

```
$ mkdir -p postgre/dbdata
```

Plik ```.env``` zawiera domyślną konfigurację aplikacji do developmentu


## Uruchomienie

Aby uruchomić aplikację należy wywołać:
```
# docker-compose up
```
lub:
```
# docker-compose up -d
```
by uruchomić ją w tle i wyciszyć logowanie, po czym będzie ona dostępna pod adresem ```http://localhost:5000```

## Migracje

Utworzenie migracji:
```shell
$ pipenv run python src\manage.py db migrate -m "Create user model"
```

Wyrównanie migracji z bazą danych:
```
$ pipenv run python src\manage.py db upgrade
```