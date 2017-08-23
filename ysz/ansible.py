import re


def host(hosts):
    with open(hosts) as f:
        data = f.read()
    s = re.search('\d+\.\d+\.\d+\.\d+', data)
    host = s.group(0)
    s = re.search('ansible_ssh_private_key_file=', data)
    _, i = s.span()
    key_filename = ''
    while data[i] != '\n':
        key_filename += data[i]
        i = i + 1
    return [host], key_filename


