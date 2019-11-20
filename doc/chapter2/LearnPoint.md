list/generator question
=======================
for x in list_a for y in list_b
tuple(x for x in list_a)
1. list sort by x now
2. write in one line equals like two for loop
3. if this is the only function callback arguments . dont need ()


tuple/nametuple
=======================
1. it's the python way to change value for two arguments 
    a, b = b, a
    
special method _field / _make
City = namedtuple("City", "name country population cordinations")
args = ("HZ", "ZJ", 100, (101,200))
1. print all City fields: City._fields
2. City._make(args) == City(*args)