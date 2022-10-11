import pickle

with open("database.pkl","rb") as f:
    x = pickle.load(f)
    y = pickle.load(f)
    z = pickle.load(f)
    s = pickle.load(f)
    l = pickle.load(f)
    d = pickle.load(f)
print(x,y,z,s,l,d,sep="\n")
或者:x,y,z,s,l,d=pickle.load(f)
