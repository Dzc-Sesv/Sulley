from sulley import *
from requests import ftp
import process_monitor
import network_monitor
# this is our ftp.py file
def receive_ftp_banner(sock):
    sock.recv(1024)

sess = sessions.session(session_filename="C:\Users\Seve\Desktop\Test\easyftp.session",sleep_time=0.01)
target = sessions.target("127.0.0.1", 21)
#target.procmon = process_monitor.ProcessMonitorPedrpcServer("127.0.0.1", 26002,"C:\Users\Seve\Desktop\Test\Quick Easy FTP Server.exe")

# Here we tie in the receive_ftp_banner function which receives
# a socket.socket() object from Sulley as its only parameter
sess.pre_send = receive_ftp_banner
sess.add_target(target)
sess.connect(s_get("user"))
sess.connect(s_get("user"), s_get("pass"))
sess.connect(s_get("pass"), s_get("cwd"))
sess.connect(s_get("pass"), s_get("dele"))
sess.connect(s_get("pass"), s_get("mdtm"))
sess.connect(s_get("pass"), s_get("mkd"))
sess.fuzz()