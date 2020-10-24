

import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException

def send_sms(username, password, to_numbers):
    # Configure HTTP basic authorization: BasicAuth
    configuration = clicksend_client.Configuration()
    configuration.username = username
    configuration.password = password

    # create an instance of the API class
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

    if not to_numbers:
        raise ValueError("No numbers have been supplied (to_numbers is empty)")

    # If you want to explictly set from, add the key _from to the message.
    sms_messages = []
    for to_number in to_numbers:
        sms_message = SmsMessage(source="sdk", # it was "php" before, what?
                                 body="Jos jedan korak prema slavi vjecnoj",
                                 to=to_number)
        sms_messages.append(sms_message)

    sms_messages = clicksend_client.SmsMessageCollection(messages=sms_messages)

    try:
        api_response = api_instance.sms_send_post(sms_messages)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
    return


if __name__ == "__main__":
    send_sms()
