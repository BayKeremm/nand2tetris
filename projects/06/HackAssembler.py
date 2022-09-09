#!/usr/bin/python
from Helpers import Parser, Code, SymbolTable
import sys

def slicer(cmdIn):
    index = cmdIn.find("//")
    if index != -1:
        return cmdIn[:index].strip()
    else:
        return cmdIn
parser1 = Parser(str(sys.argv[1]))
table = SymbolTable()

code = Code()

cmd = parser1.advance();
# first pass
while cmd != 0:
    typeOfCmd = parser1.commandType(cmd)
    if typeOfCmd == "L_COMMAND":
        cmd = slicer(cmd)
        if table.contains(parser1.symbol(cmd)):
            continue
        else:
            bin_ = '{0:015b}'.format(parser1.getCurLine())
            table.addEntry(parser1.symbol(cmd),bin_)

    cmd = parser1.advance();

output = open("outputBin.hack","w")

cmd = parser1.advance();
# second pass
while cmd != 0:
    typeOfCmd = parser1.commandType(cmd)
    if typeOfCmd == "NOT_A_COMMAND":
        cmd = parser1.advance();
        continue
    elif typeOfCmd == "L_COMMAND":
        cmd = parser1.advance();
        continue
    elif typeOfCmd == "A_COMMAND":
        output.write("0")
        cmd = slicer(cmd)
        if table.contains(str(parser1.symbol(cmd))):
            address = table.getAddress(parser1.symbol(cmd))
            output.write(address)
        else:
            if parser1.symbol(cmd).isnumeric(): 
                bin_ = '{0:015b}'.format(int(parser1.symbol(cmd)))
                output.write(bin_)
            else:
                #if it is not a number, add it to the table. It is intended as a variable
                bin_ = '{0:015b}'.format(parser1.getCurRAM())
                table.addEntryVariable(parser1.symbol(cmd),bin_)
                address = table.getAddress(parser1.symbol(cmd))
                output.write(address)

    elif typeOfCmd == "C_COMMAND":
        cmd = slicer(cmd)
        output.write("111")
        output.write(code.comp(parser1.comp(cmd)))
        output.write(code.dest(parser1.dest(cmd)))
        output.write(code.jump(parser1.jump(cmd)))
    cmd = parser1.advance();
    output.write("\n")
output.close()
#parser1.finish()


# RAM after 16 is not working for variables