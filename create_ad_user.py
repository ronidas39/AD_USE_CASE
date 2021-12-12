from pyad import *

#pyad.set_defaults(ldap_server="DC01.totaltechnology.com")
user=pyad.aduser.ADUser.from_cn("administrator")
print(user)

ou=pyad.adcontainer.ADContainer.from_dn("OU=test,DC=totaltechnology,DC=com")
def add_user(row):
    print(row)
    user_attributes=row.split("|")
    givenName=user_attributes[0]
    sn=user_attributes[1]
    dob1=user_attributes[2]
    personalTitle=user_attributes[3]
    mail=user_attributes[4]
    mobile=user_attributes[5]
    sAMAccountName=mail.split("@")[0]
    print(givenName,sn,dob1,personalTitle,mail,mobile)
    optional={"givenName":givenName,"sn":sn,"dob1":dob1,"personalTitle":personalTitle,"mail":mail,"mobile":mobile,"userAccountControl":512}
    try:
        pyad.aduser.ADUser.create(sAMAccountName,ou,password="Rambo@1234",upn_suffix=None,enable=True,optional_attributes=optional)
        print(f"{mail} user adeed")
        members=user_attributes[6].split(",")
        for member in members:
            user_to_add=pyad.aduser.ADUser.from_cn(sAMAccountName)
            group=pyad.adgroup.ADGroup.from_cn(member)
            user_to_add.add_to_group(group)
            print(f"{sAMAccountName} is added to {member}")
    except Exception as e:
        print(str(e)+mail)



    




    
