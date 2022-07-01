Credentials for Sotka accounts stage/preprod.
emails same as for "https://login.yahoo.com/" email box and for sotka accounts

**Attorney Register**
email : testqa000000@yahoo.com ()
password : pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
generate password : ksbbaatxxwotyabq
sbn: 000000
sotka password: 1234Qwer

**Attorneyqa**
email : qaautomationatt@yahoo.com
password: pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
generate password : emxbsociwrqsdcwp
sbn : 000001
sotka password: 1234Qwer

**CR**
email : qaautomationcr@yahoo.com
password: pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
generate password : rsjbfjbpzorrntuc
sbn : 000000
sotka password: 1234Qwer

**OP**
email : qaautomationop@yahoo.com
password: pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
generate password : jphbtksnxhediwws
sbn : 000002
sotka password: 1234Qwer

**OP unregisterd**
email : qaautomationopunreg@yahoo.com
password: pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
generate password : gvwdvmcqjriiwupp
sbn : 000003
sotka password: 1234Qwer

**opunregisterdel**
email: qaautomationopunregdel@yahoo.com
password: pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
general password: ahcuxsimoybcetqn
000004

**Secr**
email : qaautomationsecr@yahoo.com
password: pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
generate password : fnasmhrlsacdmozz
password: 1234Qwer

**Secr del**
email : qaautomationsecrdel@yahoo.com
password: pDLm7$_Wsw+L2P? (for https://login.yahoo.com/ email box)
generate password : xudxrtihgkpxetfh
password: 1234Qwer

pages/application.py all pages objects

Commands for running test on jenkins:
pytho3 -m venv env38 (create environment)
. env38/bin/activate (run env)
pip3 install -r requirements.txt (install all dependency)
pytest tests --alluredir=target/allure-result (run all tests from folder "tests" and save report folder target/allure-result)