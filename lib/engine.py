from lib.helper import jayze_output




class JayzeEngine:
    conf = {}
    args = {}
    app_info_str = ''


    def __init__(self, conf, args):
        """Initialize the engine, save given arguments.

        conf (dict): jayze_conf from lib.conf
        args (dict): parsed command line arguments, also see jayze_conf['args'].
        """
        self.conf = conf
        self.args = args
        self.app_info_str = '{name} {version}'.format(**conf['app'])


    def main(self):
        """Execute one generator according to given arguments and mapping in jayze_conf.arg_map.
        """

        for action, arg_map in sorted(self.conf['arg_map'].items()):
            if self.args[action] != False \
            or type(self.args[action]) == int:

                options = {}
                for k, v in arg_map['options'].items():
                    options[k] = self.args[v]

                if self.args['verbose']:
                    jayze_output('--- Generator ({}) ---'.format(self.app_info_str).ljust(80, '-'), '\n')
                    jayze_output('{}.{}('.format(arg_map['class'].__name__, arg_map['method']))
                    for k, v in sorted(options.items()):
                        if k == 'eol':
                            v = '"{}"'.format(v) if not v == '\n' else '\\n'
                        jayze_output('  {} = {} {}'.format(k,v, type(v)))
                    jayze_output('):\n')
                    jayze_output('--- Output ---'.ljust(80, '-'), '\n')

                getattr(arg_map['class'](), arg_map['method'])(**options)

                return 0

        jayze_output(self.app_info_str)

        return 0
