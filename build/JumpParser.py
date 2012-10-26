# $ANTLR 3.1.2 Jump.g 2012-10-26 10:58:11

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
STMT=6
T__23=23
T__22=22
T__21=21
T__20=20
ASSIGN1=8
ASSIGN2=9
EOF=-1
STATEMENT=5
NUM=16
IF=11
T__19=19
WS=17
EXPR=7
T__18=18
LABEL=13
OP=15
RETURN=12
IDENT=14
PROGRAM=4
GOTO=10

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "PROGRAM", "STATEMENT", "STMT", "EXPR", "ASSIGN1", "ASSIGN2", "GOTO", 
    "IF", "RETURN", "LABEL", "IDENT", "OP", "NUM", "WS", "';'", "':'", "'='", 
    "'goto'", "'if'", "'return'"
]




class JumpParser(Parser):
    grammarFileName = "Jump.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )






                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "prog"
    # Jump.g:20:1: prog : ( statement prog -> ^( PROGRAM statement prog ) | );
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement1 = None

        prog2 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_prog = RewriteRuleSubtreeStream(self._adaptor, "rule prog")
        try:
            try:
                # Jump.g:20:6: ( statement prog -> ^( PROGRAM statement prog ) | )
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == LABEL) :
                    alt1 = 1
                elif () :
                    alt1 = 2
                else:
                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # Jump.g:21:3: statement prog
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_prog81)
                    statement1 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement1.tree)
                    self._state.following.append(self.FOLLOW_prog_in_prog83)
                    prog2 = self.prog()

                    self._state.following.pop()
                    stream_prog.add(prog2.tree)

                    # AST Rewrite
                    # elements: statement, prog
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 22:3: -> ^( PROGRAM statement prog )
                    # Jump.g:22:6: ^( PROGRAM statement prog )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROGRAM, "PROGRAM"), root_1)

                    self._adaptor.addChild(root_1, stream_statement.nextTree())
                    self._adaptor.addChild(root_1, stream_prog.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt1 == 2:
                    # Jump.g:25:1: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "prog"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statement"
    # Jump.g:27:1: statement : label stmt ';' -> ^( STATEMENT label stmt ) ;
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal5 = None
        label3 = None

        stmt4 = None


        char_literal5_tree = None
        stream_18 = RewriteRuleTokenStream(self._adaptor, "token 18")
        stream_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule stmt")
        stream_label = RewriteRuleSubtreeStream(self._adaptor, "rule label")
        try:
            try:
                # Jump.g:27:11: ( label stmt ';' -> ^( STATEMENT label stmt ) )
                # Jump.g:28:3: label stmt ';'
                pass 
                self._state.following.append(self.FOLLOW_label_in_statement114)
                label3 = self.label()

                self._state.following.pop()
                stream_label.add(label3.tree)
                self._state.following.append(self.FOLLOW_stmt_in_statement116)
                stmt4 = self.stmt()

                self._state.following.pop()
                stream_stmt.add(stmt4.tree)
                char_literal5=self.match(self.input, 18, self.FOLLOW_18_in_statement118) 
                stream_18.add(char_literal5)

                # AST Rewrite
                # elements: stmt, label
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 29:3: -> ^( STATEMENT label stmt )
                # Jump.g:29:6: ^( STATEMENT label stmt )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STATEMENT, "STATEMENT"), root_1)

                self._adaptor.addChild(root_1, stream_label.nextTree())
                self._adaptor.addChild(root_1, stream_stmt.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "statement"

    class label_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "label"
    # Jump.g:32:1: label : LABEL ':' -> LABEL ;
    def label(self, ):

        retval = self.label_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LABEL6 = None
        char_literal7 = None

        LABEL6_tree = None
        char_literal7_tree = None
        stream_19 = RewriteRuleTokenStream(self._adaptor, "token 19")
        stream_LABEL = RewriteRuleTokenStream(self._adaptor, "token LABEL")

        try:
            try:
                # Jump.g:32:7: ( LABEL ':' -> LABEL )
                # Jump.g:33:3: LABEL ':'
                pass 
                LABEL6=self.match(self.input, LABEL, self.FOLLOW_LABEL_in_label141) 
                stream_LABEL.add(LABEL6)
                char_literal7=self.match(self.input, 19, self.FOLLOW_19_in_label143) 
                stream_19.add(char_literal7)

                # AST Rewrite
                # elements: LABEL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 34:3: -> LABEL
                self._adaptor.addChild(root_0, stream_LABEL.nextNode())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "label"

    class stmt_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "stmt"
    # Jump.g:37:1: stmt : ( IDENT '=' expr -> ^( ASSIGN1 IDENT expr ) | IDENT '=' e1= expr OP e2= expr -> ^( ASSIGN2 IDENT $e1 OP $e2) | 'goto' LABEL -> ^( GOTO LABEL ) | 'if' expr 'goto' LABEL -> ^( IF expr LABEL ) | 'return' expr -> ^( RETURN expr ) );
    def stmt(self, ):

        retval = self.stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT8 = None
        char_literal9 = None
        IDENT11 = None
        char_literal12 = None
        OP13 = None
        string_literal14 = None
        LABEL15 = None
        string_literal16 = None
        string_literal18 = None
        LABEL19 = None
        string_literal20 = None
        e1 = None

        e2 = None

        expr10 = None

        expr17 = None

        expr21 = None


        IDENT8_tree = None
        char_literal9_tree = None
        IDENT11_tree = None
        char_literal12_tree = None
        OP13_tree = None
        string_literal14_tree = None
        LABEL15_tree = None
        string_literal16_tree = None
        string_literal18_tree = None
        LABEL19_tree = None
        string_literal20_tree = None
        stream_21 = RewriteRuleTokenStream(self._adaptor, "token 21")
        stream_20 = RewriteRuleTokenStream(self._adaptor, "token 20")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_22 = RewriteRuleTokenStream(self._adaptor, "token 22")
        stream_LABEL = RewriteRuleTokenStream(self._adaptor, "token LABEL")
        stream_23 = RewriteRuleTokenStream(self._adaptor, "token 23")
        stream_OP = RewriteRuleTokenStream(self._adaptor, "token OP")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Jump.g:37:6: ( IDENT '=' expr -> ^( ASSIGN1 IDENT expr ) | IDENT '=' e1= expr OP e2= expr -> ^( ASSIGN2 IDENT $e1 OP $e2) | 'goto' LABEL -> ^( GOTO LABEL ) | 'if' expr 'goto' LABEL -> ^( IF expr LABEL ) | 'return' expr -> ^( RETURN expr ) )
                alt2 = 5
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # Jump.g:38:3: IDENT '=' expr
                    pass 
                    IDENT8=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_stmt160) 
                    stream_IDENT.add(IDENT8)
                    char_literal9=self.match(self.input, 20, self.FOLLOW_20_in_stmt162) 
                    stream_20.add(char_literal9)
                    self._state.following.append(self.FOLLOW_expr_in_stmt164)
                    expr10 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr10.tree)

                    # AST Rewrite
                    # elements: expr, IDENT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 39:3: -> ^( ASSIGN1 IDENT expr )
                    # Jump.g:39:6: ^( ASSIGN1 IDENT expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGN1, "ASSIGN1"), root_1)

                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 2:
                    # Jump.g:41:5: IDENT '=' e1= expr OP e2= expr
                    pass 
                    IDENT11=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_stmt183) 
                    stream_IDENT.add(IDENT11)
                    char_literal12=self.match(self.input, 20, self.FOLLOW_20_in_stmt185) 
                    stream_20.add(char_literal12)
                    self._state.following.append(self.FOLLOW_expr_in_stmt189)
                    e1 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(e1.tree)
                    OP13=self.match(self.input, OP, self.FOLLOW_OP_in_stmt191) 
                    stream_OP.add(OP13)
                    self._state.following.append(self.FOLLOW_expr_in_stmt195)
                    e2 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(e2.tree)

                    # AST Rewrite
                    # elements: e2, e1, IDENT, OP
                    # token labels: 
                    # rule labels: retval, e1, e2
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if e1 is not None:
                        stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "rule e1", e1.tree)
                    else:
                        stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "token e1", None)


                    if e2 is not None:
                        stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "rule e2", e2.tree)
                    else:
                        stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "token e2", None)


                    root_0 = self._adaptor.nil()
                    # 42:3: -> ^( ASSIGN2 IDENT $e1 OP $e2)
                    # Jump.g:42:6: ^( ASSIGN2 IDENT $e1 OP $e2)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGN2, "ASSIGN2"), root_1)

                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())
                    self._adaptor.addChild(root_1, stream_e1.nextTree())
                    self._adaptor.addChild(root_1, stream_OP.nextNode())
                    self._adaptor.addChild(root_1, stream_e2.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 3:
                    # Jump.g:44:5: 'goto' LABEL
                    pass 
                    string_literal14=self.match(self.input, 21, self.FOLLOW_21_in_stmt220) 
                    stream_21.add(string_literal14)
                    LABEL15=self.match(self.input, LABEL, self.FOLLOW_LABEL_in_stmt222) 
                    stream_LABEL.add(LABEL15)

                    # AST Rewrite
                    # elements: LABEL
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 45:3: -> ^( GOTO LABEL )
                    # Jump.g:45:6: ^( GOTO LABEL )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GOTO, "GOTO"), root_1)

                    self._adaptor.addChild(root_1, stream_LABEL.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 4:
                    # Jump.g:47:5: 'if' expr 'goto' LABEL
                    pass 
                    string_literal16=self.match(self.input, 22, self.FOLLOW_22_in_stmt239) 
                    stream_22.add(string_literal16)
                    self._state.following.append(self.FOLLOW_expr_in_stmt241)
                    expr17 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr17.tree)
                    string_literal18=self.match(self.input, 21, self.FOLLOW_21_in_stmt243) 
                    stream_21.add(string_literal18)
                    LABEL19=self.match(self.input, LABEL, self.FOLLOW_LABEL_in_stmt245) 
                    stream_LABEL.add(LABEL19)

                    # AST Rewrite
                    # elements: LABEL, expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 48:3: -> ^( IF expr LABEL )
                    # Jump.g:48:6: ^( IF expr LABEL )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IF, "IF"), root_1)

                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    self._adaptor.addChild(root_1, stream_LABEL.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 5:
                    # Jump.g:50:5: 'return' expr
                    pass 
                    string_literal20=self.match(self.input, 23, self.FOLLOW_23_in_stmt264) 
                    stream_23.add(string_literal20)
                    self._state.following.append(self.FOLLOW_expr_in_stmt266)
                    expr21 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr21.tree)

                    # AST Rewrite
                    # elements: expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 51:3: -> ^( RETURN expr )
                    # Jump.g:51:6: ^( RETURN expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RETURN, "RETURN"), root_1)

                    self._adaptor.addChild(root_1, stream_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "stmt"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "expr"
    # Jump.g:54:1: expr : ( IDENT -> ^( EXPR IDENT ) | NUM -> ^( EXPR NUM ) );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT22 = None
        NUM23 = None

        IDENT22_tree = None
        NUM23_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_NUM = RewriteRuleTokenStream(self._adaptor, "token NUM")

        try:
            try:
                # Jump.g:54:6: ( IDENT -> ^( EXPR IDENT ) | NUM -> ^( EXPR NUM ) )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENT) :
                    alt3 = 1
                elif (LA3_0 == NUM) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # Jump.g:55:3: IDENT
                    pass 
                    IDENT22=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_expr287) 
                    stream_IDENT.add(IDENT22)

                    # AST Rewrite
                    # elements: IDENT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 56:3: -> ^( EXPR IDENT )
                    # Jump.g:56:6: ^( EXPR IDENT )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_IDENT.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 2:
                    # Jump.g:58:5: NUM
                    pass 
                    NUM23=self.match(self.input, NUM, self.FOLLOW_NUM_in_expr304) 
                    stream_NUM.add(NUM23)

                    # AST Rewrite
                    # elements: NUM
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 59:3: -> ^( EXPR NUM )
                    # Jump.g:59:6: ^( EXPR NUM )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_NUM.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "expr"


    # Delegated rules


    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\16\1\24\3\uffff\1\16\2\17\2\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\27\1\24\3\uffff\1\20\2\22\2\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\3\uffff\1\2\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\1\6\uffff\1\2\1\3\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\uffff\1\7"),
        DFA.unpack(u"\1\10\2\uffff\1\11"),
        DFA.unpack(u"\1\10\2\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    DFA2 = DFA
 

    FOLLOW_statement_in_prog81 = frozenset([13])
    FOLLOW_prog_in_prog83 = frozenset([1])
    FOLLOW_label_in_statement114 = frozenset([14, 21, 22, 23])
    FOLLOW_stmt_in_statement116 = frozenset([18])
    FOLLOW_18_in_statement118 = frozenset([1])
    FOLLOW_LABEL_in_label141 = frozenset([19])
    FOLLOW_19_in_label143 = frozenset([1])
    FOLLOW_IDENT_in_stmt160 = frozenset([20])
    FOLLOW_20_in_stmt162 = frozenset([14, 16])
    FOLLOW_expr_in_stmt164 = frozenset([1])
    FOLLOW_IDENT_in_stmt183 = frozenset([20])
    FOLLOW_20_in_stmt185 = frozenset([14, 16])
    FOLLOW_expr_in_stmt189 = frozenset([15])
    FOLLOW_OP_in_stmt191 = frozenset([14, 16])
    FOLLOW_expr_in_stmt195 = frozenset([1])
    FOLLOW_21_in_stmt220 = frozenset([13])
    FOLLOW_LABEL_in_stmt222 = frozenset([1])
    FOLLOW_22_in_stmt239 = frozenset([14, 16])
    FOLLOW_expr_in_stmt241 = frozenset([21])
    FOLLOW_21_in_stmt243 = frozenset([13])
    FOLLOW_LABEL_in_stmt245 = frozenset([1])
    FOLLOW_23_in_stmt264 = frozenset([14, 16])
    FOLLOW_expr_in_stmt266 = frozenset([1])
    FOLLOW_IDENT_in_expr287 = frozenset([1])
    FOLLOW_NUM_in_expr304 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("JumpLexer", JumpParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
