from Message_Sender import encode_txt
from Message_Reciver import decode_txt
from DataBase import database_reader

txt_file_using = "test_file.txt"


def send_msg():
    message_from_user = input("Enter Text to send : ")
    encode_txt.encode(txt_file_using, message_from_user)
    #print("imaginary:\t sent txt file to dest pc")

def recv_msg():
    decode_txt.decode(txt_file_using)
if __name__ == '__main__':
    Run = True
    while(Run):
        k = input("1.Send \t2.Recv\t0.Stop\tEnter Option:")
        if k == '1':
            send_msg()
            database_reader.print_msg(database_reader.latest_message_sent())
        elif k == '2':
            recv_msg()
            database_reader.print_msg(database_reader.latest_message_recv())
        elif k == '0':
            Run = False
        else:
            print("invalid OPTION")
