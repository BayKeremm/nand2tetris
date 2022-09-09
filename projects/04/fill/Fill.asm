// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(INIT)
    @8192
    D=A
    @i
    M=D // last pixel on the screen

(LOOP)
    @i
    M=M-1 // decrease i by 1 
    D=M
    @INIT
    D;JLT

    @KBD // load keyboard
    D=M

    @WHITE // jump to white the screen if D = 0
    D;JEQ
    @BLACK // jump tp black the screen if D > 0
    D;JGT
    (WHITE)
        @SCREEN
        D=A
        @i
        A=D+M
        M=0
        @LOOP
        0;JMP
    (BLACK)
        @SCREEN
        D=A
        @i
        A=D+M
        M=-1
        @LOOP
        0;JMP