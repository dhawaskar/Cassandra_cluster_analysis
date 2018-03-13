'''
    udp socket client
    Silver Moon
'''
import time 
import socket   #for sockets
import sys  #for exit
import csv 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'cn1';
port = 8888;

header_row=["T1","T2","T3","T4","Delay","Offeset"]
result_row=[]
result_row.append(header_row)
count=100
while(count) :
    try :
	s.sendto("send time", (host, port))
	t1=float("%.20f"%time.time())
	#print time_send
	d = s.recvfrom(1024)
	t4=float("%.20f"%time.time())
	#print time_recv
	reply = d[0]
	addr = d[1]
	reply_time=reply.split('\t')
	t2=float(reply_time[0])
	t3=float(reply_time[1])
	#print 'Server receive time : ' + reply_time[0] +'server send time'+reply_time[1]
	delay=((t4-t1)-(t3-t2))*1000
        print delay
	offset=(((t2-t1)+(t3-t4))/2)*1000
        print offset
        header_list=[t1,t2,t3,t4,delay,offset]
        result_row.append(header_list)
        #wfp.writerows(header_list)
        count-=1
    except socket.error, msg:
	print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
fp=open("readings.csv","w")
with fp:
	wfp=csv.writer(fp)
	wfp.writerows(result_row)
print "Writing is done"
