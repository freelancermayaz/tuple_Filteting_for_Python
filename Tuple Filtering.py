# tuple Filtering:
a = ('Alll', 60,2.3,True,52+6j,'Noman','Baser',30,30.2,False,85+6j,56+3j,5.6,'Ahad')
# tuple convert of list Filtering:
st = []
In = []
Fl = []
bo = []
com = []

for i in a:
    if type(i) == str:
        st.append(i)
    elif type(i) == int:
        In.append(i)
    elif type(i) == float:
        Fl.append(i)
    elif type(i) == bool:
        bo.append(i)
    else:
        com.append(i)
# list convert for tuple
st = tuple(st)
In = tuple(In)
Fl = tuple(Fl)
bo = tuple(bo)
com = tuple(com)

print(st)
print(In)
print(Fl)
print(bo)
print(com)