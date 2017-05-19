class Message:
    
    def __init__(self, param):
        
        self.master = param
    
    '''
    * Sending messages
    *
    * param string phone
    * param string text Message
    * param string sender Sender name only for FULL SMS
    * param array params
    *      option bool "details" Show details of messages
    *      option bool "utf" Change encoding to UTF-8 (Only for FULL SMS)
    *      option bool "flash"
    *      option bool "speed" Priority canal only for FULL SMS
    *      option bool "test" Test mode
    *      option bool "vcard" vCard message
    *      option string "wap_push" WAP Push URL address
    *      option string "date" Set the date of sending
    *      option string "group_id" Sending to the group instead of a phone number
    *      option string "contact_id" Sending to phone from contacts
    *      option string "unique_id" Own identifiers of messages
    * return array
    *      option bool "success"
    *      option int "queued" Number of queued messages
    *      option int "unsent" Number of unsent messages
    *      option array "items"
    *          option string "id"
    *          option string "phone"
    *          option string "status" - queued|unsent
    *          option string "queued" Date of enqueued
    *          option int "parts" Number of parts a message
    *          option int "error_code"
    *          option string "error_message"
    *          option string "text"
    '''
    def send_sms(self, phone, text, sender, params):

        default = {
            'phone': phone,
            'text': text,
            'sender': sender
        }

        options = params.copy()
        options.update(default)

        return self.master.call('messages/send_sms', options)

    '''
    * Sending personalized messages
    *
    * param array messages
    *      option string "phone"
    *      option string "text"
    * param string sender Sender name only for FULL SMS
    * param array params
    *      option bool "details" Show details of messages
    *      option bool "utf" Change encoding to UTF-8 (only for FULL SMS)
    *      option bool "flash"
    *      option bool "speed" Priority canal only for FULL SMS
    *      option bool "test" Test mode
    *      option string "date" Set the date of sending
    *      option string "group_id" Sending to the group instead of a phone number
    *      option string "text" Message if is set group_id
    *      option string "uniqe_id" Own identifiers of messages
    *      option bool "voice" Send VMS
    * return array
    *      option bool "success"
    *      option int "queued" Number of queued messages
    *      option int "unsent" Number of unsent messages
    *      option array "items"
    *          option string "id"
    *          option string "phone"
    *          option string "status" - queued|unsent
    *          option string "queued" Date of enqueued
    *          option int "parts" Number of parts a message
    *          option int "error_code"
    *          option string "error_message"
    *          option string "text"
    '''
    def send_personalized(self, messages, sender, params):

        param = ''
        for message in messages:
            param += message['phone']
            param += ':'
            param += message['text']
            param += ']|["'
			
        if len(param) > 3:
            param = param[:-4]

        default = {
            'sender': sender,
            'messages': param
        }

        options = params.copy()
        options.update(default)

        return self.master.call('messages/send_personalized', options)

    '''
    * Sending Voice message
    *
    * param string phone
    * param array params
    *      option string "text" If send of text to voice
    *      option string "file_id" ID from wav files
    *      option string "date" Set the date of sending
    *      option bool "test" Test mode
    *      option string "group_id" Sending to the group instead of a phone number
    *      option string "contact_id" Sending to phone from contacts
    * return array
    *      option bool "success"
    *      option int "queued" Number of queued messages
    *      option int "unsent" Number of unsent messages
    *      option array "items"
    *          option string "id"
    *          option string "phone"
    *          option string "status" - queued|unsent
    *          option string "queued" Date of enqueued
    *          option int "parts" Number of parts a message
    *          option int "error_code"
    *          option string "error_message"
    *          option string "text"
    '''
    def send_voice(self, phone, params):

        default = {
            'phone': phone
        }

        options = params.copy()
        options.update(default)

        return self.master.call('messages/send_voice', options)

    '''
    * Sending MMS
    *
    * param string phone
    * param string title Title of message (max 40 chars)
    * param array params
    *      option string "file_id"
    *      option string "file" File in base64 encoding
    *      option string "date" Set the date of sending
    *      option bool "test" Test mode
    *      option string "group_id" Sending to the group instead of a phone number
    * return array
    *      option bool "success"
    *      option int "queued" Number of queued messages
    *      option int "unsent" Number of unsent messages
    *      option array "items"
    *          option string "id"
    *          option string "phone"
    *          option string "status" - queued|unsent
    *          option string "queued" Date of enqueued
    *          option int "parts" Number of parts a message
    *          option int "error_code"
    *          option string "error_message"
    *          option string "text"
    '''
    def send_mms(self, phone, title, params):

        default = {
            'phone': phone,
            'title': title
        }

        options = params.copy()
        options.update(default)

        return self.master.call('messages/send_mms', options)

    '''
    * View single message
    *
    * param string id
    * param array params
    *      option string "unique_id"
    *      option bool "show_contact" Show details of the recipient from the contacts
    * return array
    *      option string "id"
    *      option string "phone"
    *      option string "status"
    *          - delivered: The message is sent and delivered
    *          - undelivered: The message is sent but not delivered
    *          - sent: The message is sent and waiting for report
    *          - unsent: The message wasn't sent
    *          - in_progress: The message is queued for sending
    *          - saved: The message was saved in schedule
    *      option string "queued" Date of enqueued
    *      option string "sent" Date of sending
    *      option string "delivered" Date of deliver
    *      option string "sender"
    *      option string "type" - eco|full|mms|voice
    *      option string "text"
    *      option string "reason"
    *          - message_expired
    *          - unsupported_number
    *          - message_rejected
    *          - missed_call
    *          - wrong_number
    *          - limit_exhausted
    *          - lock_send
    *          - wrong_message
    *          - operator_error
    *          - wrong_sender_name
    *          - number_is_blacklisted
    *          - sending_to_foreign_networks_is_locked
    *          - no_permission_to_send_messages
    *          - other_error
    *      option array "contact"
    *          option string "first_name"
    *          option string "last_name"
    *          option string "company"
    *          option string "phone"
    *          option string "email"
    *          option string "tax_id"
    *          option string "city"
    *          option string "address"
    *          option string "description"
    '''
    def view(self, id, params):

        default = {
            'id': id
        }

        options = params.copy()
        options.update(default)

        return self.master.call('messages/view', options)

    '''
    * Checking messages reports
    *
    * param array params
    *      option string "id" ID message
    *      option string "unique_id" ID message
    *      option string "phone"
    *      option string "date_from" The scope of the initial
    *      option string "date_to" The scope of the final
    *      option string "status" delivered|undelivered|pending|sent|unsent
    *      option string "type" eco|full|mms|voice
    *      option int "stat_id" Id package messages
    *      option bool "show_contact" Show details of the recipient from the contacts
    *      option int "page" The number of the displayed page
    *      option int "limit" Limit items are displayed on the single page
    *      option string "order" asc|desc
    * return array
    *      option array "paging"
    *          option int "page" The number of current page
    *          option int "count" The number of all pages
    *      option array items
    *          option string "id"
    *          option string "phone"
    *          option string "status"
    *              - delivered: The message is sent and delivered
    *              - undelivered: The message is sent but not delivered
    *              - sent: The message is sent and waiting for report
    *              - unsent: The message wasn't sent
    *              - in_progress: The message is queued for sending
    *              - saved: The message was saved in the scheduler
    *          option string "queued" Date of enqueued
    *          option string "sent" Date of sending
    *          option string "delivered" Date of deliver
    *          option string "sender"
    *          option string "type" - eco|full|mms|voice
    *          option string "text"
    *          option bool "flash"
    *          option bool "utf"
    *          option int "parts"
    *          option float "cost"
    *          option string "method"
    *          option int "mnc"
    *          option string "country"
    *          option string "network"
    *          option array "attachments"
    *              option int "id"
    *          option string "reason"
    *              - message_expired
    *              - unsupported_number
    *              - message_rejected
    *              - missed_call
    *              - wrong_number
    *              - limit_exhausted
    *              - lock_send
    *              - wrong_message
    *              - operator_error
    *              - wrong_sender_name
    *              - number_is_blacklisted
    *              - sending_to_foreign_networks_is_locked
    *              - no_permission_to_send_messages
    *              - other_error
    *          option array "contact"
    *              option int "id"
    *              option string "first_name"
    *              option string "last_name"
    *              option string "company"
    *              option string "phone"
    *              option string "email"
    *              option string "tax_id"
    *              option string "city"
    *              option string "address"
    *              option string "description"
    '''
    def reports(self, params):

        return self.master.call('messages/reports', params)

    '''
    * Deleting message from the scheduler
    *
    * param string id
    * param string unique_id
    * return array
    *      option bool "success"
    '''
    def delete(self, id, unique_id):

        options = {
            'id': id,
            'unique_id': unique_id
        }

        return self.master.call('messages/delete', options)

    '''
    * List of received messages
    *
    * param string type
    *      - eco SMS ECO replies
    *      - nd Incoming messages to ND number
    *      - ndi Incoming messages to ND number
    *      - mms Incoming MMS
    * param array params
    *      option string "ndi" Filtering by NDI
    *      option string "phone" Filtering by phone
    *      option string "date_from" The scope of the initial
    *      option string "date_to" The scope of the final
    *      option bool "read" Mark as read
    *      option int "page" The number of the displayed page
    *      option int "limit" Limit items are displayed on the single page
    *      option string "order" asc|desc
    * return array
    *      option array "paging"
    *          option int "page" The number of current page
    *          option int "count" The number of all pages
    *      option array "items"
    *          option int "id"
    *          option string "type" eco|nd|ndi|mms
    *          option string "phone"
    *          option string "recived" Date of received message
    *          option string "message_id" ID of outgoing message (only for ECO SMS)
    *          option bool "blacklist" Is the phone is blacklisted?
    *          option string "text" Message
    *          option string "to_number" Number of the recipient (for MMS)
    *          option string "title" Title of message (for MMS)
    *          option array "attachments" (for MMS)
    *              option int "id"
    *              option string "name"
    *              option string "content_type"
    *              option string "data" File
    *          option array "contact"
    *              option string "first_name"
    *              option string "last_name"
    *              option string "company"
    *              option string "phone"
    *              option string "email"
    *              option string "tax_id"
    *              option string "city"
    *              option string "address"
    *              option string "description"
    '''
    def recived(self, type, params):

        default = {
            'type': type
        }

        options = params.copy()
        options.update(default)

        return self.master.call('messages/recived', options)

    '''
    * Sending a message to an ND/SC
    *
    * param string phone Sender phone number
    * param string text Message
    * return array
    *      option bool "success"
    '''
    def send_nd(self, phone, text):

        options = {
            'phone': phone,
            'text': text
        }

        return self.master.call('messages/send_nd', options)

    '''
    * Sending a message to an NDI/SCI
    *
    * param string phone Sender phone number
    * param string text Message
    * param string ndi_number Recipient phone number
    * return array
    *      option bool "success"
    '''
    def send_ndi(self, phone, text, ndi_number):

        options = {
            'phone': phone,
            'text': text,
            'ndi_number': ndi_number
        }

        return self.master.call('messages/send_ndi', options)