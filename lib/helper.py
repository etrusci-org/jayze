"""shared helper functions.
"""

import math
import random
import sys
import time




__all__ = [
    'jayze_idle',
    'jayze_n_format',
    'jayze_t_format',
    'jayze_output',
]


def jayze_idle(sec):
    """Do nothing for a specific amount of time.

    sec (int|float): for how long to do nothing.
    """
    sec = max(0, sec)
    time.sleep(sec)


def jayze_n_format(n, **options):
    """Format a number according to given arguments.

    n (int|float) : the number to format.

    **options (kwargs):
        ascinot (bool): true=automatically convert numbers to scientific number notation when they exceed the precision limit, false=keep original number.
        prec (int): precision to use for scientific number notation.
        scinot (bool): true=use scientific number notation, false=do not use scientific number notation.
        sqrt (bool): true=output square root of originally computed numbers, false=keep original numbers.
    """
    try:
        if options['sqrt']:
            n = math.sqrt(n)

        if not options['scinot'] and not options['ascinot']:
            return '{:.{}f}'.format(n, options['prec']) if type(n) == float else n

        if options['ascinot']:
            return '{:.{}g}'.format(n, options['prec'])

        if options['scinot']:
            return '{:.{}e}'.format(n, options['prec'])
    except:
        pass

    return n


def jayze_t_format(t, **options):
    """Format a text according to given arguments.

    t (int|float) : the text to format.

    **options (kwargs):
        case (str): case format to apply on the output.
    """
    if options['case'] != 'keep_case':
        if options['case'] == 'random':
            random.seed()
            t = getattr(t, random.choice(['title', 'capitalize', 'lower', 'upper']))()
        else:
            t = getattr(t, options['case'])()

    return t


def jayze_output(*msg, end='\n'):
    """Print a message to stdout.

    *msg (str|args): the message to be printed.
    end (str): which characters to add at the end of the output.
    """
    msg = ' '.join(map(str, msg))
    sys.stdout.write('{}{}'.format(msg, end))
    sys.stdout.flush()
