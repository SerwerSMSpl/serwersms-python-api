class File:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Add new file
    *
    * param string type - mms|voice
    * param array params
    *      option string "url" URL address to file
    *      option resource "file" A file content (only for MMS)
    * return array
    *      option bool "success"
    *      option string "id"
    '''
    def add(self, type, params):

        default = {
            'type': type
        }

        options = params.copy()
        options.update(default)

        return self.master.call('files/add', options)

    '''
    * List of files
    *
    * param string type - mms|voice
    * return array
    *      option array "items"
    *          option string "id"
    *          option string "name"
    *          option int "size"
    *          option string "type" - mms|voice
    *          option string "date"
    '''
    def index(self, type):

        options = {
            'type': type
        }

        return self.master.call('files/index', options)

    '''
    * View file
    *
    * param string id
    * param string type - mms|voice
    * return array
    *      option string "id"
    *      option string "name"
    *      option int "size"
    *      option string "type" - mms|voice
    *      option string "date"
    '''
    def view(self, id, type):

        options = {
            'id': id,
            'type': type
        }

        return self.master.call('files/view', options)

    '''
    * Deleting a file
    *
    * param string id
    * param string type - mms|voice
    * return array
    *      option bool "success"
    '''
    def delete(self, id, type):

        options = {
            'id': id,
            'type': type
        }

        return self.master.call('files/delete', options)
