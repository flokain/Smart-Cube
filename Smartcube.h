#ifndef SMARTCUBE_H_
#define SMARTCUBE_H_

#include "Arduino.h"
#include "EEPROM.h"
#include <time.h>

class Smartcube
{
private:
    uint8_t side_up;
    uint8_t side_up_temporary;
    long side_up_date_timestamp;
    long change_delay_ms; // time that needs to pass until a change of sides is detected.
    uint8_t calc_side_up();

public:
    Smartcube(uint8_t CORNER_SWITCH_1_GPIO, uint8_t CORNER_SWITCH_2_GPIO, uint8_t CORNER_SWITCH_3_GPIO, long change_delay_ms);
    Smartcube() : Smartcube(0, 4, 5, 2000){};
    uint8_t getSideUp();       // get the ID of the cube side that is up
    long getSideUpTimeStamp(); // get the time when side was flipped
    long getSideUpTime();      //convenience function returns duration since Timestamp
    bool detectChange();       //detect the current side up write save them
    uint8_t CORNER_SWITCH_1_GPIO;
    uint8_t CORNER_SWITCH_2_GPIO;
    uint8_t CORNER_SWITCH_3_GPIO;
};
#endif