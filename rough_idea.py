from __future__ import print_function

from collections import OrderedDict
from json import loads
from re import sub

from flask import Flask, jsonify, request, Response
from flask.json import JSONEncoder


class Keyword(object):

    def __init__(self, keyword, argument):
        self.keyword = keyword
        self.argument = argument

    def __str__(self):
        return "%s = %s" % (self.keyword, self.argument)


class FlexibleJsonEncoder(JSONEncoder):

    def default(self, object_to_encode):
        if isinstance(object_to_encode, Keyword):
            return object_to_encode.argument
        return object_to_encode


class Host(OrderedDict):

    def __init__(self, name=None, **set_keywords):
        OrderedDict.__init__(self)
        self['host'] = Keyword('host', name)
        for keyword, argument in set_keywords.items():
            self[keyword.lower()] = Keyword(keyword, argument)

    def __str__(self):
        output = "%s\n" % self['host']
        for keyword in [
                internal_keyword
                for internal_keyword
                in self
                if internal_keyword != 'host'
        ]:
            output += "    %s\n" % self[keyword]
        output += '\n'
        return output


class SshConfig(OrderedDict):

    def __init__(self, file_path):
        OrderedDict.__init__(self)
        self.file_path = file_path

    def __str__(self):
        output = ''
        for host in self:
            output += "# %s\n%s" % (host, self[host])
        return sub(r'\n+$', '\n', output)

app = Flask(__name__)
app.json_encoder = FlexibleJsonEncoder

config_file = SshConfig('some/file/path')

dummy_host = Host('fakehost', user='fakeuser')
dummy_host['hostname'] = Keyword('hostname', 'fakehostname')
dummy_host['port'] = Keyword('port', 9001)

config_file['host1'] = dummy_host
config_file['host2'] = dummy_host


@app.route('/hosts', methods=['GET'])
def get_hosts():
    hosts = []
    for host in config_file:
        hosts.append(config_file[host])
    return jsonify(hosts)


@app.route('/hosts', methods=['POST'])
def create_host():
    new_host = Host(**request.json)
    return jsonify(new_host)


@app.route('/config', methods=['GET'])
def get_config():
    return jsonify(config_file)


@app.route('/config', methods=['POST'])
def create_config():
    new_config = SshConfig('some/file/path')
    return Response('It doesn\'t do anything yet', 200)
