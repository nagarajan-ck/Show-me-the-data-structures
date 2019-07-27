class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


    
class Directory:
    def __init__(self):
        self.sub_groups=[]

    def is_user_in_group(self,user, group):       

        if(group in self.sub_groups):
            self.sub_groups=[]
            return False
        self.sub_groups.append(group)
        sub_group=group.get_groups()
        sub_users = group.get_users()
        
        if user in sub_users:
            self.sub_groups=[]
            return True
        for item in sub_group:
            return self.is_user_in_group(user, item)  
        self.sub_groups=[]
        return False
        
        
        
        
        
        
        
        
        
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child.add_group(parent)

child.add_group(sub_child)
parent.add_group(child)


dirs = Directory()
print(dirs.is_user_in_group("Not a child",sub_child)) #prints False since user not in group
print(dirs.is_user_in_group("sub_child_user",sub_child)) #prints True since user in group
print(dirs.is_user_in_group("sub_child_ser",parent)) #prints False due to a cyclic loop
