# $ANTLR 3.1.2 Jump.g 2012-10-26 10:58:11

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class JumpLexer(Lexer):

    grammarFileName = "Jump.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start "T__18"
    def mT__18(self, ):

        try:
            _type = T__18
            _channel = DEFAULT_CHANNEL

            # Jump.g:7:7: ( ';' )
            # Jump.g:7:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__18"



    # $ANTLR start "T__19"
    def mT__19(self, ):

        try:
            _type = T__19
            _channel = DEFAULT_CHANNEL

            # Jump.g:8:7: ( ':' )
            # Jump.g:8:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__19"



    # $ANTLR start "T__20"
    def mT__20(self, ):

        try:
            _type = T__20
            _channel = DEFAULT_CHANNEL

            # Jump.g:9:7: ( '=' )
            # Jump.g:9:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__20"



    # $ANTLR start "T__21"
    def mT__21(self, ):

        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # Jump.g:10:7: ( 'goto' )
            # Jump.g:10:9: 'goto'
            pass 
            self.match("goto")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__21"



    # $ANTLR start "T__22"
    def mT__22(self, ):

        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # Jump.g:11:7: ( 'if' )
            # Jump.g:11:9: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):

        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # Jump.g:12:7: ( 'return' )
            # Jump.g:12:9: 'return'
            pass 
            self.match("return")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__23"



    # $ANTLR start "OP"
    def mOP(self, ):

        try:
            _type = OP
            _channel = DEFAULT_CHANNEL

            # Jump.g:62:4: ( ( '+' | '-' | '*' | '/' | '<' | '>' | '==' ) )
            # Jump.g:62:6: ( '+' | '-' | '*' | '/' | '<' | '>' | '==' )
            pass 
            # Jump.g:62:6: ( '+' | '-' | '*' | '/' | '<' | '>' | '==' )
            alt1 = 7
            LA1 = self.input.LA(1)
            if LA1 == 43:
                alt1 = 1
            elif LA1 == 45:
                alt1 = 2
            elif LA1 == 42:
                alt1 = 3
            elif LA1 == 47:
                alt1 = 4
            elif LA1 == 60:
                alt1 = 5
            elif LA1 == 62:
                alt1 = 6
            elif LA1 == 61:
                alt1 = 7
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # Jump.g:62:7: '+'
                pass 
                self.match(43)


            elif alt1 == 2:
                # Jump.g:62:11: '-'
                pass 
                self.match(45)


            elif alt1 == 3:
                # Jump.g:62:15: '*'
                pass 
                self.match(42)


            elif alt1 == 4:
                # Jump.g:62:19: '/'
                pass 
                self.match(47)


            elif alt1 == 5:
                # Jump.g:62:23: '<'
                pass 
                self.match(60)


            elif alt1 == 6:
                # Jump.g:62:27: '>'
                pass 
                self.match(62)


            elif alt1 == 7:
                # Jump.g:62:31: '=='
                pass 
                self.match("==")






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OP"



    # $ANTLR start "NUM"
    def mNUM(self, ):

        try:
            _type = NUM
            _channel = DEFAULT_CHANNEL

            # Jump.g:63:5: ( ( '-' )? ( '0' .. '9' )+ )
            # Jump.g:63:7: ( '-' )? ( '0' .. '9' )+
            pass 
            # Jump.g:63:7: ( '-' )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 45) :
                alt2 = 1
            if alt2 == 1:
                # Jump.g:63:7: '-'
                pass 
                self.match(45)



            # Jump.g:63:11: ( '0' .. '9' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # Jump.g:63:11: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM"



    # $ANTLR start "IDENT"
    def mIDENT(self, ):

        try:
            _type = IDENT
            _channel = DEFAULT_CHANNEL

            # Jump.g:64:7: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' )* )
            # Jump.g:64:9: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' )*
            pass 
            self.matchRange(97, 122)
            # Jump.g:64:17: ( 'a' .. 'z' | '0' .. '9' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57) or (97 <= LA4_0 <= 122)) :
                    alt4 = 1


                if alt4 == 1:
                    # Jump.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop4





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENT"



    # $ANTLR start "LABEL"
    def mLABEL(self, ):

        try:
            _type = LABEL
            _channel = DEFAULT_CHANNEL

            # Jump.g:65:7: ( 'A' .. 'Z' ( 'A' .. 'Z' | '0' .. '9' )* )
            # Jump.g:65:9: 'A' .. 'Z' ( 'A' .. 'Z' | '0' .. '9' )*
            pass 
            self.matchRange(65, 90)
            # Jump.g:65:17: ( 'A' .. 'Z' | '0' .. '9' )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90)) :
                    alt5 = 1


                if alt5 == 1:
                    # Jump.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LABEL"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # Jump.g:66:4: ( ( ' ' | '\\r' | '\\n' )+ )
            # Jump.g:66:6: ( ' ' | '\\r' | '\\n' )+
            pass 
            # Jump.g:66:6: ( ' ' | '\\r' | '\\n' )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 10 or LA6_0 == 13 or LA6_0 == 32) :
                    alt6 = 1


                if alt6 == 1:
                    # Jump.g:
                    pass 
                    if self.input.LA(1) == 10 or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1


            #action start
            _channel = HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # Jump.g:1:8: ( T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | OP | NUM | IDENT | LABEL | WS )
        alt7 = 11
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # Jump.g:1:10: T__18
            pass 
            self.mT__18()


        elif alt7 == 2:
            # Jump.g:1:16: T__19
            pass 
            self.mT__19()


        elif alt7 == 3:
            # Jump.g:1:22: T__20
            pass 
            self.mT__20()


        elif alt7 == 4:
            # Jump.g:1:28: T__21
            pass 
            self.mT__21()


        elif alt7 == 5:
            # Jump.g:1:34: T__22
            pass 
            self.mT__22()


        elif alt7 == 6:
            # Jump.g:1:40: T__23
            pass 
            self.mT__23()


        elif alt7 == 7:
            # Jump.g:1:46: OP
            pass 
            self.mOP()


        elif alt7 == 8:
            # Jump.g:1:49: NUM
            pass 
            self.mNUM()


        elif alt7 == 9:
            # Jump.g:1:53: IDENT
            pass 
            self.mIDENT()


        elif alt7 == 10:
            # Jump.g:1:59: LABEL
            pass 
            self.mLABEL()


        elif alt7 == 11:
            # Jump.g:1:65: WS
            pass 
            self.mWS()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\3\uffff\1\15\3\12\1\uffff\1\7\5\uffff\1\12\1\22\2\12\1\uffff\1"
        u"\12\1\26\1\12\1\uffff\1\12\1\31\1\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\32\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\12\2\uffff\1\75\1\157\1\146\1\145\1\uffff\1\60\5\uffff\1\164"
        u"\1\60\1\164\1\157\1\uffff\1\165\1\60\1\162\1\uffff\1\156\1\60\1"
        u"\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\172\2\uffff\1\75\1\157\1\146\1\145\1\uffff\1\71\5\uffff\1\164"
        u"\1\172\1\164\1\157\1\uffff\1\165\1\172\1\162\1\uffff\1\156\1\172"
        u"\1\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\4\uffff\1\7\1\uffff\1\10\1\11\1\12\1\13\1\3\4"
        u"\uffff\1\5\3\uffff\1\4\2\uffff\1\6"
        )

    DFA7_special = DFA.unpack(
        u"\32\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\14\2\uffff\1\14\22\uffff\1\14\11\uffff\2\7\1\uffff"
        u"\1\10\1\uffff\1\7\12\11\1\2\1\1\1\7\1\3\1\7\2\uffff\32\13\6\uffff"
        u"\6\12\1\4\1\12\1\5\10\12\1\6\10\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\12\12\47\uffff\32\12"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\12\12\47\uffff\32\12"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\12\12\47\uffff\32\12"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(JumpLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
