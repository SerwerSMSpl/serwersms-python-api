class Blacklist:

    def __init__(self, param):

        self.master = param

    '''
    * Add phone to the blacklist
    *
    * param string phone
    * return array
    *      option bool "success"
    *      option int "id"
    '''
    def add(self, phone):

        options = {
            'phone': phone
        }

        return self.master.call('blacklist/add', options)

    '''
    * List of blacklist phones
    *
    * param string phone
    * param array params
    *      option int "page" The number of the displayed page
    *      option int "limit" Limit items are displayed on the single page
    * return array
    *      option array "paging"
    *          option int "page" The number of current page
    *          option int "count" The number of all pages
    *      option array "items"
    *          option string "phone"
    *          option string "added" Date of adding phone
    '''
    def index(self, phone, params):

        default = {
            'phone': phone
        }

        options = params.copy()
        options.update(default)

        return self.master.call('blacklist/index', options)

    '''
    * Checking if phone is blacklisted
    *
    * param string phone
    * return array
    *      option bool "exists"
    '''
    def check(self, phone):

        options = {
            'phone': phone
        }

        return self.master.call('blacklist/check', options)

    '''
    * Deleting phone from the blacklist
    *
    * param string phone
    * return array
    *      option bool "success"
    '''
    def delete(self, phone):

        options = {
            'phone': phone
        }

        return self.master.call('blacklist/delete', options)