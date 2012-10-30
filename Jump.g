grammar Jump;

options {
  language=Python;
  output=AST;
}

tokens {
  PROGRAM;
  STATEMENT;
  LABEL;
  STMT;
  EXPR;
  ASSIGN1;
  ASSIGN2;
  GOTO;
  IF;
  RETURN;
}

prog :
  statement*
  -> ^(PROGRAM statement*)
;

statement :
  label stmt ';'
  -> ^(STATEMENT label? stmt)
;

label :
  lbl=LABEL ':'
  -> ^(LABEL $lbl ':')
  
  | // epsilon
;

stmt :
  IDENT '=' expr
  -> ^(ASSIGN1 IDENT '=' expr)

  | IDENT '=' e1=expr OP e2=expr
  -> ^(ASSIGN2 IDENT '=' $e1 OP $e2)

  | 'goto' LABEL
  -> ^(GOTO LABEL)

  | 'if' expr 'goto' LABEL
  -> ^(IF expr LABEL)

  | 'return' expr
  -> ^(RETURN 'return' expr)
;

expr :
  IDENT
  -> IDENT

  | NUM
  -> NUM
;

OP : ('+'|'-'|'*'|'/'|'<'|'>'|'==') ;
NUM : '-'?'0'..'9'+ ;
IDENT : 'a'..'z'('a'..'z'|'0'..'9')* ;
LABEL : 'A'..'Z'('A'..'Z'|'0'..'9')* ;
WS : (' '|'\r'|'\n')+ {$channel = HIDDEN;} ;
