#include "Smartcube.h"

Smartcube::Smartcube(uint8_t CORNER_SWITCH_1_GPIO, uint8_t CORNER_SWITCH_2_GPIO, uint8_t CORNER_SWITCH_3_GPIO, long change_delay_ms)
{
    pinMode(CORNER_SWITCH_1_GPIO, INPUT_PULLUP);
    pinMode(CORNER_SWITCH_2_GPIO, INPUT_PULLUP);
    pinMode(CORNER_SWITCH_3_GPIO, INPUT_PULLUP);
    Smartcube::CORNER_SWITCH_1_GPIO = CORNER_SWITCH_1_GPIO;
    Smartcube::CORNER_SWITCH_2_GPIO = CORNER_SWITCH_2_GPIO;
    Smartcube::CORNER_SWITCH_3_GPIO = CORNER_SWITCH_3_GPIO;
    Smartcube::change_delay_ms = change_delay_ms;
    side_up = calc_side_up();
    side_up_temporary = side_up;
}

bool Smartcube::detectChange()
{
    uint8_t side_up_new = calc_side_up();

    if (side_up_new != side_up_temporary)
    {
        side_up_date_timestamp = millis();
        side_up_temporary = side_up_new;
        Serial.print("new side_up_temporary: ");
        Serial.println(side_up_temporary);
    }

    if (side_up_temporary != side_up && getSideUpTime() > change_delay_ms)
    {
        side_up = side_up_temporary;
        Serial.print("new side Up: ");
        Serial.println(side_up);
    }
}

uint8_t Smartcube::calc_side_up()
{
    return digitalRead(CORNER_SWITCH_1_GPIO) * 1 + digitalRead(CORNER_SWITCH_2_GPIO) * 2 + digitalRead(CORNER_SWITCH_3_GPIO) * 3;
}

uint8_t Smartcube::getSideUp()
{
    return side_up;
}

long Smartcube::getSideUpTime()
{
    return millis() - side_up_date_timestamp;
}