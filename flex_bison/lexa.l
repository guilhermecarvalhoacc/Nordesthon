%{
    #include <stdio.h>
    #include <string.h>
    #include "y.tab.h"
%}

%%
[ \t\n]
"BOTA"                  return PLUS;
"TIRA"                  return MINUS;
"Recebe"                return EQUAL;
"QueNem"                return EQUALEQUAL;
"MaisMiudoQ"            return MENORQ;
"MaisGraudoQ"           return MAIORQ;
"Nam"                   return NOT;
"ETBM"                  return AND;
"ou"                    return OR;
"("                     return OP;
")"                     return CP;
"{"                     return OC;
"}"                     return CC;
","                     return VIRGULA;
"."                     return DOT;
";"                     return PONTOVIRGULA;
"amostre"               return PRINT;
"DigaAi"                return READ;
"ArrochaEnquanto"       return WHILE;
"SoSe"                  return IF;
"SeNumFor"              return ELSE;
"Numero"                return VARTYPE;
"Texto"                 return VARTYPE;
"return"                return RETURN;
[a-zA-Z0-9]             return STRING;
[0-9]+                  return INT;
[a-zA-Z_][_a-zA-Z0-9]   return IDENTIFIER;

.                      printf("Token Inválido"); yyterminate();
%%