import os
import socket
import sys
from threading import Thread


def runOnce():
    try:
        with open('GetIP.txt') as f:
            lines = f.read().splitlines()
        if lines[0] == 'True':
            return True
        else:
            os.system('pip install -r install.txt')
            _ = input('Enter IP or press Enter (No Input to get default) : ')
            if _ == '':
                _ = socket.gethostbyname(socket.gethostname())
            f = open('IpOfMaster.txt', 'w')
            f.write(_)
            f = open('GetIP.txt', 'w')
            f.write('True')
        return True
    except FileNotFoundError:
        os.system('pip install -r install.txt')
        _ = input('Enter IP or press Enter (No Input to get default) : ')
        if _ == '':
            _ = socket.gethostbyname(socket.gethostname())
        f = open('IpOfMaster.txt', 'w')
        f.write(_)
        f = open('.GetIP.txt', 'w')
        f.write('True')
        return True


def main():
    runOnce()
    master = Master()
    print("[+] Starting server")
    master.run_server()
    print("[-] Stopping server")


def getMasterIP():
    with open("IpOfMaster.txt") as f:
        lines = f.read().splitlines()
    return lines[0].strip()


class Master:
    def __init__(self):
        self.s = socket.socket()
        self.port = 44095
        self.host = getMasterIP()
        self.s.bind((self.host, self.port))
        self.s.listen(95)
        self.ConnectedSlaves = {}
        self.connections = []
        self.AcceptConn = True

    def default_server(self):
        print(f"[+] Server Accepting Connections at {self.host} on {self.port} ")
        while self.AcceptConn:
            c, address = self.s.accept()
            self.ConnectedSlaves[address] = c
            self.connections.append(c)
            print(f"\n[+] Client {address} Connected \nEnter:")

    def ping_n_del(self):
        err_hosts = []
        for c in self.connections:
            try:
                c.send(b'')
            except ConnectionError:
                err_hosts.append(c)
        for dead in err_hosts:
            self.connections.remove(dead)

    def get_input(self):
        while True:
            pre_msg = ['PopUp All of you shutdown your Systems !'.encode('utf-8'),
                       'PopUp Bring yours Observations One-By-One Roll Number wise !'.encode('utf-8'),
                       'PopUp Write the Attendance in your Lab Book !'.encode('utf-8'),
                       'PopUp Bring yours Records One-By-One Roll Number wise ! !'.encode('utf-8'),
                       'PopUp Any doubts , you can come now ? '.encode('utf-8')
                       ]
            print(
                '\n0.\tExit\n\n1.\tShutdown\n2.\tObservations\n3.\tAttendance\n4.\tRecords\n5.\tdoubts\n6.\tCustoms\n'
                '\n44.\tFORCE SHUTDOWN\n95.\tALL ALIVE IPS\n')
            n = int(input('Enter Number :'))
            self.ping_n_del()
            log_list = [-1]
            if len(self.connections) == 0:
                print('No Slaves are alive !')
            else:
                exit_now = False
                if n == 0:
                    exit_now = True
                elif n == 1:
                    try:
                        log_list = [c.send(pre_msg[0]) for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                elif n == 2:
                    try:
                        log_list = [c.send(pre_msg[1]) for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                elif n == 3:
                    try:
                        log_list = [c.send(pre_msg[2]) for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                elif n == 4:
                    try:
                        log_list = [c.send(pre_msg[3]) for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                elif n == 5:
                    try:
                        log_list = [c.send(pre_msg[4]) for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                elif n == 44:
                    try:
                        [c.send(b'ShutDown') for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                elif n == 95:
                    try:
                        if len(self.connections) != 0:
                            [print('Slave', _w, 'with IP', c.getpeername()[0], 'connected at', c.getpeername()[1]) for _w, c in enumerate(self.connections)]

                        else:
                            print('No Slaves are alive !')
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                else:
                    customs = str(input('Enter Custom Message : '))
                    customs = 'PopUp ' + customs
                    try:
                        [c.send(customs.encode('utf-8')) for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                if not exit_now:
                    q = int(input(
                        "\n\n??? NOTE : DON'T PRESS 0 UNTIL UNLESS IT IS THE LAST MESSAGE ???\n\nPress 1 to resend 0 "
                        "to exit : "))
                else:
                    q = 0
                if q == 0:
                    try:
                        [c.send(b'Closed') for c in self.connections]
                    except ConnectionError:
                        print(f'conn Error for {log_list[-1]}')
                    finally:
                        break
        [c.close() for c in self.connections]
        print(f"[*] All Clients Disconnected ")
        self.AcceptConn = False
        ls = socket.socket()
        ls.connect((self.host, self.port))

    def run_server(self):
        threads_list = []
        try:
            for fun in [self.default_server, self.get_input]:
                th = Thread(target=fun)
                th.start()
                threads_list.append(th)
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            [t_s.join() for t_s in threads_list]


if __name__ == '__main__':
    main()
