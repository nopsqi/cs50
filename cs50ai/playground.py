import curses

def main(stdscr):
    # Initialize the curses window
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()

    # Create two windows within the main window
    top_window = stdscr.subwin(5, curses.COLS, 0, 0)
    bottom_window = stdscr.subwin(curses.LINES - 5, curses.COLS, 5, 0)

    top_window.addstr(0, 0, "This is the top window", curses.A_BOLD)
    bottom_window.addstr(0, 0, "This is the bottom window")

    top_window.refresh()
    bottom_window.refresh()

    stdscr.getch()

curses.wrapper(main)