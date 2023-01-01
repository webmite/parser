import enum
import re
import FCUnit as fcu

class TokenType(enum.Enum):
    T_NUM = 0
    T_PLUS = 1
    T_MINUS = 2
    T_MULT = 3
    T_DIV = 4
    T_LPAR = 5
    T_RPAR = 6
    T_UNIT = 7
    T_END = 8
    
class Node:
    def __init__(self, str_token, token_type, value=None):
        self.token=str_token
        self.token_type = token_type
        self.value = value
        self.children = []
    
    def print(self):
        print (f'{self.token} : {self.value}') 
    

def lexical_analysis(s):
    mappings = {
        '+': TokenType.T_PLUS,
        '-': TokenType.T_MINUS,
        '*': TokenType.T_MULT,
        '/': TokenType.T_DIV,
        '(': TokenType.T_LPAR,
        ')': TokenType.T_RPAR}

    tokens = []
    token_type = None
    buf=''
    for c in s:
        if c in mappings:
            if token_type == TokenType.T_NUM and len(buf) > 0:
                token = Node(buf,TokenType.T_NUM, value=float(buf))
                tokens.append(token)
                buf=''
            elif token_type == TokenType.T_UNIT and len(buf) > 0:
                if fcu.isUnit(buf):
                    unit = fcu.FCUnit(buf)
                    if mappings[c] == TokenType.T_LPAR:
                        token = Node(buf,TokenType.T_UNIT, value=unit.value)
                        tokens.append(token)
                        tokens.append(Node('*',TokenType.T_MULT,'*'))
                    else:    
                        tokens.append(Node('*',TokenType.T_MULT,'*'))
                        token = Node(buf,TokenType.T_UNIT, value=unit.value)
                        tokens.append(token)
                else:
                    raise Exception(f'Unknown Unit: {buf}')
                buf=''
            token_type = mappings[c]
            token = Node(c,token_type, value=c)
            tokens.append(token)
        elif re.match(r'\s',c):
            if token_type == TokenType.T_NUM and len(buf) > 0:
                token = Node(buf,TokenType.T_NUM, value=float(buf))
                tokens.append(token)
                buf=''
                token_type=None
            continue
        elif re.match(r'[0-9.,]', c):
            buf += c
            token_type=TokenType.T_NUM
            continue
        elif re.match(r'[a-zA-zµ"\']',c):
            if token_type == TokenType.T_NUM and len(buf) > 0:
                token = Node(buf,TokenType.T_NUM, value=float(buf))
                tokens.append(token)
                buf=''
            buf += c
            token_type=TokenType.T_UNIT
            continue
        else:
            raise Exception(f'Invalid token: {c}')

    if token_type == TokenType.T_NUM and len(buf) > 0:
        token = Node(buf,TokenType.T_NUM, value=float(buf))
        tokens.append(token)
        buf=''
    elif token_type == TokenType.T_UNIT and len(buf) > 0:
        if fcu.isUnit(buf):
            unit = fcu.FCUnit(buf)
            tokens.append(Node('*',TokenType.T_MULT,'*'))
            token = Node(buf,TokenType.T_UNIT, value=unit.value)
            tokens.append(token)
            buf=''
        else:
            raise Exception(f'Unknown Unit: {buf}')
    token_type = None
    tokens.append(Node('$',TokenType.T_END,'$'))
    return tokens


def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise Exception(f'Invalid syntax on token {tokens[0].token_type}')
        #raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))


def parse_e(tokens):
    left_node = parse_e2(tokens)

    while tokens[0].token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e2(tokens))
        left_node = node

    return left_node


def parse_e2(tokens):
    left_node = parse_e3(tokens)

    while tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node

    return left_node


def parse_e3(tokens):
    if tokens[0].token_type in [TokenType.T_NUM, TokenType.T_UNIT]:
        return tokens.pop(0)

    match(tokens, TokenType.T_LPAR)
    expression = parse_e(tokens)
    match(tokens, TokenType.T_RPAR)

    return expression


def parse(inputstring):
    tokens = lexical_analysis(inputstring)
    # print('-- analysis --')
    # for token in tokens:
    #     token.print()
    # print('-- end --')
    ast = parse_e(tokens)
    match(tokens, TokenType.T_END)
    return ast
