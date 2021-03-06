class Account:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Register new account
    *
    * param array params
    *      option string "phone"
    *      option string "email"
    *      option string "first_name"
    *      option string "last_name"
    *      option string "company"
    * return array
    *      option bool "success"
    '''
    def add(self, options):

        return self.master.call('account/add', options)

    '''
    * Return limits SMS
    * param array params
    *      option bool "show_type"
    * return array
    *      option array "items"
    *          option string "type" Type of message
    *          option string "chars_limit" The maximum length of message
    *          option string "value" Limit messages
    *
    '''
    def limits(self, options):

        return self.master.call('account/limits', options)

    '''
    * Return contact details
    *
    * return array
    *      option string "telephone"
    *      option string "email"
    *      option string "form"
    *      option string "faq"
    *      option array "account_maintainer"
    *          option string "name"
    *          option string "email"
    *          option string "telephone"
    *          option string "photo"
    '''
    def help(self):

        return self.master.call('account/help', {})

    '''
    * Return messages from the administrator
    *
    * return array
    *      option bool "new" Marking unread message
    *      option string "message"
    '''
    def messages(self):

        return self.master.call('account/messages', {})