/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    INT = 258,                     /* INT  */
    PLUS = 259,                    /* PLUS  */
    MINUS = 260,                   /* MINUS  */
    MULT = 261,                    /* MULT  */
    DIV = 262,                     /* DIV  */
    OP = 263,                      /* OP  */
    CP = 264,                      /* CP  */
    OC = 265,                      /* OC  */
    CC = 266,                      /* CC  */
    EQUAL = 267,                   /* EQUAL  */
    IDENTIFIER = 268,              /* IDENTIFIER  */
    PONTOVIRGULA = 269,            /* PONTOVIRGULA  */
    EQUALEQUAL = 270,              /* EQUALEQUAL  */
    MAIORQ = 271,                  /* MAIORQ  */
    MENORQ = 272,                  /* MENORQ  */
    AND = 273,                     /* AND  */
    OR = 274,                      /* OR  */
    NOT = 275,                     /* NOT  */
    DOT = 276,                     /* DOT  */
    STRING = 277,                  /* STRING  */
    VIRGULA = 278,                 /* VIRGULA  */
    DOISPONTOS = 279,              /* DOISPONTOS  */
    VARTYPE = 280,                 /* VARTYPE  */
    READ = 281,                    /* READ  */
    PRINT = 282,                   /* PRINT  */
    IF = 283,                      /* IF  */
    ELSE = 284,                    /* ELSE  */
    PV = 285,                      /* PV  */
    WHILE = 286,                   /* WHILE  */
    RETURN = 287                   /* RETURN  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define INT 258
#define PLUS 259
#define MINUS 260
#define MULT 261
#define DIV 262
#define OP 263
#define CP 264
#define OC 265
#define CC 266
#define EQUAL 267
#define IDENTIFIER 268
#define PONTOVIRGULA 269
#define EQUALEQUAL 270
#define MAIORQ 271
#define MENORQ 272
#define AND 273
#define OR 274
#define NOT 275
#define DOT 276
#define STRING 277
#define VIRGULA 278
#define DOISPONTOS 279
#define VARTYPE 280
#define READ 281
#define PRINT 282
#define IF 283
#define ELSE 284
#define PV 285
#define WHILE 286
#define RETURN 287

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
