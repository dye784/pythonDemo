# Learning Python

#### Printing in python
```py
print 'Hello world'
```

#### Creating Variables
Python uses underscores instead of camel case for variables
```py
my_variable = 10
```

#### Booleans
Booleans are capitalized. Operators are `and` `or` and `not`
```py
my_bool = True
```

#### Functions
Functions are defines using `def`
```py
def function_name():
    print 'Hello'
```

#### Whitespace
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

#### Comments
To comment out a single line we use the `#` sign. To comment out multiple lines we use triple single/double quotes `"""` and end it without another `"""`
```py
'''Some comment here'''
```

#### Math
The only new math operation we have is ** (exponentiation) compared to JavaScript.
```py
eggs = 10 ** 2
```

#### Strings
Same as JS. `\` to escape. Concat is the same `+`.
```py
'There\'s a snake in my boot!'
```
Some string methods :
`len()`
```py
parrot = 'Norwegian Blue'
print len(parrot) #14 length of string
```
`String.lower()` and `String.upper()`
```py
parrot = 'Norwegian Blue'
print parrot.lower() #'norwegian blue' lower case opposite for upper
```
`str()`
```py
pi = 3.14
print st(pi) #'3.14' as a string
```
Note: Methods that dot are methods only available to a specific data type. Methods that you envelop in parens apply to more than one data type.

Similar to template literals in JavaScript Python uses string formating with a %.
```py
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2) # Prints Let's not go to Camelot. 'Tis a silly place.
```
Note: you need the same number of `%s` as terms after the string aka after the `%` `(var1, var2, var3)`

#### Conditionals & Control Flow
```py
answer = "Left"
if answer == "Left": # Colon after conditional statement
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
elif answer == "Right":
    print "Something else"
else:
    print "Parrots...why..."
```
Comparators : `==`, `!=`, `<`, `>`, `<=`, `>=`
Boolean Operators : `and`, `or`, `not`

