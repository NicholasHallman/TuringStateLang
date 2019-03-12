import sys
import time

data = []
language = []
states = {"START" : 0, "END" : -1,"FAIL" : -2}
debug = False
head = 0


def main():
    global debug
    filename = ""
    for arg in sys.argv:
        if arg == "-d":
            print("Debug Enabled")
            debug = True
        if arg[0] != "-":
            filename = arg
    file = open(filename, 'r')
    firstPass(file)
    if debug:
        printStates()
        print("-----------------------------")

    start(file)

'''
firstPass
-----------------------------
Description: Run through the 
given source code and find all
state names
-----------------------------
Input: file, the source code
Output: fills the state table library
-----------------------------
'''
def firstPass(file):
    lineNum = 1
    for line in file:
        line.strip()
        if line[0] == '#':
            states[line[1:].strip()] = lineNum
        if line.upper().strip() == "START":
            states["START"] = lineNum
        if line.upper().strip() == "END":
            states["END"] = lineNum
        if line.upper().strip() == "FAIL":
            states["FAIL"] = lineNum
        if line[0] == "[":
            for char in line.strip():
                if char != "[" and char != "]":
                    data.append(char)
        if line[0] == "{":
            for char in line.strip():
                if char != "{" and char != "}":
                    language.append(char)
        lineNum += 1

    if len(data) == 0:
        data.append(None)
    if len(language) == 0:
        print("Syntax Error: expected language definition {} ")
        sys.exit()

'''
printStates
-----------------------------
Description: in debug prints
the states in the machine
-----------------------------
Input: None
Output: None
-----------------------------
'''

def printStates():
    for key,val in states.items():
        print("{0:<3} | {1:<3}".format(key, val))

'''
start
-----------------------------
Description: Run through the 
given source code and find all
state names
-----------------------------
Input: file, the source code
Output: fills the state table library
-----------------------------
'''
def start(file):
    print(data)
    symbols = []
    global head
    file.seek(0)
    lineNum = states["START"]
    i = 0
    line = file.readline()
    while i < lineNum and line is not None:
        line = file.readline()
        i+=1

    end = False

    while not end:
        valid = False
        symbols = []
        while not valid:
            symbols = parse(line)
            if symbols[0] == data[head]:
                valid = True
            else:
                line = file.readline()
        if debug:
            print(symbols)
        if symbols[1] is not None:
            data[head] = symbols[1]
            if symbols[1] == "None":
                data[head] = None

        if symbols[2] == "RIGHT":
            head += 1
            if head == len(data):
                data.append(None)
        elif symbols[2] == "LEFT":
            head -= 1
            if head <= 0:
                data.insert(0, None)
                head = 1
        
        if symbols[3] == -1 or symbols[3] == -2:
            end = True
        else:
            file.seek(0)
            i = 0
            lineNum = symbols[3]
            line = file.readline()
            while i < lineNum and line is not None:
                line = file.readline()
                i+=1

    print(data)
    if symbols[3] == -2:
        print("Program reached REJECT state")
    else:
        print("Program reached ACCEPT state")

    




'''
parse
-----------------------------
Description: interpret a line of code
-----------------------------
Input: line
Output: [read, assign, move, jump]
-----------------------------
'''
def parse(line):
    output = [None, None, None, None]
    line = line.strip()
    line = line.replace(" ", "")
    line = line.replace("READ","&")
    while len(line) > 0:
        if line[0] == "&":
            line = line.replace("&","")
            if line[0] in language:
                output[0] = line[0]
                line = line[1:]

            else:
                output[0] = None
        elif line[0] == "=":
            line = line.replace("=","")
            if line[0] in language:
                output[1] = line[0]
                line = line[1:]
            else:
                output[1] = "None"
        elif line[0] == "<":
            output[2] = "LEFT"
            line = line[1:]
        elif line[0] == ">":
            output[2] = "RIGHT"
            line = line[1:]
        elif line in states.keys():
            output[3] = states[line]
            line = ""

    return output   
        

main()

