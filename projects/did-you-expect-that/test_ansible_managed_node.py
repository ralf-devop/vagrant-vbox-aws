
def test_ansible_user_exists(host):
    assert host.user("ansible").exists

def test_ansible_sudoers_conf_exists(host):
    sudoers_conf = host.file("/etc/sudoers.d/99_ansible")
    assert sudoers_conf.exists
    assert sudoers_conf.user == "root"
    assert sudoers_conf.group == "root"
    assert oct(sudoers_conf.mode) == "0o640"
