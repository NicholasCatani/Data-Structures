### Internet simulation

import time

class Packet:
    def __init__(self, content):
        self.content = content

class Alice:
    def __init__(self, internet):
        self.internet = internet
        self.packet_queue = []

    def create_packet(self, content):
        packet = Packet(content)
        self.packet_queue.append(packet)
        self.internet.notify_packet_available()

    def send_packet(self):
        if self.packet_queue:
            packet = self.packet_queue(0)
            return packet
        return None

class Bob:
    def __init__(self, internet):
        self.internet = internet

    def check_for_packet(self):
        packet = self.internet.deliver_packet()
        if packet:
            print(f"Bob received packet: {packet.content}")

class Internet:
    def __init__(self):
        self.packet_available = False

    def notify_packet_available(self):
        self.packet_available = True

    def deliver_packet(self):
        if self.packet_available:
            self.packet_available = False
            return Alice(self).send_packet()
        return None

if __name__ == "__main__":
    internet = Internet()
    alice = Alice(internet)
    bob = Bob(internet)

    # Alice creates and sends packets periodically
    for i in range(5):
        content = f"Packet {i + 1}"
        alice.create_packet(content)
        time.sleep(1) # It simulates some time passing

    # Bob checks for packets periodically
    for i in range(5):
        bob.check_for_packet()
        time.sleep(1) # It simulates some time passing
