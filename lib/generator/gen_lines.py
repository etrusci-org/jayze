import random
from lib.helper import *




class JayzeLines:

    @staticmethod
    def gen_lines(length, **options):
        """Output lines with randomized characters.

        length (int): line character count.

        **options (kwargs):
            case (str): case format to apply on the output.
            center (list): 2 characters to use for the center effect.
            chars (str): characters to use for output.
            delay (float|int): how many seconds to idle after each output iteration.
            eol (str): which characters to add at the end of a output iteration.
            floater (list): 4 characters to use for the floater effect.
            rep (bool): true=allow  immediate repetition, false=avoid immediate repetition.
            sparkle (list): 1 or more characters to use for the sparkle effect.
        """
        line_w = max(1, length)
        sparkle_chars = options['sparkle']

        if options['floater']:
            floater_index = 0
            floater_char_right = options['floater'][0]
            floater_char_left = options['floater'][1]
            floater_char_border_right = options['floater'][2]
            floater_char_border_left = options['floater'][3]

        if options['center']:
            center_char = options['center'][0]
            center_char_blip = options['center'][1]

        prev_line = None
        while True:
            line = []
            prev_char = ''

            while len(line) < line_w:
                random.seed()
                char = random.choice(options['chars'])
                if not options['rep']:
                    if char != prev_char:
                        line.append(char)
                    else:
                        continue
                    prev_char = char
                else:
                    line.append(char)

            if options['sparkle']:
                sparkle_count_prev = -1
                while True:
                    random.seed()
                    sparkle_count = random.randint(0, len(line) // 13)
                    if sparkle_count == sparkle_count_prev:
                        continue
                    else:
                        sparkle_count_prev = sparkle_count
                        break

                sparkle_indexes = []
                c = 1
                sparkle_index_prev = -1
                while c <= sparkle_count:
                    random.seed()
                    r = random.randint(0, len(line)-1)
                    if r == sparkle_index_prev:
                        continue
                    sparkle_indexes.append(r)
                    c += 1

                for sparkle_index in sparkle_indexes:
                    random.seed()
                    line[sparkle_index] = random.choice(sparkle_chars)

            line_center_index = int(len(line) / 2)
            if options['center']:
                line[line_center_index] = center_char

            if options['floater']:
                line_len = len(line)
                line_last_index = line_len - 1

                if floater_index == 0:
                    line[floater_index] = floater_char_border_left
                    floater_moveto = 'right'
                    floater_index += 1

                elif floater_index == line_last_index:
                    line[floater_index] = floater_char_border_right
                    floater_moveto = 'left'
                    floater_index -= 1

                else:
                    if floater_moveto == 'right':
                        if floater_index < line_last_index:
                            if not options['center']:
                                line[floater_index] = floater_char_right
                            else:
                                line[floater_index] = floater_char_right if floater_index != line_center_index else center_char_blip
                            floater_index += 1

                    if floater_moveto == 'left':
                        if floater_index > 0:
                            if not options['center']:
                                line[floater_index] = floater_char_left
                            else:
                                line[floater_index] = floater_char_left if floater_index != line_center_index else center_char_blip
                            floater_index -= 1

            line = jayze_t_format(''.join(line), **options)

            if not options['rep']:
                if line != prev_line:
                    jayze_output(line, end=options['eol'])
                else:
                    continue
            else:
                jayze_output(line, end=options['eol'])

            jayze_idle(options['delay'])

            prev_line = line
