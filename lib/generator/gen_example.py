from lib.helper import *

class JayzeExample:
    """Minimal generator module example.
    """
    def gen_example(self, foo, **options):
        """Example output.

        foo (str): some value.

        **options (kwargs):
            delay (float|int): how many seconds to idle after each output iteration.
            eol (str): which characters to add at the end of a output iteration.
        """
        jayze_output('It is alive!', end=options['eol'])
        jayze_idle(options['delay'])

        jayze_output('foo =', foo, end=options['eol'])
        jayze_idle(options['delay'])

        jayze_output('options =', options, end=options['eol'])
