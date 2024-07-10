from DataBase import database_updater,database_reader
import os

def decode(txtfile):
    txt_file = open(txtfile,"r")
    file_details = os.stat(txtfile)
    mtime = file_details[8]
    last_message_recived = database_reader.latest_message_recv()
    if(len(last_message_recived) == 4):
        if(int(last_message_recived[3]) != int(mtime)):
            #print(last_message_recived[3],mtime,int(last_message_recived[3]) != int(mtime))
            actual_msg = txt_file.read().split(',')
            database_updater.get_msg_fromUser(actual_msg, 1,mtime)
        else:
            print("No New Messages :: Last Message is")
    #print("Message Decoded from Txt")
