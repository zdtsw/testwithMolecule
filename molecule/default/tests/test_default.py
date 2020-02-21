import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_myservice_up(host):
    assert host.package("mypackage").is_installed
    assert host.ansible("package", "name=mypackage state=present")["changed"]
    assert host.process("myprocess").is_running is True


def test_myservice2_up(host):
    assert host.service("myservice2").is_enabled is True
    assert host.service("myservice2").is_running


def test_myport8080_open(host):
    assert host.socket('tcp://0.0.0.0:8080').is_listening


def test_myconfig_correct(host):
    assert host.file("myConfigFile").contains("keyword")


def test_mycmd_return(host):
    assert 'return_string' in host.run('myCommand').stdout
