---
layout: toc
permalink: /j/6
---
*View all the videos from this unit a [single playlist on youtube](https://youtube.com/playlist?list=PLnVRBITSZMSMAnMTQ5Lh5kXGW6Ofjb1uD)*
# Networking

##  What is the internet?

The **Internet** by definition is a network of networks composed of computers. As a non-technical term, we use the term Internet as a catchall for all connected computers, but in technical terms, it is just one part of a larger ecosystem of networks and protocols that enable the sharing of information.

This is not a class on networking or the internet, but the ability to communicate over a network is an integral part of modern programming that fits nicely within the OOP models of IO we've been discussing with Java so far. But, to really understand network programming, you have to first have a decent understanding of the protocols that underly the Internet, and one thing you learn quickly about network programming is that the protocol is king. Understanding the protocols is will make you a better programmer. 

### Packet Switching

The internet is a **packet switched** network. A packet is defined as follows: 
 
<img src="/images/network-packet.png" alt="Networking Packet"
width="80%"
style="display: block;
margin-left: auto;
margin-right: auto;"/>
 
All packets have a header, which stores the address or destination of a packet, and a payload which stores the data or message of the packet. The switching part of packet switching is that at network devices, like routers and switches, the packet arrives, and based solely on the header of the packet, the device knows where to send the data next. There are no pre-defined routs for data but the protocols ensure that the next hop in the path to the destination can be determined. As you might imagine, in such a model, addressing becomes very important. 

<font color="red"><b>PAUSE: Let's work on Q1 in the worksheet together now (one minute)</b></font>

### The TCP/IP Protocol Stack

The Internet is modelled as a protocol stack where each protocol defines a different interaction layer. Information flows up and down the protocol stack, and at each layer, a different protocol comes to bare for forwarding the packet onward to the next hop. 


<img src="/images/network-osi.png" alt="Networking Stack"
width="80%"
style="display: block;
margin-left: auto;
margin-right: auto;"/>


Each layer has different goal in mind. Starting with the physical layer, the main purpose is to actually transmit 1's and 0's over medium, like a wire. The link layer adds protocols for how the medium is shared across many connected devices, as well as error correction. An example of protocols on the link layer is ethernet or wifi.

The internet and transport layer of are particular interest in this class because you will interact directly with these protocol through their addressing schemes. The purpose of the internet layer is to inter-connect networks; for example,e GW has a network, and if you want to send data to Google, your packets must traverse GW network and potentially many other federated networks before finally reaching a server at Google. The internet layer both describes the protocols for how networks inter connect with each other and the way that computers are identified, via the internet protocol address or ip address.

At a certain point, though, two processes running on different computers are actually sending and receiving data across the vastness of the Internet. The transport layer provides an abstraction for those two process to apear as if they are communicating directly with each other. Since many process can be communicating on the network at the same time, the transport layer also provides a mechanism, called ports, to differentiate communication destined for one process versus another.

Finally, at the application layer, additional protocols are available depending on the task at hand. For example, SMTP is used to transmit email messages and HTTP is used to download web content and BitTorrent is used to pirate music and videos :) From a generic programmers perspective, the application layer is the domain where we get to choose what data is sent and received and how that data is interpreted; the systems programming perspective also concerns itself with system calls that enable that communication. 

<font color="red"><b>PAUSE: Let's work on Q2-Q4 in the worksheet together now (five minutes)</b></font>

## Internet Addressing

Each layer has its own addressing scheme and information needed to perform routing/switching. This information is traditionally encoded within the header of the packet. There are two key addressing systems that we will use in this class, ip addresses and ports. Additionally, we also refer to computers by name, a domain name, which must be translated into an address. 

### IP Addresses

An ip address is a 4-byte/32-bit number in Version 4 of TCP/IP protocol. We usually represented in a dotted quad notation: 

```
     4-bytes
 _____________
/             \
192.168.128.101
\_/
 |
1 byte
```

A byte is 8-bits, and thus can represent numbers between 0-255, which is why ip addresses do not have numbers greater than 255. The ip address is hierarchical where bytes to the left are more general while bytes to the right are more specific. Based on a subset of the bytes, routers can determine where to send a packet next. 

### Domain Names and Hosts



While IP addresses are somewhat usable, it is quite a burden to memorize the ip address of all the computers we might want to vist on the web. For exampel, while I might know the ip address of a single computer off hand, e.g., "10.53.37.142" is the ip address of a lab machine, I can't recall the ip address of Google or Facebook or much of anything else.

Instead, we use domain names to identify a networked device. A hostname, is a dotted string of names, usually ending in the canonical .com or .org or .edu or .gov or etc. For example, the domain name for Google is google.com, but the Internet does not function on domain names. It needs IP addresses. A separate protocol called the Domain Name Service or DNS is tasked with converting domain names into IP addresses.


We can access the DNS system on Unix through the host command. For example, suppose we wanted to learn the IP address of google.com: 

```
#> google.com
google.com has address 74.125.228.110
google.com has address 74.125.228.103
google.com has address 74.125.228.96
google.com has address 74.125.228.99
google.com has address 74.125.228.104
google.com has address 74.125.228.101
google.com has address 74.125.228.102
google.com has address 74.125.228.97
google.com has address 74.125.228.100
google.com has address 74.125.228.105
google.com has address 74.125.228.98
google.com has IPv6 address 2607:f8b0:4004:803::1003
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
```

The output may not be what you expect. There are many, many different IP addresses available to server google.com, and this is by intention to balance the load of request across multiple machines. In fact, every time you rerun host, you'll find that you get a different set of IP address: 

```
#> host google.com
google.com has address 74.125.228.104
google.com has address 74.125.228.101
google.com has address 74.125.228.102
google.com has address 74.125.228.97
google.com has address 74.125.228.100
google.com has address 74.125.228.105
google.com has address 74.125.228.98
google.com has address 74.125.228.110
google.com has address 74.125.228.103
google.com has address 74.125.228.96
google.com has address 74.125.228.99
google.com has IPv6 address 2607:f8b0:4004:803::1003
google.com mail is handled by 50 alt4.aspmx.l.google.com.
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
```

If we were to query a less used domain name, one that isn't serving as much traffic as google, we get IP addresses that are a bit more sane. For example, let's see what the IP addresses are for `www.cs.gwu.edu`:

```
 $ host www.cs.gwu.edu
www.cs.gwu.edu is an alias for www2old.gwu.edu.
www2old.gwu.edu has address 161.253.128.45
```

Interesting, you can see that `www.cs.gwu.edu` is an alias for another domain `www2old.gwu.edu`, which in turn has a stable IP address `161.253.128.45`. 

<font color="red"><b>PAUSE: Let's work on Q5 in the worksheet together now (two minutes)</b></font>

### Ports


The last bits of addressing relevant to this class is the port address. While the IP address is used to deliver packets to a destination computer, the port address is used to deliver the packets on the computer to the right process. Consider that a single computer all share the same IP address, there are many different applications using that connection at the same time. You might have multiple web pages open with email and playing games and etc, each of those interactions is performed by a separate process but all the data arrives at the computer through a single point.

The port address is a way for the Operating System to divide up the data arriving from the network based on the destination process. Additionally, ports tend to be tightly coupled with applications. For example, to initiate a HTTP connection for web browsing, you connect using port 80; to initiate a secure shell connection with ssh, you connect using port 22; and, to initiate a connection to send email, you connect using port 25, and so on. What makes ports important is that all those services, web server, ssh, and email, can all be running on the same computer. The ports allows the operating system differentiate traffic for each application.

<font color="red"><b>PAUSE: Let's work on Q6 in the worksheet together now (one minute)</b></font>

## Client/Server Model

Most interactions of applications are dictated by the client-server model. In this model there exists clients who are requesting a services for a server. 



<img src="/images/network-client-server.png" alt="Client Server Diagram"
width="60%"
style="display: block;
margin-left: auto;
margin-right: auto;"/>

In the model, we describe clients as connecting to servers and servers listening to incoming connections. When a connection is established, or data is received, the server replies to the client with data as required by the application protocol.

While this class will focus on the client server model, there are other models of network interaction. For example, the peer-to-peer model is when clients act as both client and servers. This is common for many distributed systems, such as BitTorrent or Skype. 
 

## Socket Programming in Java


Now that you have a good idea of how networking works, we turn our attention to how Java enables access to networking API. At this point, it shouldn't surprising you that this occurs via Objects and that it fits into an already established framework of I/O. That means communicating over the network in a programmatic way is similar to read/writing to files, except the endpoint is not a file, but rather a remote computer.

Java divides socket programming into server and client programming. There are two main classes

* [Socket](https://docs.oracle.com/javase/8/docs/api/java/net/Socket.html)

* [ServerSocket](https://docs.oracle.com/javase/8/docs/api/java/net/ServerSocket.html)

We'll review using both below. And if you want more information, Oracle offers a nice [tutorial](https://docs.oracle.com/javase/tutorial/networking/sockets/index.html) of using sockets

### The `Socket` class

In Java, the `Socket` class is used as the **client** socket in a two-way communication with a **server**. Key to this idea is that the socket is *connected* to the server at a ipaddress/host and port. The main constructor you'll use is

```java
Socket(String host, int port); 
//Creates a TCP stream socket and connects 
//it to the specified port number on the named host. 
```

> Note that all `Socket`s in java are TCP (SOCKSTREAM) sockets, if you want to use a different socket type, you'll need to use one of the other socket classes, like `DatagramSocket`. 

Importantly, the `Socket` is to connect to the server, but communication with the server is a two-way procedure. So once we connect to the server, we can *both* read and write to the socket via the socket's `InputStream` and `OutputStream`. And like with other I/O we can wrap those streams in other buffered readers/writers.

Let's start with a "Hello World" example of a client connecting to a server and writing "Hello World". Our basic program looks like the following

```java
import java.util.*;
import java.net.*;
import java.io.*;

public class HelloSocket{

    public static void main(String args[]){

        Socket sock=null;        
        try{
           sock = new Socket("localhost",2021);
        }catch(Exception e){
            System.err.println("Cannot Connect");
            System.exit(1);
        }

        try{
            PrintWriter pw = new PrintWriter(sock.getOutputStream());
            pw.println("HelloWorld");
            pw.close(); //close the stream
            sock.close();//close the socket
        }catch(Exception e){
            System.err.print("IOException");
            System.exit(1);
        }

    }
}
```

Note that we need the try/catch blocks because there are a number of errors that can occur when dealing with I/O. 
The socket is two-way, so we can also "read" for input after having written to the socket. This is a small expansion of the above program 

```java
        try{
            PrintWriter pw = new PrintWriter(sock.getOutputStream());
            pw.println("HelloWorld");
            pw.flush(); //flush the output (recall PrintWriters buffer)

            
            BufferedReader in =
                new BufferedReader(
                         new InputStreamReader(sock.getInputStream()));

            String reply = in.readLine();//read a line from ther server
            System.out.println("Server said: "+reply);

            
            pw.close(); //close the stream
            in.close();//close the input stream
            sock.close();//close the socket
        }catch(Exception e){
            System.err.print("IOException");
            System.exit(1);
        }
```

Now when we run the program, we can type input after "HelloWorld" which get's written to our client. 

<font color="red"><b>PAUSE: Let's work on Q7-Q8 in the worksheet together now (one minute)</b></font>

### The `ServerSocket` class

The server side of this works pretty much like the client side, except for an additional step of the server needing to *accept* an incoming connect. The key class is the `ServerSocket` which we initialize like so

```java
 ServerSocket serverSocket = new ServerSocket(portNumber);
```

The `portNumber` is which port we want to be listening for on an incoming connection.  Once the `serverSocket` is established we call `accept()`, which returns a new `Socket` that is used to communicate with that client. 

```java
    Socket clientSocket = serverSocket.accept();
```

Importantly, the server socket can accept more connections from other client sockets. That is why a new socket is created for each client. 

To demonstrate this, we want to create a "Hello World" server that writes "Hello World" every time you connect to it. We put the accept call in a loop.

```java
import java.util.*;
import java.net.*;
import java.io.*;

public class HelloServer{

    public static void main(String args[]){

        ServerSocket serverSock=null;
        
        try{
           serverSock = new ServerSocket(2021);
        }catch(Exception e){
            System.err.println("Cannot open server socket");
            System.exit(1);
        }

        try{

            while(true){
                Socket clientSock = serverSock.accept();

                System.out.println("Connection from: "+clientSock.getRemoteSocketAddress());
                
                PrintWriter pw = new PrintWriter(clientSock.getOutputStream());
                pw.println("Hello World");

                
                pw.close(); //close the stream
                clientSock.close();//close the socket

                //loop and get the new connection
            }
        }catch(Exception e){
            System.err.print("IOException");
            System.exit(1);
        }

    }
}
```

Note that we can easily see who is connecting to the server by retrieving the remote socket address and print that out. 

Each connection comes from `127.0.0.1`, which is the IP address used when connecting within a single localhost computer. Also note that the port changes each time, that's because once the connection is established, the server is still listening on the original port `2021`, so this new connection should use a different port

<font color="red"><b>PAUSE: Let's work on Q9 in the worksheet together now (one minute)</b></font>

### Threaded Echo Socket Server

The final step in programming a sockets is to consider the threaded socket server. A threaded socket server starts a new thread for each thread so that the main thread can continue to listen to incoming connections. To understand why this would be needed, consider that in the example above that while the server is printing to the client, another client may be queued to connect. In this example, this is probably fine because the action the server does is somewhat complex, but let's consider a more complex server that echos back to the client anything written to the socket until the client closes the socket.


You should be able to trace the function of this program now ... 

```java
import java.util.*;
import java.net.*;
import java.io.*;


public class EchoSocketServer{

    ServerSocket serverSock;

    public EchoSocketServer(int port){

        try{
            serverSock = new ServerSocket(port);
        }catch(Exception e){
            System.err.println("Cannot establish server socket");
            System.exit(1);
        }
        
    }

    public void serve(){

        while(true){
            try{
                //accept incoming connection
                Socket clientSock = serverSock.accept();
                System.out.println("New connection: "+clientSock.getRemoteSocketAddress());
                
                //start the thread
                (new ClientHandler(clientSock)).start();
                
                //continue looping
            }catch(Exception e){} //exit serve if exception
        }
    }

    private class ClientHandler extends Thread{

        Socket sock;
        public ClientHandler(Socket sock){
            this.sock=sock;
        }

        public void run(){
            PrintWriter out=null;
            BufferedReader in=null;
            try{
                out = new PrintWriter(sock.getOutputStream());
                in = new BufferedReader(new InputStreamReader(sock.getInputStream()));

                //read and echo back forever!
                while(true){
                    String msg = in.readLine();
                    if(msg == null) break; //read null, remote closed
                    out.println(msg);
                    out.flush();
                }

                //close the connections
                out.close();
                in.close();
                sock.close();
                
            }catch(Exception e){}

            //note the loss of the connection
            System.out.println("Connection lost: "+sock.getRemoteSocketAddress());
        }

    }

    public static void main(String args[]){
        EchoSocketServer server = new EchoSocketServer(2021);
        server.serve();
    }
       
    
}
```

> On your own, can you write an EchoClient and connect it to the server so that they go back and forth for ever!!!

<font color="red"><b>PAUSE: Let's work on Q10 in the worksheet together now (one minute)</b></font>
