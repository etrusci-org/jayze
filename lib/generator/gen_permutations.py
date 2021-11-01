import itertools
from lib.helper import *




class JayzePermutations:

    def gen_permutations(self, chars, **options):
        for p in itertools.permutations(chars):
            p = jayze_t_format(''.join(p), **options)
            jayze_output(p, end=options['eol'])
            jayze_idle(options['delay'])
