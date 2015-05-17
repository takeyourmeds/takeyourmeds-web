# 'reminder'
a low-tech phone reminder application which has come about from the joining of 2 projects pitched at NHS Hackday London 2015, at King's College Hospital.

Fiona Stacey, a Dental Hygienist from the North East, pitched an idea about using a low-tech means to remind post-radiotherapy head and neck cancer patients to use mouthwash regularly.

Helen Jackson (@DeckOfPandas) also pitched an idea about a simpler type of medication reminder using standard phone calls, for patients unable to use a smartphone.

The two teams quickly realised they were designing different facets of the same project and joined forces to work on a single application that would send a configurable audio message via phone call to a patient, reminding them to use the mouthwash, or take their medication.

## What is it?
Patients, carers or friends can enable a reminder to be set via a phone message advising the patient it is time to take their medication. Medication reminder applications are readily available for smartphones, however many patients, especially in vulnerable groups, do not own or are unable to use a smartphone. They usually have a standard telephone though, so our application calls patients with a recorded reminder message.

##Technology Stack
* reminder is a Python/Django application with a lightweight HTML5 frontend.
* the Celery/Redis-based scheduler within the Django app
* Calls are made to a thin wrapper around the Twilio API, enabling the application to place a telephone call or send an SMS. The current 'proof-of-concept' is set to deliver one of two prerecorded audio files.

#TODO
* improve frontend to allow flexible configuration of reminder times. (currently the options for reminder frequency are hard-coded in the UI to offer 1 times, 2 times, 3 times or 4 times per day which was sufficient for our NHSHD proof-of-concept)
* create multi-user interface with username/password login and persistence of settings.
* enable creation of a customised reminder message instead of the choice of 2 default messages in the proof-of-concept version.
* enable creation of multiple customised reminder messages depending on the time of the message, ie "Remember to take your morning medications Mum", "Remember to take your evening medications Mum", etc
* closing app feedback loop - the patient receiving the call should be able to press a key during the call to acknowledge the reminder and to indicate that they have taken the medication/used the mouthwash. This information should propagate back to the user interface, giving a real-time indication of the patient's use of medication. This would serve as an 'early warning' of poor comliance which might indicate increased confusion or patient intercurrent illness.
* Work out the telephony root url (using build_absolute_url) instead of configuring it.

##Contributing
* find an issue you think you may be able to assist with
* fork the code and make your improvements
* submit a pull request

##Credits
* Fiona
* Helen @DeckOfPandas
* Ross Jones @rossjones - Twilio wrapper
* Sym - Scheduler
* Jude Gibbons - UI/frontend
* Mike Thompson - UI/frontend
* Carrie Christensen - Twilio wrapper
* David Szotten - Django/Python app
* Marcus Baw @marcus_baw - Documentation
* 


## Configuration

### Telephony

To be able to make calls and send SMS you will need to sign up for an account at [Twilio](https://www.twilio.com). Once you have done this, you can visit the [Manage Numbers page](https://www.twilio.com/user/account/phone-numbers/incoming) to purchase a new number from which to make calls and send SMS.

If you visit your [Account Settings](https://www.twilio.com/user/account/settings) you will also be able to retrieve your *AccountSID* and *AuthToken* which you will need for the next steps.


   * Copy the file nhs_reminders/local_settings.py.sample to nhs_reminders/local_settings.py
   * Set the string value for ```TW_ACCOUNT_SID``` to the value from *AccountSID* above.
   * Set the string value for ```TW_AUTH_TOKEN``` to the value from *AuthToken* above.
   * Set the ```TW_FROM_NUMBER``` to the phone number that you purchased during Twilio setup.
   * Set the ```TW_ROOT_URL``` string value to the location of the /telephony/info url.
   