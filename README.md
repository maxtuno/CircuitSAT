# Circuit SAT Assembler

## Installation

    pip install circuitsat
  
## Usage  
    
    csat file.csat

## Opcodes

    not                 ; A = NOT B
    and                 ; A = B AND C
    or                  ; A = B OR C
    nand                ; A = B NAND C
    nor                 ; A = B NOR C
    xor                 ; A = B XOR C
    equ                 ; A = B EQU C
    copy                ; A = B
    new                 ; Create a new BIT on REGISTER.
    push                ; Push REGISTER to STACK.
    pop                 ; Pop STACK to REGISTER.
    true                ; Set BIT on TOP of STACK as TRUE.
    false               ; Set BIT on TOP of STACK as FALSE.
    set ALPHANUMERIC    ; Save REGISTER at SLOT ALPHANUMERIC.
    get ALPHANUMERIC    ; Load SLOT ALPHANUMERIC into REGISTER.
    cur NUMBER          ; Set the current BIT to NUMBER.
    end                 ; Mandatory at the end of file.

# Example (examples folder)

    
    ; HALF ADDER
    
    new
    set A
    new
    set B
    new
    set C
    new
    set S

    get S
    push
    get B
    push
    get A
    push
    xor

    get C
    push
    get B
    push
    get A
    push
    and

    end
    
    > csat half_adder.csat
    > python3 test_tool.py hald_adder.cnf
    
## Note
Work in progress!
