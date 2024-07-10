
def ep2time(time_to):
    days = time_to // (24 * 60 * 60)
    today = time_to - (days * 60 * 60 * 24)
    hour = today / (60 * 60)
    hr = hour + 5.5
    minute = (hour - int(hour)) * 60
    minu = minute + 30
    return (int(hr)%24,int(minu)%60)

def latest_message_sent():
    db_file = open("Database\DB_Source_records.csv", "r")
    fulldb = db_file.read().split('\n')
    latest_msg = fulldb[-2].split(',')
    db_file.close()
    return latest_msg

def latest_message_recv():
    db_file = open("Database\DB_Destination_records.csv", "r")
    fulldb = db_file.read().split('\n')
    latest_msg = fulldb[-2].split(',')
    db_file.close()
    return latest_msg

def latest_message_recv2():
    db_file = open("Database\DB_Destination_records.csv", "r")
    fulldb = db_file.read().split('\n')
    latest_msg = fulldb[-3].split(',')
    db_file.close()
    return latest_msg

def print_msg(k):
    tym = ep2time(float(k[1]))
    hr,min = tym
    time_ist = str(hr)+':'+str(min)
    print('[',time_ist,':',k[2],']\t',k[0])