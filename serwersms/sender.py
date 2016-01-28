class Sender:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Creating new Sender name
    *
    * param string name
    * return array
    *      option bool "success"
    '''
    def add(self, name):

        options = {
            'name': name
        }

        return self.master.call('senders/add', options)

    '''
    * Senders list
    *
    * param array params
    *      option bool "predefined"
    *      option string "sort" Values: name
    *      option string "order" Values: asc|desc
    * return array
    *      option array "items"
    *          option string "name"
    *          option string "agreement" delivered|required|not_required
    *          option string "status" pending_authorization|authorized|rejected|deactivated
    '''
    def index(self, options):

        return self.master.call('senders/index', options)