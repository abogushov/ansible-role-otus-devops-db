import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mongo_running_and_enabled(host):
    # check if MongoDB is enabled and running
    mongo = host.service("mongod")
    assert mongo.is_running
    assert mongo.is_enabled
    assert host.socket("tcp://0.0.0.0:27017").is_listening


def test_config_file(host):
    # check if configuration file contains the required line
    config_file = host.file('/etc/mongod.conf')
    assert config_file.contains('bindIp: 0.0.0.0')
    assert config_file.is_file
