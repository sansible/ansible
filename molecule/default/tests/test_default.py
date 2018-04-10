import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pip_packes(host):
    pip_packages = host.pip_package.get_packages()
    assert pip_packages.get('ansible').get('version') == '2.4.3.0'
    assert pip_packages.get('cryptography').get('version') == '2.2.2'
    assert pip_packages.get('setuptools').get('version') == '39.0.1'


def test_ansible_version(host):
    ansible_version = host.run('ansible --version')
    assert 'ansible 2.4.3.0' in ansible_version.stdout
