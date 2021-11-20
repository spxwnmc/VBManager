#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko


class SSHConnection():
    def __init__(self, host=None, username=None, port=None, password=None):
        self.session = paramiko.SSHClient()
        self.host = host
        self.username = username
        self.port = port
        self.password = password

    def connect(self):
        try:
            self.session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.session.connect(hostname=self.host, port=self.port,
                                 username=self.username, password=self.password)
            return True
        except Exception as e:
            print(e)
            return False

    def send_command(self, command):
        stdin, stdout, stderr = self.session.exec_command(command)
        return (stdout.readlines(), stderr.readlines())

    def close(self):
        self.session.close()

    def __del__(self):
        self.close()


if __name__ == "__main__":
    pass
