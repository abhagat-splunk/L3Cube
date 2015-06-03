import dpkt,os

counter=0
ipcounter=0
tcpcounter=0
udpcounter=0
arpcounter=0
httpcounter=0
filename = raw_input("Enter the file name: \n>")

for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):

    counter+=1
    eth=dpkt.ethernet.Ethernet(pkt)    
    #print "start"
    if eth.type==dpkt.ethernet.ETH_TYPE_ARP:  
       arpcounter+=1
       hlen = eth.arp.hln
       operation = eth.arp.op
       src_pa =  eth.arp.spa
       f1 = open("arp_packets.txt","a")
       f1.write("Hardware Length: "+str(hlen)+'\n')
       if operation==1:
            added = "Request"
       else:
            added = "Reply"    
       f1.write("Operation Type: "+added+'\n')
       f1.write("Protocol Address Length: "+str(eth.arp.pln)+'\n')
       #f1.write("Source Protocol Address: "+(src_pa)+'\n')
       #f1.write("Destination Protocol Address: "+str(eth.arp.tpa)+'\n\n')
       #print "HEEREEE"
       #os.system(str(eth.arp.sha)>"xyz.txt")
       b = list(str(src_pa))
       a = []
       for element in b:
          #print element
          a.append(str(ord(element)))
          a.append('.')
       a = a[:-1]
       f1.write("Source Protocol Address: " +''.join(a)+"\n")
       b = list(str(eth.arp.tpa))
       a = []
       for element in b:
          #print element
          a.append(str(ord(element)))
          a.append('.')
       a = a[:-1]
       f1.write("Destination Protocol Address: " +''.join(a)+"\n\n")
       #f1.write("Destination Hardware Address: "+str(eth.arp.tha)+'\n')  
       f1.close()
    #print "end"   
    if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
      continue
    x = eth.data
    y = x.data
    try: 
    	if y.sport == 80:
    		httpcounter+=1
    		#print httpcounter
        	#http1 = dpkt.http.Request(y.data)
        	http2 = dpkt.http.Response(y.data)
        	#print http1.headers
        	f1 = open("HTTP_Response.txt","a")
        	f1.write("Headers: "+str(http2.headers)+"\n")
        	f1.write("Body: "+str(http2.body)+"\n")
        	f1.write("Version: "+str(http2.version)+"\n\n")	
        	f1.close()
        	#print "YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"	
        	
        	#print http2.method
        	# print str(dpkt.http.Reply.reason)
        	# print str(dpkt.http.Reply.body)
        	
        	# print dpkt.http.Request.body
        	# print str(dpkt.http.Request.headers)
        	# print dpkt.http.Request.method
        	# print dpkt.http.Request.uri
        	# print dpkt.http.Request.version
    except:
    	pass
    try:
    	f2 = open("HTTP_Request.txt","a")
        http=dpkt.http.Request(y.data)
        if str(http.method)=="GET":
        	f2.write("Method is GET, therefore no body.\n")
        else:
        	f2.write("Body: "+str(http.body)+"\n")
        f2.write("Headers: "+str(http.headers)+"\n")
        f2.write("URI: "+str(http.uri)+"\n")
        f2.write("Method: "+str(http.method)+"\n")
        f2.write("Version: "+str(http.version)+"\n\n")
    	f2.close()
    except:
        pass	
    try:
    	ip=eth.data
    	ipcounter+=1
    	if ip.p==dpkt.ip.IP_PROTO_TCP: 
    	   tcpcounter+=1
    	   f1 = open("tcp_packets.txt","a")
    	   f1.write("TCP sequence number: "+str(ip.data.seq)+'\n')
    	   f1.write("Acknowledgement number: "+str(ip.data.ack)+"\n")
    	   f1.write("TCP header size in bytes: "+str(ip.data.off*4)+'\n')
    	   f1.write("Source Port Number: "+str(ip.data.sport)+'\n')
    	   f1.write("Destination port number: "+str(ip.data.dport)+'\n\n')    
    	   f1.close()
    except:
    	pass	   
print "Total number of packets in the pcap file: ", counter
print "Total number of ip packets: ", ipcounter
print "Total number of tcp packets: ", tcpcounter
print "Total number of arp packets: ",arpcounter
print "Total number of http packets: ",httpcounter
