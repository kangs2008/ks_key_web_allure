import pytest, os, subprocess
from Common.handle_config import ReadWriteConfFile
from conftest import set_exec_ini
# cmd =['D:/allure-2.13.6/bin/allure generate D:/desk20201127/ks_web_allure/temp -o D:/desk20201127/ks_web_allure/Report --clean']

# pytest.main(['./TestCases/Login/test_login.py', '--alluredir', './temp'])


set_exec_ini('exec', 'exec_sheet_name', 't_接口测试')

pytest.main([])  # '--report','re2021'
cmd = 'allure generate ./temp -o ./Report --clean'
os.system(cmd)
