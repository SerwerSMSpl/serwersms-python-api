import json
import requests
try:
    from urllib2 import Request, urlopen, URLError
    from urllib import urlencode
except ImportError:
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from urllib.error import URLError
from .message import Message
from .blacklist import Blacklist
from .group import Group
from .contact import Contact
from .phone import Phone
from .sender import Sender
from .template import Template
from .file import File
from .payment import Payment
from .subaccount import Subaccount
from .account import Account
from .stat import Stat
from .premium import Premium
from .error import Error


class SerwerSMS:

    def __init__(self, token=None):

        self.token = token

        self.api_url = 'https://api2.serwersms.pl/'

        self.format = 'json'

        self.client = 'client_python'

        self.test = ''

        self.message = Message(self)

        self.blacklist = Blacklist(self)

        self.group = Group(self)

        self.contact = Contact(self)

        self.phone = Phone(self)

        self.sender = Sender(self)

        self.template = Template(self)

        self.file = File(self)

        self.payment = Payment(self)

        self.subaccount = Subaccount(self)

        self.account = Account(self)

        self.stat = Stat(self)

        self.premium = Premium(self)

        self.error = Error(self)

    def call(self, action, params):

        url = self.api_url + action + "." + self.format

        tmp = {
            'system': self.client
        }

        params.update(tmp)

        headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }

        data = json.dumps(params)

        req = requests.post(url, data=data, headers=headers)

        if(action == 'payments/invoice'):
            return req.content
        else:
            return req.text
