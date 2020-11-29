
# Smartcube
Smartcube aims to be the IOT Cube anyone can **a**fford, **b**uild and **c**onfigure.

Smartcube is a physical die, which houses electronics to detect when the die is tilted and which side is facing up. It then triggers events over the internet via its wifi connection.

At the moment smartcube can be configured to
- track the time you work on your projects (Toogl)
- trigger any generic webhooks

# User Guide
Please find the user guide [here](https://flokain.github.io/Smart-Cube/)

# Project Goals
The Smartcube Project started as an exercise and personal challenge to deliver a polished OpenSource IOT product for real world applications that can be used by anyone, not just tinkers.

To accomplish this vision I set the following goals:

| Goal                                    | Description                                                                                                                                                                                                                          |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Low cost                                | the costs for components and Material to build smartcube must be lower than 10€ in total on the regular market                                                                                                                       |
| power efficient                         | one battery charge for Smartcube lasts to detect 30 turns a day for 3 months (92 days).                                                                                                                                              |
| instructions for dummies                | At least one person has build this as his or her first IOT project. The Instructions to build and configure the smartcube are written with non technical users in mind to make sure anyone can build the Smartcube.                  |
| configuration for dummies               | At least one 50+yo nontechnical user has configured Smartcube by himself. a web interface guides through all configuuration steps                                                                                                    |
| 100% Automateable                       | Every configuration and every status can be configured via REST API.                                                                                                                                                                 |
| clean, extensible software architecture | At least one component was contributed by someone else. The architecture is simple and easy to understand. It encourages contributers to write and submit their own software components and find new applications for the Smartcube. |




# requirements

# Setup

# Testing
Smart Cube is tested in 2 ways.

# Unit Tests On Device
The python code depends on platform dependent libraries.
Because of this unittests must be executed on a device.
unittests a run on the device. connect via REPL
and execute
```
import unittest
unittest.main("unittests")
```
TODO: #10 seperate unittests that are device independent

# functional testing
Tests against the webAPI are ran against an operational device.
at the moment one has to change the host variable in tests/api_test.py
and then run from the project root dir TODO: #11 parse host as variable to tests 
```
pytest
```

# Rest API Reference
restapi is openapi conform:
https://app.swaggerhub.com/apis-docs/flokain/smartcube/v1
# Contribute

## Bug reports
## Feature requests

## Development
### Webhook interfaces
### Hardware Trigger
### core components


### pullrequest

# Support
# Development
project structure is created via [micropy-cli](https://github.com/BradenM/micropy-cli). 
Files from src are transfered to the microcontroller.