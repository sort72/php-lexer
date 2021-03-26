import ply.lex as lex
import sys

#Alejandro Ortega, Nicole Rios, Jhon Edison Parra

# https://www.dabeaz.com/ply/ply.html#ply_nn6
reserved = {
    'and' : 'AND',
    'array' : 'ARRAY',
    'as' : 'AS',
    'break' : 'BREAK',
    'callable' : 'CALLABLE',
    'case' : 'CASE',
    'cath' : 'CATH',
    'class' : 'CLASS',
    'clone' : 'CLONE',
    'const' : 'CONST',
    'continue' : 'CONTINUE',
    'declare' : 'DECLARE',
    'default' : 'DEFAULT',
    'die' : 'DIE',
    'do' : 'DO',
    'echo' : 'ECHO',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'empty' : 'EMPTY',
    'enddeclare' : 'ENDDECLARE',
    'endfor' : 'ENDFOR',
    'endforeach' : 'ENDFOREACH',
    'endif' : 'ENDIF',
    'endswitch' : 'ENDSWITCH',
    'endwhile' : 'ENDWHILE',
    'eval' : 'EVAL',
    'exit' : 'EXIT',
    'extends' : 'EXTENDS',
    'final' : 'FINAL',
    'finally' : 'FINALLY',
    'fn' : 'FN',
    'for' : 'FOR',
    'foreach' : 'FOREACH',
    'function' : 'FUNCTION',
    'global' : 'GLOBAL',
    'goto' : 'GOTO',
    'if' : 'IF',
    'implements' : 'IMPLEMENTS',
    'include' : 'INCLUDE',
    'include_once' : 'INCLUDE_ONCE',
    'instanceof' : 'INSTANCEOF',
    'insteadof' : 'INSTEADOF',
    'interface' : 'INTERFACE',
    'isset' : 'ISSET',
    'list' : 'LIST',
    'match' : 'MATCH',
    'namespace' : 'NAMESPACE',
    'new' : 'NEW',
    'or' : 'OR',
    'php' : 'PHP',
    'print' : 'PRINT',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'public' : 'PUBLIC',
    'require' : 'REQUIRE',
    'require_once' : 'REQUIRE_ONCE',
    'return' : 'RETURN',
    'static' : 'STATIC',
    'switch' : 'SWITCH',
    'this' : 'THIS',
    'throw' : 'THROW',
    'trait' : 'TRAIT',
    'try' : 'TRY',
    'unset' : 'UNSET',
    'use' : 'USE',
    'var' : 'VAR',
    'while' : 'WHILE',
    'xor' : 'XOR',
    'yield' : 'YIELD',
    'yield from' : 'YIELDFROM',
    '__CLASS__' : '__CLASS__',
    '__DIR__' : '__DIR__',
    '__FILE__' : '__FILE__',
    '__FUNCTION__' : '__FUNCTION__',
    '__LINE__' : '__LINE__',
    '__METHOD__' : '__METHOD__',
    '__NAMESPACE__' : '__NAMESPACE__',
    '__TRAIT__' : '__TRAIT__',
}

tokens = [
    # Symbols
    'MOD',
    'PLUS',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'QUESTIONMARK',
    'COMILLASIMPLE',
    'COMILLASDOBLES',

    #variables
    'DOLLAR',

    # Others   
    'VARIABLE', 
    'VARIABLE2', 
    'NUMBER',
    'CADENA1',
    'CADENA2',
    'ID',
] + list(reserved.values())

# Regular expressions rules for simple tokens
t_MOD = r'%'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_COMILLASIMPLE = r'\''
t_COMILLASDOBLES = r'\"'
t_QUESTIONMARK = r'\?'
 
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'\$[^0-9]\w*(\d|\w)*'
    return t

# Check reserved words
# This approach greatly reduces the number of regular expression rules and is likely to make things a little faster.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        t_error(t)

def t_CADENA1(t):
    r'\"([^\"].)*\"'
    return t
def t_CADENA2(t):
    r'\'([^\'].)*\''
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:     
		tok = lexer.token()
		if not tok:
			break
		print(tok)


lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'index.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	#lexer.input(data)
	test(data, lexer)
	#input()

