class Payment:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * List of payments
    *
    * return array
    *      option array "items"
    *          option int "id"
    *          option string "number"
    *          option string "state" paid|not_paid
    *          option float "paid"
    *          option float "total"
    *          option string "payment_to"
    *          option string "url"
    '''
    def index(self):

        return self.master.call('payments/index', {})

    '''
    * View single payment
    *
    * param int id
    * return array
    *      option int "id"
    *      option string "number"
    *      option string "state" paid|not_paid
    *      option float "paid"
    *      option float "total"
    *      option string "payment_to"
    *      option string "url"
    '''
    def view(self, id):

        options = {
            'id': id
        }

        return self.master.call('payments/view', options)


    '''
    * Download invoice as PDF
    *
    * param int id
    * return resource
    '''
    def invoice(self, id):

        options = {
            'id': id
        }

        return self.master.call('payments/invoice', options)