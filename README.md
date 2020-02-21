Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: testrole, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).



------------------

This is a demo project to show beginner how Molecule is working
In this repo, the "testrole" is the one we created with ansible and will be deployed to our target host
by running >molecule create role -r testrole
Molecule helps to setup a brand new folder with all the structure in place

testrole/molecule/default/molecule.yml is the file for config how ansible startup, which driver molecule to use, any env for container, which verifier to use etc

You main focus part for the testing should be all located in testrole/molecule/default which uses default scenario
Some basic commands to use:
>molecule create
>molecule test
>molecule login
>molecule destroy

Actions for each scenario:
lint=>dependency=>cleanup=>destroy
syntax
create
prepare
converge
idempotence=>side-effect
verify
cleanup
destroy

prepare is following plays in testrole/molecule/default/prepare.yml, this is optional 
converge is following plays in testrole/molecule/default/playbook.yml
verify is following plays in testrole/molecule/default/verify.yml, this is optional

https://docs.ansible.com/ansible-lint/rules/default_rules.html for you to follow ansible-lint error

It is good to have your .gitignore for pyc files

