class Contact:

    def __init__(self, param):

        self.master = param

    '''
    * Add new contact
    *
    * param string group_id
    * param string phone
    * param array params
    *      option string "email"
    *      option string "first_name"
    *      option string "last_name"
    *      option string "company"
    *      option string "tax_id"
    *      option string "address"
    *      option string "city"
    *      option string "description"
    * return array
    *      option bool "success"
    *      option int "id"
    '''
    def add(self, group_id, phone, params):

        default = {
            'group_id': group_id,
            'phone': phone
        }

        options = params.copy()
        options.update(default)

        return self.master.call('contacts/add', options)

    '''
    * List of contacts
    *
    * param int group_id
    * param string search
    * param array params
    *      option int "page" The number of the displayed page
    *      option int "limit" Limit items are displayed on the single page
    *      option string "sort" Values: first_name|last_name|phone|company|tax_id|email|address|city|description
    *      option string "order" Values: asc|desc
    * return array
    *      option array "paging"
    *          option int "page" The number of current page
    *          option int "count" The number of all pages
    *      options array "items"
    *          option int "id"
    *          option string "phone"
    *          option string "email"
    *          option string "company"
    *          option string "first_name"
    *          option string "last_name"
    *          option string "tax_id"
    *          option string "address"
    *          option string "city"
    *          option string "description"
    *          option bool "blacklist"
    *          option int "group_id"
    *          option string "group_name"
    '''
    def index(self, group_id, search, params):

        default = {
            'group_id': group_id,
            'search': search
        }

        options = params.copy()
        options.update(default)

        return self.master.call('contacts/index', options)

    '''
    * View single contact
    *
    * param int id
    * return array
    *      option integer "id"
    *      option string "phone"
    *      option string "email"
    *      option string "company"
    *      option string "first_name"
    *      option string "last_name"
    *      option string "tax_id"
    *      option string "address"
    *      option string "city"
    *      option string "description"
    *      option bool "blacklist"
    '''
    def view(self, id):

        options = {
            'id': id
        }

        return self.master.call('contacts/view', options)

    '''
    * Editing a contact
    *
    * param int id
    * param string group_id
    * param string phone
    * param array params
    *      option string "email"
    *      option string "first_name"
    *      option string "last_name"
    *      option string "company"
    *      option string "tax_id"
    *      option string "address"
    *      option string "city"
    *      option string "description"
    * return array
    *      option bool "success"
    *      option int "id"
    '''
    def edit(self, id, group_id, phone, params):

        default = {
            'id': id,
            'group_id': group_id,
            'phone': phone
        }

        options = params.copy()
        options.update(default)

        return self.master.call('contacts/edit', options)

    '''
    * Deleting a phone from contacts
    *
    * param int id
    * return array
    *      option bool "success"
    '''
    def delete(self, id):

        options = {
            'id': id
        }

        return self.master.call('contacts/delete', options)

    '''
    * Import contact list
    *
    * param string group_name
    * param array contact[]
    *      option string "phone"
    *      option string "email"
    *      option string "first_name"
    *      option string "last_name"
    *      option string "company"
    * return array
    *      option bool "success"
    *      option int "id"
    *      option int "correct" Number of contacts imported correctly
    *      option int "failed" Number of errors
    '''
    def imports(self, group_name, contacts):

        options = {
            'group_name': group_name,
            'contact': contacts
        }

        return self.master.call('contacts/import', options)