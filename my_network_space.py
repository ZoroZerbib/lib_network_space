from lib_network_space import SpaceEntity, SpaceNetwork, Packet
from lib_network_space import TemporalInterferenceError, DataCorruptedError,LinkTerminatedError,OutOfRangeError
from  lib_network_space import CommsError
import time


class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        print(f"[{self.name}] Received: {packet}")
class BrokenConnectionError(CommsError):
    pass

def attempt_transmission(packet,network):
    while True:
        try:
            network.send(packet)
            break
        except TemporalInterferenceError:
            print("waiting ,Interference...")
            time.sleep(2)
        except DataCorruptedError:
            print("Data corrupted ,retrying...")
        except LinkTerminatedError:
            print ("Link lost")
            raise BrokenConnectionError
        except OutOfRangeError:
            print ("Target out of range")
            raise BrokenConnectionError

network = SpaceNetwork(3)
Sat1 = Satellite("aba", 100)
Sat2 = Satellite("ema", 200)
packet = Packet("אנחנו בחיים ואתם?", Sat1, Sat2)
try:
    attempt_transmission(packet,network)
except BrokenConnectionError:
    print("Transmission failed")
