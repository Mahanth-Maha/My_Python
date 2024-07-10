import os
import threading
import time

import main
from DataBase import database_updater, database_reader

Run = True

def send():
    global Run
    printed = 0
    while(Run):
        txt_file = open(main.txt_file_using, "r")
        file_details = os.stat(main.txt_file_using)
        mtime = file_details[8]
        last_message_sent = database_reader.latest_message_sent()
        if (len(last_message_sent) == 4):
            if (int(last_message_sent[3]) != int(mtime)):
                #actual_msg = txt_file.read().split(',')
                print("SENTMSG")
                database_reader.print_msg(database_reader.latest_message_sent())
                #database_updater.get_msg_fromUser(actual_msg, 0, mtime)
        else:
            print("SENT err : len!=4",last_message_sent)
        txt_file.close()
        time.sleep(1)


def receive():
    global Run
    flag = 0
    while (Run):
        txt_file = open(main.txt_file_using, "r")
        file_details = os.stat(main.txt_file_using)
        mtime = file_details[8]
        last_message_recived = database_reader.latest_message_recv2()
        if (len(last_message_recived) == 4):
            if (int(last_message_recived[3]) != int(mtime) and flag == 0):
                actual_msg = txt_file.read().split(',')
                print("RECEIVED")
                database_reader.print_msg(database_reader.latest_message_recv())
                database_updater.get_msg_fromUser(actual_msg, 1, mtime)
                flag = 1
            else:
                if(int(last_message_recived[3]) != int(mtime)):
                    flag = 0
        else:
            print("RECV err : len!=4",last_message_recived)
        txt_file.close()
        time.sleep(1)

if __name__ == '__main__':
    try:
        thread_send = threading.Thread(target=send)
        thread_send.start()
        thread_receive = threading.Thread(target=receive)
        thread_receive.start()
    except:
        print("Error: unable to start thread")
