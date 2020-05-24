import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']
            ).get_hosts('all')


def test_filebeat_running_enabled(host):
    assert host.service("filebeat").is_enabled is True
    assert host.service("filebeat").is_running




def test_filebeat_version(host):
    v = host.check_output("filebeat -v")
    assert re.match(".*6.2.2.*", v)

