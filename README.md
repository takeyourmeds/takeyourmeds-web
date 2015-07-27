# 'TakeYourMeds'

A low-tech phone reminder application which has come about from the joining of 2 projects pitched at NHS Hackday 10 in London 2015, at King's College London.

Fiona Stacey, a Dental Hygienist from the North East, pitched an idea about using a low-tech means to remind radiotherapy head and neck cancer patients to use mouthwash regularly.

Helen Jackson (@DeckOfPandas), a grad-entry medical student and programmer from London, also pitched an idea about a simple type of medication reminder using standard phone calls, for patients unable to use a smartphone.

The two teams quickly realised they were designing different facets of the same project and joined forces to work on a single application that would send a configurable audio message via phone call to a patient, reminding them to use the mouthwash, or take their medication.

## What is it?
Patients, carers or friends can enable a reminder to be sent via a phone message advising the patient it is time to take their medication. Medication reminder applications are readily available for smartphones; however many patients, especially in vulnerable groups, do not own or are unable to use a smartphone. These patients are also more likely to have complex medical needs and to be on more different medications. Our application calls patients on their landline with a recorded reminder message.

## Technology Stack
* Take Your Meds is a Python/Django application with a lightweight HTML5 frontend.
* It uses a Celery/Redis-based scheduler within the Django app
* Calls are made to a thin wrapper around the Twilio API, enabling the application to place a telephone call or send an SMS. The current 'proof-of-concept' is set to deliver one of two prerecorded audio files.

## Installation
See Wiki pages at https://github.com/takeyourmeds/takeyourmeds-web/wiki/Installation

# TODO
* improve frontend to allow flexible configuration of reminder times. (currently the options for reminder frequency are hard-coded in the UI to offer 1 times, 2 times, 3 times or 4 times per day which was sufficient for our NHSHD proof-of-concept)
* create multi-user interface with username/password login and persistence of settings.
* enable creation of a customised reminder message instead of the choice of 2 default messages in the proof-of-concept version.
* enable creation of multiple customised reminder messages depending on the time of the message, ie "Remember to take your morning medications Mum", "Remember to take your evening medications Mum", etc
* closing app feedback loop - the patient receiving the call should be able to press a key during the call to acknowledge the reminder and to indicate that they have taken the medication/used the mouthwash. This information should propagate back to the user interface, giving a real-time indication of the patient's use of medication. This would serve as an 'early warning' of poor compliance which might indicate increased confusion or patient intercurrent illness.
* Investigate whether it is possible to upgrade the call to a conference after some trigger, and call the reminder owner to invite them to the conference.
* Work out the telephony root url (using build_absolute_url) instead of configuring it.

## Contributing
* find an issue you think you may be able to assist with
* fork the code and make your improvements
* submit a pull request

## Credits
* Fiona Stacey [@fiona_stacey](http://twitter.com/fiona_stacey) (Dental Hygienist) - pitched Mouthwash reminder idea
* Helen [@DeckOfPandas](http://twitter.com/DeckOfPandas) (Med student & Dev) - pitched Medication reminder idea, copy writing
* Ross Jones [@rossjones](http://twitter.com/rossjones) - Twilio wrapper code
* Sym Roe [@symroe](http://twitter.com/symroe) - Scheduler code
* Jude Gibbons [@judegibbons](http://twitter.com/judegibbons) - UI/frontend
* Mike Thompson [@mikejthompson](http://twitter.com/mikejthompson) - UI/frontend
* Carrie Christensen [@c-christensen](http://twitter.com/c-christensen) - Twilio wrapper
* David Szotten [@szotten](http://twitter.com/szotten) - Django/Python app
* Marcus Baw [@marcus_baw](http://twitter.com/marcus_baw) - Documentation
