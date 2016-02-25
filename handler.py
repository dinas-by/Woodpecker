import http.client
import random
import re
import string


class Handler:
    def __init__(self, scenario):
        self.host = str
        self.set = str
        self.uri = str
        self.method = str
        self.body = ''
        self.scenario = scenario.splitlines()

    def handle_file(self):
        for line in self.scenario:
            if re.match('Set:.*', line, re.I):
                self.check_post_body()
                self.set = re.match('Set:.?(.*)', line, re.I).group(1)
            elif re.match('Host:.*', line, re.I):
                self.check_post_body()
                self.host = re.match('Host:.?(.*)', line, re.I).group(1)
            elif re.match('(GET) (/.*)', line, re.I):
                self.check_post_body()
                self.method, self.uri = re.match('(GET) (/.*)', line, re.I).group(1, 2)
                self.start_uri_test()
            elif re.match('(POST) (/.*)', line, re.I):
                self.method, self.uri = re.match('(POST) (/.*)', line, re.I).group(1, 2)
                self.check_post_body(start=True)
            elif self.body:
                self.body += line + '\n'

    def check_post_body(self, start=False):
        if self.body:
            self.start_test_with_body()
            self.body = ''
        elif start:
            self.body += '\n'

    def start_test_with_body(self):
        print(self.set)
        print(self.body)

    def start_uri_test(self):
        print(self.set, self.method, self.uri)



