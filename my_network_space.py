from lib_network_space import SpaceEntity,SpaceNetwork,Packet

class Satellite(SpaceEntity):

    def receive_signal(self, packet):
        print (f"[{self.name}] Received: {packet}")

my=SpaceNetwork(1)
Sat1=Satellite("aba",100)
Sat2=Satellite("ema",200)
sos=Packet("אנחנו בחיים ואתם?",Sat1,Sat2)
my.send(sos)
