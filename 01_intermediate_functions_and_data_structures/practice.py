from functools import reduce
lambda x : abs(10-x)

numbers = [1,2,3,4,5]
squared =list(map(lambda x : x*x, numbers))
print(squared)

even_numbers=list(filter(lambda x: x%2 == 0,numbers))
print(even_numbers)

sum=reduce(lambda x,y: x+y, numbers)
print(sum)

num=[15, 20, 33, 40, 55, 60]
ten_num=list(filter(lambda x: x%10 ==0, num))
print(ten_num)

data = [('cherry', 2), ('apple', 1), ('banana', 3)]
sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)

sorted_data=sorted(data, key=lambda x: x[1])
print(sorted_data)

iterable = [1, 2, 3, 4, 5]
result=[i for i in iterable if i%2 ==0]
print(result)

numbers = [1, 2, 3, 4, 5]
squared = [x*x for x in numbers]
print(squared)

squared=list(map(lambda x:x*x, numbers))
print(squared)


squares=[i**2 for i in range(1,6)]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
result=[i**i for i in numbers if i%2 ==0]
print(result)

def build_greet(*names):
    greeting="Hi"
    for name in names:
        greeting += f", {name}"
        
    greeting += "!"
    return greeting

greeting= build_greet("Alex", "Bob")
print(greeting)

def create_employee_record(**details):
    return details

record1 = create_employee_record(name="John", age=28, department="Marketing", position="Manager")

print(record1)

def create_average_calculator():
    total_sum=0
    count=0
    
    def add_number(number):
        nonlocal total_sum, count
        total_sum += number
        count += 1
        return total_sum / count
    
    return add_number

average_calculator=create_average_calculator()
print(average_calculator(10))
print(average_calculator(20))

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

import time

def time_this(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time: {end_time - start_time} seconds to run.")
        return result
    return wrapper

@time_this
def do_something():
    time.sleep(2)

do_something()


def fibonacci():
    a=0
    b=1
    
    while True:
        yield a
        next_value = a+b
        a=b
        b=next_value
        
seq=fibonacci()

for i in range(10):
    print(next(seq))
    

string="Hello, world"
substring="world"
print(string.find(substring))
print(string.replace(substring, "Python"))
print(string.split(","))

user_input="123, 142, 34, 255, 255, 255, 0, 0, 0, 124, 24, 39"

words=user_input.split(",")
newdel="->"
result=newdel.join(words)
print(result)

import re

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
text = """
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <div>
        Contact us <a href="mailto:support@example.com">here</a> for support.
    </div>
    <div>
        For inquiries, <a href="mailto:inquiry@service.co.uk">email us</a>.
    </div>
    <div>
        Join our <a href="mailto:subscribe-news@example2023.org">mailing list</a>.
    </div>
    <footer>
        <p>Visit our <a href="http://www.exampleblog.com">blog</a>.For any questions, reach out at contact-us@example.net.</p>
    </footer>
</body>
</html>
"""
print(re.findall(pattern,text))