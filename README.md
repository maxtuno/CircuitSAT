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
    true                ; Set BIT on REGISTER as TRUE.
    false               ; Set BIT on REGISTER as FALSE.
    set ALPHANUMERIC    ; Save REGISTER at SLOT ALPHANUMERIC.
    get ALPHANUMERIC    ; Load SLOT ALPHANUMERIC into REGISTER.
    cur NUMBER          ; Set the current BIT to NUMBER.
    end                 ; Mandatory at the end of file.

# Note
Work in progress!
