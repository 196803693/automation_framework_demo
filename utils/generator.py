import random
from faker import Factory

fake = Factory().create('zh_CN')

def random_phone_number():
    return fake.phone_number()

def random_name():
    return fake.name()

def random_address():
    return fake.address()

def random_email():
    return fake.email()

def random_ipv4():
    return fake.ipv4()

def random_str(min=0,max=20):
    return fake.pystr(min_chars=min,max_chars=max)

def factory_generator_ids(starting_id=1,increment=2):
    '''返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment.'''
    def generator_started_ids():
        val = starting_id
        while True:
            yield val
            val += increment
    return generator_started_ids()

def choice_generator(value):
    '''生成器，从指定的list中随机取一项'''
    val_list = list(value)
    while True:
        yield random.choice(val_list)

if __name__ == '__main__':
    print(random_phone_number())
    print(random_name())
    print(random_address())
    print(random_email())
    print(random_ipv4())
    print(random_str())
    fg = factory_generator_ids(2)
    print('fg is ',fg)
    for i in range(5):
        print(next(fg))
    choices = ['John', 'Sam', 'Lily', 'Rose']
    choice_gen = choice_generator(choices)
    print('choice_gen is ',choice_gen)
    for i in range(5):
        print(next(choice_gen))