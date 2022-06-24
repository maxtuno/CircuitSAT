grammar CircuitSAT;

circuitsat
    : (line EOL) * end
    ;

end
    : END
    ;

line
   : (opcode)? COMMENT?
   ;

opcode
   : OPCODE
   ;

OPCODE
   : N E W
   | N O T
   | A N D
   | O R
   | N A N D
   | N O R
   | X O R
   | E Q U
   | C O P Y
   | P U S H
   | P O P
   | T R U E
   | F A L S E
   | S E T ' ' NAME
   | G E T ' ' NAME
   | C U R ' ' NUMBER
   ;

END
    : E N D
    ;

NAME
   :  [a-zA-Z0-9] [a-zA-Z0-9]*
   ;

NUMBER
   : [0-9] [0-9]*
   ;

COMMENT
   : ';' ~ [\r\n]* -> skip
   ;

WS
   : [ \t] -> skip
   ;

EOL
   : [\r\n] +
   ;

fragment A
   : ('a' | 'A')
   ;


fragment B
   : ('b' | 'B')
   ;


fragment C
   : ('c' | 'C')
   ;


fragment D
   : ('d' | 'D')
   ;


fragment E
   : ('e' | 'E')
   ;


fragment F
   : ('f' | 'F')
   ;


fragment G
   : ('g' | 'G')
   ;


fragment H
   : ('h' | 'H')
   ;


fragment I
   : ('i' | 'I')
   ;


fragment J
   : ('j' | 'J')
   ;


fragment K
   : ('k' | 'K')
   ;


fragment L
   : ('l' | 'L')
   ;


fragment M
   : ('m' | 'M')
   ;


fragment N
   : ('n' | 'N')
   ;


fragment O
   : ('o' | 'O')
   ;


fragment P
   : ('p' | 'P')
   ;


fragment Q
   : ('q' | 'Q')
   ;


fragment R
   : ('r' | 'R')
   ;


fragment S
   : ('s' | 'S')
   ;


fragment T
   : ('t' | 'T')
   ;


fragment U
   : ('u' | 'U')
   ;


fragment V
   : ('v' | 'V')
   ;


fragment W
   : ('w' | 'W')
   ;


fragment X
   : ('x' | 'X')
   ;


fragment Y
   : ('y' | 'Y')
   ;


fragment Z
   : ('z' | 'Z')
   ;