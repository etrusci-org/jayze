import argparse




class CLIParser:
    conf   = {}
    parser = None
    args   = None


    def __init__(self, conf):
        self.conf = conf
        self.parser = argparse.ArgumentParser()
        for arg_conf in self.conf:
            if type(arg_conf['arg']) == str:
                arg = arg_conf['arg']
                del arg_conf['arg']
                self.parser.add_argument(arg, **arg_conf)
            else:
                arg_long, arg_short = arg_conf['arg']
                del arg_conf['arg']
                self.parser.add_argument(arg_long, arg_short, **arg_conf)


    def parse_args(self, return_dict=True):
        if self.parser:
            args = self.parser.parse_args()
        if not return_dict:
            return args
        else:
            return vars(args)


    def print_help(self):
        self.parser.print_help()
