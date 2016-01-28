class Subaccount:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Creating new subaccount
    *
    * param string subaccount_username
    * param string subaccount_password
    * param int subaccount_id Subaccount ID, which is template of powers
    * param array params
    *      option string "name"
    *      option string "phone"
    *      option string "email"
    * return type
    '''
    def add(self, subaccount_username, subaccount_password, subaccount_id, params):

        default = {
            'subaccount_username': subaccount_username,
            'subaccount_password': subaccount_password,
            'subaccount_id': subaccount_id,
        }

        options = params.copy()
        options.update(default)

        return self.master.call('subaccounts/add', options)

    '''
    * List of subaccounts
    *
    * return array
    *      option array "items"
    *          option int "id"
    *          option string "username"
    '''
    def index(self):

        return self.master.call('subaccounts/index', {})

    '''
    * View details of subaccount
    *
    * param int id
    * return array
    *      option int "id"
    *      option string "username"
    *      option string "name"
    *      option string "phone"
    *      option string "email"
    '''
    def view(self, id):

        options = {
            'id': id
        }

        return self.master.call('subaccounts/view', options)

    '''
    * Setting the limit on subaccount
    *
    * param int id
    * param string type Message type: eco|full|voice|mms|hlr
    * param int value
    * return array
    *      option bool "success"
    *      option int "id"
    '''
    def limit(self, id, type, value):

        options = {
            'id': id,
            'type': type,
            'value': value
        }

        return self.master.call('subaccounts/limit', options)

    '''
     * Deleting a subaccount
     *
     * param int id
     * return array
     *      option bool "success"
     '''
    def delete(self, id):

        options = {
            'id': id
        }

        return self.master.call('subaccounts/delete', options)