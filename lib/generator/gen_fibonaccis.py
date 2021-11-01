from lib.helper import *




class JayzeFibonaccis:

    def gen_fibonaccis(self, n_range, **options):
        """Run range or endless generator depending on n_range contents.

        n_range (list|tuple): the smallest and biggest number in the range to test.

        **options (kwargs):
            ascinot (bool): true=automatically convert numbers to scientific number notation when they exceed the precision limit, false=keep original number.
            delay (float|int): how many seconds to idle after each output iteration.
            eol (str): which characters to add at the end of a output iteration.
            prec (int): precision to use for scientific number notation.
            scinot (bool): true=use scientific number notation, false=do not use scientific number notation.
            sqrt (bool): true=output square root of originally computed numbers, false=keep original numbers.
        """
        endless_output = True if n_range[1] <= 0 else False

        n_start, n_end = n_range
        n_start = max(0, n_start)
        n_end = max(0, n_end)

        a, b = 0, 1
        while True:
            if a < n_start:
                a, b = self.get_next_ab(a, b)
                continue

            if not endless_output and a > n_end:
                break

            jayze_output(jayze_n_format(a, **options), end=options['eol'])
            jayze_idle(options['delay'])

            a, b = self.get_next_ab(a, b)


    @staticmethod
    def get_next_ab(a, b):
        """Get the next number pair.

        a (int): current number a
        b (int): current number b
        """
        a, b = b, a + b
        return a, b
