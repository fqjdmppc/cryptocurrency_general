import eth_keys
import random
target_prefix = '123456' # [0~9, a~f] case-insensitive. length < 7 or wait forever
target_prefix = target_prefix.lower()
total_possibility = 16 ** len(target_prefix)
counter = 0
while 1:
	pk = random.randint(1 << 255, (1<<256) - 1)
	addr = eth_keys.keys.PrivateKey(b''.fromhex(hex(pk)[2:])).public_key.to_checksum_address()
	if addr[2: 2 + len(target_prefix)].lower() == target_prefix:
		print(hex(pk), addr)
		break
	else:
		counter += 1
		if not counter % 0xfff:
			print("%d keys tried. Probability : %.2f%%" % (counter, counter * 100.0 / total_possibility))