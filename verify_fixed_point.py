#!/usr/bin/env python3
import logging
import sys
import collections
import random
import binascii

from not_des import *


def Compress(reader):
  """Davies–Meyer single-block-length compression function."""
  key = reader.read(KEY_SIZE)
  inp = reader.read(BLOCK_SIZE)
  output = Xor(DESEncrypt(inp, key), inp)
  return Block(key, inp, output)

def main():
  key = b'\x00' * KEY_SIZE
  inp = b'\x00' * KEY_SIZE
  print('E(0, 0)     = {}'.format(binascii.hexlify(DESEncrypt(inp, key))))

  inp = binascii.unhexlify('0f97040400000008')
  print('fixed point = {}'.format(binascii.hexlify(DESEncrypt(inp, key))))


if __name__ == '__main__':
  main()
