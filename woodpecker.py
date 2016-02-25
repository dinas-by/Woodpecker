import sys
from handler import Handler

try:
    with open(sys.argv[1], 'r') as file_body:
        scenario = file_body.read()
except IndexError:
    sys.exit('Woodpecker: apium filename')
except FileNotFoundError:
    sys.exit('File %s do not exist' % sys.argv[1])


parser = Handler(scenario)
test_suit = parser.handle_file()
