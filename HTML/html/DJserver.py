import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8800))
sock.listen(5)

while 1:
    print("server waiting......")
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("data",data)
    # 读取html文件r
    with open(r"HTML\login.html", "rb") as f:
        data = (f.read()).encode('utf-8')
    conn.send("HTTP/1.1 200 OK\r\nconten-type:text\r\n\r\n%s"%data)
    conn.close()