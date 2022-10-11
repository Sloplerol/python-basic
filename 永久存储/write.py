import pickle
x,y,z = 1,2,3
s = "satrol_"
l = ["666",233,22]
d = {"one":1,"two":2}
with open("database.pkl","wb") as f:
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(z,f)
    pickle.dump(s,f)
    pickle.dump(l,f)
    pickle.dump(d,f)
或者:pickle.dump((x,y,z,s,l,d),f)
