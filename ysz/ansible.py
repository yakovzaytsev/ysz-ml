import re


def host(hosts):
    with open(hosts) as f:
        data = f.read()
    s = re.search('(\d+\.\d+\.\d+\.\d+)', data)
    if s is None:
        s = re.search('(.*\w+.\w+)(\s+|$)', data) # XXX
    host = s.group(1)
    key_filename = None
    s = re.search('ansible_ssh_private_key_file=', data)
    if s is None:
        return [host], None
    _, i = s.span()
    key_filename = ''
    while data[i] != '\n':
        key_filename += data[i]
        i = i + 1
    return [host], key_filename


