# SerwerSMS.pl Python Client API
Klient Python do komunikacji zdalnej z API v2 SerwerSMS.pl

Uwaga. Aktualna wersja działa w oparciu o token API. 

W celu autoryzacji za pośrednictwem Tokenu API, należy wygenerować go po stronie Panelu Klienta w menu Ustawienia interfejsów → HTTP API → Tokeny API. Format nagłówka autoryzacyjnego jest zgodny z formatem Bearer token.

#### Przykładowe wywołanie
```python
import sys
import json
import serwersms

api = serwersms.SerwerSMS('token')

try:

    params = {
        'test': 'true',
        'details': 'true'
    }

    response = api.message.send_sms('500600700', 'Test message', 'INFORMACJA', params)

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
api = serwersms.SerwerSMS('token')

try:

    params = {
        'details': 'true'
    }

    response = api.message.send_sms('500600700', 'Test message', 'INFORMACJA', params)
    
    print(response)
    
except Exception:

    print('ERROR: ', sys.exc_info()[1])
```

#### Wysyłka spersonalizowanych SMS
```python
api = serwersms.SerwerSMS('token')

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
api = serwersms.SerwerSMS('token')

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
api = serwersms.SerwerSMS('token')

try:

    params = {
        'phone': '500600700'
    }
    response = api.message.recived('ndi',params)
    
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

## Konsola API
http://apiconsole.serwersms.pl
