import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
MULTICAST_TTL = 16

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

while True:
    preMsg = ['PopUp All of you shutdown your Systems !'.encode('utf-8'),
                'PopUp Bring yours Observations One-By-One Roll Number wise !'.encode('utf-8'),
                'PopUp Write the Attendence in your Lab Book !'.encode('utf-8'),
                'PopUp Bring yours Records One-By-One Roll Number wise ! !'.encode('utf-8'),
                'PopUp Any doubts , you can come now ? '.encode('utf-8'),
                ]
    print('\n0.\tExit\n\n1.\tShutdown\n2.\tObservations\n3.\tAttendence\n4.\tRecords\n5.\tdoubts\n6.\tCustoms')
    n = int(input('Press Number :'))
    if n == 1:
        sock.sendto(preMsg[0], (MCAST_GRP, MCAST_PORT))
    elif n == 2:
        sock.sendto(preMsg[1], (MCAST_GRP, MCAST_PORT))
    elif n == 3:
        sock.sendto(preMsg[2], (MCAST_GRP, MCAST_PORT))
    elif n == 4:
        sock.sendto(preMsg[3], (MCAST_GRP, MCAST_PORT))
    elif n == 5:
        sock.sendto(preMsg[4], (MCAST_GRP, MCAST_PORT))
    else:
        customs = str(input('Enter Custom Message : '))
        customs = 'PopUp ' + customs
        sock.sendto(customs.encode('utf-8'), (MCAST_GRP, MCAST_PORT))
    q = int(input('Press 1 to resend 0 to exit : '))
    if q == 0:
        break
