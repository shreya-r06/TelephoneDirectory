import csv
from prettytable import PrettyTable
myfile="directory.csv"
from os.path import exists

file_exists = exists(myfile)
if file_exists!=True:
    fh=open(myfile,"w",newline="")
    dwriter=csv.writer(fh)
    dwriter.writerow(['Name', 'Phone_No', 'Address','Pincode'])
    fh.close()
def add_data():
    
    fh=open(myfile,"a",newline="")
    dwriter=csv.writer(fh)
    name=input("Enter name\t").upper()
    ph=input("Enter phone no.\t")
    add=input("Enter address\t").upper()
    code=input("Enter pincode\t")
    
    myrecord=[name,ph,add,code]
    dwriter.writerow(myrecord)
    fh.close()
def read_data():
    t1=PrettyTable()
    t1.field_names=["Name","Phone no","Address","Pincode"]
    with open(myfile, "r") as fin:
        myrec=csv.reader(fin)
        next(myrec)
        for rec in myrec:
            t1.add_row(rec)
        print(t1)
def search_name(name):
    with open(myfile,"r") as fin:
        rec=csv.reader(fin)
        for x in rec:
            if x[0]==name:
                print(x)
                break
        else:
            print("No records found.")
def search_first_alpha(ch):
    t1=PrettyTable()
    flag=0
    t1.field_names=["Name","Phone no","Address","Pincode"]
    with open(myfile,"r") as fin:
        rec=csv.reader(fin)
        next(rec)
        for x in rec:
            if x[0][0]==ch:
                t1.add_row(x)
                flag=1
        if flag==0:
            print("No records found.")
        else:
            print(t1)
def delete_rec(name):
    flag=0
    myrec=[['Name', 'Phone_No', 'Address','Pincode']]
    with open(myfile,"r") as fh:
        record=csv.reader(fh)
        next(record)
        for i in record:
            if i[0]==name:
                print("Successfully deleted.")
                flag=1
                continue
            else:
                myrec.append(i)
    with open(myfile,"w",newline="") as fout:
        data=csv.writer(fout)
        data.writerows(myrec)
    if flag==0:
        print("Record not found")
def update_data(name):
    flag=0
    myrec=[]
    with open(myfile,"r") as fh:
        record=csv.reader(fh)
        next(record)
        for i in record:
            if i[0]==name:
                flag=1
                nm=name
                ph=input("Enter phone no.\t")
                add=input("Enter address\t").upper()
                code=input("Enter pincode\t")
                myrec.append([nm,ph,add,code])
                
                print("Successfully updated.")
            else:
                myrec.append(i)
    with open(myfile,"w",newline="") as fout:
        data=csv.writer(fout)
        data.writerows([['Name', 'Phone_No', 'Address','Pincode'],myrec])
    if flag==0:
        print("Record not found")


print('''Choose an option:
1. Add a record
2. Display all records
3. Search Record by name
4. Search Record alphabet-wise
5. Delete a record by name
6. Update a record by name
7. Exit''')

c=int(input("Enter choice: "))
while c!=7:
    if c==1:
        add_data()
    elif c==2:
        read_data()
    elif c==3:
        x=input("Enter name: ").upper()
        search_name(x)
    elif c==4:
        x=input("Enter an alphabet: ").upper()
        search_first_alpha(x)
    elif c==5:
        x=input("Enter name: ").upper()
        delete_rec(x)
    elif c==6:
        x=input("Enter name: ").upper()
        update_data(x)
    c=int(input("Enter choice: "))


