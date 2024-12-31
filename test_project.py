import pytest
import curses
from curses import wrapper
from project import welcome_screen, display50, main, speed50

stdscr = curses.initscr()
def test_welcome_screen():
    assert welcome_screen(stdscr) == "\t~~~~~~~~~Welcome to SPEED-TYPE50!!~~~~~~~~~~~~\n\t\t ** Press any key to begin"

def test_display50():
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    assert display50(stdscr, "h", "h" , wpm = 0 ) == stdscr.addstr(0, "h", "h", curses.color_pair(1))
    assert display50(stdscr, "h", "e" , wpm = 0 ) == stdscr.addstr(0, "h", "e", curses.color_pair(2))

def test_speed50():
    test_text = ["h","e"]
    assert speed50("\b") == test_text.pop()





if __name__ == "__main__":
    test_welcome_screen()