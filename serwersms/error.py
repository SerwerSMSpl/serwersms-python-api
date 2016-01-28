class Error:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Preview error
    *
    * param int code
    * return array
    *      option int "code"
    *      option string "type"
    *      option string "message"
    '''
    def view(self, code):

        return self.master.call('error/' + str(code), {})