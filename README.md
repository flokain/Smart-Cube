
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
TODO
Developing for a microcontroller can be quite a challenge. The intention of this section is to provide a development environment that is as quickly as possible to setup and convenient as can be, requiring little to non knowledge of the microptython firmware building process for contributing.
If you choose to use your own environment feel free to use parts from mine and share ideas for making it better in an issue.
### setup development environment
The development environment looks like this:
Using VsCode you have code completion for micropython and the used thirdparty libraries installed by micropython-cli
via the pymakr vscode extension

1. install vscode
2. clone repo with sumbodules

    ```bash
    git clone --recurse-submodules -j8 https://github.com/flokain/Smart-Cube
    ```

3. cd into the repository and run micropy. NOTE: this command results in an error. but it works until the point where the stubs for intellisense are installed. TODO: #15 fix json parse error when running micropy

    ```bash
    cd Smart-Cube
    micropy
    ```

4. start vscode in the repos root folder

    ```bash
    code .
    ```

5. [activate recommended vscode extensions](https://stackoverflow.com/questions/35929746/automatically-install-extensions-in-vs-code). TODO: #13 write how to activate all recommended extensions
6. check where at which path your device is mounted.`ls -la /dev/ttyUSB*` The default is /dev/ttyUSB0. If multiple are listed. try them out until one works ;)
   1. If your device is not connected at /dev/ttyUSB0 run the        following command and substitute /dev/ttyUSB0 with your device. *(you have to set the environment variable as it will be used in the buildscripts too.)* TODO: #14 automate this somehow

    ```bash
    export SMART_CUBE_PATH=/dev/ttyUSB0
    sed -i 's@"address": .*@"address": "'$SMART_CUBE_PATH'",@g' pymakr.conf
    ```

7. Prepare the build tool chain. From the project root run

   ```
   make -C misc/micropython/mpy-cross/
   ```

8. The environment is now setup for development.


### Webhook interfaces
### Hardware Trigger
### core components


### pullrequest

# Support
# Development
project structure is created via [micropy-cli](https://github.com/BradenM/micropy-cli). 
Files from src are transfered to the microcontroller.