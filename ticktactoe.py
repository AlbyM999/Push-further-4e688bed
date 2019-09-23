#! python3
#tick tak toe
#imports
import random
#AIvar
AIlayers = ['t','m','l']
AIsides = ['L','M','R']
#boardlist
theboard = {'topL':' ','topM':' ','topR':' ','midL':' ','midM':' ','midM':' ','midR':' ','lowL':' ','lowM':' ','lowR':' '}
#functions
def printboard():
    print(theboard['topL']+ '|'+ theboard['topM']+'|'+ theboard['topR'])
    print(theboard['midL']+ '|'+ theboard['midM']+'|'+ theboard['midR'])
    print(theboard['lowL']+ '|'+ theboard['lowM']+'|'+ theboard['lowR'])
def boardcheck():
    #horizontaal
    if theboard['topL'] == 'X' and theboard['topM'] == 'X' and theboard['topR'] =='X':
        print('you win')
    elif theboard['midL'] == 'X' and theboard['midM'] == 'X' and theboard['midR'] =='X':
        print('you win')
    elif theboard['lowL'] == 'X' and theboard['lowM'] == 'X' and theboard['lowR'] =='X':
        print('you win')
    #verticaal
    elif theboard['topL'] == 'X' and theboard['midL'] == 'X' and theboard['lowL'] =='X':
        print('you win')
    elif theboard['topM'] == 'X' and theboard['midM'] == 'X' and theboard['lowM'] =='X':
        print('you win')
    elif theboard['topR'] == 'X' and theboard['midR'] == 'X' and theboard['lowR'] =='X':
        print('you win')
    #schuin
    elif theboard['topL'] == 'X' and theboard['midM'] == 'X' and theboard['lowR'] =='X':
        print('you win')
    elif theboard['topR'] == 'X' and theboard['midM'] == 'X' and theboard['lowL'] =='X':
        print('you win')
def AIboardcheck():
    #horizontaal
    if theboard['topL'] == 'O' and theboard['topM'] == 'O' and theboard['topR'] =='O':
        print('you lose')
    elif theboard['midL'] == 'O' and theboard['midM'] == 'O' and theboard['midR'] =='O':
        print('you lose')
    elif theboard['lowL'] == 'O' and theboard['lowM'] == 'O' and theboard['lowR'] =='O':
        print('you lose')
    #verticaal
    elif theboard['topL'] == 'O' and theboard['midL'] == 'O' and theboard['lowL'] =='O':
        print('you lose')
    elif theboard['topM'] == 'O' and theboard['midM'] == 'O' and theboard['lowM'] =='O':
        print('you lose')
    elif theboard['topR'] == 'O' and theboard['midR'] == 'O' and theboard['lowR'] =='O':
        print('you lose')
    #schuin
    elif theboard['topL'] == 'O' and theboard['midM'] == 'O' and theboard['lowR'] =='O':
        print('you lose')
    elif theboard['topR'] == 'O' and theboard['midM'] == 'O' and theboard['lowL'] =='O':
        print('you lose')
def AI():
    AIlayer = (random.choice(AIlayers))
    AIside = (random.choice(AIsides))
    print(AIlayer)
    print(AIside)
    if AIlayer == 't':
        if AIside == 'L':
            theboard['topL'] = 'O'
        elif AIside == 'M':
            theboard['topM'] = 'O'
        elif AIside == 'R':
            theboard['topR'] = 'O'
    elif AIlayer == 'm':
        if AIside == 'L':
            theboard['midL'] = 'O'
        elif AIside == 'M':
            theboard['midM'] = 'O'
        elif AIside == 'R':
            theboard['midR'] = 'O'
    elif AIlayer == 'l':
        if AIside == 'L':
            theboard['lowL'] = 'O'
        elif AIside == 'M':
            theboard['lowM'] = 'O'
        elif AIside == 'R':
            theboard['lowR'] = 'O'
        else:
            AI()
def playerinput():
    layer = input('layder')
    side = input('side')
    if layer == 'top':
        if side == 'L':
            theboard['topL'] = 'X'
        elif side == 'M':
            theboard['topM'] = 'X'
        elif side == 'R':
            theboard['topR'] = 'X'
    elif layer == 'mid':
        if side == 'L':
            theboard['midL'] = 'X'
        elif side == 'M':
            theboard['midM'] = 'X'
        elif side == 'R':
            theboard['midR'] = 'X'
    elif layer == 'low':
        if side == 'L':
            theboard['lowL'] = 'X'
        elif side == 'M':
            theboard['lowM'] = 'X'
        elif side == 'R':
            theboard['lowR'] = 'X'
        else:
            playerinput()
#loop
while True:
    boardcheck()
    AIboardcheck()
    printboard()
    playerinput()
    AI()
        
        



