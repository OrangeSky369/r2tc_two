def execute_function(func):
    func()  # 调用传入的函数

def say_hello():
    print("Hello")

execute_function(say_hello) # 输出：Hello
