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

STATEMENT =  ((λ | (ASSIGNMENT | "(" , (")" | RELEXPRESSION, ",") | ("Amostre", "(", RELEXPRESSION, ")")  | VAR, ";")  | BLOCK | CONDITIONS | "retorne" , RELEXPRESSION);

CONDITIONS = ("SoSe", "(", RELEXPRESSION ,")", STATEMENT, (("SeNumFor", STATEMENT) | λ )) | ("ArrochaEnquanto", "(", RELEXPRESSION ,")", STATEMENT));

RELEXPRESSION = EXPRESSION , {("<" | ">" | "==") , EXPRESSION } ;

FACTOR = INT | STRING | IDENTIFIER_FACTOR | (( "+" | "-" | "!" ) , FACTOR) | "(" , RELEXPRESSION, ")" | READ, "(" , ")" ;

IDENTIFIER_FACTOR = ( λ | "(" , ( ")" | { RELEXPRESSION, "," }, ")" );

TERM = FACTOR, { ("*" | "/" | "&&"), FACTOR };

EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;

ASSIGNMENT = (IDENTIFIER, "=", RELEXPRESSION) | ( "(", { RELEXPRESSION, { "," | RELEXPRESSION } }, ")" );

READ = "DigaAi", "(" , ")" ;

VAR = ("Numero" | "Texto") , IDENTIFIER , (λ | {"," , IDENTIFIER });

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

STRING = """, (LETTER | DIGIT), """;
