x= int(input("Enter a number of repetitions"))

def repeatNTimes(func):
    def repeat():
        for i in range(x):
            func()
    return repeat

@repeatNTimes
def hello():
    print ('Hello')


hello()

