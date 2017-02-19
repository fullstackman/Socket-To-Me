# the CS 352 socket library 

import binascii
import socket as syssock
import struct
import sys

transmitter = ""
receiver = ""
mainSocket = ""
sock352PktHdrData = "!12B" #'!B_BB_BBB__B_'0
#each one of these are represented as a B
version = 0x1
opt_ptr = 0x0
protocol = 0x0
checksum = 0x0
source_port = 0x0
dest_port = 0x0
window = 0x0
#header_len = struct.calcsize(sock352PktHdrData)
header_len = 12

"""
by = bytes(st, "utf-8")
by += b"0" * (100 - len(by))
print(by)
"""

"""
Flag Name       (Hex) Value     (Binary) Value  (Binary) Meaning
SOCK352_SYN     0x01            00000001        Connection initiation
SOCK352_FIN     0x02            00000010        Connection end
SOCK352_ACK     0x04            00000100        Acknowledgement #
SOCK352_RESET   0x08            00001000        Reset the connection
SOCK352_HAS_OPT 0xA0            00010000        Option field is valid
"""

# this init function is global to the class and
# defines the UDP ports all messages are sent
# and received from.
def init(UDPportTx,UDPportRx):
    global mainSocket, transmitter, receiver

    # create a UDP/datagram socket 
    # bind the port to the Rx (receive) port number
    mainSocket = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    transmitter = UDPportTx
    receiver = UDPportRx
    #mainSocket.bind( (UDPportTx, int(UDPportRx) ) )  #'localhost',4512
    pass 
    
class socket:
    
    def __init__(self):  # fill in your code here
        # create any lists/arrays/hashes you need
        
        return
    
    def bind(self,address):
       # null function for part 1 
        return 

    def connect(self,address):  # fill in your code here
        global UDPportTx, sock352PktHdrData, header_len, version, opt_ptr, protocol, checksum, source_port, dest_port, window
        
        print("\tInitiating a conection...")
        print(address[0])
        print(address[1])
        #  create a new sequence number
        #  create a new packet header with the SYN bit set in the flags (use the Struct.pack method)
        #  also set the other fields (e.g sequence #)
        flags = 0x01
        sequence_no = 1
        ack_no = sequence_no
        payload_len = 33

        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        header = udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len, checksum, source_port, dest_port, sequence_no, ack_no, window, payload_len)
        
        #   add the packet to the outbound queue
        #   set the timeout
        mainSocket.settimeout(0.000001)
        #      wait for the return SYN
        #        if there was a timeout, retransmit the SYN packet
        #   set the outbound and inbound sequence numbers

        return header
    

    def accept(self):
        print('\n\tWe are waiting for accept!\n')
        (clientsocket, address) = (1,1)  # change this to your code
        # call  __sock352_get_packet() until we get a new conection
        # check the the connection list - did we see a new SYN packet?
        # This will implement the handshake protocol
        return (clientsocket,address)
  
    def close(self):   # fill in your code here
        # send a FIN packet (flags with FIN bit set)
        # remove the connection from the list of connections
        return

    def listen(self,buffer): #null code for part 1 
        pass 
        return 

    def send(self,buffer):
        global UDPportTx  # example using a variable global to the Python module 
        bytessent = 0     # fill in your code here
        # make sure the correct fields are set in the flags
        # make sure the sequence and acknowlegement numbers are correct
        # create a new sock352 header using the struct.pack
        # create a new UDP packet with the header and buffer 
        # send the UDP packet to the destination and transmit port
        # set the timeout
        # wait or check for the ACK or a timeout

        return bytesreceived 


    def recv(self,bytes_to_receive):
        # call __sock352_get_packet() to get packets (polling)
        # check the list of received fragements
        # copy up to bytes_to_receive into a buffer
        # return the buffer if there is some data
        pass
    
    # this is an internal function that demultiplexes all incomming packets
    # it update lists and data structures used by other methods
    
    def  __sock352_get_packet(self):
        global mainSocket
        #mainSocket.recvfrom(4096)
        # There is a differenct action for each packet type, based on the flags
        
        #  First check if it's a connection set up (SYN bit set in flags)
        #    Create a new fragment list
        #    Send a SYN packet back with the correct sequence number
        #    Wake up any readers wating for a connection via accept() or return 
        #  else
        #      if it is a connection tear down (FIN) 
        #        send a FIN packet, remove fragment list
        #      else if it is a data packet
        #           check the sequence numbers, add to the list of received fragments
        #           send an ACK packet back with the correct sequence number
        #          else if it's nothing it's a malformed packet.
        #              send a reset (RST) packet with the sequence number
        print('\tget_packet was called\n')
        return
    