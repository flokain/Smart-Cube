import utime as time
import logging
import machine

log = logging.getLogger(__name__)


class BallSwitchSensor:
    @property
    def side_up(self) -> int:
        """reads the value of the ball switches and calculates
        the up side of the cube. to save energie all pins are set
        tu pull up only for the time of evaluation.

        Returns:
            int: side id between 1-6
        """

        self.corner_1.init(machine.Pin.IN, machine.Pin.PULL_UP)
        self.corner_2.init(machine.Pin.IN, machine.Pin.PULL_UP)
        self.corner_3.init(machine.Pin.IN, machine.Pin.PULL_UP)

        side = (
            self.corner_1.value()
            + self.corner_2.value() * 2
            + self.corner_3.value() * 2
            + 1
        )

        self.corner_1.init(machine.Pin.OUT,0)
        self.corner_2.init(machine.Pin.OUT,0)
        self.corner_3.init(machine.Pin.OUT,0)

        return side

    @property
    def has_changed(self) -> bool:
        """returns true if sideUp has changed since the last time has_changed was called.

        Returns:
            bool: true if up side has change
        """
        last_change_ms = self._change_delay_ms
        side_up_new = self.side_up
        if self._temporary_side_up != side_up_new:
            self._temporary_side_up = self.side_up
            self._side_up_tick_ms = time.ticks_ms()
            log.debug("detecting new temporary side: {}".format(side_up_new))



        if (
            time.ticks_diff(time.ticks_ms(),self._side_up_tick_ms)
            > self._change_delay_ms and
            self._temporary_side_up != self._last_side_up
        ):
            log.debug(
                "temporary side {} is now accepted.".format(self._temporary_side_up)
            )
            self._last_side_up = self._temporary_side_up
            return True

        return False

    def __init__(
        self, corner_1_gpio=5, corner_2_gpio=4, corner_3_gpio=0, change_delay_ms=3000
    ):

        self.corner_1 = machine.Pin(corner_1_gpio, machine.Pin.OUT)
        self.corner_2 = machine.Pin(corner_2_gpio, machine.Pin.OUT)
        self.corner_3 = machine.Pin(corner_3_gpio, machine.Pin.OUT)
        self._temporary_side_up = self.side_up
        self._last_side_up = self._temporary_side_up
        self._side_up_tick_ms = time.ticks_ms()
        self._change_delay_ms = change_delay_ms
