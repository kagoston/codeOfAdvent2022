class CRT():
    def __init__(self):
        # the CRT screen 40 wide and 6 high represented as one line
        self.crtScreen = [[0 for i in range(40)] for j in range(6)]
        # position of the first pixel of the sprite    
        self.spritePosition = 0
        self.currentPixel = 0
        self.currentRow = 0


    def draw(self):
        # the CRT draws a single pixel during each cycle
        # if the sprite is positioned such that one of its three
        # pixels is the pixel currently being drawn
        if self.currentPixel >= self.spritePosition and self.currentPixel <= self.spritePosition + 2:
            # lit pixel (#) = 1
            pixel = 1
        else:
            # dark pixel (.) = 0
            pixel = 0

        self.crtScreen[self.currentRow][self.currentPixel] = pixel
    

    def updatePosition(self):
        """
        after 40 pixels change the row on the CRT screen
        """
        self.currentPixel += 1
        if self.currentPixel == 40:
            self.currentPixel = 0
            self.currentRow += 1


    def printCRT(self):
        # lit pixel (#) = 1, dark pixel (.) = 0
        for row in self.crtScreen:
            for cell in row:
                if cell == 1:
                    print("{:<2s}".format('#'), end='')
                else:
                    print("{:<2s}".format(". ."), end='')
            print('\n', end='')


class CPU:
    """
    simulate a simple CPU
    """
    
    def __init__(self):
        self.cycles = {"addx": 2, "noop": 1} # number of CPU cycles for each command
        self.cycleCounter = 0
        self.registerX = 1
        self.signalStrength = 0


    def process(self, command, crt):
        # FETCH the next command
        function = command[0]
        value = command[1] if len(command) > 1 else ''
        exp = 'self.' + function + '(' + value + ')'
        
        for _ in range(self.cycles[function]):
            # run a cycle
            self.cycleCounter += 1
            self.cummulateSignalStrength()

            crt.draw()            
            crt.updatePosition()

        # EXECUTE the command
        eval(exp, {'self' : self})
        # the X register sets the horizontal position of the
        # middle of the sprite (3 pixel)
        crt.spritePosition = self.registerX - 1


    def cummulateSignalStrength(self):
        """
        Sum the signal strength during the 20th, 60th, 100th,
        140th, 180th, and 220th cycles.
        """
        # the cycle number multiplied by the value of the X register
        if (self.cycleCounter - 20) % 40 == 0 and  self.cycleCounter <= 220:
            self.signalStrength += self.cycleCounter * self.registerX


    def noop(self):
        pass


    def addx(self, value):
        self.registerX += value


if __name__ == "__main__":
    """
    advent of code 2022, day 10
    """

    cpu = CPU()
    crt = CRT()

    # read the file containing a instructions for the CPU
    with open("advent10.txt", "r") as f:
        for line in f:
            command = line.strip().split()
            cpu.process(command, crt)

    # task 1:
    print(cpu.signalStrength)
    # task 2
    crt.printCRT()
