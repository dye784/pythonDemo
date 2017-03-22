# Learning Python

###Printing in python
```py
print 'Hello world'
```

###Creating Variables
Python uses underscores instead of camel case for variables
```py
my_variable = 10
```

###Booleans
Booleans are capitalized
```py
my_bool = True
```

###Whitespace
Whitespace is important in python to structure code. This is broken.
```py
def spam():
eggs = 12
return eggs

print spam()
```

to fix it you need to indent. Indentation should be 4 spaces
```py
def spam():
    eggs = 12
    return eggs

print spam()
```

###Comments
To comment out a single line we use the `#` sign. To comment out multiple lines we use triple single/double quotes `"""` and end it without another `"""`
```py
'''Some comment here'''
```

###Math
The only new math operation we have is ** (exponentiation) compared to JavaScript.
```py
eggs = 10 ** 2
```
