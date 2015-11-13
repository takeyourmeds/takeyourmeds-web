# 'TakeYourMeds'

[![Build Status](https://api.travis-ci.org/takeyourmeds/takeyourmeds-web.svg?branch=master)](https://travis-ci.org/takeyourmeds/takeyourmeds-web)

A low-tech phone reminder application which has come about from the joining of 2 projects pitched at NHS Hackday 10 in 2015 at King's College London

Fiona Stacey, a Dental Hygienist from the North East, pitched an idea about using a low-tech means to remind radiotherapy head and neck cancer patients to use mouthwash regularly.

Helen Jackson (@DeckOfPandas), a grad-entry medical student and programmer from London, also pitched an idea about a simple type of medication reminder using standard phone calls, for patients unable to use a smartphone.

The two teams quickly realised they were designing different facets of the same project and joined forces to work on a single application that would send a configurable audio message via phone call to a patient, reminding them to use the mouthwash, or take their medication.

## What is it?
Patients, carers or friends can set up a reminder advising the patient it is time to take their medication. TYM can call any UK phone or mobile number, or can send a text message.

## Why do we need TYM?
Medication reminder applications are readily available for smartphones; however many patients, especially in vulnerable groups, do not own or are unable to use a smartphone. These patients are also more likely to have complex medical needs and to be on more different medications. Our application calls patients on their landline with a recorded reminder message (or can send a text message if preferred).

## Technology Stack
* Take Your Meds is a Python/Django application with a lightweight HTML5 frontend.
* It uses a Celery/Redis-based scheduler within the Django app
* Calls are made to a thin wrapper around the Twilio API, enabling the application to place a telephone call or send an SMS. The current 'proof-of-concept' is set to deliver one of two prerecorded audio files.

## Installation
See Wiki pages at https://github.com/open-health-hub/reminder/wiki/Installation

# TODO
See Git Hub issues for a fuoll and up-to0date list
* IN PROGRESS: enable creation of a customised reminder message instead of the choice of 2 default messages in the proof-of-concept version.
* IN PROGRESS: closing app feedback loop - the patient receiving the call should be able to press a key during the call to acknowledge the reminder and to indicate that they have taken the medication/used the mouthwash. This information should propagate back to the user interface, giving a real-time indication of the patient's use of medication. This would serve as an 'early warning' of poor compliance which might indicate increased confusion or patient intercurrent illness.
* improve frontend to allow flexible configuration of reminder times. (currently the options for reminder frequency are hard-coded in the UI to offer 1 times, 2 times, 3 times or 4 times per day which was sufficient for our NHSHD proof-of-concept)
* * Offer an option for the message receiver to contact the person who set up the reminder
* ??? Work out the telephony root url (using build_absolute_url) instead of configuring it.

## Contributing
* Find an issue you think you may be able to assist with
* Email hello@takeyourmeds.co.uk to say hello anda let us know what you want to do
* Fork the code and make your improvements
* Submit a pull request
* Admire :)

## Credits
* Fiona Stacey [@fiona_stacey](http://twitter.com/fiona_stacey) (Dental Hygienist) - pitched Mouthwash reminder idea
* Helen [@DeckOfPandas](http://twitter.com/DeckOfPandas) (Med student & Dev) - pitched Medication reminder idea, copy writing
* Marcus Baw [@marcus_baw](http://twitter.com/marcus_baw) - Documentation
* Ross Jones [@rossjones](http://twitter.com/rossjones) - Twilio wrapper code
* Sym Roe [@symroe](http://twitter.com/symroe) - Scheduler code
* Jude Gibbons [@judegibbons](http://twitter.com/judegibbons) - UI/frontend
* Mike Thompson [@mikejthompson](http://twitter.com/mikejthompson) - UI/frontend
* Carrie Christensen [@c-christensen](http://twitter.com/c-christensen) - Twilio wrapper
* David Szotten [@szotten](http://twitter.com/szotten) - Django/Python app
