#after  push
import mysql.connector as mycon
# model class
class UserContact:
    def __init__(self,id=0,fname='',lname='',email='',contact=0):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.contact  = contact
    
    def __str__(self):
        return str(self.id) + " : "+self.fname+" : "+str(self.contact)
    
c1 = UserContact(1,"Alok","yadav","alok@gmail.com",101)
print(c1) # print(c1.__str__())
#print(id(c1))
#print(hex(id(c1)))
#print(dir(c1))
my_con = None
try:
    my_con = mycon.connect(host="localhost",port=3307,
                 username="root",password="root",
                 )
except Exception as e:
    print(e)
        
def insertContact(userContact):
    if(my_con != None):
            print(my_con)
            cur = my_con.cursor()
            #query = "insert into mycontacts (fname,lname,email,contact) values (%s,%s,%s,%s)"
            #values = (userContact.fname,userContact.lname,userContact.email,userContact.contact)
            query1 = "use gl_contact"
            cur.execute(query1)
            query = "insert into mycontacts (fname,lname,email,contact) values"+"('"+userContact.fname+"',"+"'"+userContact.lname+"',"+"'"+userContact.email+"',"+str(userContact.contact)+")"
            print(query)
            cur.execute(query)
            my_con.commit()
            print(cur.rowcount)

    else:
        print("connection issues...")


insertContact(c1)