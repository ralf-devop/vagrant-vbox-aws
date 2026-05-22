
def test_curl_is_installed(host):
    curl = host.package("curl-minimal")
    assert curl.is_installed

def test_jq_is_installed(host):
    jq = host.package("jq")
    assert jq.is_installed

def test_vim_is_installed(host):
    vim = host.package("vim-common")
    assert vim.is_installed
