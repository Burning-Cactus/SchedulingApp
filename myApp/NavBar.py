
class NavBar:

    def getNavBar(self, activePermission, permissions):
        navHtml = []
        if activePermission.__eq__("1"):
            if len(permissions) == 1:
                navHtml = ['Database',
                           'Create Account',
                           'Create Course',
                           'Create Lab',
                           'Edit Account',
                           'Edit Course',
                           'Edit Lab',
                           'Instructor To Course',
                           'Assistant To Course',
                           'Assistant To Lab',
                           'Delete Account',
                           'Delete Course',
                           'Delete Lab',
                           'Email',
                           'Logout']
            else:
                navHtml = ['Database',
                           'Create Account',
                           'Create Course',
                           'Create Lab',
                           'Edit Account',
                           'Edit Course',
                           'Edit Lab',
                           'Instructor To Course',
                           'Assistant To Course',
                           'Assistant To Lab',
                           'Delete Account',
                           'Delete Course',
                           'Delete Lab',
                           'Email',
                           'Switch Permission',
                           'Logout']

        if activePermission.__eq__("2"):
            if len(permissions) == 1:
                navHtml = ['Database',
                           'Create Account',
                           'Create Course',
                           'Create Lab',
                           'Edit Account',
                           'Edit Course',
                           'Edit Lab',
                           'Delete Account',
                           'Delete Course',
                           'Delete Lab',
                           'Email',
                           'Logout']

            else:
                navHtml = ['Database',
                           'Create Account',
                           'Create Course',
                           'Create Lab',
                           'Edit Account',
                           'Edit Course',
                           'Edit Lab',
                           'Delete Account',
                           'Delete Course',
                           'Delete Lab',
                           'Email',
                           'Switch Permission',
                           'Logout']

        if activePermission.__eq__("3"):
            if len(permissions) == 1:
                 navHtml = ['Assign Assistant',
                            'View Courses',
                            'View Assistants',
                            'View Contacts',
                            'Edit Contact Info',
                            'Email',
                            'Logout']
            else:
                navHtml = ['Assign Assistant',
                           'View Courses',
                           'View Assistants',
                           'View Contacts',
                           'Edit Contact Info',
                           'Email',
                           'Switch Permission',
                           'Logout']

        if activePermission.__eq__("4"):
            if len(permissions) == 1:
                navHtml = ['View Assistants',
                           'View Contacts',
                           'Edit Contact Info',
                           'Logout']
            else:
                navHtml = ['View Other Assistants',
                           'View Contacts',
                           'Edit Contact Info',
                           'Switch Permission',
                           'Logout']

        return navHtml
