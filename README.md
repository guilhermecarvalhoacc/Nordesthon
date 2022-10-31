# Nordesthon

## *EBNF*

"Print" = Amostre 

"+" = Bota

"-" = Tira

"While" = ArrochaEnquanto

"IF" = SoSe

"Else" = SeNumFor

"Read" = DigaAi

"!" = Nam

"*" = Vez

"/" = Dividi


BLOCK = (λ | Statement);

STATEMENT =  ((λ | ASSIGNMENT | ("Amostre", "(", RELEXPRESSION, ")")  | VAR, ";")  | BLOCK | CONDITIONS);

CONDITIONS = ("SoSe", "(", RELEXPRESSION ,")", STATEMENT, (("SeNumFor", STATEMENT) | λ )) | ("ArrochaEnquanto", "(", RELEXPRESSION ,")", STATEMENT));

RELEXPRESSION = EXPRESSION , {("MaisMiudoQ" | "MaisGraudoQ" | QueNem") , EXPRESSION } ;

FACTOR = INT | STRING | IDENTIFIER | (( Bota | Tira | Nam ) , FACTOR) | "(" , RELEXPRESSION, ")" | READ, "(" , ")" ;

TERM = FACTOR, { ("Vez" | "Dividi" | "E"), FACTOR };

EXPRESSION = TERM, { ("Bota" | "Tira" | "OU"), TERM } ;

ASSIGNMENT = (IDENTIFIER, "Recebe", RELEXPRESSION) | ( "(", { RELEXPRESSION, { "," | RELEXPRESSION } }, ")" );

READ = "DigaAi", "(" , ")" ;

VAR = ("Numero" | "Texto") , IDENTIFIER , (λ | {"," , IDENTIFIER });

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

STRING = """, (LETTER | DIGIT), """;
