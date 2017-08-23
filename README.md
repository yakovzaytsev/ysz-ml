# ysz

Assorted utilities (Python >=3.6)

## Install from GitHub with pip 

Replace ??? with git hash

    pip install -e git+https://github.com/ysz/ysz.git@???#egg=ysz

or install HEAD

    pip install -e git+https://github.com/ysz/ysz.git#egg=ysz

## Hamcrest matchers for Ansible

Ensure Ansible playbook runs successfully

    from hamcrest import assert_that
    from ysz.hamcrest import ansible_playbook, runs_successfully


    def before_scenario(context, scenario):
        assert_that(ansible_playbook('myhosts', 'myplaybook.yml'),
                    runs_successfully())

