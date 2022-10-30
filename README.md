# Nordesthon

## *EBNF*

BLOCK = (λ | Statement);

STATEMENT =  (λ | ASSIGNMENT | ("Amostre", "(", RELEXPRESSION, ")")  | VAR  | BLOCK | ("SoSe", "(", RELEXPRESSION ,")", STATEMENT, (("SeNumFor", STATEMENT) | λ )) | ("ArrochaEnquanto", "(", RELEXPRESSION ,")", STATEMENT));

RELEXPRESSION = EXPRESSION , {("MaisMiudoQ" | "MaisGraudoQ" | QueNem") , EXPRESSION } ;

FACTOR = INT | STRING | IDENTIFIER | (( Bota | Tira | Nam ) , FACTOR) | "(" , RELEXPRESSION, ")" | READ, "(" , ")" ;

TERM = FACTOR, { ("Vez" | "Dvidi" | "E"), FACTOR };

EXPRESSION = TERM, { ("Bote" | "Tire" | "OU"), TERM } ;

ASSIGNMENT = (IDENTIFIER, "Recebe", RELEXPRESSION) | ( "(", { RELEXPRESSION, { "," | RELEXPRESSION } }, ")" );

VAR = ("Numero" | "Texto") , IDENTIFIER , (λ | {"," , IDENTIFIER });
