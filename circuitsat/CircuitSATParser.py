# Generated from C:/Users/oscar/Downloads/Development/TL\CircuitSAT.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,60,396,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,3,0,41,
        8,0,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,1,1,1,3,1,54,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,3,1,3,3,3,
        70,8,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,78,8,4,1,4,1,4,1,4,1,4,3,4,84,
        8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,102,8,4,1,5,1,5,5,5,106,8,5,10,5,12,5,109,9,5,1,5,3,5,112,
        8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,3,9,135,8,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,5,12,159,8,12,10,12,12,12,162,9,12,1,12,1,12,1,13,1,
        13,1,13,5,13,169,8,13,10,13,12,13,172,9,13,1,14,1,14,1,14,5,14,177,
        8,14,10,14,12,14,180,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,3,15,192,8,15,1,15,1,15,3,15,196,8,15,1,15,1,15,3,15,200,
        8,15,1,15,1,15,3,15,204,8,15,1,15,1,15,1,15,1,15,3,15,210,8,15,1,
        15,1,15,1,15,3,15,215,8,15,1,15,3,15,218,8,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        5,15,250,8,15,10,15,12,15,253,9,15,1,16,1,16,3,16,257,8,16,1,16,
        1,16,1,17,1,17,1,17,1,17,4,17,265,8,17,11,17,12,17,266,1,18,1,18,
        1,18,3,18,272,8,18,1,18,1,18,1,18,3,18,277,8,18,1,18,1,18,1,18,3,
        18,282,8,18,1,18,1,18,1,18,3,18,287,8,18,1,18,1,18,1,18,3,18,292,
        8,18,1,18,1,18,1,18,3,18,297,8,18,1,18,1,18,1,18,3,18,302,8,18,1,
        18,1,18,1,18,3,18,307,8,18,1,18,1,18,1,18,3,18,312,8,18,1,18,1,18,
        1,18,3,18,317,8,18,1,18,1,18,1,18,3,18,322,8,18,1,18,1,18,1,18,3,
        18,327,8,18,1,18,1,18,1,18,3,18,332,8,18,1,18,1,18,1,18,3,18,337,
        8,18,1,18,1,18,1,18,3,18,342,8,18,1,18,1,18,1,18,3,18,347,8,18,1,
        18,1,18,1,18,3,18,352,8,18,1,18,1,18,1,18,3,18,357,8,18,1,18,1,18,
        1,18,3,18,362,8,18,1,18,1,18,1,18,3,18,367,8,18,1,18,1,18,1,18,3,
        18,372,8,18,1,18,1,18,1,18,3,18,377,8,18,1,18,1,18,1,18,3,18,382,
        8,18,1,18,1,18,1,18,3,18,387,8,18,1,18,1,18,1,18,3,18,392,8,18,3,
        18,394,8,18,1,18,0,1,30,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,0,4,1,0,30,33,1,0,28,29,2,0,22,23,26,27,1,0,20,21,
        459,0,38,1,0,0,0,2,46,1,0,0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,101,1,
        0,0,0,10,103,1,0,0,0,12,115,1,0,0,0,14,120,1,0,0,0,16,126,1,0,0,
        0,18,130,1,0,0,0,20,140,1,0,0,0,22,150,1,0,0,0,24,156,1,0,0,0,26,
        165,1,0,0,0,28,173,1,0,0,0,30,217,1,0,0,0,32,254,1,0,0,0,34,264,
        1,0,0,0,36,393,1,0,0,0,38,40,3,2,1,0,39,41,5,0,0,1,40,39,1,0,0,0,
        40,41,1,0,0,0,41,1,1,0,0,0,42,45,3,4,2,0,43,45,3,18,9,0,44,42,1,
        0,0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,
        53,1,0,0,0,48,46,1,0,0,0,49,50,5,9,0,0,50,51,3,30,15,0,51,52,5,40,
        0,0,52,54,1,0,0,0,53,49,1,0,0,0,53,54,1,0,0,0,54,3,1,0,0,0,55,56,
        3,6,3,0,56,57,5,40,0,0,57,66,1,0,0,0,58,59,3,8,4,0,59,60,5,40,0,
        0,60,66,1,0,0,0,61,66,3,10,5,0,62,66,3,20,10,0,63,66,3,22,11,0,64,
        66,3,24,12,0,65,55,1,0,0,0,65,58,1,0,0,0,65,61,1,0,0,0,65,62,1,0,
        0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,5,1,0,0,0,67,69,5,57,0,0,68,70,
        3,34,17,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,41,0,
        0,72,73,3,30,15,0,73,7,1,0,0,0,74,75,5,57,0,0,75,77,5,38,0,0,76,
        78,3,28,14,0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,102,5,
        39,0,0,80,81,5,1,0,0,81,83,5,38,0,0,82,84,3,30,15,0,83,82,1,0,0,
        0,83,84,1,0,0,0,84,85,1,0,0,0,85,102,5,39,0,0,86,87,5,2,0,0,87,88,
        5,38,0,0,88,89,3,30,15,0,89,90,5,39,0,0,90,102,1,0,0,0,91,92,5,4,
        0,0,92,93,5,38,0,0,93,94,3,30,15,0,94,95,5,39,0,0,95,102,1,0,0,0,
        96,97,5,5,0,0,97,98,5,38,0,0,98,99,3,30,15,0,99,100,5,39,0,0,100,
        102,1,0,0,0,101,74,1,0,0,0,101,80,1,0,0,0,101,86,1,0,0,0,101,91,
        1,0,0,0,101,96,1,0,0,0,102,9,1,0,0,0,103,107,3,12,6,0,104,106,3,
        14,7,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,
        0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,110,112,3,16,8,0,111,110,1,
        0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,5,15,0,0,114,11,1,
        0,0,0,115,116,5,7,0,0,116,117,3,30,15,0,117,118,5,13,0,0,118,119,
        3,2,1,0,119,13,1,0,0,0,120,121,5,8,0,0,121,122,5,7,0,0,122,123,3,
        30,15,0,123,124,5,13,0,0,124,125,3,2,1,0,125,15,1,0,0,0,126,127,
        5,8,0,0,127,128,5,13,0,0,128,129,3,2,1,0,129,17,1,0,0,0,130,131,
        5,6,0,0,131,132,5,57,0,0,132,134,5,38,0,0,133,135,3,26,13,0,134,
        133,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,137,5,39,0,0,137,
        138,3,2,1,0,138,139,5,15,0,0,139,19,1,0,0,0,140,141,5,10,0,0,141,
        142,5,57,0,0,142,143,5,41,0,0,143,144,3,30,15,0,144,145,5,12,0,0,
        145,146,3,30,15,0,146,147,5,13,0,0,147,148,3,2,1,0,148,149,5,15,
        0,0,149,21,1,0,0,0,150,151,5,11,0,0,151,152,3,30,15,0,152,153,5,
        13,0,0,153,154,3,2,1,0,154,155,5,15,0,0,155,23,1,0,0,0,156,160,5,
        14,0,0,157,159,3,36,18,0,158,157,1,0,0,0,159,162,1,0,0,0,160,158,
        1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,163,164,
        5,15,0,0,164,25,1,0,0,0,165,170,5,57,0,0,166,167,5,42,0,0,167,169,
        5,57,0,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,27,1,0,0,0,172,170,1,0,0,0,173,178,3,30,15,0,174,175,
        5,42,0,0,175,177,3,30,15,0,176,174,1,0,0,0,177,180,1,0,0,0,178,176,
        1,0,0,0,178,179,1,0,0,0,179,29,1,0,0,0,180,178,1,0,0,0,181,182,6,
        15,-1,0,182,183,5,29,0,0,183,218,3,30,15,20,184,185,5,25,0,0,185,
        218,3,30,15,19,186,218,5,56,0,0,187,218,5,55,0,0,188,218,5,17,0,
        0,189,191,3,8,4,0,190,192,3,34,17,0,191,190,1,0,0,0,191,192,1,0,
        0,0,192,218,1,0,0,0,193,195,3,32,16,0,194,196,3,34,17,0,195,194,
        1,0,0,0,195,196,1,0,0,0,196,218,1,0,0,0,197,199,5,57,0,0,198,200,
        3,34,17,0,199,198,1,0,0,0,199,200,1,0,0,0,200,218,1,0,0,0,201,203,
        5,58,0,0,202,204,3,34,17,0,203,202,1,0,0,0,203,204,1,0,0,0,204,218,
        1,0,0,0,205,206,5,38,0,0,206,207,3,30,15,0,207,209,5,39,0,0,208,
        210,3,34,17,0,209,208,1,0,0,0,209,210,1,0,0,0,210,218,1,0,0,0,211,
        212,5,3,0,0,212,214,5,38,0,0,213,215,5,58,0,0,214,213,1,0,0,0,214,
        215,1,0,0,0,215,216,1,0,0,0,216,218,5,39,0,0,217,181,1,0,0,0,217,
        184,1,0,0,0,217,186,1,0,0,0,217,187,1,0,0,0,217,188,1,0,0,0,217,
        189,1,0,0,0,217,193,1,0,0,0,217,197,1,0,0,0,217,201,1,0,0,0,217,
        205,1,0,0,0,217,211,1,0,0,0,218,251,1,0,0,0,219,220,10,18,0,0,220,
        221,5,24,0,0,221,250,3,30,15,18,222,223,10,17,0,0,223,224,7,0,0,
        0,224,250,3,30,15,18,225,226,10,16,0,0,226,227,7,1,0,0,227,250,3,
        30,15,17,228,229,10,15,0,0,229,230,7,2,0,0,230,250,3,30,15,16,231,
        232,10,14,0,0,232,233,7,3,0,0,233,250,3,30,15,15,234,235,10,13,0,
        0,235,236,5,19,0,0,236,250,3,30,15,14,237,238,10,12,0,0,238,239,
        5,18,0,0,239,250,3,30,15,13,240,241,10,11,0,0,241,242,5,43,0,0,242,
        243,3,30,15,0,243,244,5,44,0,0,244,245,3,30,15,12,245,250,1,0,0,
        0,246,247,10,10,0,0,247,248,5,16,0,0,248,250,3,30,15,11,249,219,
        1,0,0,0,249,222,1,0,0,0,249,225,1,0,0,0,249,228,1,0,0,0,249,231,
        1,0,0,0,249,234,1,0,0,0,249,237,1,0,0,0,249,240,1,0,0,0,249,246,
        1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,31,1,
        0,0,0,253,251,1,0,0,0,254,256,5,36,0,0,255,257,3,28,14,0,256,255,
        1,0,0,0,256,257,1,0,0,0,257,258,1,0,0,0,258,259,5,37,0,0,259,33,
        1,0,0,0,260,261,5,36,0,0,261,262,3,30,15,0,262,263,5,37,0,0,263,
        265,1,0,0,0,264,260,1,0,0,0,265,266,1,0,0,0,266,264,1,0,0,0,266,
        267,1,0,0,0,267,35,1,0,0,0,268,269,5,45,0,0,269,271,5,57,0,0,270,
        272,3,30,15,0,271,270,1,0,0,0,271,272,1,0,0,0,272,394,1,0,0,0,273,
        274,5,46,0,0,274,276,5,57,0,0,275,277,3,30,15,0,276,275,1,0,0,0,
        276,277,1,0,0,0,277,278,1,0,0,0,278,279,5,42,0,0,279,281,5,57,0,
        0,280,282,3,30,15,0,281,280,1,0,0,0,281,282,1,0,0,0,282,394,1,0,
        0,0,283,284,5,47,0,0,284,286,5,57,0,0,285,287,3,30,15,0,286,285,
        1,0,0,0,286,287,1,0,0,0,287,288,1,0,0,0,288,289,5,42,0,0,289,291,
        5,57,0,0,290,292,3,30,15,0,291,290,1,0,0,0,291,292,1,0,0,0,292,293,
        1,0,0,0,293,294,5,42,0,0,294,296,5,57,0,0,295,297,3,30,15,0,296,
        295,1,0,0,0,296,297,1,0,0,0,297,394,1,0,0,0,298,299,5,48,0,0,299,
        301,5,57,0,0,300,302,3,30,15,0,301,300,1,0,0,0,301,302,1,0,0,0,302,
        303,1,0,0,0,303,304,5,42,0,0,304,306,5,57,0,0,305,307,3,30,15,0,
        306,305,1,0,0,0,306,307,1,0,0,0,307,308,1,0,0,0,308,309,5,42,0,0,
        309,311,5,57,0,0,310,312,3,30,15,0,311,310,1,0,0,0,311,312,1,0,0,
        0,312,394,1,0,0,0,313,314,5,49,0,0,314,316,5,57,0,0,315,317,3,30,
        15,0,316,315,1,0,0,0,316,317,1,0,0,0,317,318,1,0,0,0,318,319,5,42,
        0,0,319,321,5,57,0,0,320,322,3,30,15,0,321,320,1,0,0,0,321,322,1,
        0,0,0,322,323,1,0,0,0,323,324,5,42,0,0,324,326,5,57,0,0,325,327,
        3,30,15,0,326,325,1,0,0,0,326,327,1,0,0,0,327,394,1,0,0,0,328,329,
        5,50,0,0,329,331,5,57,0,0,330,332,3,30,15,0,331,330,1,0,0,0,331,
        332,1,0,0,0,332,333,1,0,0,0,333,334,5,42,0,0,334,336,5,57,0,0,335,
        337,3,30,15,0,336,335,1,0,0,0,336,337,1,0,0,0,337,338,1,0,0,0,338,
        339,5,42,0,0,339,341,5,57,0,0,340,342,3,30,15,0,341,340,1,0,0,0,
        341,342,1,0,0,0,342,394,1,0,0,0,343,344,5,51,0,0,344,346,5,57,0,
        0,345,347,3,30,15,0,346,345,1,0,0,0,346,347,1,0,0,0,347,348,1,0,
        0,0,348,349,5,42,0,0,349,351,5,57,0,0,350,352,3,30,15,0,351,350,
        1,0,0,0,351,352,1,0,0,0,352,353,1,0,0,0,353,354,5,42,0,0,354,356,
        5,57,0,0,355,357,3,30,15,0,356,355,1,0,0,0,356,357,1,0,0,0,357,394,
        1,0,0,0,358,359,5,52,0,0,359,361,5,57,0,0,360,362,3,30,15,0,361,
        360,1,0,0,0,361,362,1,0,0,0,362,363,1,0,0,0,363,364,5,42,0,0,364,
        366,5,57,0,0,365,367,3,30,15,0,366,365,1,0,0,0,366,367,1,0,0,0,367,
        368,1,0,0,0,368,369,5,42,0,0,369,371,5,57,0,0,370,372,3,30,15,0,
        371,370,1,0,0,0,371,372,1,0,0,0,372,394,1,0,0,0,373,374,5,53,0,0,
        374,376,5,57,0,0,375,377,3,30,15,0,376,375,1,0,0,0,376,377,1,0,0,
        0,377,378,1,0,0,0,378,379,5,42,0,0,379,381,5,57,0,0,380,382,3,30,
        15,0,381,380,1,0,0,0,381,382,1,0,0,0,382,394,1,0,0,0,383,384,5,54,
        0,0,384,386,5,57,0,0,385,387,3,30,15,0,386,385,1,0,0,0,386,387,1,
        0,0,0,387,388,1,0,0,0,388,389,5,42,0,0,389,391,5,57,0,0,390,392,
        3,30,15,0,391,390,1,0,0,0,391,392,1,0,0,0,392,394,1,0,0,0,393,268,
        1,0,0,0,393,273,1,0,0,0,393,283,1,0,0,0,393,298,1,0,0,0,393,313,
        1,0,0,0,393,328,1,0,0,0,393,343,1,0,0,0,393,358,1,0,0,0,393,373,
        1,0,0,0,393,383,1,0,0,0,394,37,1,0,0,0,52,40,44,46,53,65,69,77,83,
        101,107,111,134,160,170,178,191,195,199,203,209,214,217,249,251,
        256,266,271,276,281,286,291,296,301,306,311,316,321,326,331,336,
        341,346,351,356,361,366,371,376,381,386,391,393
    ]

class CircuitSATParser ( Parser ):

    grammarFileName = "CircuitSAT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'write'", "'input'", "'assert'", 
                     "'size'", "'def'", "'if'", "'else'", "'return'", "'for'", 
                     "'while'", "'to'", "'do'", "'asm'", "'end'", "'in'", 
                     "'null'", "'||'", "'&&'", "'=='", "'!='", "'>='", "'<='", 
                     "'^'", "'!'", "'>'", "'<'", "'+'", "'-'", "'*'", "'/'", 
                     "'//'", "'%'", "'{'", "'}'", "'['", "']'", "'('", "')'", 
                     "';'", "'='", "','", "'?'", "':'", "'new'", "'not'", 
                     "'and'", "'or'", "'nand'", "'nor'", "'xor'", "'equ'", 
                     "'copy'", "'put'" ]

    symbolicNames = [ "<INVALID>", "Println", "Print", "Input", "Assert", 
                      "Size", "Def", "If", "Else", "Return", "For", "While", 
                      "To", "Do", "Asm", "End", "In", "Null", "Or", "And", 
                      "Equals", "NEquals", "GTEquals", "LTEquals", "Pow", 
                      "Excl", "GT", "LT", "Add", "Subtract", "Multiply", 
                      "Divide", "IDivide", "Modulus", "OBrace", "CBrace", 
                      "OBracket", "CBracket", "OParen", "CParen", "SColon", 
                      "Assign", "Comma", "QMark", "Colon", "OpNew", "OpNot", 
                      "OpAnd", "OpOr", "OpNand", "OpNor", "OpXor", "OpEqu", 
                      "OpCopy", "OpPut", "Bool", "Number", "Identifier", 
                      "String", "Comment", "Space" ]

    RULE_circuit = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_functionCall = 4
    RULE_ifStatement = 5
    RULE_ifStat = 6
    RULE_elseIfStat = 7
    RULE_elseStat = 8
    RULE_functionDecl = 9
    RULE_forStatement = 10
    RULE_whileStatement = 11
    RULE_assemblerStatement = 12
    RULE_idList = 13
    RULE_exprList = 14
    RULE_expression = 15
    RULE_list = 16
    RULE_indexes = 17
    RULE_opcode = 18

    ruleNames =  [ "circuit", "block", "statement", "assignment", "functionCall", 
                   "ifStatement", "ifStat", "elseIfStat", "elseStat", "functionDecl", 
                   "forStatement", "whileStatement", "assemblerStatement", 
                   "idList", "exprList", "expression", "list", "indexes", 
                   "opcode" ]

    EOF = Token.EOF
    Println=1
    Print=2
    Input=3
    Assert=4
    Size=5
    Def=6
    If=7
    Else=8
    Return=9
    For=10
    While=11
    To=12
    Do=13
    Asm=14
    End=15
    In=16
    Null=17
    Or=18
    And=19
    Equals=20
    NEquals=21
    GTEquals=22
    LTEquals=23
    Pow=24
    Excl=25
    GT=26
    LT=27
    Add=28
    Subtract=29
    Multiply=30
    Divide=31
    IDivide=32
    Modulus=33
    OBrace=34
    CBrace=35
    OBracket=36
    CBracket=37
    OParen=38
    CParen=39
    SColon=40
    Assign=41
    Comma=42
    QMark=43
    Colon=44
    OpNew=45
    OpNot=46
    OpAnd=47
    OpOr=48
    OpNand=49
    OpNor=50
    OpXor=51
    OpEqu=52
    OpCopy=53
    OpPut=54
    Bool=55
    Number=56
    Identifier=57
    String=58
    Comment=59
    Space=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CircuitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CircuitSATParser.BlockContext,0)


        def EOF(self):
            return self.getToken(CircuitSATParser.EOF, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_circuit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircuit" ):
                listener.enterCircuit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircuit" ):
                listener.exitCircuit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircuit" ):
                return visitor.visitCircuit(self)
            else:
                return visitor.visitChildren(self)




    def circuit(self):

        localctx = CircuitSATParser.CircuitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_circuit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.block()
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 39
                self.match(CircuitSATParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.StatementContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.StatementContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.FunctionDeclContext,i)


        def Return(self):
            return self.getToken(CircuitSATParser.Return, 0)

        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def SColon(self):
            return self.getToken(CircuitSATParser.SColon, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CircuitSATParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Def) | (1 << CircuitSATParser.If) | (1 << CircuitSATParser.For) | (1 << CircuitSATParser.While) | (1 << CircuitSATParser.Asm) | (1 << CircuitSATParser.Identifier))) != 0):
                self.state = 44
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CircuitSATParser.Println, CircuitSATParser.Print, CircuitSATParser.Assert, CircuitSATParser.Size, CircuitSATParser.If, CircuitSATParser.For, CircuitSATParser.While, CircuitSATParser.Asm, CircuitSATParser.Identifier]:
                    self.state = 42
                    self.statement()
                    pass
                elif token in [CircuitSATParser.Def]:
                    self.state = 43
                    self.functionDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CircuitSATParser.Return:
                self.state = 49
                self.match(CircuitSATParser.Return)
                self.state = 50
                self.expression(0)
                self.state = 51
                self.match(CircuitSATParser.SColon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CircuitSATParser.AssignmentContext,0)


        def SColon(self):
            return self.getToken(CircuitSATParser.SColon, 0)

        def functionCall(self):
            return self.getTypedRuleContext(CircuitSATParser.FunctionCallContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(CircuitSATParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(CircuitSATParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(CircuitSATParser.WhileStatementContext,0)


        def assemblerStatement(self):
            return self.getTypedRuleContext(CircuitSATParser.AssemblerStatementContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CircuitSATParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.assignment()
                self.state = 56
                self.match(CircuitSATParser.SColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.functionCall()
                self.state = 59
                self.match(CircuitSATParser.SColon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.assemblerStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CircuitSATParser.Identifier, 0)

        def Assign(self):
            return self.getToken(CircuitSATParser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def indexes(self):
            return self.getTypedRuleContext(CircuitSATParser.IndexesContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = CircuitSATParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(CircuitSATParser.Identifier)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CircuitSATParser.OBracket:
                self.state = 68
                self.indexes()


            self.state = 71
            self.match(CircuitSATParser.Assign)
            self.state = 72
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CircuitSATParser.RULE_functionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssertFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Assert(self):
            return self.getToken(CircuitSATParser.Assert, 0)
        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertFunctionCall" ):
                listener.enterAssertFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertFunctionCall" ):
                listener.exitAssertFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertFunctionCall" ):
                return visitor.visitAssertFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class SizeFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Size(self):
            return self.getToken(CircuitSATParser.Size, 0)
        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeFunctionCall" ):
                listener.enterSizeFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeFunctionCall" ):
                listener.exitSizeFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeFunctionCall" ):
                return visitor.visitSizeFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class PrintlnFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Println(self):
            return self.getToken(CircuitSATParser.Println, 0)
        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)
        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)
        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintlnFunctionCall" ):
                listener.enterPrintlnFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintlnFunctionCall" ):
                listener.exitPrintlnFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintlnFunctionCall" ):
                return visitor.visitPrintlnFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(CircuitSATParser.Identifier, 0)
        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)
        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)
        def exprList(self):
            return self.getTypedRuleContext(CircuitSATParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierFunctionCall" ):
                listener.enterIdentifierFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierFunctionCall" ):
                listener.exitIdentifierFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierFunctionCall" ):
                return visitor.visitIdentifierFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class PrintFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Print(self):
            return self.getToken(CircuitSATParser.Print, 0)
        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFunctionCall" ):
                listener.enterPrintFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFunctionCall" ):
                listener.exitPrintFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintFunctionCall" ):
                return visitor.visitPrintFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def functionCall(self):

        localctx = CircuitSATParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircuitSATParser.Identifier]:
                localctx = CircuitSATParser.IdentifierFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(CircuitSATParser.Identifier)
                self.state = 75
                self.match(CircuitSATParser.OParen)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 76
                    self.exprList()


                self.state = 79
                self.match(CircuitSATParser.CParen)
                pass
            elif token in [CircuitSATParser.Println]:
                localctx = CircuitSATParser.PrintlnFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(CircuitSATParser.Println)
                self.state = 81
                self.match(CircuitSATParser.OParen)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 82
                    self.expression(0)


                self.state = 85
                self.match(CircuitSATParser.CParen)
                pass
            elif token in [CircuitSATParser.Print]:
                localctx = CircuitSATParser.PrintFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(CircuitSATParser.Print)
                self.state = 87
                self.match(CircuitSATParser.OParen)
                self.state = 88
                self.expression(0)
                self.state = 89
                self.match(CircuitSATParser.CParen)
                pass
            elif token in [CircuitSATParser.Assert]:
                localctx = CircuitSATParser.AssertFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.match(CircuitSATParser.Assert)
                self.state = 92
                self.match(CircuitSATParser.OParen)
                self.state = 93
                self.expression(0)
                self.state = 94
                self.match(CircuitSATParser.CParen)
                pass
            elif token in [CircuitSATParser.Size]:
                localctx = CircuitSATParser.SizeFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.match(CircuitSATParser.Size)
                self.state = 97
                self.match(CircuitSATParser.OParen)
                self.state = 98
                self.expression(0)
                self.state = 99
                self.match(CircuitSATParser.CParen)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStat(self):
            return self.getTypedRuleContext(CircuitSATParser.IfStatContext,0)


        def End(self):
            return self.getToken(CircuitSATParser.End, 0)

        def elseIfStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ElseIfStatContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ElseIfStatContext,i)


        def elseStat(self):
            return self.getTypedRuleContext(CircuitSATParser.ElseStatContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = CircuitSATParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.ifStat()
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.elseIfStat() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CircuitSATParser.Else:
                self.state = 110
                self.elseStat()


            self.state = 113
            self.match(CircuitSATParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(CircuitSATParser.If, 0)

        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def Do(self):
            return self.getToken(CircuitSATParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(CircuitSATParser.BlockContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_ifStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = CircuitSATParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(CircuitSATParser.If)
            self.state = 116
            self.expression(0)
            self.state = 117
            self.match(CircuitSATParser.Do)
            self.state = 118
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else(self):
            return self.getToken(CircuitSATParser.Else, 0)

        def If(self):
            return self.getToken(CircuitSATParser.If, 0)

        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def Do(self):
            return self.getToken(CircuitSATParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(CircuitSATParser.BlockContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_elseIfStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfStat" ):
                listener.enterElseIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfStat" ):
                listener.exitElseIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfStat" ):
                return visitor.visitElseIfStat(self)
            else:
                return visitor.visitChildren(self)




    def elseIfStat(self):

        localctx = CircuitSATParser.ElseIfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseIfStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(CircuitSATParser.Else)
            self.state = 121
            self.match(CircuitSATParser.If)
            self.state = 122
            self.expression(0)
            self.state = 123
            self.match(CircuitSATParser.Do)
            self.state = 124
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else(self):
            return self.getToken(CircuitSATParser.Else, 0)

        def Do(self):
            return self.getToken(CircuitSATParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(CircuitSATParser.BlockContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_elseStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStat" ):
                listener.enterElseStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStat" ):
                listener.exitElseStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStat" ):
                return visitor.visitElseStat(self)
            else:
                return visitor.visitChildren(self)




    def elseStat(self):

        localctx = CircuitSATParser.ElseStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(CircuitSATParser.Else)
            self.state = 127
            self.match(CircuitSATParser.Do)
            self.state = 128
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Def(self):
            return self.getToken(CircuitSATParser.Def, 0)

        def Identifier(self):
            return self.getToken(CircuitSATParser.Identifier, 0)

        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)

        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)

        def block(self):
            return self.getTypedRuleContext(CircuitSATParser.BlockContext,0)


        def End(self):
            return self.getToken(CircuitSATParser.End, 0)

        def idList(self):
            return self.getTypedRuleContext(CircuitSATParser.IdListContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = CircuitSATParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(CircuitSATParser.Def)
            self.state = 131
            self.match(CircuitSATParser.Identifier)
            self.state = 132
            self.match(CircuitSATParser.OParen)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CircuitSATParser.Identifier:
                self.state = 133
                self.idList()


            self.state = 136
            self.match(CircuitSATParser.CParen)
            self.state = 137
            self.block()
            self.state = 138
            self.match(CircuitSATParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(CircuitSATParser.For, 0)

        def Identifier(self):
            return self.getToken(CircuitSATParser.Identifier, 0)

        def Assign(self):
            return self.getToken(CircuitSATParser.Assign, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)


        def To(self):
            return self.getToken(CircuitSATParser.To, 0)

        def Do(self):
            return self.getToken(CircuitSATParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(CircuitSATParser.BlockContext,0)


        def End(self):
            return self.getToken(CircuitSATParser.End, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = CircuitSATParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CircuitSATParser.For)
            self.state = 141
            self.match(CircuitSATParser.Identifier)
            self.state = 142
            self.match(CircuitSATParser.Assign)
            self.state = 143
            self.expression(0)
            self.state = 144
            self.match(CircuitSATParser.To)
            self.state = 145
            self.expression(0)
            self.state = 146
            self.match(CircuitSATParser.Do)
            self.state = 147
            self.block()
            self.state = 148
            self.match(CircuitSATParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(CircuitSATParser.While, 0)

        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def Do(self):
            return self.getToken(CircuitSATParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(CircuitSATParser.BlockContext,0)


        def End(self):
            return self.getToken(CircuitSATParser.End, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = CircuitSATParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(CircuitSATParser.While)
            self.state = 151
            self.expression(0)
            self.state = 152
            self.match(CircuitSATParser.Do)
            self.state = 153
            self.block()
            self.state = 154
            self.match(CircuitSATParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssemblerStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asm(self):
            return self.getToken(CircuitSATParser.Asm, 0)

        def End(self):
            return self.getToken(CircuitSATParser.End, 0)

        def opcode(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.OpcodeContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.OpcodeContext,i)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_assemblerStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssemblerStatement" ):
                listener.enterAssemblerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssemblerStatement" ):
                listener.exitAssemblerStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssemblerStatement" ):
                return visitor.visitAssemblerStatement(self)
            else:
                return visitor.visitChildren(self)




    def assemblerStatement(self):

        localctx = CircuitSATParser.AssemblerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assemblerStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(CircuitSATParser.Asm)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.OpNew) | (1 << CircuitSATParser.OpNot) | (1 << CircuitSATParser.OpAnd) | (1 << CircuitSATParser.OpOr) | (1 << CircuitSATParser.OpNand) | (1 << CircuitSATParser.OpNor) | (1 << CircuitSATParser.OpXor) | (1 << CircuitSATParser.OpEqu) | (1 << CircuitSATParser.OpCopy) | (1 << CircuitSATParser.OpPut))) != 0):
                self.state = 157
                self.opcode()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
            self.match(CircuitSATParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.Identifier)
            else:
                return self.getToken(CircuitSATParser.Identifier, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.Comma)
            else:
                return self.getToken(CircuitSATParser.Comma, i)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = CircuitSATParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(CircuitSATParser.Identifier)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CircuitSATParser.Comma:
                self.state = 166
                self.match(CircuitSATParser.Comma)
                self.state = 167
                self.match(CircuitSATParser.Identifier)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.Comma)
            else:
                return self.getToken(CircuitSATParser.Comma, i)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = CircuitSATParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.expression(0)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CircuitSATParser.Comma:
                self.state = 174
                self.match(CircuitSATParser.Comma)
                self.state = 175
                self.expression(0)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CircuitSATParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BoolExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Bool(self):
            return self.getToken(CircuitSATParser.Bool, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)


    class NumberExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(CircuitSATParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpression" ):
                listener.enterNumberExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpression" ):
                listener.exitNumberExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpression" ):
                return visitor.visitNumberExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(CircuitSATParser.Identifier, 0)
        def indexes(self):
            return self.getTypedRuleContext(CircuitSATParser.IndexesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Excl(self):
            return self.getToken(CircuitSATParser.Excl, 0)
        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def Or(self):
            return self.getToken(CircuitSATParser.Or, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpression" ):
                return visitor.visitOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Subtract(self):
            return self.getToken(CircuitSATParser.Subtract, 0)
        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpression" ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpression" ):
                listener.exitUnaryMinusExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpression" ):
                return visitor.visitUnaryMinusExpression(self)
            else:
                return visitor.visitChildren(self)


    class PowerExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def Pow(self):
            return self.getToken(CircuitSATParser.Pow, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpression" ):
                listener.enterPowerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpression" ):
                listener.exitPowerExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpression" ):
                return visitor.visitPowerExpression(self)
            else:
                return visitor.visitChildren(self)


    class EqExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def Equals(self):
            return self.getToken(CircuitSATParser.Equals, 0)
        def NEquals(self):
            return self.getToken(CircuitSATParser.NEquals, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpression" ):
                listener.enterEqExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpression" ):
                listener.exitEqExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpression" ):
                return visitor.visitEqExpression(self)
            else:
                return visitor.visitChildren(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def And(self):
            return self.getToken(CircuitSATParser.And, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpression" ):
                return visitor.visitAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def In(self):
            return self.getToken(CircuitSATParser.In, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInExpression" ):
                listener.enterInExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInExpression" ):
                listener.exitInExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInExpression" ):
                return visitor.visitInExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def String(self):
            return self.getToken(CircuitSATParser.String, 0)
        def indexes(self):
            return self.getTypedRuleContext(CircuitSATParser.IndexesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)
        def indexes(self):
            return self.getTypedRuleContext(CircuitSATParser.IndexesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionExpression" ):
                listener.enterExpressionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionExpression" ):
                listener.exitExpressionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionExpression" ):
                return visitor.visitExpressionExpression(self)
            else:
                return visitor.visitChildren(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def Add(self):
            return self.getToken(CircuitSATParser.Add, 0)
        def Subtract(self):
            return self.getToken(CircuitSATParser.Subtract, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpression" ):
                listener.enterAddExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpression" ):
                listener.exitAddExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpression" ):
                return visitor.visitAddExpression(self)
            else:
                return visitor.visitChildren(self)


    class CompExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def GTEquals(self):
            return self.getToken(CircuitSATParser.GTEquals, 0)
        def LTEquals(self):
            return self.getToken(CircuitSATParser.LTEquals, 0)
        def GT(self):
            return self.getToken(CircuitSATParser.GT, 0)
        def LT(self):
            return self.getToken(CircuitSATParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompExpression" ):
                listener.enterCompExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompExpression" ):
                listener.exitCompExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompExpression" ):
                return visitor.visitCompExpression(self)
            else:
                return visitor.visitChildren(self)


    class NullExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Null(self):
            return self.getToken(CircuitSATParser.Null, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullExpression" ):
                listener.enterNullExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullExpression" ):
                listener.exitNullExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullExpression" ):
                return visitor.visitNullExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(CircuitSATParser.FunctionCallContext,0)

        def indexes(self):
            return self.getTypedRuleContext(CircuitSATParser.IndexesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpression" ):
                return visitor.visitFunctionCallExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def Multiply(self):
            return self.getToken(CircuitSATParser.Multiply, 0)
        def Divide(self):
            return self.getToken(CircuitSATParser.Divide, 0)
        def Modulus(self):
            return self.getToken(CircuitSATParser.Modulus, 0)
        def IDivide(self):
            return self.getToken(CircuitSATParser.IDivide, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpression" ):
                listener.enterMultExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpression" ):
                listener.exitMultExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultExpression" ):
                return visitor.visitMultExpression(self)
            else:
                return visitor.visitChildren(self)


    class ListExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(CircuitSATParser.ListContext,0)

        def indexes(self):
            return self.getTypedRuleContext(CircuitSATParser.IndexesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpression" ):
                listener.enterListExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpression" ):
                listener.exitListExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpression" ):
                return visitor.visitListExpression(self)
            else:
                return visitor.visitChildren(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)

        def QMark(self):
            return self.getToken(CircuitSATParser.QMark, 0)
        def Colon(self):
            return self.getToken(CircuitSATParser.Colon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpression" ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpression" ):
                listener.exitTernaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpression" ):
                return visitor.visitTernaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class InputExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitSATParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Input(self):
            return self.getToken(CircuitSATParser.Input, 0)
        def OParen(self):
            return self.getToken(CircuitSATParser.OParen, 0)
        def CParen(self):
            return self.getToken(CircuitSATParser.CParen, 0)
        def String(self):
            return self.getToken(CircuitSATParser.String, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputExpression" ):
                listener.enterInputExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputExpression" ):
                listener.exitInputExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputExpression" ):
                return visitor.visitInputExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircuitSATParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = CircuitSATParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 182
                self.match(CircuitSATParser.Subtract)
                self.state = 183
                self.expression(20)
                pass

            elif la_ == 2:
                localctx = CircuitSATParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 184
                self.match(CircuitSATParser.Excl)
                self.state = 185
                self.expression(19)
                pass

            elif la_ == 3:
                localctx = CircuitSATParser.NumberExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 186
                self.match(CircuitSATParser.Number)
                pass

            elif la_ == 4:
                localctx = CircuitSATParser.BoolExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.match(CircuitSATParser.Bool)
                pass

            elif la_ == 5:
                localctx = CircuitSATParser.NullExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.match(CircuitSATParser.Null)
                pass

            elif la_ == 6:
                localctx = CircuitSATParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.functionCall()
                self.state = 191
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 190
                    self.indexes()


                pass

            elif la_ == 7:
                localctx = CircuitSATParser.ListExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.list_()
                self.state = 195
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 194
                    self.indexes()


                pass

            elif la_ == 8:
                localctx = CircuitSATParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 197
                self.match(CircuitSATParser.Identifier)
                self.state = 199
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 198
                    self.indexes()


                pass

            elif la_ == 9:
                localctx = CircuitSATParser.StringExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 201
                self.match(CircuitSATParser.String)
                self.state = 203
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 202
                    self.indexes()


                pass

            elif la_ == 10:
                localctx = CircuitSATParser.ExpressionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                self.match(CircuitSATParser.OParen)
                self.state = 206
                self.expression(0)
                self.state = 207
                self.match(CircuitSATParser.CParen)
                self.state = 209
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 208
                    self.indexes()


                pass

            elif la_ == 11:
                localctx = CircuitSATParser.InputExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 211
                self.match(CircuitSATParser.Input)
                self.state = 212
                self.match(CircuitSATParser.OParen)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CircuitSATParser.String:
                    self.state = 213
                    self.match(CircuitSATParser.String)


                self.state = 216
                self.match(CircuitSATParser.CParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 249
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = CircuitSATParser.PowerExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 219
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 220
                        self.match(CircuitSATParser.Pow)
                        self.state = 221
                        self.expression(18)
                        pass

                    elif la_ == 2:
                        localctx = CircuitSATParser.MultExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 222
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 223
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Multiply) | (1 << CircuitSATParser.Divide) | (1 << CircuitSATParser.IDivide) | (1 << CircuitSATParser.Modulus))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 224
                        self.expression(18)
                        pass

                    elif la_ == 3:
                        localctx = CircuitSATParser.AddExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 225
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 226
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CircuitSATParser.Add or _la==CircuitSATParser.Subtract):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 227
                        self.expression(17)
                        pass

                    elif la_ == 4:
                        localctx = CircuitSATParser.CompExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 228
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 229
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.GTEquals) | (1 << CircuitSATParser.LTEquals) | (1 << CircuitSATParser.GT) | (1 << CircuitSATParser.LT))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 230
                        self.expression(16)
                        pass

                    elif la_ == 5:
                        localctx = CircuitSATParser.EqExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 231
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 232
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CircuitSATParser.Equals or _la==CircuitSATParser.NEquals):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 233
                        self.expression(15)
                        pass

                    elif la_ == 6:
                        localctx = CircuitSATParser.AndExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 234
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 235
                        self.match(CircuitSATParser.And)
                        self.state = 236
                        self.expression(14)
                        pass

                    elif la_ == 7:
                        localctx = CircuitSATParser.OrExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 237
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 238
                        self.match(CircuitSATParser.Or)
                        self.state = 239
                        self.expression(13)
                        pass

                    elif la_ == 8:
                        localctx = CircuitSATParser.TernaryExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 240
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 241
                        self.match(CircuitSATParser.QMark)
                        self.state = 242
                        self.expression(0)
                        self.state = 243
                        self.match(CircuitSATParser.Colon)
                        self.state = 244
                        self.expression(12)
                        pass

                    elif la_ == 9:
                        localctx = CircuitSATParser.InExpressionContext(self, CircuitSATParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 246
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 247
                        self.match(CircuitSATParser.In)
                        self.state = 248
                        self.expression(11)
                        pass

             
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBracket(self):
            return self.getToken(CircuitSATParser.OBracket, 0)

        def CBracket(self):
            return self.getToken(CircuitSATParser.CBracket, 0)

        def exprList(self):
            return self.getTypedRuleContext(CircuitSATParser.ExprListContext,0)


        def getRuleIndex(self):
            return CircuitSATParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = CircuitSATParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(CircuitSATParser.OBracket)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                self.state = 255
                self.exprList()


            self.state = 258
            self.match(CircuitSATParser.CBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBracket(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.OBracket)
            else:
                return self.getToken(CircuitSATParser.OBracket, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)


        def CBracket(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.CBracket)
            else:
                return self.getToken(CircuitSATParser.CBracket, i)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_indexes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexes" ):
                listener.enterIndexes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexes" ):
                listener.exitIndexes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexes" ):
                return visitor.visitIndexes(self)
            else:
                return visitor.visitChildren(self)




    def indexes(self):

        localctx = CircuitSATParser.IndexesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_indexes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 260
                    self.match(CircuitSATParser.OBracket)
                    self.state = 261
                    self.expression(0)
                    self.state = 262
                    self.match(CircuitSATParser.CBracket)

                else:
                    raise NoViableAltException(self)
                self.state = 266 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpNew(self):
            return self.getToken(CircuitSATParser.OpNew, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.Identifier)
            else:
                return self.getToken(CircuitSATParser.Identifier, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.ExpressionContext,i)


        def OpNot(self):
            return self.getToken(CircuitSATParser.OpNot, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.Comma)
            else:
                return self.getToken(CircuitSATParser.Comma, i)

        def OpAnd(self):
            return self.getToken(CircuitSATParser.OpAnd, 0)

        def OpOr(self):
            return self.getToken(CircuitSATParser.OpOr, 0)

        def OpNand(self):
            return self.getToken(CircuitSATParser.OpNand, 0)

        def OpNor(self):
            return self.getToken(CircuitSATParser.OpNor, 0)

        def OpXor(self):
            return self.getToken(CircuitSATParser.OpXor, 0)

        def OpEqu(self):
            return self.getToken(CircuitSATParser.OpEqu, 0)

        def OpCopy(self):
            return self.getToken(CircuitSATParser.OpCopy, 0)

        def OpPut(self):
            return self.getToken(CircuitSATParser.OpPut, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_opcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcode" ):
                listener.enterOpcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcode" ):
                listener.exitOpcode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcode" ):
                return visitor.visitOpcode(self)
            else:
                return visitor.visitChildren(self)




    def opcode(self):

        localctx = CircuitSATParser.OpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_opcode)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircuitSATParser.OpNew]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(CircuitSATParser.OpNew)
                self.state = 269
                self.match(CircuitSATParser.Identifier)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 270
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpNot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(CircuitSATParser.OpNot)
                self.state = 274
                self.match(CircuitSATParser.Identifier)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 275
                    self.expression(0)


                self.state = 278
                self.match(CircuitSATParser.Comma)
                self.state = 279
                self.match(CircuitSATParser.Identifier)
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 280
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpAnd]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(CircuitSATParser.OpAnd)
                self.state = 284
                self.match(CircuitSATParser.Identifier)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 285
                    self.expression(0)


                self.state = 288
                self.match(CircuitSATParser.Comma)
                self.state = 289
                self.match(CircuitSATParser.Identifier)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 290
                    self.expression(0)


                self.state = 293
                self.match(CircuitSATParser.Comma)
                self.state = 294
                self.match(CircuitSATParser.Identifier)
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 295
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpOr]:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.match(CircuitSATParser.OpOr)
                self.state = 299
                self.match(CircuitSATParser.Identifier)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 300
                    self.expression(0)


                self.state = 303
                self.match(CircuitSATParser.Comma)
                self.state = 304
                self.match(CircuitSATParser.Identifier)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 305
                    self.expression(0)


                self.state = 308
                self.match(CircuitSATParser.Comma)
                self.state = 309
                self.match(CircuitSATParser.Identifier)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 310
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpNand]:
                self.enterOuterAlt(localctx, 5)
                self.state = 313
                self.match(CircuitSATParser.OpNand)
                self.state = 314
                self.match(CircuitSATParser.Identifier)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 315
                    self.expression(0)


                self.state = 318
                self.match(CircuitSATParser.Comma)
                self.state = 319
                self.match(CircuitSATParser.Identifier)
                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 320
                    self.expression(0)


                self.state = 323
                self.match(CircuitSATParser.Comma)
                self.state = 324
                self.match(CircuitSATParser.Identifier)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 325
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpNor]:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.match(CircuitSATParser.OpNor)
                self.state = 329
                self.match(CircuitSATParser.Identifier)
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 330
                    self.expression(0)


                self.state = 333
                self.match(CircuitSATParser.Comma)
                self.state = 334
                self.match(CircuitSATParser.Identifier)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 335
                    self.expression(0)


                self.state = 338
                self.match(CircuitSATParser.Comma)
                self.state = 339
                self.match(CircuitSATParser.Identifier)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 340
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpXor]:
                self.enterOuterAlt(localctx, 7)
                self.state = 343
                self.match(CircuitSATParser.OpXor)
                self.state = 344
                self.match(CircuitSATParser.Identifier)
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 345
                    self.expression(0)


                self.state = 348
                self.match(CircuitSATParser.Comma)
                self.state = 349
                self.match(CircuitSATParser.Identifier)
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 350
                    self.expression(0)


                self.state = 353
                self.match(CircuitSATParser.Comma)
                self.state = 354
                self.match(CircuitSATParser.Identifier)
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 355
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpEqu]:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
                self.match(CircuitSATParser.OpEqu)
                self.state = 359
                self.match(CircuitSATParser.Identifier)
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 360
                    self.expression(0)


                self.state = 363
                self.match(CircuitSATParser.Comma)
                self.state = 364
                self.match(CircuitSATParser.Identifier)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 365
                    self.expression(0)


                self.state = 368
                self.match(CircuitSATParser.Comma)
                self.state = 369
                self.match(CircuitSATParser.Identifier)
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 370
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpCopy]:
                self.enterOuterAlt(localctx, 9)
                self.state = 373
                self.match(CircuitSATParser.OpCopy)
                self.state = 374
                self.match(CircuitSATParser.Identifier)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 375
                    self.expression(0)


                self.state = 378
                self.match(CircuitSATParser.Comma)
                self.state = 379
                self.match(CircuitSATParser.Identifier)
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 380
                    self.expression(0)


                pass
            elif token in [CircuitSATParser.OpPut]:
                self.enterOuterAlt(localctx, 10)
                self.state = 383
                self.match(CircuitSATParser.OpPut)
                self.state = 384
                self.match(CircuitSATParser.Identifier)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 385
                    self.expression(0)


                self.state = 388
                self.match(CircuitSATParser.Comma)
                self.state = 389
                self.match(CircuitSATParser.Identifier)
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.Println) | (1 << CircuitSATParser.Print) | (1 << CircuitSATParser.Input) | (1 << CircuitSATParser.Assert) | (1 << CircuitSATParser.Size) | (1 << CircuitSATParser.Null) | (1 << CircuitSATParser.Excl) | (1 << CircuitSATParser.Subtract) | (1 << CircuitSATParser.OBracket) | (1 << CircuitSATParser.OParen) | (1 << CircuitSATParser.Bool) | (1 << CircuitSATParser.Number) | (1 << CircuitSATParser.Identifier) | (1 << CircuitSATParser.String))) != 0):
                    self.state = 390
                    self.expression(0)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 10)
         




