// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
    @2
    M=0  // initialize result as 0

    @0  // load ram0
    D=M
    @END
    D;JEQ // if ram0 is 0 go to the end

    @1  // load ram1
    D=M
    @END
    D;JEQ // if ram0 is 0 go to the end

(LOOP)
    @0
    D=M // load ram0
    @2
    M=D+M // load ram2 and add ram0 to ram2
    @1
    M=M-1 // decrease ram1 by 1
    D=M
    @LOOP
    D;JGT // if not go through the loop again
(END)
    @END
    0;JMP