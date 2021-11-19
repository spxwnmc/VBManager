#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pexpect import pxssh

class SSHConnection():
    def __init__(self):
        self.username = None
        self.ip = None
        self.port = None
        self.password = None
    
    def connect(self):
        try:
            self.ssh = pxssh.pxssh()
            self.ssh.login(self.ip, self.username, self.password, port=self.port)
            return True
        except Exception as e:
            print(e)
            return False