# Packets Primer 📦🚩

Platform: [PicoCTF](https://play.picoctf.org/)

## Description

Download the packet capture file and use packet analysis software to find the flag.

## Solution

A PACP (Packet Capture) file is given store raw network traffic data and communication.

[Wireshark](https://www.wireshark.org/) is the best packet capture analyser to see the network information such as ports, protocol and messages.

Open Wireshark and Open the PCAP file.

<img width="958" height="338" alt="image" src="https://github.com/user-attachments/assets/c24d4d98-46d2-4038-9204-a5db00067e4e" />

We see 4 network packets having information such as Protcol, Source and Destination IP Addresses and much more.

One unique thing is the S101 protocol at pacekt 4 as others are TCP to maintain the communication.

**Note**: The S101 protocol (s101) is a specialized transport protocol used to carry messages.

Click the Packet 4 to see additional information then you see the flag!

<img width="1906" height="802" alt="image" src="https://github.com/user-attachments/assets/ac183380-dde7-44ec-9880-04f99f56464c" />

The data is in hex format, if you wanna see in readable text format, you can right click to the packet 4, click Follow -> TCP Stream then you get the data.
