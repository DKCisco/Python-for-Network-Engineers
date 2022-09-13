import pdb

def test_func(device, command):
    print(f"sending {command} to {device}")

pdb.set_trace()
test_func("R1", "show run")

