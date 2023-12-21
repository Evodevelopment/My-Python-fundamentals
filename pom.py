import socket
import threading
import queue
import sys
import atexit
import time

try:
    import curses
except ImportError:
    import unicurses as curses

mqueue = queue.Queue()

import logging

def server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(65535)
        while True:
            conn, addr = s.accept()
            create_client(conn, addr)

clients = []
def create_client(sock, addr):
    thread = threading.Thread(target=client_main, args=(sock, addr))
    thread.daemon = True
    thread.start()
    clients.append(thread)

def client_main(sock, addr):
    buff = ""
    logging.info(f"Connected by {addr}")

    while True:
        data = sock.recv(1024)
        if not data:
            break

        buff += data.decode('utf-8')
        while True:
            line, sep, rest = buff.partition('\n')
            if sep != '':
                process_line(sock, line)
                buff = rest
            else:
                break

def process_line(client, line):
    global mqueue
    mqueue.put((client, line))

class TCPTerminal():
    def __init__(self, host, port):
        global mqueue
        # queue for terminal command messages from clients
        self.mqueue = mqueue
        self.server = None
        self.server_thread = None
        self.server_address = (None, None)
        self.start_server(host, port)
        self.stdscr = self.start_terminal()

    def start_server(self, host, port):
        '''function starts TCP server with specified host and port.
        if the port is 0, any unused port number will be allocated.'''

        self.server_thread = threading.Thread(target=server, args=(host, port))
        self.server_thread.daemon = True
        self.server_thread.start()

    def start_terminal(self):
        def my_except_hook(exctype, value, traceback):
            curses.endwin()
            sys.__excepthook__(exctype, value, traceback)
        sys.excepthook = my_except_hook

        def exit_handler():
            curses.endwin()
        atexit.register(exit_handler)

        stdscr = curses.initscr() # required
        curses.noecho() # don't show keyboard input
        curses.cbreak() # don't require enter to send input
        curses.curs_set(0) # hide cursor
        stdscr.keypad(True) # use arrow keys
        stdscr.nodelay(1) # don't block on getch()
        return stdscr

    def process_command(self):
        client, cmdstring = self.mqueue.get()
        cmd, *args = cmdstring.split('\0')

        if cmd == 'addch':
            x, y, ch, *_ = args
            ix = int(x)
            iy = int(y)
            logging.info(f'stdscr.addch({ix}, {iy}, {ch})')
            rows, cols = self.stdscr.getmaxyx()
            if ix < 0 or iy < 0 or ix > (cols -1) or iy > (rows -1):
                #logging.error(f'stdscr.addch: writing out of valid coordinates')
                return 

            self.stdscr.addch(iy, ix, ch)
            self.stdscr.refresh()

        elif cmd == 'getch':
            logging.info(f'stdscr.getch()')
            ch = self.stdscr.getch()
            client.sendall(f"getch\0{ch}\n".encode())

        elif cmd == 'readch':
            x, y, *_ = args
            ix = int(x)
            iy = int(y)
            logging.info(f'stdscr.readch({ix}, {iy})')
            rows, cols = self.stdscr.getmaxyx()
            if ix < 0 or iy < 0 or ix > (cols -1) or iy > (rows -1):
                #logging.error(f'stdscr.addch: writing out of valid coordinates')
                client.sendall(f"readch\0 \n".encode())
                return 

            attrs = self.stdscr.inch(iy, ix)
            ch = chr(attrs & 0xFF)
            client.sendall(f"readch\0{ch}\n".encode())

        elif cmd == 'clear':
            self.stdscr.clear()
            self.stdscr.refresh()


    def run(self):
        while True:
            self.process_command()


class TerminalClient:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.buff = ""

    def clear(self):
        logging.info(f'client.clear()')
        self.sock.sendall(f'clear\n'.encode())

    def addch(self, x, y, ch):
	# TOTO Odkomentuj pokud chces delay mezi kazdym prikazem
        #time.sleep(1)
        logging.info(f'client.addch({int(x)}, {int(y)}, {ch})')
        self.sock.sendall(f'addch\0{x}\0{y}\0{ch}\n'.encode())

    def readch(self, x, y):
        self.sock.sendall(f'readch\0{x}\0{y}\n'.encode())
        ch = None
        while True:
            line = self.receive_line()
            cmd, ch, *_ = line.split('\0')
            if cmd == 'readch':
                break

        logging.info(f'client.readch({int(x)}, {int(y)} = {ch}')
        return ch

    def getch(self):
        self.sock.sendall(f'getch\n'.encode())
        ch = None
        while True:
            line = self.receive_line()
            cmd, ch, *_ = line.split('\0')
            if cmd == 'getch':
                break

        ich = int(ch)
        logging.info(f'client.getch() = {ich}')
        return ich

    def receive_line(self):
        data = self.sock.recv(1024)
        if not data:
            raise IOError('Server disconnected')

        self.buff += data.decode('utf-8')
        while True:
            line, sep, rest = self.buff.partition('\n')
            if sep != '':
                self.buff = rest
                return line
            else:
                break

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.WARNING)

    # Port 0 means to select an arbitrary unused port
    tcpterminal = TCPTerminal('localhost', 9999)
    tcpterminal.run()
else:
    #logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.WARNING)

    terminalclient = TerminalClient('localhost', 9999)
    vymaz = terminalclient.clear
    znak = terminalclient.addch
    cti = terminalclient.readch
    klavesa = terminalclient.getch
    
KEY_RIGHT = curses.KEY_RIGHT
KEY_LEFT = curses.KEY_LEFT
KEY_UP = curses.KEY_UP
KEY_DOWN = curses.KEY_DOWN
