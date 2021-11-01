from lib.helper import *




class JayzeTriangulars:

    def gen_triangulars(self, n_range, **options):
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

        i = 0

        while True:
            dots = self.get_next_dots_count(iteration=i)

            if dots < n_start:
                i += 1
                continue

            if not endless_output and dots > n_end:
                break

            jayze_output(jayze_n_format(dots,**options), end=options['eol'])

            i += 1
            jayze_idle(options['delay'])


    @staticmethod
    def get_next_dots_count(iteration):
        """Get next iterations dots count.

        iteration (int): current iteration.
        """
        return iteration * (iteration + 1) // 2
