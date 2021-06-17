import requests
url = 'http://129.211.184.235/api/login_register/register/'
for i in range(2, 1000):
    data = {'uid': 'testuser' + str(i), 'pwd': '111111', 'mail': 'testuser' + str(i) + '@example.com',
            'trueName': 'testuser' + str(i), 'studentId': str(19000000 + i)}
    res = requests.post(url, data=data)#data可以直接传字典
    print(i)
    print(res)