import time
from DataBase import database_updater
import os

def encode(txt_file,message):
    fo = open(txt_file,"w")
    file_details = os.stat(txt_file)
    mtime = file_details[8]
    sent_tym = time.time()
    fo.write(message+","+str(sent_tym))
    actual_msg = [message,sent_tym]
    database_updater.get_msg_fromUser(actual_msg, 0,mtime)
    fo.close()
    #print("Message Encoded in Txt")
