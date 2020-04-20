#Create a 'User' class that contains information like [1] a list that will contain unique set-translations for certain Japanese/English words [2] a first name [3] a last name [4] email [5] date when the account was created (datetime class)
from datetime import date

class User:
  def __init__(self, Fname_EN, Lname_EN, Fname_JP, Lname_JP, Email):
    self.Fname_EN = Fname_EN
    self.Lname_EN = Lname_EN
    self.Fname_JP = Fname_JP
    self.Lname_JP = Lname_JP
    self.Email = Email
    self.date_created = date.today()

  def __str__(self): 
    return self.Fname_EN + " " + self.Lname_EN

  def SetName_EN(self,Fname_EN, Lname_EN):
    Name_EN = Fname_EN + Lname_EN
    print(Name_EN)

  def SetName_JP(self, Lname_JP, Fname_JP):
    Name_JP = Lname_JP + Fname_JP
    print(Name_JP)

  def SetDate(self):
    return self.date_created


def CreateAccount():
  enfn = input("First name: ")
  enln = input("Last name: ")
  jpln = input("名字: ")
  jpfn = input("名前: ")
  email = input("Email: ")
  return User(enfn, enln, jpfn, jpln, email) 

user = CreateAccount()
print(user)

"""
create dictionary which contains inputs from user 
special [1] JP-EN amd [2] EN-JP)

"""
