import time
def get_msg_fromUser(msg,flag,mtime):
    #from_src = ['Hello How are You ? ',time]
    if(flag == 0):
        db_file = open("Database\DB_Source_records.csv", "a")
        message = msg[0]
        tim = msg[1]
        db_file.write(message + ',' + str(tim) + ',Sent,' + str(mtime) + '\n')
    else:
        db_file = open("Database\DB_Destination_records.csv", "a")
        message = msg[0]
        tim = time.time()
        db_file.write(message + ',' + str(tim) + ',Recv,' + str(mtime) + '\n')
    db_file.close()

