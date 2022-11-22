#Schleifen lassen
list_a = ["a", "b", "c", "d", "e"]
out = ""
for item in list_a:
    out += item
print()
#Durchgang 1
#item = a
#out = a

#Durchgang 2
#item = b
#out = ab

#Durchgang 3
#item = c
#out = abc

#Durchgang 4
#item = d
#out= abcd

#Durchgang 5
#item = e
#out = abcde

list_b = [1, 3, 2, 5, 8]
out = 0
for item in list_b:
    out = out * item
#Durchgang 1
#item = 1
#out = 0

#Durchgang 2
#item = 3
#out = 0

#Durchgang 3
#item = 2
#out = 0

#Durchgang 4
#item = 5
#out = 0

#Durchgang 5
#item = 8
#out = 0

list_c = [1,3,2,5,8]
out = 0
for item in list_c:
    item = item*10
    out += item
#Durchgang 1
#item = 10
#out = 10

#Durchgang 2
#item = 30
#out = 40

#Durchgang 3
#item = 20
#out = 60

#Durchgang 4
#item = 50
#out = 110

#Durchgang 5
#item = 80
#out = 190

list_d = [0, 1, 2, 3, 4]
out = 0
for item in list_d:
    item = item * 10
    if item > 10:
        out += item
#Durchgang 1:
#item = 0
#out = 0

#Durchgang 2:
#item = 10
#out = 0

#Durchgang 3:
#item = 20
#out = 20

#Durchgang 4:
#item = 30
#out = 50

#Durchgang 5:
#item = 40
#out = 90

list_e = [0, 1, 2, 3, 4]
out = 0
index = 0
for item in list_e:
    if index > 3:
        item = item * 10
    else:
        item = 0
        out = out + item
        index = index + 1
#Durchgang 1:
#item = 0
#out = 0
#index = 1

#Durchgang 2:
#item = 0
#out = 0
#index = 2

#Durchgang 3:
#item = 0
#out = 0
#index = 3

#Durchgang 4:
#item = 0
#out = 0
#index = 4

#Durchgang 5:
#item = 40
#out = 0
#index = 4

