class Stat:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Statistics an sending
    *
    * param array params
    *      option string "type" eco|full|voice|mms
    *      option string "begin" Start date
    *      option string "end" End date
    * return array
    *      option array "items"
    *          option int "id"
    *          option string "name"
    *          option int "delivered"
    *          option int "pending"
    *          option int "undelivered"
    *          option int "unsent"
    *          option string "begin"
    *          option string "end"
    *          option string "text"
    *          option string "type" eco|full|voice|mms
    '''
    def index(self, options):

        return self.master.call('stats/index', options)
