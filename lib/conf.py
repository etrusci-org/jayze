"""jayze configuration.

jayze_conf...
    app : app information.
    args : configuration for lib.vendor.cliparser.
    arg_map : argument->module mapping for automatic execution in lib.engine.JayzeEngine.main.
"""

# from lib.generator.gen_example import JayzeExample
from lib.generator.gen_primes import JayzePrimes
from lib.generator.gen_triangulars import JayzeTriangulars
from lib.generator.gen_fibonaccis import JayzeFibonaccis
from lib.generator.gen_lines import JayzeLines
from lib.generator.gen_phrases import JayzePhrases
from lib.generator.gen_permutations import JayzePermutations
from lib.generator.gen_dummyfile import JayzeDummyfile




jayze_conf = {
    'app': {
        'name': 'jayze',
        'version': '1.0.1',
    },

    'args': [
        # Misc arguments
        {
            'arg': ('-v', '--verbose'),
            'default': False,
            'action': 'store_true',
            'help': 'show generator info, useful for development'
        },
        # Generator arguments
        # {
        #     'arg': '--gen-example',
        #     'metavar': 'FOO',
        #     'type': str,
        #     'default': False,
        # },
        {
            'arg': '--gen-fibonaccis',
            'metavar': ('START', 'END'),
            'type': int,
            'default': False,
            'nargs': 2,
        },
        {
            'arg': '--gen-primes',
            'metavar': ('START', 'END'),
            'type': int,
            'default': False,
            'nargs': 2,
        },
        {
            'arg': '--gen-triangulars',
            'metavar': ('START', 'END'),
            'type': int,
            'default': False,
            'nargs': 2,
        },
        {
            'arg': '--gen-lines',
            'metavar': 'LENGTH',
            'type': int,
            'default': False,
        },
        {
            'arg': '--gen-phrases',
            'metavar': 'FILE',
            'type': str,
            'default': False,
            'nargs': '+',
        },
        {
            'arg': '--gen-typewriter',
            'metavar': 'FILE',
            'type': str,
            'default': False,
            'nargs': '+',
        },
        {
            'arg': '--gen-permutations',
            'metavar': 'CHARACTERS',
            'type': str,
            'default': False,
        },
        {
            'arg': '--gen-dummyfile',
            'metavar': ('SIZE', 'FILE'),
            'type': str,
            'default': False,
            'nargs': 2,
        },
        # Option arguments
        {
            'arg': '--ascinot',
            'default': False,
            'action': 'store_true',
        },
        {
            'arg': '--case',
            'metavar': 'CASE',
            'type': str,
            'default': 'keep_case',
            'choices': ['capitalize', 'lower', 'title', 'upper', 'random'],
        },
        {
            'arg': '--center',
            'metavar': ('CHARACTER_CENTER', 'CHARACTER_BLIP'),
            'type': str,
            'default': [],
            'nargs': 2,
        },
        {
            'arg': '--chars',
            'metavar': 'CHARACTERS',
            'type': str,
            'default': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@!?#',
        },
        {
            'arg': '--delay',
            'metavar': 'SECONDS',
            'type': float,
            'default': 0.0,
        },
        {
            'arg': '--eol',
            'metavar': 'CHARACTERS',
            'type': str,
            'default': '\n',
        },
        {
            'arg': '--floater',
            'metavar': ('CHARACTER_TO_RIGHT', 'CHARACTER_TO_LEFT', 'CHARACTER_BORDER_RIGHT', 'CHARACTER_BORDER_LEFT'),
            'type': str,
            'default': [],
            'nargs': 4,
        },
        {
            'arg': '--prec',
            'metavar': 'PRECISION',
            'type': int,
            'default': 8,
        },
        {
            'arg': '--rep',
            'default': False,
            'action': 'store_true',
        },
        {
            'arg': '--scinot',
            'default': False,
            'action': 'store_true',
        },
        {
            'arg': '--sparkle',
            'metavar': 'CHARACTER',
            'type': str,
            'default': [],
            'nargs': '+',
        },
        {
            'arg': '--sqrt',
            'default': False,
            'action': 'store_true',
        },
        {
            'arg': '--varlen',
            'metavar': 'CHANCE',
            'type': float,
            'default': 0.0,
        },
    ],
    'arg_map': {
        # # --gen-example
        # # the key must match the argument arg key translation,
        # # e.g. "--gen-example" will become "gen_example".
        # 'gen_example': {
        #     'class': JayzeExample,      # (object) class object
        #     'method': 'gen_example',    # (str) method to run
        #     # options the method accepts, these will be passed as kwargs to the method:
        #     'options': {
        #         # method key: args key
        #         'foo': 'gen_example',   # foo, gets value from args.gen_example (--gen-example)
        #         'delay': 'delay',       # delay, gets value from args.delay (--delay)
        #         'eol': 'eol',           # eol, gets value from args.eol (--eol)
        #     },
        # },
        # --gen-primes
        'gen_primes': {
            'class': JayzePrimes,
            'method': 'gen_primes',
            'options': {
                'n_range': 'gen_primes',
                'delay': 'delay',
                'scinot': 'scinot',
                'ascinot': 'ascinot',
                'prec': 'prec',
                'sqrt': 'sqrt',
                'eol': 'eol',
            },
        },
        # --gen-triangulars
        'gen_triangulars': {
            'class': JayzeTriangulars,
            'method': 'gen_triangulars',
            'options': {
                'n_range': 'gen_triangulars',
                'delay': 'delay',
                'scinot': 'scinot',
                'ascinot': 'ascinot',
                'prec': 'prec',
                'sqrt': 'sqrt',
                'eol': 'eol',
            },
        },
        # --gen-fibonaccis
        'gen_fibonaccis': {
            'class': JayzeFibonaccis,
            'method': 'gen_fibonaccis',
            'options': {
                'n_range': 'gen_fibonaccis',
                'delay': 'delay',
                'scinot': 'scinot',
                'ascinot': 'ascinot',
                'prec': 'prec',
                'sqrt': 'sqrt',
                'eol': 'eol',
            },
        },
        # --gen-lines
        'gen_lines': {
            'class': JayzeLines,
            'method': 'gen_lines',
            'options': {
                'length': 'gen_lines',
                'chars': 'chars',
                'rep': 'rep',
                'delay': 'delay',
                'case': 'case',
                'floater': 'floater',
                'center': 'center',
                'sparkle': 'sparkle',
                'eol': 'eol',
            },
        },
        # --gen-phrases
        'gen_phrases': {
            'class': JayzePhrases,
            'method': 'gen_phrases',
            'options': {
                'str_files': 'gen_phrases',
                'delay': 'delay',
                'rep': 'rep',
                'varlen': 'varlen',
                'case': 'case',
                'eol': 'eol',
            },
        },
        # --gen-typewriter
        'gen_typewriter': {
            'class': JayzePhrases,
            'method': 'gen_typewriter',
            'options': {
                'str_files': 'gen_typewriter',
                'delay': 'delay',
                'case': 'case',
            },
        },
        # --gen-permutations
        'gen_permutations': {
            'class': JayzePermutations,
            'method': 'gen_permutations',
            'options': {
                'chars': 'gen_permutations',
                'delay': 'delay',
                'case': 'case',
                'eol': 'eol',
            },
        },
        # --gen-dummyfile
        'gen_dummyfile': {
            'class': JayzeDummyfile,
            'method': 'gen_dummyfile',
            'options': {
                'out_file_conf': 'gen_dummyfile',
            },
        },
    },
}
