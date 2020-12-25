# Python string assembler

## Description
Program used for constructing strings in python without usage of characters ```'``` or ```"```.
Constructed string does not require any builtin methods.
String is constructed by joining individual characters found in available docstrings of native python classes.
Output may vary on different versions of python since the docstrings are different.

## Example
### Python 2
```
$ python2 mp.py -s "Assemble this"
().__class__.__base__.__subclasses__()[6].__doc__[420]+().__class__.__base__.__subclasses__()[0].__doc__[27]+().__class__.__base__.__subclasses__()[0].__doc__[27]+().__class__.__base__.__subclasses__()[0].__doc__[3]+().__class__.__base__.__subclasses__()[0].__doc__[41]+().__class__.__base__.__subclasses__()[0].__doc__[6]+().__class__.__base__.__subclasses__()[4].__doc__[19]+().__class__.__base__.__subclasses__()[0].__doc__[3]+().__class__.__base__.__subclasses__()[0].__doc__[12]+().__class__.__base__.__subclasses__()[0].__doc__[0]+().__class__.__base__.__subclasses__()[0].__doc__[17]+().__class__.__base__.__subclasses__()[0].__doc__[53]+().__class__.__base__.__subclasses__()[0].__doc__[27]
```

### Python 3
```
$ python3 py-string-assembler.py -s "Assemble this"
().__class__.__base__.__subclasses__()[5].__doc__[493]+().__class__.__base__.__subclasses__()[0].__doc__[23]+().__class__.__base__.__subclasses__()[0].__doc__[23]+().__class__.__base__.__subclasses__()[0].__doc__[3]+().__class__.__base__.__subclasses__()[0].__doc__[17]+().__class__.__base__.__subclasses__()[0].__doc__[6]+().__class__.__base__.__subclasses__()[4].__doc__[174]+().__class__.__base__.__subclasses__()[0].__doc__[3]+().__class__.__base__.__subclasses__()[0].__doc__[20]+().__class__.__base__.__subclasses__()[0].__doc__[0]+().__class__.__base__.__subclasses__()[0].__doc__[51]+().__class__.__base__.__subclasses__()[0].__doc__[29]+().__class__.__base__.__subclasses__()[0].__doc__[23]
```