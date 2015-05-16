# 'reminder' - a low-tech phone reminder application which has come about from the joining of 2 projects pitched at NHS Hackday London 2015.

Fiona Stacey, a Dental Hygienist from the North East, pitched an idea about reminding post-radiotherapy head and neck cancer patients to use mouthwash regularly.

## What is it?
Patients, carers or friends can enable a reminder to be set via a phone message advising the patient it is time to take their medication. Medication reminder applications are readily available for smartphones, however many patients, especially in vulnerable groups do not have or are unable to use a smartphone. They usually have a standard telephone though, so our application calls patients with a recorded reminder message.

##technology stack
* reminder is a Python/Django application with a lightweight HTML5 frontend
* the scheduler within the Django app makes calls to a thin wrapper around the Twilio API enabling the application to place a telephone call or send an SMS. The current 'proof-of-concept' is set to deliver one of two prerecorded audio files 

#TODO
* improve frontend to allow flexible configuration of reminder times (currently the options for reminder frequency are hard-coded in the UI to offer 1 times, 2 times, 3, times or 4 times per day which was sufficient for our NHSHD proof of concept)
* closing app feedback loop - the patient receiving the call should be able to press a key during the call to acknowledge the reminder and to indicate that they have taken the medication/used the mouthwash. This information should propagate back to the user interface, giving a real-time indication of the patient's use of medication. This would serve as an 'early warning' of poor comliance which might indicate increased confusion or patient intercurrent illness.

##Contributing
* find an issue you think you may be able to assist with
* fork the code and make your improvements
* submit a pull request

##Credits
* Fiona
* Helen @DeckOfPandas
* Ross Jones
* Sym 
* Jude Gibbons - UI/frontend
* Mike Thompson - UI/frontend
* Carrie Christensen - 
* David Szotten - Django/Python app
* Marcus Baw @marcus_baw
* 
