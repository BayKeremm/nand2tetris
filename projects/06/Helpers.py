#!/usr/bin/python
class Parser(object):
    def __init__(self, filePath):
        with open(filePath) as f:
            lines = []
            for line in f:
                lines.append(line.strip())
        self.lines = lines
        self.address = 0
        self.curRAM = 16
        self.index = 0
        self.length = len(self.lines)

    def getCurLine(self):
        return self.address

    def getCurRAM(self):
        self.curRAM = self.curRAM + 1
        ret = self.curRAM
        return ret

    def advance(self):
        if self.index < self.length:
            res =  self.lines[self.index]
            self.index = self.index + 1
        else:
            self.index = 0
            res=  0
        return res

    def commandType(self,command):
        if command[0:2] == "//" or command == "":
            return "NOT_A_COMMAND"
        elif command[0] == '(':
            return "L_COMMAND"
        elif command[0] == '@':
            self.address =self.address + 1
            return "A_COMMAND"
        else:
            self.address =self.address + 1
            return "C_COMMAND"

    # should be called only when the command is an A instruction
    def symbol(self, command):
        if command[0]=='@':
            return str(command[1:])
        else:
            return str(command[1:-1])


    # returns the dest mnemonic of the C instruction
    def dest(self, command):
        ret = "null"
        if '=' in command:
            ret = command.split('=')
            return str(ret[0])
        else:
            return ret

    # returns the comp mnemonic in the current C command
    def comp(self, command):
        ret = 0
        if '=' in command and ';' in command:
            ret = command.split('=')
            ret = ret[1].split(';')
            return str(ret[0])
        elif '=' not in command and ';' in command:
            ret = command.split(';')
            return str(ret[0])
        elif '='  in command and ';' not in command:
            ret = command.split('=')
            return str(ret[1])
        else:
            return str(ret)
            
    # returns the jump mnemonic in the current C command
    def jump(self,command):
        ret = "null"
        if ';' in command:
            ret = command.split(';')
            return str(ret[1])
        else:
            return str(ret)

    #def finish(self):
        #self.file.close()

class Code(object):
    def __init__(self):
        self.CmpTable = {
            "0":"0101010",
            "1":"0111111",
            "-1":"0111010",
            "D":"0001100",
            "A":"0110000",
            "!D":"0001101",
            "!A":"0110001",
            "-D":"0001111",
            "-A":"0110011",
            "D+1":"0011111",
            "A+1":"0110111",
            "D-1":"0001110",
            "A-1":"0110010",
            "D+A":"0000010",
            "D-A":"0010011",
            "A-D":"0000111",
            "D&A":"0000000",
            "D|A":"0010101",
            "M":"1110000",
            "!M":"1110001",
            "-M":"1110011",
            "M+1":"1110111",
            "M-1":"1110010",
            "D+M":"1000010",
            "D-M":"1010011",
            "M-D":"1000111",
            "D&M":"1000000",
            "D|M":"1010101"
        }
        self.DestTable = {
            "null":"000",
            "M":"001",
            "D":"010",
            "MD":"011",
            "A":"100",
            "AM":"101",
            "AD":"110",
            "AMD":"111"
        }
        self.JumpTable = {
            "null":"000",
            "JGT":"001",
            "JEQ":"010",
            "JGE":"011",
            "JLT":"100",
            "JNE":"101",
            "JLE":"110",
            "JMP":"111"
        }
    # returns the binary code of the mnemonic 
    def dest(self, symbol):
        return self.DestTable[symbol]
    # returns the binary code of the mnemonic 
    def comp(self, symbol):
        return self.CmpTable[symbol]
    # returns the binary code of the mnemonic 
    def jump(self, symbol):
        return self.JumpTable[symbol]

class SymbolTable:
    def __init__(self):
        self.Table = {
            "R0":"000000000000000",
            "R1":"000000000000001",
            "R2":"000000000000010",
            "R3":"000000000000011",
            "R4":"000000000000100",
            "R5":"000000000000101",
            "R6":"000000000000110",
            "R7":"000000000000111",
            "R8":"000000000001000",
            "R9":"000000000001001",
            "R10":"000000000001010",
            "R11":"000000000001011",
            "R12":"000000000001010",
            "R13":"000000000001101",
            "R14":"000000000001110",
            "R15":"000000000001111",
            "SP":"000000000000000",
            "LCL":"000000000000001",
            "ARG":"000000000000010",
            "THIS":"000000000000011",
            "THAT":"000000000000100",
            "SCREEN":"100000000000000",
            "KBD":"110000000000000"
        }
    def addEntry(self,symbol,address):
        self.Table[symbol]=address
        return True
    def addEntryVariable(self,symbol,address):
        self.Table[symbol]=address
        return True
    def contains(self,symbol):
        return symbol in self.Table
    def getAddress(self,symbol):
        return self.Table[symbol]
    def printTable(self):
        print(self.Table)
        