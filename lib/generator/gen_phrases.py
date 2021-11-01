import random
from lib.helper import *




class JayzePhrases:

    def gen_phrases(self, str_files, **options):
        """Output phrases with randomized parts from text files.

        str_files (list): file paths to load the input from.

        **options (kwargs):
            case (str): case format to apply on the output.
            delay (float|int): how many seconds to idle after each output iteration.
            eol (str): which characters to add at the end of a output iteration.
            rep (bool): true=allow  immediate repetition, false=avoid immediate repetition.
            varlen (bool): true=vary parts count, false=do not vary parts count.
        """
        str_dump = self.load_str_files(str_files, allow_empty_lines=True)

        prev_phrase = ''
        while True:
            phrase = []
            for i, parts in enumerate(str_dump):
                random.seed()
                if random.random() <= options['varlen']:
                    if len(str_dump) > 2:
                        if (i == 0 or i == len(str_dump)-1):
                            continue
                    if len(str_dump) == 2:
                        if (i == 0):
                            continue
                random.seed()
                phrase.append(random.choice(parts))

            phrase = jayze_t_format(' '.join(phrase), **options)

            if not options['rep']:
                if phrase != prev_phrase:
                    jayze_output(phrase, end=options['eol'])
                else:
                    continue
            else:
                jayze_output(phrase, end=options['eol'])

            jayze_idle(options['delay'])

            prev_phrase = phrase


    def gen_typewriter(self, str_files, **options):
        """Output lines from a textfile in a typewriter manner.

        str_files (list): file paths to load the input from.

        **options (kwargs):
            case (str): case format to apply on the output.
            delay (float|int): how many seconds to idle after each output iteration.
        """
        str_dump = self.load_str_files(str_files, allow_empty_lines=True)
        # while True:
        for parts_dump_index, parts_dump in enumerate(str_dump):
            for part in parts_dump:
                if options['case'] == 'random':
                   random.seed()
                   part = ''.join(getattr(v, random.choice(['title', 'capitalize', 'lower', 'upper']))() for v in list(part))
                else:
                    part = jayze_t_format(part, **options)

                letters = list(part)
                for letter in letters:
                    jayze_output(letter, end='')
                    jayze_idle(options['delay'])
                jayze_output('')
                jayze_idle(options['delay'])


    @staticmethod
    def load_str_files(str_files, allow_empty_lines=False):
        """Read lines from text files.

        str_files (list): file paths to load the input from.
        allow_empty_lines (bool): true=allow empty lines, false=ignore empty lines.
        """
        dump = []
        for str_file in str_files:
            with open(str_file, 'r') as f:
                lines = f.readlines()
            if not allow_empty_lines:
                lines = [v.strip() for v in lines if v.strip() != '' and not v.startswith('#')]
            else:
                lines = [v.strip() for v in lines if not v.startswith('#')]
            dump.append(lines)
        return dump

