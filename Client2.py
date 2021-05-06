from twisted.internet.protocol import DatagramProtocol,Factory
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
import socket


class Client_Receiver(DatagramProtocol):
    def __init__(self,):
        self.peer_addr=None
        self.NAP_SERVER="127.0.0.1",9999
        self.is_exist=True


    def startProtocol(self):
        reactor.callLater(3,self.exist_port)#포트 중복시 프로그램 종료 루틴
    def stopProtocol(self):        #"called after all transport is teared down"
        pass
    def datagramReceived(self, datagram: bytes, addr):
        global is_connect
        global is_running

        if(addr==self.NAP_SERVER):
            datagram=datagram.decode('utf-8')
            print("Server message:",datagram)
            self.is_exist=False
        else:
            if(is_connect=='0',0):
                is_connect=addr
            print(is_connect,"received message: ", datagram.decode('utf-8'))#peer: received message:
    def exist_port(self):
        if(self.is_exist==True):
            print("중복된 포트로 접근하셨습니다. 다른 포트를 입력하여 주십시오")
            reactor.stop()




class Client_Sender(DatagramProtocol):
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.NAP_SERVER="127.0.0.1",9999
        self.peer_addr=None


    def startProtocol(self):
        self.transport.write("login".encode('utf-8'),self.NAP_SERVER)
        self.loopObj=LoopingCall(self.chat_handler)
        self.loopObj.start(0.5,now=False)
    def datagramReceived(self, datagram: bytes, addr):
        if(addr==self.NAP_SERVER):
            print(datagram.decode('utf-8'))
        else:
            pass #peer가 연락할 경우 Clinet_Receiver한테 처리를 맡긴다.
    def chat_handler(self):
        global is_connect

        line = input("enter your command").split()
        if not line:
            print("명령어가 필요합니다. 다시 입력하여 주세요")
        elif( line[0]=="help"):
            print("명령어 목록")
            print("online_users:현재 연결 가능한 peer들의 목록을 가져옵니다.")
            print("connect [peer]: ip,port를 가진 peer와 연결합니다.")
            print("disconnect [peer]:연결된 peer와 연결을 해제합니다.")
            print("logoff: 서버와 연결을 해제하고 프로그램을 종료합니다.")
            print("talk [peer] [message]: peer와 연락을 주고받습니다. 비동기식으로 얼마든지 보내도 상관 없습니다.")
        elif (line[0] == "online_users"):
            self.transport.write(line[0].encode('utf-8'), self.NAP_SERVER)
        elif (line[0] == "logoff"):
            self.transport.write(line[0].encode('utf-8'), self.NAP_SERVER)
            reactor.stop()
        elif(line[0] == "connect"):  # connect ip port:request to chat with peer with the given ip and port
            self.peer_addr = line[1], int(line[2])
            is_connect =self.peer_addr
            print("connect success! ")
        elif(line[0]=="talk"):
            peer=str(line[1]).split(',')
            if(is_connect==(peer[0],int(peer[1]))):
                line=" ".join(line[2:]).encode('utf-8')
                self.transport.write(line,is_connect)
                print("전달됨")
            elif(is_connect=="0",0):
                print("connect가 먼저 필요한 peer입니다.")
            else:
                print("잘못된 피어 주소입니다. 'ip,port'로 peer주소를 입력해주십시오")
        elif(line[0]=="disconnect"):
            peer=str(line[1]).split(',')
            if(self.peer_addr==peer[0],int(peer[1])):
                is_connect='0',0
            else:
                print("잘못된 peer주소입니다.")


if __name__=='__main__':
    is_connect='0',0

    port=int(input("input port:"))
    my_ip=socket.gethostbyname(socket.getfqdn())
    print(my_ip,port)
    SenderObj=Client_Sender(my_ip,port)
    reactor.listenMulticast(port,Client_Receiver(),listenMultiple=True)
    reactor.listenMulticast(port,SenderObj,listenMultiple=True)
    reactor.run()

