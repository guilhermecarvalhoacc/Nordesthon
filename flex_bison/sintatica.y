%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf(ERROR: %sn, s); }
%}

%token INT
%token PLUS
%token MINUS
%token MULT
%token DIV
%token OP
%token CP
%token OC
%token CC
%token EQUAL
%token IDENTIFIER
%token PONTOVIRGULA
%token EQUALEQUAL
%token MAIORQ
%token MENORQ
%token AND
%token OR
%token NOT
%token DOT
%token STRING
%token VIRGULA
%token DOISPONTOS
%token RETURN

%start program

%%

block : OC statement CC
      | OC CC
      ;


relexpression: expression EQUALEQUAL expression
             | expression MENORQ expression
             | expression MAIORQ expression
             | expression DOT expression
             | expression
             ;



expression: term PLUS term
          | term MINUS term
          | term OR term
          | term
          ;

term: factor
    | factor MULT factor
    | factor DIV factor
    | factor AND factor
    ;


factor: INT
    | STRING
    | IDENTIFIER
    | PLUS factor
    | MINUS factor
    | NOT factor
    | READ OP CP
    | OP relexpression CP
    ;


statement : VARTYPE IDENTIFIER EQUAL relexpression;
          | block
          | PRINT OP relexpression CP;
          | IF OP relexpression CP statement ELSE statement 
          | PV;
          | WHILE OP relexpression CP statement;
          | VARTYPE IDENTIFIER
          | VIRGULA IDENTIFIER;
          SEMI_COLON
          ;

%%

int main(){
  yyparse();
  return 0;
}