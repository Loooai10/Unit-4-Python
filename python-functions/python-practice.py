
# def first _function():
#     return "My python function"

# Array.forEach():
#     return "hi"
    
# Python lambda function (equivalent of arrow functions)
# #const nums = [1,2,3,4,5]
# nums = [1,2,3,4,5,6] #list

# #let odds = nums.filter(eachNum => num % 2)
# oddds = list(filter(lambda eachNum:num %2, numbers))
# print(odds)

# #Hoisting??

# #const mySum = findSum(3,5)
# function findSum(a,b){
#     return a+b
# }

# def add(a,b)
# return a+b
# print(add)

# def add(a,b,*args,**kwargs):
#     print(type(kwargs))
#     print(kwargs[0])
#     print(args)
#     return a+b
#     # for eachArg in args:
#     #     print(eachArg)
        
# print(add(5,2,3,4,5,6,7, name='Alex', topic='Python'))

# def add(**kwargs):
#     for key,value in kwargs.items():
#         print(f'key: {key} and value: {value}')
#         print(add(name='Alex', topic='Python', fun='coding'))
        
# def add(a,b):
#     #convert all parameters/args to integer u add int
    
    # challenge 3
def occurances(string, sos):
  # remove each occuance of sos
  stripped_string = string.replace(sos, '')
  # compute based on length of the strings
  return (len(string) - len(stripped_string)) // len(sos)

# Python actually has a method to solve this too!
def occurances(string, sos):
  return string.count(sos)
    
    