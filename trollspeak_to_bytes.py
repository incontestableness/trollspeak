#!/usr/bin/env python3

from shared import trollspeak, trollregex
import textwrap



message = input("Enter a message in trollspeak: ").upper()
if not trollregex.fullmatch(message):
	print(f"Your message can only contain the following letters (no spaces): {trollspeak}")
	exit(1)


bitstring = ""
hexstring = "0x"
for char in message:
	index = trollspeak.find(char)
	bitstring += bin(index)[2:].zfill(4)
	hexstring += hex(index)[2:].upper()

intstring = ", ".join([str(int(nybble, 2)) for nybble in textwrap.wrap(bitstring, 4)])
print(f"Bitstring: {bitstring}\nHexstring: {hexstring}\nIntstring: {intstring}")
print(f"Your message is {len(message)} letters/nybbles, represented as {len(message)/2} bytes.")
