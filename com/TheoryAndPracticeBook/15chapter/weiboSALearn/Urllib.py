
import urllib;
import urllib.request

#response = urllib.request("http://www.baidu.com");
    #urlopen("http://www.baidu.com");
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
