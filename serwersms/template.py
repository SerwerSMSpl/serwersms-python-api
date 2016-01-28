class Template:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * List of templates
    * param array params
    *      option string "sort" Values: name
    *      option string "order" Values: asc|desc
    * return array
    *      option array "items"
    *          option int "id"
    *          option string "name"
    *          option string "text"
    '''
    def index(self, options):

        return self.master.call('templates/index', options)

    '''
    * Adding new template
    *
    * param string name
    * param string text
    * return array
    *      option array
    *          option bool "success"
    *          option int "id"
    '''
    def add(self, name, text):

        options = {
            'name': name,
            'text': text
        }

        return self.master.call('templates/add', options)

    '''
    * Editing a template
    *
    * param int id
    * param string name
    * param string text
    * return array
    *      option bool "success"
    *      option int "id"
    '''
    def edit(self, id, name, text):

        options = {
            'id': id,
            'name': name,
            'text': text
        }

        return self.master.call('templates/edit', options)


    '''
    * Deleting a template
    *
    * param int id
    * return array
    *      option bool "success"
    '''
    def delete(self, id):

        options = {
            'id': id
        }

        return self.master.call('templates/delete', options)