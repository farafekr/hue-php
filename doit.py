import sys
from django.contrib.auth.models import User,Permission,Group
usrname='sample'
passwd='123'
fname='Jack'
lname='Allen'
mail='Jack.Allen@gmail.com'
groupname='default'
userobj = User.objects.create_user(username=usrname,password=passwd,first_name=fname,last_name=lname,email=mail)
userobj.save()
usergroupobj = Group.objects.get(name=groupname)
usergroupobj.user_set.add(userobj.id)
sys.stdout.write('1')
