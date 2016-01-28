class Premium:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
     * List of received SMS Premium
     *
     * return array
     *      option array "items"
     *          option int "id"
     *          option string "to_number" Premium number
     *          option string "from_number" Sender phone number
     *          option string "date"
     *          option int "limit" Limitation the number of responses
     *          option string "text" Message
    '''
    def index(self):

        return self.master.call('premium/index', {})

    '''
    * Sending replies for received SMS Premium
    *
    * param string phone
    * param string text Message
    * param string gate Premium number
    * param int id ID received SMS Premium
    * return array
    *      option bool "success"
    '''
    def send(self, phone, text, gate, id):

        options = {
            'phone': phone,
            'text': text,
            'gate': gate,
            'id': id
        }

        return self.master.call('premium/send', options)

    '''
    * View quiz results
    *
    * param int id
    * return array
    *      option int "id"
    *      option string "name"
    *      option array "items"
    *          option int "id"
    *          option int "count" Number of response
    '''
    def quiz(self, id):

        options = {
            'id': id
        }

        return self.master.call('quiz/view', options)