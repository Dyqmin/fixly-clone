# Fixly-clone

## Opis i cel projektu

### Cel
Projekt jest kopią serwisu fixly.pl. 
Umożliwia dodawanie zgłoszeń z listy usług przez użytkownika. 
Każdy kontraktor może zgłosić swoją osobę na wykonawcę danego zlecenia oraz czekać na 
decyzję właściciela zgłoszenia. Osoba tworząca zgłoszenie otrzymuje podgląd do listy
osób chętnych do realizacji zadania. Po znalezieniu odpowiedniej osoby, użytkownik może
zaakceptować czyjeś usługi, tym samym kończąc zgłoszenie. 

#### Przykładowa ścieżka działania aplikacji
1. Użytkownik wystawia zgłoszenie na pomalowanie mieszkania z podaniem metrażu
2. Wykonawca A odpowiada na realizację zadania za 200zł
2. Wykonawca B odpowiada na realizację zadania za 180zł
3. Użytkownik wybiera z listy zgłoszeń Wykonawcę B
4. Zgłoszenie zostaje zamknięte

### Opis techniczny
Backend aplikacji bazuje na frameworku **Flask** oraz podległych mu bibliotekach do 
łatwiejszego zarządzania kodem:
- flask-migrate - system migracji bazy danych
- flask-script - szybszy proces obsługi ustawień aplikacji, np. tworzenie migracji
- sqlalchemy-serializer - procesowanie zapytania z bazy danych do odpowiedzi w formie JSONa

Aplikacja uruchamiana jest w wirtualnym środowisku **pipenv**.
Do przechowywania danych użyliśmy bazy **PostgreSQL**. 
W celu szybkiego prototypowania modeli bazodanowych wybraliśmy ORM **SQLAlchemy**.
W procesie developmentu postanowiliśmy na kontyneryzowanie aplikacji z pomocą **Dockera** 
oraz funkcji ***docker-compose***. 


## Funkcjonalności

### Użytkownik
- Logowanie
- Rejestracja
- Tworzenie zgłoszeń na daną usługę
- Przegląd wykonawców
- Akceptowanie zgłoszeń

### Wykonawca
- Logowanie
- Rejestracja
- Ustawianie opisu usług
- Przegląd aktywnych zgłoszeń
- Oferowanie usług na otwarte zgłoszenia

## Proces developmentu na lokalnym środowisku

Przed pierwszym uruchomieniem aplikacji należy stworzyć folder w którym będą przechowywane dane Postgre:

```
$ mkdir -p postgre/dbdata
```

Plik ```.env``` zawiera domyślną konfigurację aplikacji do developmentu


### Uruchomienie

Aby uruchomić aplikację należy wywołać:
```
# docker-compose up
```
lub:
```
# docker-compose up -d
```
by uruchomić ją w tle i wyciszyć logowanie, po czym będzie ona dostępna pod adresem ```http://localhost:5000```

### Migracje

Utworzenie migracji:
```shell
$ pipenv run python src\manage.py db migrate -m "Create user model"
```

Wyrównanie migracji z bazą danych:
```
$ pipenv run python src\manage.py db upgrade
```