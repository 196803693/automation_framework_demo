'''一些支持方法，例如加密'''
import hashlib
from utils.log import logger

class EncryptError(Exception):
    pass

def encrypt(string,salt='',encrypt_way='MD5'):
    """根据输入的string与加密盐，按照encrypt方式进行加密，并返回加密后的字符串"""
    string += salt
    if encrypt_way == 'MD5':
        hash_string = hashlib.md5()
    elif encrypt_way == 'SHA1':
        hash_string = hashlib.sha1()
    else:
        logger.exception(EncryptError('请输入正确的加密方式，目前只支持MD5和SHA1'))
        return False
    hash_string.update(string.encode())
    return hash_string.hexdigest()

def sign(sign_dict,private_key='',encrypt_way='MD5'):
    '''
    :param sign_dict: 待签名的字典
    :param private_key: 加密盐
    :param encrypt_way: 加密方式，默认MD5
    :return: 返回签名后字符串，用&连接
    '''
    dict_keys = sorted(sign_dict)
    string = ''
    for key in dict_keys:
        if sign_dict[key] == None:
            pass
        else:
            string += '{0}={1}&'.format(key,sign_dict[key])
    string = string[0:len(string)-1]
    #return string
    return encrypt(string,salt=private_key,encrypt_way=encrypt_way)

if __name__ == '__main__':
    from utils.generator import random_name,random_phone_number
    test_dict = {}
    for i in range(5):
        test_dict[random_name()] = random_phone_number()
    print(sign(test_dict))