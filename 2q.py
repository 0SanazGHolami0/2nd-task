o ="""ali
1233
0
""
[]
{}
'False'
'0'
'None'
None
-1
[1, 2, 3]
{'key': 'value'}
True
' '
'[]'
'[1, 2, 3]'
'{}'
'{'a': 1}'
'True'
'ali'
'1234'
1
0.1
-0.1
True
' '
'[]'
'[1, 2, 3]'
'{}'
'{'a': 1}'
'True'
'ali'
'1234'
1
0.1
-0.1
True
' '
'[]'
'[1, 2, 3]'
'{}'
'{'a': 1}'
'True'
'ali'
'1234'
1
0.1
-0.1 """

li1 = o.split("\n")
li2 = []

for i in li1:
    if i:
        li2.append("True")
    else:
        li2.append("False")
print(li2)


