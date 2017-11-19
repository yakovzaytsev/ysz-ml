# ysz

My own personal library (Python >=3.6, MATLAB R2017B)

## Install to MATLAB

Add

    addpath path-to-ysz

to `startup.m`

    which startup

## Install to Python

Install from GitHub with pip 

Replace ??? with git hash

    pip install -e git+https://github.com/ysz/ysz.git@???#egg=ysz

or install HEAD

    pip install -e git+https://github.com/ysz/ysz.git#egg=ysz

## Documentation

- **thresholdHist** (MATLAB)

    **thresholdHist**(I, from, to) returns binary image with pixels in intensity range [from, to]

- hamcrest matchers for Ansible

    **TODO** ReadTheDocs

    Ensure Ansible playbook runs successfully

        from hamcrest import assert_that
        from ysz.hamcrest import ansible_playbook, runs_successfully


        def before_scenario(context, scenario):
            assert_that(ansible_playbook('myhosts', 'myplaybook.yml'),
                        runs_successfully())

