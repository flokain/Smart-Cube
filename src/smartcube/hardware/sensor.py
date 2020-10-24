import utime as time


class BallSwitchSensor:
    @property
    def side_up() -> int:
        pass

    @property
    def has_changed() -> bool:
        """returns true if sideUp has changed since the last time has_changed was called.

        Returns:
            bool: true if up side has change
        """
        pass

    def __init__(
        self, corner_1_gpio=, 
        corner_2_gpio=, 
        corner_3_gpio=, 
        change_delay_ms=3000 ):

        self.corner_1_gpio = corner_1_gpio
        self.corner_2_gpio = corner_2_gpio
        self.corner_3_gpio = corner_3_gpio
        self._side_up = self.side_up()
        self._side_up_time = time.ticks_ms()
        self._change_delay_ms = change_delay_ms
