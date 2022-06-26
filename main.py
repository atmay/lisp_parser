# blah
from lisp_parser import parse


test_data = """
(test lisp expression)
( # commentary here
    also
    multi-line
    (multi-inserted lists)
    structure here
)

example: ( dotted . pair )
"""


def main():
    expression = parse(test_data)

    print(expression)


if __name__ == '__main__':
    main()
