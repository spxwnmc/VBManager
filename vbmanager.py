#!/usr/bin/env python
# -*- coding: utf-8 -*-
from getpass import getpass
from src import sshconnect
import re


class VBoxManager():
    def __init__(self, user=None, host=None, port=None, password=None):
        self.user = user
        self.host = host
        self.port = port
        self.password = password
        self.vbox = sshconnect.SSHConnection()

    def show_menu(self):
        print("""
        1. Connect to SSH
        2. List VM
        3. List running VM
        4. Run VM
        5. Stop VM
        6. Save VM
        7. Exit
        """)

    def __get_ssh_info(self):
        self.user = input("Enter remote user: ")
        self.host = input("Enter host address: ")
        __port = input("Enter port: ")
        if __port:
            self.port = __port
        else:
            self.port = "22"
        self.password = getpass("Enter password: ")

    def connect_ssh(self):
        print("\nConnect to SSH:")
        self.__get_ssh_info()
        self.vbox.__setattr__("user", self.user)
        self.vbox.__setattr__("host", self.host)
        self.vbox.__setattr__("port", self.port)
        self.vbox.__setattr__("password", self.password)
        if self.vbox.connect():
            print("Connected to SSH")
        else:
            print("Connection failed")

    def __clear_line(self, string):
        __clean_string = re.compile('(\".+\")')
        __clean_string = __clean_string.findall(string).__str__()
        __clean_string = __clean_string.replace("\"", "")
        __clean_string = __clean_string.replace("'", "")
        __clean_string = __clean_string.replace("[", "")
        __clean_string = __clean_string.replace("]", "")
        return __clean_string

    def __format_reply_vms(self, reply):
        for i in reply:
            for j in i:
                print(self.__clear_line(j.__str__()))

    def list_vm(self):
        print("\nList of VM:")
        self.__format_reply_vms(self.vbox.send_command("vboxmanage list vms"))

    def list_running_vm(self):
        print("\nList of running VM:")
        self.__format_reply_vms(
            self.vbox.send_command("vboxmanage list runningvms"))

    def run_vm(self):
        print("\nRun VM:")
        vm_name = input("Enter VM name: ")
        request = "vboxmanage startvm " + vm_name + " --type headless &"
        print(self.vbox.send_command(request))

    def stop_vm(self):
        print("\nStop VM:")
        vm_name = input("Enter VM name: ")
        request = "vboxmanage controlvm " + vm_name + " poweroff &"
        print(self.vbox.send_command(request))

    def save_vm(self):
        print("\nSave VM:")
        vm_name = input("Enter VM name: ")
        request = "vboxmanage controlvm " + vm_name + " savestate &"
        print(self.vbox.send_command(request))

    def __del__(self):
        self.vbox.close()


def main():
    vb = VBoxManager()
    while True:
        vb.show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            vb.connect_ssh()
        elif choice == "2":
            vb.list_vm()
        elif choice == "3":
            vb.list_running_vm()
        elif choice == "4":
            vb.run_vm()
        elif choice == "5":
            vb.stop_vm()
        elif choice == "6":
            vb.save_vm()
        elif choice == "7":
            vb.__del__()
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
