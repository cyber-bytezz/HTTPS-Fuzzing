#HTTP FUZZING

#ITS AND FUZZING LIBIRAIES

#REQUEST USED FOR FUZZING

from sully import *

#REQUEST GETS FROM (GET,BODY,POST) HTTP 1.1

s_initialize("HTTP BASIC")

s_group("verbs", values=["GET","HEAD","POST","TRACE"])

if s_block_start ("body","group","trace")

#HERE ARE THE REQUEST

s_delim("")
s_delim("/")
s_string("index.html")
s_delim(" ")
s_string("HTTP")
s_delim("/")
s_string("1")
s_delim(".")
s_string("1")

s_static("/r/n/r/n")

s_block_end("body")