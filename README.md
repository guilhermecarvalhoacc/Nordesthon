# Nordesthon

## *EBNF*

"Print" = Amostre 

"While" = ArrochaEnquanto

"IF" = SoSe

"Else" = SeNumFor

"Read" = DigaAi


PROGRAM = (λ | DECLARATION);

DECLARATION = ( "fn" , IDENTIFIER , "(" , ( IDENTIFIER, ( "," | ":") "TYPE", ",") | ")" , "->", TYPE, BLOCK);

BLOCK = ("{", λ , "}" | "{", STATEMENT,"}") ;

STATEMENT =  ((λ | (IDENTIFIER, ("=" , RELEXPRESSION) | , { RELEXPRESSION, ","}) | ("Amostre", "(", RELEXPRESSION, ")")  | VAR, ";")  | BLOCK | CONDITIONS | "retorne" , RELEXPRESSION);

CONDITIONS = ("SoSe", "(", RELEXPRESSION ,")", STATEMENT, (("SeNumFor", STATEMENT) | λ )) | ("ArrochaEnquanto", "(", RELEXPRESSION ,")", STATEMENT));

RELEXPRESSION = EXPRESSION , {("<" | ">" | "==") , EXPRESSION } ;

FACTOR = INT | STRING | IDENTIFIER | (( "+" | "-" | "!" ) , FACTOR) | "(" , RELEXPRESSION, ")" | READ, "(" , ")" ;

TERM = FACTOR, { ("Vez" | "Dividi" | "ETBM"), FACTOR };

EXPRESSION = TERM, { ("Bota" | "Tira" | "OU"), TERM } ;

ASSIGNMENT = (IDENTIFIER, "Recebe", RELEXPRESSION) | ( "(", { RELEXPRESSION, { "," | RELEXPRESSION } }, ")" );

READ = "DigaAi", "(" , ")" ;

VAR = ("Numero" | "Texto") , IDENTIFIER , (λ | {"," , IDENTIFIER });

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

STRING = """, (LETTER | DIGIT), """;
