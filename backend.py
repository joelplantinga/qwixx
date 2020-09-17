import random
from throw import throw


def ran():
    return random.randint(0, 6)

def newThrow(id, player, totPlay):
    if id == -1:
        # print(throw(0, 1, ran(), ran(), ran(), ran(), ran(), ran() ))
        return throw(0, 1, ran(), ran(), ran(), ran(), ran(), ran() )
    else:
        # print(throw(id+1, ((player+1)%totPlay)+1 , ran(), ran(), ran(), ran(), ran(), ran() ))
        return throw(id+1, (player+1)%totPlay+1 , ran(), ran(), ran(), ran(), ran(), ran() )
