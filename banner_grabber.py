import socket

def banner_grabber(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target, port))
        banner = s.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return str(e)
    finally:
        s.close()

if __name__ == "__main__":
    # url = input("Enter a url: ")
    target = "128.199.26.61"
    port = 22
    print(f"banner from {target}:{port} - {banner_grabber(target, port)}")