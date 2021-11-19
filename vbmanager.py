#!/usr/bin/env python
#-*- coding: utf-8 -*-
from getpass import getpass

class VBoxManager():
    def __init__(self):
        pass
    
    def show_menu(self):
        print("""
        1. Connect to SSH
        1. Create VM
        2. Delete VM
        3. List VM
        4. List running VM
        5. Create Snapshot
        6. Delete Snapshot
        7. List Snapshot
        8. Exit
        """)

    def connect_ssh(self):
        print("\nConnect to SSH:")
        input_user = input("Enter SSH user: ")
        input_ip = input("Enter IP address: ")
        input_port = input("Enter SSH port: ")
        input_pass = getpass("Enter SSH password: ")
        self._test_connect_ssh(input_user, input_ip, input_port, input_pass)
 
    def list_vm(self):
        print("\nList of VM:")
        for vm in self.vbox.machines:
            print(vm.name)

def main():
    vb = VBoxManager()
    vb.connect_ssh()


if __name__ == '__main__':
    main()
