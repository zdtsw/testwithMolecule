import os
import rc

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']
            ).get_hosts('all')


def test_nginx_running_enabled(host):
    assert host.service("nginx").is_enabled is True
    assert host.service("nginx").is_running


def test_nginx_version(host):
    v = host.check_output("nginx -v")
    assert re.match(".*1.16.1.*", v)

