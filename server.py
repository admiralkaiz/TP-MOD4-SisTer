# TP MOD 4 Sistem Paralel dan Terdistribusi
# Topik: RPC (Remote Procedure Call)
# Filename  : server.py
# Author    : Kaisar Kertarajasa (1301213276)

# Import necessary modules
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Define RequestHandler class
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')

# Make a class for voting candidate
class Candidate:
    def __init__(self, 
                 leader='Anonymous', 
                 vice='Anonymous'
                 ):
        self.__leader = leader
        self.__vice   = vice
        self.__votes  = 0
    
    def getCandidate(self):
        return self.__leader, self.__vice

    def getVotes(self):
        return self.__votes

    def voteCandidate(self):
        self.__votes += 1
    
# Make a tuple of candidates
candidateList = (Candidate('Meikai', 'Fumika'),
                 Candidate('Shinya', 'Tomoe'))

# A function to process voter's choice
def vote(number=0):
    if number > 0 and number < len(candidateList)+1:
        candidateList[number-1].voteCandidate()
        return 'Thanks for voting!'
    else:
        return 'Please enter a valid candidate number'
    
# Show list of candidates to voter
def listCandidates():
    cout = ''
    cout += '=' * 30
    cout += '\n'
    if len(candidateList) < 1:
        cout += 'Sorry, no candidates applied!'
    else:
        num = 1
        cout += 'Applicable candidates:\n'
        cout += '=' * 30
        cout += '\n'
        for cand in candidateList:
            leader, vice = cand.getCandidate()
            cout += 'Candidate #' + str(num) + ": " + leader + " - " + vice + '\n'
            num += 1
    cout += '=' * 30
    cout += '\n'
    return cout
    
# In the server's screen, show voting result
def showResult():
    print('=' * 30)
    if len(candidateList) < 1:
        print('Voting is not applicable right now!')
        return 'Not voted!' # To be shown in voter's screen
    else:
        num = 1
        print("Results:")
        for cand in candidateList:
            leader, vice = cand.getCandidate()
            print('Candidate #{}: {} - {} \t\t --> Votes: {}'
                  .format(num, leader, vice, cand.getVotes()))
    print('=' * 30)
    return ''

# Main function
if __name__=='__main__':
    with SimpleXMLRPCServer(('127.0.0.1', 8888), requestHandler=RequestHandler) as server:
        server.register_introspection_functions()

        server.register_function(vote)
        server.register_function(listCandidates)
        server.register_function(showResult)

        server.serve_forever()
