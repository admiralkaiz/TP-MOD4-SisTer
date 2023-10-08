# TP MOD 4 Sistem Paralel dan Terdistribusi
# Topik: RPC (Remote Procedure Call)
# Filename  : client.py
# Author    : Kaisar Kertarajasa (1301213276)

# Import necessary module
import xmlrpc.client

# Start proxy
s = xmlrpc.client.ServerProxy('http://127.0.0.1:8888')

# Show candidate list to be voted
# Client acts as the voter
print(s.listCandidates())

# Receive input from client (voter), then send choice to the server
choice = int(input('Select candidate: '))
print(s.vote(choice))

# Done, result is shown in server's screen
print(s.showResult())
