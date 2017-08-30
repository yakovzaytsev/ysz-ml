import tempfile
from hamcrest import assert_that, equal_to, is_, none
from ysz import ansible


def test_host():
    inventories = {
        '1.2.3.4': """[foo]
1.2.3.4 """,
        '1.2.3.4': """[foo]
1.2.3.4""",
        'bar.com': """[foo]
bar.com """,
        'bar.com': """[foo]
bar.com""",

    }
    for host, inventory in inventories.items():
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(inventory.encode())
            fp.flush()
            hosts, key_filename = ansible.host(fp.name)
            assert_that(len(hosts), equal_to(1))
            assert_that(hosts[0], equal_to(host))
            assert_that(key_filename, is_(none()))

