from sulley import *
from requests import ftp
# this is our ftp.py file
def receive_ftp_banner(sock):
    sock.recv(1024)

sess = sessions.session(session_filename="C:\Users\Seve\Desktop\Test\easyftp.session",sleep_time=0.01)
target = sessions.target("127.0.0.1", 21)
target.netmon = pedrpc.client("127.0.0.1",26001)
target.procmon = pedrpc.client("127.0.0.1", 26002)
target.procmon_options = \
{ 
    "proc_name" : "easyftp.exe",
    "stop_commands" : ['net stop "trend serverprotect"'],
    "start_commands" : ['net start "trend serverprotect"'], 
}

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