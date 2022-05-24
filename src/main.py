print("__main__ started")
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

def read_sensor() -> dict:
    bme = BME280(i2c=i2c)
    return dict(temperature = str(bme.temperature), humidity = str(bme.humidity), pressure = str(bme.pressure))

def get_web_page(filepath:str):
    with open(filepath, 'r') as f:
        html = f.read()
    data = read_sensor()
    data["refresh_rate"] = str(10)
    return html.format(**data)

def web_server():
    s = socket.socket()
    s.bind(('', 80))
    s.listen(5)
    return s

def main():
    ser = web_server()
    while True:
        try:
            if gc.mem_free() < 102000:
                gc.collect()
            conn, addr = ser.accept()
            print("Connection is setting up...")
            conn.settimeout(3.0)
            print(f"Got a connection from {str(addr)}")
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            print(f"Content = {request}")
            filepath = "status_page.html"
            response = get_web_page(filepath)
            conn.send("HTTP/1.1 200 OK\n")
            conn.send("Content-Type: text/html\n")
            conn.send("Connection: close\n\n")
            conn.sendall(response)
            conn.close()
        except (OSError, KeyboardInterrupt) as e:
            conn.close()
            print("Connection unexpectedly closed")
            print(f"Reason: {e}\n")

main()
