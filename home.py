# Tokens
BOOLEAN, AND,OR,LPAREN,RPAREN,EOF,EQUALS = 'BOOLEAN','AND','OR','(',')','EOF','='

class Token(object):
    def __init__(self, type,value):
        self.type = type
        self.value = value
    
    def __str__(self) -> str:
        return 'Token({type},{value})'.format(
            type = self.type,
            value = self.type
        )
    
#Lexical analysis/lexical analyzer--Tokenization
class Lexer(object):
    def __init__(self, bool_exp):
        self.text = bool_exp
        self.pos =0
        self.current_char = self.text[self.pos]

    def error():
        raise Exception("Unidentified tokn")
    
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_white_spaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_white_spaces()
                continue
            if self.current_char == '^':
                self.advance()
                return Token(AND,'^')
            if self.current_char == 'v':
                self.advance()
                return Token(OR,'v')
            if self.current_char == 'T':
                self.advance()
                return Token(BOOLEAN,'T')
            if self.current_char == 'F':
                self.advance()
                return Token(BOOLEAN,'F')
            if self.current_char == '(':
                self.advance()
                return Token(LPAREN,'(')
            if self.current_char ==')':
                self.advance()
                return Token(RPAREN,')')
            if self.current_char == '=':
                self.advance()
                return Token(EQUALS,'=')
            self.error()
        return Token(EOF,None)
    
#Both parsing and interpretation 
class Interpreter(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self,token_type):
        if self.current_token.type== token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def error():
        raise Exception("Syntax error")
    
    def factor(self):
        token = self.current_token

        if token.type == BOOLEAN:
            self.eat(BOOLEAN)
            if token.value =='T':
                return True
            else:
                return False
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result
        elif token.type == EQUALS:
            self.eat(EQUALS)
            result = self.equals()
            return result
    
    def equals(self):
        left = self.expr()
        self.current_token = self.lexer.get_next_token()
        if self.current_token.value == 'T':
            temp = True
        else:
            temp = False
        result = left ==temp
        return result

        
    def expr(self):
        result = self.factor()

        while self.current_token.type in (AND, OR):
            token = self.current_token
            if token.type == AND:
                self.eat(AND)
                result = result & self.factor()
            elif token.type == OR:
                self.eat(OR)
                result = result | self.factor()
        return result
        

def main():
    while True:
        try:
            bool_exp = input(">> ")
        except EOFError:
            break
        if not bool_exp:
            continue
        lexer = Lexer(bool_exp)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)
    

if __name__ == '__main__':
    main()
    