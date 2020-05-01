#로그인 애플리케이션
def login(_id):
    members = ['egoing','k8805','leezche']
    for member in members:
        if member == _id:
            return True
        return False
