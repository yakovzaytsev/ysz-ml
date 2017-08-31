import fileinput
import os
import re


def host(hosts):
    data = ''
    # skip comments
    with fileinput.input(files=(hosts)) as f:
        for line in f:
            if line[0] == '#':
                continue
            data += line
    s = re.search('(\d+\.\d+\.\d+\.\d+)', data)
    if s is None:
        s = re.search('(.*\w+\.\w+)(\s+|$)', data) # XXX
    host = s.group(1)
    key_filename = None
    s = re.search('ansible_ssh_private_key_file=', data)
    if s is None:
        return [host], os.path.expanduser('~/.ssh/id_rsa.pub')
    _, i = s.span()
    key_filename = ''
    while data[i] != '\n':
        key_filename += data[i]
        i = i + 1
    return [host], key_filename


