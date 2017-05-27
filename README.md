# Socket-To-Me
Term Project for CS 352 - Internet Technology.
Extends the basic UDP socket to provide more functionality.

Requirements
------------
python 2.7.x with certain libraries (os, socket, nacl)
Specific instructions and execution parameters are detailed in the individual parts' project descriptions.

Part 1
------
Implemented a handshake policy for setting up and tearing down connections along with a basic Go-Back-N policy for packets that exceed the size of the `recv()` or `send()` function calls.

Part 2
------
Implemented encryption by using the [NaCl](http://nacl.cr.yp.to/features.html) library for encrypting packet payloads.

Part 3
------
Implemented windowing to increase performance of data transmission.
