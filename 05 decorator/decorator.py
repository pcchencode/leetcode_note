import time

def timer(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        res_of_func = func(*args, **kwargs)
        e =time.time()
        print('it costs ' + str(round(e-s,2)) + ' secs')
        return res_of_func
    return wrapper

@timer
def main():
    for i in range(0,10000000):
        pass
    a = 1
    b = 2
    print(a+b)
    return 
@timer
def add(a,b):

    print(a)
    print(b)
    return


print(add(1,2))





# if __name__ == '__main__':
#     main()
    