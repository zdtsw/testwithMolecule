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


def test_consul_up(host):
    assert host.package("consul").is_installed
    assert host.ansible("package", "name=consul state=present")["changed"]
    assert host.process("consul").is_running is True


def test_consul_nginx_up(host):
    assert host.service("nginx").is_enabled is True
    assert host.service("consul").is_running


def test_consul_open(host):
    assert host.socket('tcp://0.0.0.0:8500').is_listening


def test_config_correct(host):
    assert host.file("/etc/consul/config.json").contains("advertise_addr")
