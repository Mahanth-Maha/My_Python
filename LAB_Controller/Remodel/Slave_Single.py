import os
import socket
import time
import sys
from threading import Thread

try:
    import win32api
    import win32con
    from pynput.keyboard import Key, Controller
except ModuleNotFoundError:
    os.system('''pip install pypiwin32 pywin32 pynput''')
    import win32api
    import win32con
    from pynput.keyboard import Key, Controller


def getMasterIP():
    with open("IpOfMaster.txt") as f:
        lines = f.read().splitlines()
    return lines[0].strip()


class ShutdownAuto:
    def __init__(self):
        self.keyboard = Controller()
        self.m1 = 6
        self.TIMER_TO_USER_INPUT = 10

    def enter_explicit(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def ask_user(self):
        self.m1 = win32api.MessageBox(0, "Press No to stop", "SHUTDOWN AUTO", win32con.MB_YESNO)

    def enter_by_bot(self):
        time.sleep(self.TIMER_TO_USER_INPUT)
        if self.m1 not in (6, 7):
            self.enter_explicit()

    def DoesUserResponded(self):
        threads_list = []
        try:
            for fun in [self.enter_by_bot, self.ask_user]:
                th = Thread(target=fun)
                th.start()
                threads_list.append(th)
                # time.sleep(5)
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            [t_s.join() for t_s in threads_list]
            # if self.m1 == 1:
            #     return False
            # return True
            return self.m1


class Slave:
    def __init__(self):
        self.s = socket.socket()
        # host = "10.66.17.222"
        # self.host = '127.0.0.1'
        self.port = 44095
        self.host = getMasterIP()
        # host = input('enter IP of master : ')
        # port = input('enter port of master : ')
        self.OK = False
        self.conn()

    def conn(self):
        try:
            self.s.connect((self.host, self.port))
            self.OK = True
        except ConnectionRefusedError:
            print('Retrying')

    def Start_session(self):
        if self.OK:
            while True:
                try:
                    k = self.s.recv(10240)
                    k = k.decode()
                    cmd = k.split(' ')
                    if len(cmd) != 0:
                        if cmd[0] == 'PopUp':
                            st = ''
                            for i in cmd[1:]:
                                st += ' ' + i
                            win32api.Beep(500, 500)
                            win32api.MessageBox(0, str(st), "Sir Says", win32con.MB_OK)
                        if cmd[0] == 'ShutDown':
                            shut = ShutdownAuto()
                            reply = shut.DoesUserResponded()
                            if reply == 6:
                                print('shutdown successful')
                                self.s.close()
                                print('Shutting Down')
                                # os.system("shutdown /s /t 1")
                                break
                            else:
                                print("Sending To Master ! (NOT IMPLEMENTED)")
                        if cmd[0] == 'Closed':
                            print("Server Closed Connection ")
                            self.s.close()
                except ConnectionResetError:
                    print('retry due to reset')
                    self.OK = False
                    break
                except OSError:
                    print('Issue Raised')
                    self.OK = False
                    break


def main():
    # os.system('''pip install  pynput pypiwin32 pywin32 six''')
    while True:
        print("[+] Starting Slave")
        slave = Slave()
        slave.Start_session()
        print("[-] Stopping Slave")


if __name__ == '__main__':
    main()
