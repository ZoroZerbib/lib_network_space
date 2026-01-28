from lib_network_space import SpaceEntity, SpaceNetwork, Packet
from lib_network_space import TemporalInterferenceError, DataCorruptedError
import time


class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        print(f"[{self.name}] Received: {packet}")


def transmission_attempt(packet,network):
    while True:
        try:
            network.send(packet)
            break
        except TemporalInterferenceError:
            print("waiting ,Interference...")
            time.sleep(2)
        except DataCorruptedError:
            print("Data corrupted ,retrying...")


network = SpaceNetwork(2)
Sat1 = Satellite("aba", 100)
Sat2 = Satellite("ema", 200)
packet = Packet("אנחנו בחיים ואתם?", Sat1, Sat2)
transmission_attempt(packet,network)
