grammar Jump;

options {
  language=Python;
  output=AST;
}

tokens {
  PROGRAM;
  STATEMENT;
  STMT;
  EXPR;
  ASSIGN1;
  ASSIGN2;
  GOTO;
  IF;
  RETURN;
}

prog :
  statement prog
  -> ^(PROGRAM statement prog)
  
  | // epsilon
;

statement :
  label stmt ';'
  -> ^(STATEMENT label stmt)
;

label :
  LABEL ':'
  -> LABEL
;

stmt :
  IDENT '=' expr
  -> ^(ASSIGN1 IDENT expr)

  | IDENT '=' e1=expr OP e2=expr
  -> ^(ASSIGN2 IDENT $e1 OP $e2)

  | goto=GOTO LABEL
  -> ^(GOTO $goto LABEL)

  | 'if' expr GOTO LABEL
  -> ^(IF expr GOTO LABEL)

  | 'return' expr
  -> ^(RETURN expr)
;

expr :
  IDENT
  -> ^(EXPR IDENT)

  | NUM
  -> ^(EXPR NUM)
;

OP : ('+'|'-'|'*'|'/'|'<'|'>'|'==') ;
NUM : '-'?'0'..'9'+ ;
IDENT : 'a'..'z'('a'..'z'|'0'..'9')* ;
LABEL : 'A'..'Z'('A'..'Z'|'0'..'9')* ;
GOTO : 'goto' ;
