# SerwerSMS.pl Python Client API
Klient Python do komunikacji zdalnej z API v2 SerwerSMS.pl

Zalecane jest, aby komunikacja przez HTTPS API odbywała się z loginów utworzonych specjalnie do połączenia przez API. Konto użytkownika API można utworzyć w Panelu Klienta → Ustawienia interfejsów → HTTPS XML API → Użytkownicy.

#### Przykładowe wywołanie
```python
import sys
import json
import serwersms

api = serwersms.SerwerSMS('login', 'haslo')

try:

    params = {
        'test': 'true',
        'details': 'true'
    }

    response = api.message.send_sms('500600700', 'Test message', '', params)

    result = json.loads(response)

    if 'items' not in result:
        raise Exception('Empty items')

    for item in result['items']:
        print(item['id'] + ' - ' + item['phone'] + ' - ' + item['status'])
        
except Exception:

    print('ERROR: ', sys.exc_info()[1])
```

#### Wysyłka SMS
```python
api = serwersms.SerwerSMS('login', 'haslo')

try:

    params = {
        'details': 'true'
    }

    response = api.message.send_sms('500600700', 'Test message', '', params)
    
    print(response)
    
except Exception:

    print('ERROR: ', sys.exc_info()[1])
```

#### Wysyłka spersonalizowanych SMS
```python
api = serwersms.SerwerSMS('login', 'haslo')

try:

    messages = []

    message1 = {
        'phone': '500600700',
        'text': 'First message'
    }
    
    messages.append(message1)

    message2 = {
        'phone': '600700800',
        'text': 'Second  message'
    }
    
    messages.append(message2)

    params = {
        'details': 'true'
    }

    response = api.message.send_personalized(messages, 'INFORMACJA', params)
    
    print(response)
    
except Exception:

    print('ERROR: ', sys.exc_info()[1])
```

#### Pobieranie raportów doręczeń
```python
api = serwersms.SerwerSMS('login', 'haslo')

try:

    params = {
        'id': 'aca3944055'
    }
    
    response = api.message.reports(params)
    
    print(response)
    
except Exception:

    print('ERROR: ', sys.exc_info()[1])
```

#### Pobieranie wiadomości przychodzących
```python
api = serwersms.SerwerSMS('login', 'haslo')

try:

    params = {
        'phone': '500600700'
    }
    response = api.message.recived('eco',params)
    
    print(response)
    
except Exception:

    print('ERROR: ', sys.exc_info()[1])
```

## Instalacja

Po ściągnięciu paczki należy uruchomić procedurę instalacyjną
modułu poprzez komendę :

```
python setup.py install
```


## Wymagania
Python 3.4.*

## Dokumentacja
http://dev.serwersms.pl
