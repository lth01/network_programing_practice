from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class NAP_SERVER(DatagramProtocol):
    def __init__(self):
        self.users=[]

    def datagramReceived(self, datagram: bytes, addr):
        receive_data=datagram.decode('utf-8')

        if addr in self.users:
            pass
        else:
            self.users.append(addr)
            print(self.users)
            self.transport.write("user index success".encode('utf-8'),addr)
        if receive_data=="online_users":
            print("receive")
            user_list_to_str=str(self.users[0:])
            self.transport.write(user_list_to_str.encode('utf-8'),addr)
        elif receive_data=="logoff":
            del self.users[self.users.index(addr)]
        elif receive_data=="confirm":
            self.transport.write("ok...".encode('utf-8'),addr)

if __name__=='__main__':
    reactor.listenUDP(9999,NAP_SERVER())
    reactor.run()