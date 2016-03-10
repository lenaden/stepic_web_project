import socket
import threading
def servCycle():
    while True:
        data = conn.recv(SIZE)
        if data == 'close': break
        conn.send(data)
    conn.close()
if __name__ == '__main__':
    IP = '0.0.0.0'
    PORT = 2222
    SIZE = 1024
    COUNT = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen(COUNT)
    while True:
        conn, addr = s.accept()
        for i in range(COUNT):
            t = threading.Thread(target=servCycle, args=(conn, ))
            t.start()