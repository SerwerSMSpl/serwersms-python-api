class Group:

    def __init__(self, param):

        self.master = param

    '''
    * Add new group
    *
    * param string name
    * return array
    *      option bool "success"
    *      option int "id"
    '''
    def add(self, name):

        options = {
            'name': name
        }

        return self.master.call('groups/add', options)

    '''
    * List of group
    *
    * param string search Group name
    * param array params
    *      option int "page" The number of the displayed page
    *      option int "limit" Limit items are displayed on the single page
    *      option string "sort" Values: name
    *      option string "order" Values: asc|desc
    * return array
    *      option array "paging"
    *          option int "page" The number of current page
    *          option int "count" The number of all pages
    *      option array "items"
    *          option int "id"
    *          option string "name"
    *          option int "count" Number of contacts in the group
    */
    '''
    def index(self, search, params):

        default = {
            'search': search
        }

        options = params.copy()
        options.update(default)

        return self.master.call('groups/index', options)

    '''
    * View single group
    *
    * param int id
    * return array
    *      option int "id"
    *      option string "name"
    *      option int "count" Number of contacts in the group
    '''
    def view(self, id):

        options = {
            'id': id
        }

        return self.master.call('groups/view', options)

    '''
    * Editing a group
    *
    * param int id
    * param string name
    * return array
    *      option bool "success"
    *      option int "id"
    '''
    def edit(self, id, name):

        options = {
            'id': id,
            'name': name
        }

        return self.master.call('groups/edit', options)

    '''
    * Deleting a group
    *
    * param int id
    * return array
    *      option bool "success"
    '''
    def delete(self, id):

        options = {
            'id': id
        }

        return self.master.call('groups/delete', options)

    '''
    * Viewing a groups containing phone
    *
    * param string phone
    * return array
    *      option int "id"
    *      option int "group_id"
    *      option string "group_name"
    '''
    def check(self, phone):

        options = {
            'phone': phone
        }

        return self.master.call('groups/check', options)