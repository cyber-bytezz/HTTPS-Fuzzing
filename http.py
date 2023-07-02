 from sulley import *

# Get user input for target IP address and port
target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port: "))

# Create a new session
sess = sessions.session()

# Define the target
target = sessions.target(target_ip, target_port)

# Define the protocol
sess.add_target(target)
sess.connect(s_get("HTTP BASIC"))

s_initialize("HTTP BASIC")

s_group("verbs", values=["GET","HEAD","POST","TRACE"])

if s_block_start ("body","group","trace"):
    s_delim("")
    s_delim("/")
    s_string("index.html")
    s_delim(" ")
    s_string("HTTP")
    s_delim("/")
    s_string("1")
    s_delim(".")
    s_string("1")

s_static("\r\n\r\n")

s_block_end("body")
