import os,time
from scapy.all import *
from threading import Thread

def sweep(ip):
	try:
		pakt=Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(hwdst='00:00:00:00:00:00',pdst=ip)
		result=srpl(pakt,timeout=1,verbose=0)
		if result:
			time.sleep(0.1)
			print(ip+'online')
			return
	except:
		return

for i in range(1,62):
	ip='10.31.7.'+str(i)
	threading.Thread(target=sweep,args=(ip,)).start()




# import sys
# from scapy.all import *
# from threading import Thread


# def scanHOST(IP_list):	#构造数据包并发送
#     pkt = Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(pdst=IP_list)		
#     sendp(pkt,verbose=False)		


# def is_host_live():		//捕捉数据包并过滤出指定条件的数据包确定主机是否存活
#     def arp_scan_callback(pkt):
#         if ARP in pkt and pkt[ARP].op is 2:			//如果捕捉的数据包有ARP层并且是op 参数为is-at,则确定主机存活
#             return pkt.sprintf("%ARP.hwsrc%\t%ARP.psrc%    is lived")
    
#     sniff(filter='arp', store=0,prn=arp_scan_callback,timeout=3)	//定义一个过滤器，只捕捉arp 数据包，并调用回调函数进行处理

# def main():
#     args = sys.argv
#     if len(args) != 2:   //如果接受的参数不是两个的话，则打印提示并退出
#         print('Usage: python arp_scan.py 192.168.10.0/24')
#         exit()

#     Thread(target=is_host_live).start()		//定义一个子线程并运行捕捉器函数
#     scanHOST(args[1])						//将参数传入扫描函数并运行

# if __name__ == '__main__':
#     main()
   



# from scapy.all import *
 
# if __name__ == "__main__":
#     netif = "vmnet8"  #net iface
#     ip_prefix = "10.31.7."
    
#     live_host = {}; 
 
#     for i in range(1,255):
#         ip_str = ip_prefix + str(i)
#         print("ip:",ip_str)
#         arp_req_pkt = Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ip_str)
#         arp_rsp_pkt = srp1(arp_req_pkt,iface=netif,timeout=0.01)
 
#         if arp_rsp_pkt != None:
#             live_host[arp_rsp_pkt.psrc] = arp_rsp_pkt.hwsrc
 
#     for key,value in live_host.items():
#         print(key,value)
