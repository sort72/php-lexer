import ply.yacc as yacc
from php_lexer import tokens
import php_lexer
import sys

VERBOSE = 1

def p_program(p):
	'program : header_declaration declaration_list footer_declaration'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration'
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
                    | selection_stmt
                    | iteration_stmt
				    | fun_declaration
                    | show_in_screen
                    | expression_stmt'''

	pass

def p_header_declaration(p):
    'header_declaration : LESS QUESTIONMARK PHP'
    pass

def p_footer_declaration(p):
    'footer_declaration : QUESTIONMARK GREATER'
    pass

def p_show_in_screen_1(p):
    'show_in_screen : ECHO var_val SEMICOLON'
    pass

def p_show_in_screen_2(p):
    'show_in_screen : ECHO CADENA1 SEMICOLON'
    pass

def p_show_in_screen_3(p):
    'show_in_screen : ECHO CADENA2 SEMICOLON'
    pass
def p_show_in_screen_3(p):
    'show_in_screen : ECHO selection_stmt'
    pass

def p_var_declaration_1(p):
	'var_declaration : var_declaration2 SEMICOLON'
	pass

def p_var_declaration_2(p):
	'var_declaration : VARIABLE LBRACKET NUMBER RBRACKET SEMICOLON'
	pass

def p_var_declaration_3(p):                     
	'''var_declaration2 : VARIABLE
                        | VARIABLE COMMA var_declaration2
                        | VARIABLE EQUAL NUMBER COMMA var_declaration2
                        | VARIABLE EQUAL NUMBER
                        | VARIABLE EQUAL VARIABLE COMMA var_declaration2
                        | VARIABLE EQUAL VARIABLE
                        | COMMA 
                        | VARIABLE EQUAL VARIABLE simple_expression
                        | VARIABLE EQUAL LBRACKET NUMBER COMMA var_declaration2
                        | NUMBER COMMA var_declaration2
                        | NUMBER RBRACKET
                        | VARIABLE EQUAL LBRACKET CADENA1 COMMA var_declaration2
                        | CADENA1 COMMA var_declaration2
                        | CADENA1 RBRACKET
        '''
	pass

def p_fun_declaration(p):
	'fun_declaration : FUNCTION VARIABLE2 LPAREN params RPAREN statement'
	pass

def p_params_1(p):
	'params : param_list'
	pass

def p_param_list_1(p):
	'param_list : param_list COMMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_1(p):
	'param : VARIABLE'
	pass

def p_param_2(p):
	'param : VARIABLE LBRACKET RBRACKET'
	pass 

def p_param_3(p):
    'param : empty_function'
    pass

def p_compount_stmt(p):
	'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_1(p):
    'local_declarations : var_declaration'
    pass

def p_local_declarations_2(p):
	'local_declarations : empty_function'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : statement'
	pass
def p_statement_list_3(p):
	'statement_list : empty_function'
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
                | show_in_screen
				| return_stmt
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt_1(p):
    'selection_stmt : IF LPAREN expression RPAREN statement'
    pass

def p_selection_stmt_2(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
    pass

def p_selection_stmt_3(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSEIF statement'
    pass

def p_selection_stmt_4(p):
	'selection_stmt : SWITCH LPAREN var_val RPAREN statement'
	pass

def p_selection_stmt_5(p):
	'selection_stmt : CASE NUMBER COLON statement BREAK SEMICOLON'
	pass

def p_selection_stmt_6(p):
	'selection_stmt : DEFAULT COLON statement BREAK SEMICOLON'
	pass

def p_selection_stmt_7(p):
    'selection_stmt : VARIABLE relop VARIABLE QUESTIONMARK expression COLON expression SEMICOLON'
    pass

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement'
	pass

def p_iteration_stmt_3(p):
    'iteration_stmt : FOREACH LPAREN var_val AS var_val RPAREN statement'
    pass

def p_return_stmt_1(p):
	'return_stmt : RETURN SEMICOLON'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression SEMICOLON'
	pass

def p_expression_1(p):
	'expression : var_val EQUAL expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_var_1(p):
	'var_val : VARIABLE'
	pass

def p_var_2(p):
	'var_val : VARIABLE LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass


def p_relop(p):
	'''relop : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
			| ISEQUAL
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term
                                              
        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass


def p_additive_expression_3(p):
	'additive_expression : term MINUSMINUS'
	pass

def p_additive_expression_4(p):
	'additive_expression : term PLUSPLUS'
	pass

def p_additive_expression_5(p):
    '''additive_expression : addop term
                                            
    '''
    pass

def p_addop(p):
	'''addop : PLUS 
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_term_3(p):
    'term : CADENA1'
    pass

def p_term_4(p):
    'term : CADENA2'
    pass


def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var_val'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMBER' 
	pass

def p_call_1(p):
	'call : VARIABLE2 LPAREN args RPAREN'
	pass


def p_args(p):
	'''args : args_list
			| empty_function
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty_function(p):
	'empty_function :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			pass
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'index.php'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
	#input()