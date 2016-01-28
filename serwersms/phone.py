class Phone:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Checking phone in to HLR
    *
    * param string phone
    * param string id Query ID returned if the processing takes longer than 60 seconds
    * return array
    *      option string "phone"
    *      option string "status"
    *      option int "imsi"
    *      option string "network"
    *      option bool "ported"
    *      option string "network_ported"
    '''
    def check(self, phone, id):

        options = {
            'phone': phone,
            'id': id
        }

        return self.master.call('phones/check', options)

    '''
    * Validating phone number
    *
    * param string phone
    * return array
    *      option bool "correct"
    '''
    def test(self, phone):

        options = {
            'phone': phone
        }

        return self.master.call('phones/test', options)