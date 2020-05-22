##  RUN local manual docker test (without molecule)  
```cli
$GITROOT> ansible-galaxy install --force --roles-path ./roles -r requirements.yml
$GITROOT> docker run --detach --privileged --name docker-local-test-consul nexus.mycompany.com:18443/iac/docker-centos7-ansible:1.0.12
$GITROOT> ansible-playbook -i env/local consul.yml --extra-vars dest_hosts=local -vvv
```
when local test is done, remember to cleanup dependnecies roles in ./roles before push commits

```cli
$GITROOT> docker stop docker-local-test-consul
$GITROOT> docker rm docker-local-test-consul
```


## RUN local with molecule  
$GITROOT> cd roles/consul
$GITROOT> molecule test




## Pre-requisite for molecule to run  
#  install: python3 pip3 docker(not python-docker) git
#  user who runs it need setup ssh keys for gitlab.mycompany.com thus can download dependencies from requirements
#  user who runs it need to have docker token to pull image from nexus.mycompany.com


## MISC
#  Make sure "ansible-lint" is ran before code commit to master
#  molecule 3+ version has many difference compare to v2, molecule init role consul --verifier-name testinfra
##  goss is not support but only ansible and testinfra as verifier
##  lint is not support only to use external lint tools , see https://molecule.readthedocs.io/en/latest/configuration.html#lint
##  playbook.yaml rename to converge.yml
#  molecule only runs from roles/consul
# depedency download to ~/.cache/molecule/consul/default/roles/<depedency-roles>  (this is from molecule dependencies)


## Trobleshooting
# Cannot access docker container: 
make sure you can docker pull image,
make sure this image does exist,
make sure container started, if not can manually cleanup ~/.cache/molecule/consul/default/state.yml to have a fresh docker sanity check


