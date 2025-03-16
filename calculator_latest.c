[calc.l]
%{
    #include "y.tab.h"
    #include <stdlib.h>
%}

%% 
[0-9]+    { yylval = atoi(yytext); return NUMBER; } 
[\t\n]    ;  /* Ignore tabs and newlines */
.         { return yytext[0]; } /* Return other characters */

%%

int yywrap() { return 1; }

[calc.y]
%{
    #include <stdio.h>
%}

%token NUMBER
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%% 

Expr: E { printf("\nResult = %d\n", $$); return 0; };

E: E '+' E { $$ = $1 + $3; }
 | E '-' E { $$ = $1 - $3; }
 | E '*' E { $$ = $1 * $3; }
 | E '/' E { $$ = $1 / $3; }
 | E '%' E { $$ = $1 % $3; }
 | '(' E ')' { $$ = $2; }
 | NUMBER { $$ = $1; }
 ;

%%

int main() {
    printf("\nEnter an arithmetic expression:\n");
    return yyparse();
}

void yyerror() {
    printf("\nInvalid expression\n");
}


[OUTPUT]
 lex calc.l
 yacc -d calc.y
 gcc lex.yy.c y.tab.c -w
 ./a.out
