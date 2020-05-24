import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']
            ).get_hosts('all')


def test_sensuclient_running_enabled(host):
    assert host.service("sensu_client").is_enabled is True
    assert host.service("sensu_client").is_running


def test_sensuclient_version(host):
    v = host.check_output("sensu-client -v")
    assert re.match(".*1.0.3.*", v)

