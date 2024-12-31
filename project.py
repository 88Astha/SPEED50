import curses

from curses import wrapper
import time
import requests



def welcome_screen(stdscr):
    stdscr.clear()
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    stdscr.addstr("\t~~~~~~~~~Welcome to SPEED-TYPE50!!~~~~~~~~~~~~",curses.color_pair(4))
    stdscr.addstr("\n\t\t ** Press any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def display50(stdscr, t, test, wpm = 0):

#    stdscr.clear()
    stdscr.addstr(t)
    stdscr.addstr(1,0, f"\n\n\n WPM: {wpm}")

    for i, ch in enumerate(test):

        try:
            correct_ch = t[i]
        except IndexError:
            break

        if len(t) < len(test):
            break
       
        elif ch != correct_ch:
            color = curses.color_pair(2)
        else: 
            color = curses.color_pair(1)

        stdscr.addstr(1, i, ch, color) # trynaa change 0 to 1



def speed50(stdscr):


    api_url = 'https://api.api-ninjas.com/v1/quotes?happiness={}'
    response = requests.get(api_url, headers={'X-Api-Key': 'qBrcglZZBWP2A+QtEt1N6g==5tckRryc1zJKmMw3'})
    if response.status_code == requests.codes.ok:
        x = (response.text)

        l = x.split(":")
  
        t_text = l[1][1:-10]
    else:
        print("Error:", response.status_code, response.text)


    #t_text = "HELLO WELCOME TO THE GAME... THIS IS A TEST LET THE GAMES BEGIN!"
    
    test_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while 1:

        time_elapsed = max(time.time() - start_time , 1)
        wpm = round((len(test_text) / (time_elapsed / 60))/5)
        stdscr.clear()
        display50(stdscr, t_text, test_text, wpm)
        stdscr.refresh()


        if "".join(test_text) == t_text:
            stdscr.nodelay(False)
            break


        try:
            key = stdscr.getkey()
        except:
            if len(test_text) < len(t_text):
                continue
            else:
                break
     
        #stdscr.addstr(t_text)

#        for t in test_text:
#           stdscr.addstr(t, curses.color_pair(1)) 
        

        

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\x7f", '\b'):
            if len(test_text) > 0:
                test_text.pop()
        elif len(test_text) < len(t_text):
            test_text.append(key)
        else:
            stdscr.addstr("\n")
            break




def main(stdscr):




    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
  

    welcome_screen(stdscr)

    while 1:
        speed50(stdscr)
        stdscr.addstr("\n")
        stdscr.clear()

        stdscr.addstr(2, 0, f"You completed the test. Press any key to continue", curses.color_pair(1))
        kkey = stdscr.getkey()

        if ord(kkey) == 27:
            break



if __name__ == "__main__":
    wrapper(main)



