#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest
import re
from src import sshconnect


class TestSSHConnect(unittest.TestCase):
    def setUp(self):
        self.session = sshconnect.SSHConnection(
            'sysadmin.spawnmc.me', 'spawn', '5700', '123123123')
        self.session.connect()

    def test_whoami(self):
        output = str(self.session.send_command('whoami'))
        if re.search(r'\(\[\'[a-zA-Z]+\\n\'\]\,\s\[\]\)', output):
            regex_status = True
        else:
            regex_status = False
        self.assertTrue(regex_status, msg='command failed')

    def tearDown(self):
        self.session.close()


if __name__ == '__main__':
    unittest.main()
