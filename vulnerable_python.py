import os
import pickle
import subprocess
import yaml

user_input = input("Enter command: ")

# Command Injection
os.system(user_input)

# Dangerous subprocess
subprocess.call(user_input, shell=True)

# Arbitrary code execution
eval(user_input)

# Arbitrary code execution
exec(user_input)

# Unsafe deserialization
data = pickle.loads(open("data.bin", "rb").read())

# Unsafe YAML loading
config = yaml.load(open("config.yml"), Loader=yaml.Loader)

# Weak randomness
import random
password_reset_token = random.randint(100000, 999999)

print(password_reset_token)
