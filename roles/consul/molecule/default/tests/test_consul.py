import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parameterize("dependency", [
    ("cronie")
    ])

def test_os(host):
    os = host.system_info.distribution
    assert os == "centos"
    assert host.exists("yum")

def test_consul_dependencies(host, dependency):
    assert host.package(depedency).is_installed

def test_consul_installed_running(host):
    assert host.package("consul").is_installed
    assert host.ansible("package", "name=consul state=present")["changed"]
    assert host.process("consul").is_running is True

def test_consul_upgrade_version(host):
    v = host.check_output("consul -v")
    assert re.match("Consul v2.1.1", v)


def test_consul_is_open(host):
    assert host.socket('tcp://0.0.0.0:8500').is_listening


def test_consul_config(host):
    f = host.file("/etc/consul/config.json")
    a = host.addr("docker-local-test-consul").ipv4_addresses
    assert f.linked_to == "/etc/consul/server.json"
    assert f.contains("advertise_addr")
    assert f.contains(a)


def test (host):
     f = host.file("/etc/sysconfig/consul")
     assert f.user == 'root'
     assert f.group == 'root'
     assert f.mode == 0o644


