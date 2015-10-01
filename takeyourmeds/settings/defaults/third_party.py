TWILIO_CONFIG = {
    #"test": {
    #    # You can retrieve these settings from
    #    # https://www.twilio.com/user/account/developer-tools/test-credentials
    #    "ACCOUNT_SID": "",
    #    "AUTH_TOKEN": "",
    #    "FROM_NUMBER": "+15005550006",
    #    "ROOT_URL": "http://127.0.0.1:8000/telephony/info"
    #},
    "ACCOUNT_SID": "XXX", # Your Twilio account SID
    "AUTH_TOKEN": "XXX",  # Your twilio account SID
    "FROM_NUMBER": "0000",  # Your twilio SMS-enabled phone number
    # The root URL from where the Twilio service can pick
    # up the TwilML because Ross is too lazy to work out the
    # server name dynamically.
    "ROOT_URL": "http://takeyourmeds.fixme/telephony/info",
}
