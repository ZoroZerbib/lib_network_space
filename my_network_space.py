from lib_network_space import SpaceEntity, SpaceNetwork, Packet
from lib_network_space import TemporalInterferenceError, DataCorruptedError, LinkTerminatedError, OutOfRangeError
from lib_network_space import CommsError
import time


class EarthEntity(SpaceEntity):
    def receive_signal(self, packet):
        pass


class Satellite(SpaceEntity):
    def receive_signal(self, packet):
        if isinstance(packet, RelayPacket):
            inner_packet = packet.data
            print(f"Unwrapping and forwarding to {inner_packet.receiver}")
            attempt_transmission(inner_packet, network)
        else:
            print(f"Final destination reached: {packet.data}")


class BrokenConnectionError(CommsError):
    pass


def attempt_transmission(packet, network):
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
            print("Link lost")
            raise BrokenConnectionError
        except OutOfRangeError:
            print("Target out of range")
            raise BrokenConnectionError


class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(packet_to_relay, sender, proxy)

    def __repr__(self):
        return f"RelayPacket(Relaying [{self.data}] to {self.receiver} from {self.sender})"


network = SpaceNetwork(4)
Earth = EarthEntity("Earth", 0)
Sat1 = Satellite("Sat1", 100)
Sat2 = Satellite("Sat2", 200)
p_final = Packet("Hello from Earth!!", "Sat1", "Sat2")
p_earth_to_sat1 = RelayPacket(p_final, "Earth", "Sat1")
try:
    attempt_transmission(p_earth_to_sat1, network)
except BrokenConnectionError:
    print("Transmission failed")
