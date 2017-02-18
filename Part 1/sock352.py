# the CS 352 socket library 

import binascii
import socket as syssock
import struct
import sys

var transmitter
var receiver
basicSocket

# this init function is global to the class and
# defines the UDP ports all messages are sent
# and received from.
def init(UDPportTx,UDPportRx):   # initialize your UDP socket here
    # create a UDP/datagram socket 
    # bind the port to the Rx (receive) port number
    syssock.create()
    pass 
    
class socket:
    
    def __init__(self):  # fill in your code here
        # create any lists/arrays/hashes you need
        # MAYBE intialize things like
            #Family: AF_INET
            #Type: SOCK_STREAM
            #Protocol: IPPROTO_TCP
        
        return
    
    def bind(self,address):
       # null function for part 1 
        return 

    def connect(self,address):  # fill in your code here
        global UDPportTx  # example using a variable global to the Python module 

        #  create a new sequence number 
        #  create a new packet header with the SYN bit set in the flags (use the Struct.pack method)
        #  also set the other fields (e.g sequence #) 
        #   add the packet to the outbound queue
        #   set the timeout
        #      wait for the return SYN
        #        if there was a timeout, retransmit the SYN packet 
        #   set the outbound and inbound sequence numbers  
        return 
    
    def listen(self,backlog):
        # MAYBE Call syssock.listen
        return

    def accept(self):
        (clientsocket, address) = (1,1)  # change this to your code
        # call  __sock352_get_packet() until we get a new conection
        # check the the connection list - did we see a new SYN packet?
        # This will implement the handshake protocol
        return (clientsocket,address)
  
    def close(self):   # fill in your code here
        # send a FIN packet (flags with FIN bit set)
        # remove the connection from the list of connections
        return

    def listen(self): #null code for part 1 
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
    # There is a differenct action for each packet type, based on the flags:
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
    '''
            chack the version number
            chacker the header length
            gth the flag settings
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
        '''
        pass
    