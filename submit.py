from pwn import *
import binascii

r = remote('dm-col.ctfcompetition.com', 1337)

r.send('\x00' * 8)
r.send('\x00' * 8)

r.send('\x00' * 8)
r.send(unhex('7c0b7ee5a4b22be0'))

r.send('\x00' * 8)
r.send(unhex('0f97040400000008'))

print r.recvall()
