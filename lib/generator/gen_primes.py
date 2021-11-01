from lib.helper import *




class JayzePrimes:

    def gen_primes(self, n_range, **options):
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

        n = n_start
        while True:
            if self.trial_division(n):
                if not endless_output and n > n_end:
                    break

                jayze_output(jayze_n_format(n, **options), end=options['eol'])
                jayze_idle(options['delay'])

            n = self.get_next_n(n_cur=n)


    @staticmethod
    def trial_division(n):
        """Test a number for primality.

        n (int): the number to test.
        """
        if n < 2:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        div_last = int(n ** 0.5) + 1
        div_cur  = 3
        while div_cur <= div_last:
            # print(div_cur, div_cur <= div_last)
            if n % div_cur == 0:
                return False
            div_cur += 2

        return True


    @staticmethod
    def get_next_n(n_cur):
        """Get the next number that makes sense to test.

        n_cur (int): the current number.
        """
        if n_cur > 0 and n_cur < 2:
            return 2

        elif n_cur % 2 == 0:
            return n_cur + 1

        else:
            return n_cur + 2
