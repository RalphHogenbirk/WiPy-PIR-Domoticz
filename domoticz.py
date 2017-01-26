import socket
class Domoticz:
    
    def __init__(self, ip, port,  basic):
        self.basic = basic
        self.ip = ip
        self.port = port
    
    def setLight(self, idx, command):
        return self.sendRequest("type=command&param=switchlight&idx="+idx+"&switchcmd="+command)

    def setVariable(self, name, value):
        return self.sendRequest("type=command&param=updateuservariable&vtype=0&vname="+name+"&vvalue="+value)

    def sendRequest(self, path):
        try:
            s = socket.socket()
            s.connect((self.ip,self.port))
            s.send(b"GET /json.htm?"+path+" HTTP/1.1\r\nHost: pycom.io\r\nAuthorization: Basic "+self.basic+"\r\n\r\n")
            status = str(s.readline(), 'utf8')
            code = status.split(" ")[1]
            s.close()
            return code
            
        except Exception:
            print("HTTP request failed")
            return 0
