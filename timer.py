from sys import argv
from time import sleep, strftime
from os import system
from functools import wraps

crab = "_.-^-."

# Makes decorated function return 1 if keyboard interrupt
def handle_kb_interrupt(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print(' '*20)
            return 1
    return wrapper

@handle_kb_interrupt
def main() -> int:
    if (len(argv) != 2):
        print('Invalid number of arguments.\nUSAGE: python3 timer.py NUM_SECONDS')
        return 1
    try:
        seconds = int(argv[1])
    except ValueError:
        print('Argument must be a positive integer.')
        return 1
    if (seconds < 1):
        print('Invalid number of seconds.')
        return 1

    start = strftime("%H:%M:%S")
    for i in range(seconds):
        crab_offset = "".join([crab[(x+i)%len(crab)] for x in range(len(crab))])
        print(f'|{crab_offset}| TIMER: {seconds-i}s     \r', end='')
        sleep(1)
    end = strftime("%H:%M:%S")
    print(f'TIMER DONE | {start} -> {end}{" "*10}')
    # Toggle speech on MacOS
    #system('say "TIMER DONE!"')
    return 0

if __name__ == '__main__':
    exit(main())
