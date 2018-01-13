# -- coding: utf-8 --
import socket

obj = socket.socket()

obj.connect(("120.76.246.20",38411))
#ret_bytes = obj.recv(1024);
#print ret_bytes;
#ret_str = str(ret_bytes);
#print("接收到的数据是: %s" % (ret_str));



while True:
    #inp = input("你好请问您有什么问题？ \n >>>")
    #print "输入的内容是: %s" % (inp);
    inp = '{"api":"socket_client_connect_wrcs","data":{"uuid":"10001","co":"wrcs","timestamp":"1234567890","pwd":"5cdebd47afa6e09e30edb496c08b9896"}}\n';
    print "发送的内容是:%s" % (inp);
    if inp == "q":
        obj.sendall(bytes(inp))
        break
    else:
        obj.sendall(bytes(inp))
        ret_bytes = obj.recv(1024)
        ret_str = str(ret_bytes)
        print("------->接收到的数据是: %s" % (ret_str));