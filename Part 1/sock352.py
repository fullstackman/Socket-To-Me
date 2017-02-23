# the CS 352 socket library 

import binascii
import socket as syssock
import struct
import sys
import errno

transmitter = ""
receiver = ""
mainSocket = (0,0)
otherHostAddress = ""
simulatedDrop = 0;
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
deliveredData = ""

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
    receiver = int(UDPportRx)
    if(UDPportTx == ''):
        transmitter = receiver
    else:
        transmitter = int(UDPportTx)
    mainSocket.bind( ('', receiver) )  #'localhost', receiver port #
    #mainSocket.settimeout(2)
    print('Initialization complete!')
    return 
    
class socket:
    
    def __init__(self):  # fill in your code here
        # create any lists/arrays/hashes you need
        print("\tReturning your new 352-socket!")
        return
    
    def bind(self,address):   # null function for part 1 
        print("\tWe are binding!\n")
        return

    def connect(self,address):
        global mainSocket
        print("\tInitiating a conection on %s" % (transmitter) )
        
        #  create a new sequence number
        #  create a new packet header with the SYN bit set in the flags
        #  (use the Struct.pack method)
        #  also set the other fields (e.g sequence #)
        #   add the packet to the outbound queue

        #header = self.__make_header(0x07, 1, 1, 33)
        #print("\t%d fake bytes sent!" % (mainSocket.sendto(header
        #    +"Release the kraken!", (address[0], int(transmitter)) ) ) )
        header = self.__make_header(0x01, 1, 1, 0)
        flag = -1

        #   set the timeout
        #      wait for the return SYN
        #        if there was a timeout, retransmit the SYN packet
        while(flag != 0x01):
            print("\t%d bytes sent!" % (mainSocket.sendto(header,
                (address[0], transmitter) ) ) )
            flag = self.__sock352_get_packet()
        # We are safe to establich this UDP connection to the other host
        mainSocket.connect( (address[0], transmitter) )
        header = self.__make_header(0x04, 1, 1, 0)
        print("\t%d confirmation bytes sent!" % (mainSocket.send(header) ) )
        #   set the outbound and inbound sequence numbers

        return header

    def accept(self):
        global mainSocket, simulatedDrop, receiver

        # Set this variable to simulate the server not receiving a packet
        #simulatedDrop += 1
        print('\tWe are waiting for a connection on %s\n' % (receiver) )
        flag = -1
        # call  __sock352_get_packet() until we get a new connection
        while(flag != 0x01):
            flag = self.__sock352_get_packet()
            print("\tFlag returned was: %d" % flag)
        # check the the connection list - did we see a new SYN packet?
        # This will implement the handshake protocol
        header = self.__make_header(0x01,0,0,13)
        mainSocket.sendto(header+"I accept you.", otherHostAddress)
        #TODO: send reset on timeout
        while(flag != 0x04):
            flag = self.__sock352_get_packet()
        print("\tAcquired a connection! Calling new init...")
        clientsocket = socket() #init('',receiver)
        #syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
        #clientsocket.bind( ('', receiver) )
        return (clientsocket,otherHostAddress)
  
    def close(self):   # fill in your code here
        # send a FIN packet (flags with FIN bit set)
        # remove the connection from the list of connections
        return

    def listen(self,buffer): #null code for part 1 
        print("\tWe are listening!\n")
        return

    def send(self,buffer):
        global mainSocket, header_len
        bytesSent = 0
        # make sure the correct fields are set in the flags
        # make sure the sequence and acknowlegement numbers are correct
        # create a new sock352 header using the struct.pack
        # create a new UDP packet with the header and buffer 
        # send the UDP packet to the destination and transmit port
        # set the timeout
        # wait or check for the ACK or a timeout
        header = self.__make_header(0x03,0,0,len(buffer))
        bytesSent = mainSocket.send(header+buffer)
        return bytesSent - header_len

    def recv(self,bytes_to_receive):
        global mainSocket, deliveredData
        print("\tStarted the recv call!\n\n")
        deliveredData = ""
        # call __sock352_get_packet() to get packets (polling)
        # check the list of received fragements
        # copy up to bytes_to_receive into a buffer
        # return the buffer if there is some data
        flag = -1
        while(flag != 0x03):
            flag = self.__sock352_get_packet()
        return deliveredData
    
    # this is an internal function that demultiplexes all incomming packets
    # it update lists and data structures used by other methods
    
    def  __sock352_get_packet(self):
        global mainSocket, sock352PktHdrData, otherHostAddress, deliveredData, simulatedDrop
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
        (data, senderAddress) = mainSocket.recvfrom(4096)
        (data_header, data_msg) = (data[:12],data[12:])
        header = struct.unpack(sock352PktHdrData, data_header)
        print("\t\tWe received this flag: %d" % header[1])
        print("\t\tThis was the message: ( %s )" % data_msg)
        flag = header[1]
        # pretend this packet got dropped or corrupted
        if(simulatedDrop > 0):
            flag = 831
            simulatedDrop -= 1
        #Python lacks a switch statement!
        #   First check if it's a connection set up (SYN bit set in flags)
        #    Create a new fragment list
        #    Send a SYN packet back with the correct sequence number
        #    Wake up any readers wating for a connection via accept()
        #    or return
        if(flag == 0x01):
            otherHostAddress = senderAddress
            return flag
        #   if it is a connection tear down (FIN) 
        #   send a FIN packet, remove fragment list
        elif(flag == 0x02):
            return flag
        #      else if it is a data packet
        #      check the sequence numbers, add to the list of received fragments
        #      send an ACK packet back with the correct sequence number
        elif(flag == 0x03):
            deliveredData = data_msg
            return flag
        #   else if it is an ACK packet...
        elif(flag == 0x04):
            return flag
        #   If we get a reset packet, ignore it. The calling function should
        #   handle the resend
        elif(flag == 0x08):
            return flag
        #   else if it's nothing it's a malformed packet.
        #   send a reset (RST) packet with the sequence number
        else:
            header = self.__make_header(0x08,header[8],header[9],0)
            if(mainSocket.sendto(header,senderAddress) > 0):
                print("\t\tSent a reset packet!")
            else:
                print("\t\tFailed to send a reset packet!")
            return flag
    
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