# the CS 352 socket library 

import binascii
import socket as syssock
import struct
import sys
import errno

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
    mainSocket.bind( ('localhost', int(UDPportRx) ) )  #'localhost', receiver port #
    #mainSocket.settimeout(2)
    print('Initialization complete!')
    return 
    
class socket:
    
    def __init__(self):  # fill in your code here
        # create any lists/arrays/hashes you need
        
        return
    
    def bind(self,address):
       # null function for part 1 
        return 

    def connect(self,address):  # fill in your code here
        global mainSocket
        print("\tInitiating a conection on %s" % (transmitter) )
        
        #  create a new sequence number
        #  create a new packet header with the SYN bit set in the flags
        #  (use the Struct.pack method)
        #  also set the other fields (e.g sequence #)
        header = self.__make_header(0x07, 1, 1, 33)
        
        #   add the packet to the outbound queue
        print("\t%d bytes sent!" % (mainSocket.sendto(header
            +"Release the kraken!", (address[0], int(transmitter)) ) ) )
        header = self.__make_header(0x01, 1, 1, 33)
        print("\t%d bytes sent!" % (mainSocket.sendto(header
            +"Where is it!?", (address[0], int(transmitter)) ) ) )
        #response = mainSocket.recv(20)
        #print("\tGot this response: %s" % (response) )

        #   set the timeout
        #      wait for the return SYN
        #        if there was a timeout, retransmit the SYN packet
        #   set the outbound and inbound sequence numbers

        return header
    

    def accept(self):
        global mainSocket

        print('\tWe are waiting for a connection on %s\n' % (receiver) )
        message = ""

        # call  __sock352_get_packet() until we get a new connection
        #(message, address) = mainSocket.recvfrom(50)
        while(message != "zQ90$"):
            (message, address) = self.__sock352_get_packet()
        print("\tAcquired a connection!")
        mainSocket.sendto("We are connected!", address)
        clientsocket = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
        # check the the connection list - did we see a new SYN packet?
        # This will implement the handshake protocol
        return (clientsocket,address)
  
    def close(self):   # fill in your code here
        # send a FIN packet (flags with FIN bit set)
        # remove the connection from the list of connections
        return

    def listen(self,buffer): #null code for part 1 
        print("\tWe are listening!\n")
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
        global mainSocket, sock352PktHdrData
        """
        check the version number
        check the header length
        get the flag settings
        get seq/ack numbers
        if(connection setup)
            create new fragment list
            send syn packet back with correct sequence number
            wakeup any headers waiting for a connection via accept
        else if(connected server down)
            send fin packet
            remove fragment list
        else if(data packet)
            check sequence number, add to fragment list
            send ack on that sequence number
        else
            packet is corrupted. send a RST packet
        """
        flag = -1
        while(flag != 1):
            (data, senderAddress) = mainSocket.recvfrom(4096)
            (data_header, data_msg) = (data[:12],data[12:])
            header = struct.unpack(sock352PktHdrData, data_header) #data[:13] ?
            print("\t\tWe received this flag: %d" % header[1])
            print("\t\tThis was the message: %s" % data_msg)
            flag = header[1]
        return ("zQ90$",senderAddress)
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
    
    def  __make_header(self, givenFlag, givenSeqNo, givenAckNo, givenPayload):
        global sock352PktHdrData, header_len, version, opt_ptr, protocol
        #TODO: figure out line breaks!
        global checksum, source_port, dest_port, window

        flags = givenFlag
        sequence_no = givenSeqNo
        ack_no = givenAckNo
        payload_len = givenPayload
        
        udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
        return udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol,
            header_len, checksum, source_port, dest_port, sequence_no,
            ack_no, window, payload_len)
#end