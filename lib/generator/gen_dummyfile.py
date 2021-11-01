import os
from lib.helper import *




class JayzeDummyfile:

    def gen_dummyfile(self, out_file_conf, **options):
        """Create a dummy file with a specific size in bytes.

        out_file_conf (list|tuple): the size in bytes and file path.

        **options (kwargs):
            none
        """
        out_bytes = max(0, int(out_file_conf[0]))
        out_file = os.path.abspath(out_file_conf[1])

        if os.path.exists(out_file):
            jayze_output('Output file exists already, not going to overwrite it.')
            return

        jayze_output('Writing {} {} to: {} ...'.format(out_bytes, 'byte' if out_bytes == 1 else 'bytes', out_file), end=' ')

        with open(out_file, 'wb') as f:
            out_data = b'0' * out_bytes
            f.write(out_data)

        jayze_output('done.')
