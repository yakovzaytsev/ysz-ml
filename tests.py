import os
import tempfile
from hamcrest import assert_that, equal_to, is_, none
from ysz import ansible


def test_host():
    inventories = {
        '1.2.3.4': """# used only in tests
[foo]
1.2.3.4 """,
        '1.2.3.4': """# used only in tests
[foo]
1.2.3.4""",
        'bar.com': """# used only in tests
[foo]
bar.com """,
        'bar.com': """# used only in tests
[foo]
bar.com""",
        'baz.bar.com': """# used only in tests
[foo]
baz.bar.com ansible_ssh_user=root""",
        '1.2.3.4': """# used only in tests
[foo]
1.2.3.4 ansible_ssh_user=root""",
        'baz.bar.com': """# used only in tests
[foo]
baz.bar.com ansible_ssh_user=root
""",
        '1.2.3.4': """# used only in tests
[foo]
1.2.3.4 ansible_ssh_user=root
""",

    }
    for host, inventory in inventories.items():
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(inventory.encode())
            fp.flush()
            hosts, key_filename = ansible.host(fp.name)
            assert_that(len(hosts), equal_to(1))
            assert_that(hosts[0], equal_to(host))
            # assert_that(key_filename, is_(none()))
    
    with tempfile.NamedTemporaryFile() as fp:
        fp.write("""[foo]
bar.com""".encode())
        fp.flush()
        hosts, key_filename = ansible.host(fp.name)
        path = os.path.expanduser('~/.ssh/id_rsa.pub')
        assert_that(key_filename, equal_to(path))

