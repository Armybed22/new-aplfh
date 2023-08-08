import string
import pathlib


# STANDARD LIBRARIES
BASE_DIR = pathlib.Path(__file__).parent.parent
CURRENT_DIR = None

STDLIBS = [
    'Argparser',
    'Array',
    'Math',
    'System',
    'String',
    'Winlib',
]


# CONSTANTS
DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS


class Position:
    '''Cursor Position'''

    def __init__(self, idx, ln, col, fn, ftxt):
        """_summary_

        Args:
            idx (_type_): _description_
            ln (_type_): _description_
            col (_type_): _description_
            fn (function): _description_
            ftxt (_type_): _description_
        """
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
        """_summary_

        Args:
            current_char (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)


# TOKENS
TT_INT = 'INT'  # 123456
TT_FLOAT = 'FLOAT'  # 5.5
TT_STRING = 'STRING'  # "Hello World"
TT_IDENTIFIER = 'IDENTIFIER'  # var_name
TT_KEYWORD = 'KEYWORD'  # v, if, for, while, f
TT_PLUS = 'PLUS'  # Plus
TT_MINUS = 'MINUS'  # Minus
TT_MUL = 'MUL'  # Times
TT_DIV = 'DIV'  # Divide
TT_POW = 'POW'  # Power
TT_MOD = 'MOD'  # Modulo
TT_EQ = 'EQ'  # Equal
TT_LPAREN = 'LPAREN'  # (
TT_RPAREN = 'RPAREN'  # )
TT_LBRACE = 'LBRACE'  # {
TT_RBRACE = 'RBRACE'  # }
TT_LSQUARE = 'LSQUARE'  # [
TT_RSQUARE = 'RSQUARE'  # ]
TT_EE = 'EE'  # Equal Equal
TT_NE = 'NE'  # Not Equal
TT_LT = 'LT'  # Less Than
TT_GT = 'GT'  # Greater Than
TT_LTE = 'LTE'  # Less Than or Equal
TT_GTE = 'GTE'  # Greater Than or Equal
TT_PE = 'PE'  # Plus Equal
TT_ME = 'ME'  # Minus Equal
TT_TE = 'TE'  # Times Equal
TT_DE = 'DE'  # Divide Equal
TT_IDIV = 'IDIV'  # Int Divide
TT_MDE = 'MDE'  # Modulo Divide Equal
TT_POWE = 'POWE'  # Power Equal
TT_COMMA = 'COMMA'  # ,
TT_COLON = 'COLON'  # :
TT_ARROW = 'ARROW'  # ->
TT_NEWLINE = 'NEWLINE'  # \n
TT_DOT = 'DOT'  # .
TT_EOF = 'EOF'  # End Of File

KEYWORDS = [
    'v',
    'and',
    'or',
    'not',
    'if',
    'elif',
    'else',
    'for',
    'to',
    'step',
    'while',
    'f',
    'return',
    'continue',
    'break',
    'class',
    'include',
]


class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        """_summary_

        Args:
            type_ (_type_): _description_
            value (_type_, optional): _description_. Defaults to None.
            pos_start (_type_, optional): _description_. Defaults to None.
            pos_end (_type_, optional): _description_. Defaults to None.
        """
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

    def matches(self, type_, value):
        """_summary_

        Args:
            type_ (_type_): _description_
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.type == type_ and self.value == value

    def __repr__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
