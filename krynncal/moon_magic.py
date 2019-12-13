from decimal import Decimal
from math import sin, cos, pi
from krynncal.krynndatetime import (
    date as kdate, timedelta as ktimedelta, datetime as kdatetime)


INITIAL_DATE = kdate(351, 9, 13)
NIGHT_OF_THE_EYE = kdatetime(351, 10, 15, 0, 0, 0)

HIGH = "high sanction"
WAXING = "waxing"
WANING = "waning"
LOW = "low sanction"
OTHER = None
PHASES = (HIGH, WAXING, WANING, LOW, OTHER)


def hyphen_range(s):
    """ yield each integer from a complex range string like "1-9,12, 15-20,23"

    >>> list(hyphen_range('1-9,12, 15-20,23'))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19, 20, 23]

    >>> list(hyphen_range('1-9,12, 15-20,2-3-4'))
    Traceback (most recent call last):
        ...
    ValueError: format error in 2-3-4
    """
    for x in s.split(','):
        elem = x.split('-')
        if len(elem) == 1:  # a number
            yield int(elem[0])
        elif len(elem) == 2:  # a range inclusive
            start, end = map(int, elem)
            for i in range(start, end + 1):
                yield i
        else:  # more than one hyphen
            raise ValueError('format error in %s' % x)


def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]


class Moon(object):

    def __init__(self, name, pd):
        super(Moon, self).__init__()
        self.name = name
        self.period = Decimal(str(pd))

    @property
    def period_sec(self):
        return self.period * Decimal('86400')

    def influence(self, date):
        daydiff = Decimal(str((date - NIGHT_OF_THE_EYE).total_seconds()))
        circular_period = Decimal(str(2 * pi))
        # Get the potency of the moon's modifier
        modifier = Decimal(str(cos(
            circular_period * (daydiff / self.period_sec)))) * Decimal('1.33')
        # Get the derivitave of the potency function as the waxing/waning state
        state = Decimal(str(sin(
            circular_period * (daydiff / self.period_sec)))) * Decimal('-1')
        if modifier > Decimal('1'):
            # Moon in High Sanction regardless of wax/wane state
            modifier = Decimal('1')
            phase = HIGH
        elif modifier < Decimal('-1'):
            # Moon in Low Sanction regardless of wax/wane state
            modifier = Decimal('-1')
            phase = LOW
        elif state < Decimal('0'):
            # Sign of derivitive of potency function is decreasing, so waning
            phase = WANING
        else:
            # Only one possible "phase" left...  waxing
            phase = WAXING
        return modifier, phase

    def astrolabe(self, date):
        spacer = ""
        modifier, phase = self.influence(date)
        displayed_modifier = Decimal("{:.1f}".format(modifier))
        if phase in (HIGH, LOW):
            spacer = "in "
            trailer = ""
        else:
            if displayed_modifier < 0:
                spacer = "a "
                trailer = " crescent"
            elif displayed_modifier == 0:
                spacer = "a "
                trailer = " half moon"
            else:
                trailer = " gibbous"
        return (
            "{} is {}{}{} ({:.1f})").format(
                self.name, spacer, phase, trailer, modifier)


class Moonless(object):
    name = "moonless"

    def influence(self, *args, **kwargs):
        return Decimal('0'), OTHER


SOLINARI = Moon('Solinari', 36)
LUNITARI = Moon('Lunitari', 28)
NUITARI = Moon('Nuitari', 8)
MOONS = (SOLINARI, LUNITARI, NUITARI)


class Order(object):

    def __init__(self, name, moon):
        super(Order, self).__init__()
        self.name = name
        if isinstance(moon, Moon):
            self.moon = moon
        elif isinstance(moon, int):
            self.moon = MOONS[moon]
        else:
            self.moon = Moonless()


WHITE = Order('White Robes', SOLINARI)
RED = Order('Red Robes', LUNITARI)
BLACK = Order('Black Robes', NUITARI)
ORDERS = (WHITE, RED, BLACK)


class SolarSystem(object):

    def __init__(self, right_now=NIGHT_OF_THE_EYE):
        if not isinstance(right_now, (kdate, kdatetime)):
            if isinstance(right_now, (tuple, list)):
                right_now = kdatetime(*right_now)
            else:
                right_now = kdatetime(right_now)
        self.right_now = right_now

    @property
    def report_influence(self):
        right_now = self.right_now
        return ", ".join([
            "{}: {:.1f} ({})".format(moon.name, *moon.influence(right_now))
            for moon in MOONS
        ])

    def order_influence(self, order):
        right_now = self.right_now
        moons_right_now = {
            phase: []
            for phase in PHASES
        }
        order_influence = order_phase = None
        for moon in MOONS:
            influence, phase = moon.influence(right_now)
            moons_right_now[phase].append(influence)
            if order.moon.name == moon.name:
                order_influence = influence
                order_phase = phase
        if order_influence is None or order_phase is None:
            return order.moon.influence(right_now)[0]
        phase_influence = sum(moons_right_now[order_phase])
        if order_phase == HIGH:
            return int(phase_influence)
        elif order_phase == LOW:
            return int(
                (phase_influence * Decimal('-1')) +
                (order_influence * Decimal('2')))
        else:
            return len(moons_right_now[order_phase]) - 1


def Moon_Magic(date):
    datestr = None
    if isinstance(date, tuple):
        tup_len = len(date)
        date = kdatetime(*date)
        if tup_len > 3:
            datestr = date.ktime()
    elif isinstance(date, int):
        date = INITIAL_DATE + ktimedelta(days=date-1)
    elif isinstance(date, kdatetime):
        datestr = date.ktime()
    elif not isinstance(date, kdate):
        raise ValueError("Invalid date format.")
    if not datestr:
        datestr = date.kdatestr()
    retstr = "Moon Magic for {}:\n\n".format(datestr)
    system_state = SolarSystem(date)
    for order in ORDERS:
        moonstr = "Bonus to Caster Level and Save DCs for {}: {} ({})".format(
            order.name, system_state.order_influence(order),
            order.moon.astrolabe(system_state.right_now))
        retstr += moonstr
        retstr += "\n"
        print(moonstr)
    return retstr
