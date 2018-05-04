from subprocess import run, PIPE


def r(command):
    """
    Run command and return output as a string
    :param command: Command to be executed
    :return: return string
    """
    return run(command, shell=True, stdout=PIPE, stderr=PIPE).stdout.decode()


#  who needs regular expressions when you got list comprehensions >:)
_output = [x for x in (r(command='xinput |grep Pen').split('\n'))]
print(_output)
pen = [x.strip("id=") for x in _output[0].split() if "id" in x][0]
pressure = [x.strip("id=") for x in _output[1].split() if "id" in x][0]
try:
    extra = [x.strip("id=") for x in _output[2].split() if "id" in x][0]
    print('Three pens')
except:
    print('only two Pens')

SCREEN = "HDMI-0"


def reset(device_number):
    r(command="xinput disable " + device_number)
    r(command="xinput enable " + device_number)


def map_to_screen(device_number, display):
    r(command="xinput map-to-output " + device_number + ' ' + display)
    print('setting pen to', display)


def main(par=0, screen=SCREEN):
    print(par)  # kivy needs this for some reason I don't understand :-)
    print("Resettinggggg")
    reset(pen)
    reset(pressure)
    map_to_screen(pen, screen)


if __name__ == "__main__":
    main()

# Zucy loves this bunch of code
