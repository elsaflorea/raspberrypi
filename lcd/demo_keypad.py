import Rpi.GPIO as GPIO
import Keypad

ROWS=4
COLS=4
keys = [
    '1', '2', '3', 'A',
    '4', '5', '6', 'B',
    '7', '8', '9', 'C',
    '*', '0', '#', 'D', ]
rowsPins = [7, 11, 13, 15]
colsPins = [29, 31, 33, 35]


def loop():
    keypad = Keypad.Keypad(keys, rowsPins, colsPins, ROWS, COLS)
    keypad.setDebounceTime(50)
    whileTrue:
        key = keypad.getKey()
        if key != keypad.NULL:
            print("You pressed: %c "%(key))


if __name__ == '__main__':
    print("start program")
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()

