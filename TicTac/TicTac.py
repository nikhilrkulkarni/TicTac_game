from datetime import time
import time
import logging,configparser

def game(participant,avail_plots,n,m):   
    '''This function has the core logic of the game. 
    '''
    #print('-----------------------Welcome to TicTac-----------------\n')
    #print('--------------------------TicTac-------------------------\n')
    #print('---------------------------------------------------------\n')
    print('Score by A:',n)
    #logging.basicConfig(filename='info.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    #logging.info('Score by A:',n)
    logging.info('{}'.format('Score by A:'))
    print('Score by B:',m)
    #logging.info('Score by B:',m)
    logging.info('{}'.format('Score by B:'))
    if len(n) != 0 and len(m) != 0 and len(avail_plots) <= 4:
        if sum(n)%3 == 0:
            print("A WON THE GAME !!!") 
            logging.info('A WON THE GAME !!!')
            return
        elif sum(m)%3 == 0:
            print("B WON THE GAME!!!")
            logging.info('B WON THE GAME !!!')
            return
        if sum(n)%3 != 0 or sum(m)%3 !=0:
            print('CLOSE THE GAME! NOBODY WILL WIN!!!')
            logging.info('CLOSE THE GAME! NOBODY WILL WIN!!!')
            return
    if len(avail_plots) == 1:
        input('Last Move:')
        return 
    print('Available Plots for Participant',participant,':',avail_plots)
    if participant == 'A':
        while True:
            try:
                a = int(input('Move by Participant A:'))
                if a in avail_plots:
                    break
                else:
                    raise Exception('PLEASE ENTER A NO WITHIN AVAILABLLE NOS')
                    logging.info('PLEASE ENTER A NO WITHIN AVAILABLLE NOS')
            except Exception as e:
                print('PLEASE ENTER A NO WITHIN AVAILABLLE NOS') 
                logging.info('PLEASE ENTER A NO WITHIN AVAILABLLE NOS')
        n.append(a)
        avail_plots.remove(a)
        
        game('B',avail_plots,n,m)
    else:
        while True:
            try:
                b = int(input('Move by Participant B:'))
                if b in avail_plots:
                    break
                else:
                    raise Exception('PLEASE ENTER A NO WITHIN AVAILABLLE NOS')
                    logging.info('PLEASE ENTER A NO WITHIN AVAILABLLE NOS')
            except Exception as e:
                print('PLEASE ENTER A NO WITHIN AVAILABLLE NOS')
                logging.info('PLEASE ENTER A NO WITHIN AVAILABLLE NOS')
        m.append(b)
        avail_plots.remove(b)
        game('A',avail_plots,n,m)

def main():
    logging.basicConfig(filename='info.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    print('-----------------------Welcome to TicTac-----------------\n')
    print('--------------------------TicTac-------------------------\n')
    print('---------------------------------------------------------\n')

    participant = 'z'
    avail_plots = list(range(9))
    n = [] #Moves of 'A'
    m = [] #Moves of 'B'
    game('A',avail_plots,n,m)

if __name__ == '__main__':
    main()
