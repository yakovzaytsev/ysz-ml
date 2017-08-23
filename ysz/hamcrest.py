import subprocess
import re
from hamcrest.core.base_matcher import BaseMatcher


class AnsiblePlaybook:

    def __init__(self, hosts, playbook):
        self.hosts = hosts
        self.playbook = playbook

    def run(self):
        self.cp = subprocess.run(['ansible-playbook', '-i',
                                  self.hosts,
                                  self.playbook], stdout=subprocess.PIPE)

    @property
    def returncode(self):
        return self.cp.returncode

    @property
    def stdout(self):
        return self.cp.stdout


class AnsiblePlaybookRunsWithReturnCode(BaseMatcher):

    def __init__(self, code):
        self.code = code

    def _matches(self, cp):
        if not isinstance(cp, AnsiblePlaybook):  # ???
            raise ValueError('item should be AnsiblePlaybook')
        cp.run()
        if self.code == 0:
            return (cp.returncode == self.code and
                    re.search('failed=0', cp.stdout.decode('utf8')))
        return cp.returncode == self.code

    def describe_to(self, description):
        if self.code == 0:
            text = 'playbook runs successfully'
        else:
            text = f'playbook fails with code {self.code}'
        description.append_text(text)


def ansible_playbook(hosts, playbook):
    return AnsiblePlaybook(hosts, playbook)


def runs_successfully():
    return AnsiblePlaybookRunsWithReturnCode(0)
