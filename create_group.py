from pyad import *
ou=pyad.adcontainer.ADContainer.from_dn("OU=groupou,DC=totaltechnology,DC=com")
optional={"managedBy":"CN=AbbeyAshwell,OU=test,DC=totaltechnology,DC=com"}
pyad.adgroup.ADGroup.create("test_group_2",ou,security_enabled=True,scope="UNIVERSAL",optional_attributes=optional)