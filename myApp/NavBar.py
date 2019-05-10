
class NavBar:

    def getNavBar(self, activePermission, permissions):
        navHtml = []
        if activePermission.__eq__("1"):
            if len(permissions) == 1:
                navHtml = ['<div class="nav"><ul>',
                           '<li>Database</li>',
                           '<li><a>Create Account</a></li>',
                           '<li><a>Create Course</a></li>',
                           '<li><a>Create Lab</a></li>',
                           '<li><a>Edit Account</a></li>',
                           '<li><a>Edit Course</a></li>',
                           '<li><a>Edit Lab</a></li>',
                           '<li><a>Instructor To Course</a></li>',
                           '<li><a>Assistant To Course</a></li>',
                           '<li><a>Assistant To Lab</a></li>',
                           '<li><a>Delete Account</a></li>',
                           '<li><a>Delete Course</a></li>',
                           '<li><a>Delete Lab</a></li>',
                           '<li><a>Email</a></li>',
                           '<li><a>Logout</a></li>',
                           '</ul></div>']
            else:
                navHtml = ['<div class="nav"><ul>',
                           '<li>Database</li>',
                           '<li><a>Create Account</a></li>',
                           '<li><a>Create Course</a></li>',
                           '<li><a>Create Lab</a></li>',
                           '<li><a>Edit Account</a></li>',
                           '<li><a>Edit Course</a></li>',
                           '<li><a>Edit Lab</a></li>',
                           '<li><a>Instructor To Course</a></li>',
                           '<li><a>Assistant To Course</a></li>',
                           '<li><a>Assistant To Lab</a></li>',
                           '<li><a>Delete Account</a></li>',
                           '<li><a>Delete Course</a></li>',
                           '<li><a>Delete Lab</a></li>',
                           '<li><a>Email</a></li>',
                           '<li><a>Switch Permission</a></li>',
                           '<li><a>Logout</a></li>',
                           '</ul></div>']

        if activePermission.__eq__("2"):
            if len(permissions) == 1:
                navHtml = '<div class="nav"><ul>' \
                          '<li><a>Database</a></li>' \
                          '<li><a>Create Account</a></li>' \
                          '<li><a>Create Course</a></li>' \
                          '<li><a>Create Lab</a></li>' \
                          '<li><a>Edit Account</a></li>' \
                          '<li><a>Edit Course</a></li>' \
                          '<li><a>Edit Lab</a></li>' \
                          '<li><a>Delete Account</a></li>' \
                          '<li><a>Delete Course</a></li>' \
                          '<li><a>Delete Lab</a></li>' \
                          '<li><a>Email</a></li>' \
                          '<li><a>Logout</a></li>' \
                          '</ul></div>'

            else:
                navHtml = '<div class="nav"><ul>' \
                          '<li><a>Database</a></li>' \
                          '<li><a>Create Account</a></li>' \
                          '<li><a>Create Course</a></li>' \
                          '<li><a>Create Lab</a></li>' \
                          '<li><a>Edit Account</a></li>' \
                          '<li><a>Edit Course</a></li>' \
                          '<li><a>Edit Lab</a></li>' \
                          '<li><a>Delete Account</a></li>' \
                          '<li><a>Delete Course</a></li>' \
                          '<li><a>Delete Lab</a></li>' \
                          '<li><a>Email</a></li>' \
                          '<li><a>Switch Permission</a></li>' \
                          '<li><a>Logout</a></li>' \
                          '</ul></div>'

        if activePermission.__eq__("3"):
            if len(permissions) == 1:
                 navHtml = '<div class="nav"><ul>' \
                           '<li><a>Assign Assistant</a></li>' \
                           '<li><a>View Courses</a></li>' \
                           '<li><a>View Assistants</a></li>' \
                           '<li><a>View Contacts</a></li>' \
                           '<li><a>Edit Contact Info</a></li>' \
                           '<li><a>Email</a></li>' \
                           '<li><a>Logout</a></li>' \
                           '</ul></div>'
            else:
                navHtml = '<div class="nav"><ul>' \
                          '<li><a>Assign Assistant</a></li>' \
                          '<li><a>View Courses</a></li>' \
                          '<li><a>View Assistants</a></li>' \
                          '<li><a>View Contacts</a></li>' \
                          '<li><a>Edit Contact Info</a></li>' \
                          '<li><a>Email</a></li>' \
                          '<li><a>Switch Permission</a></li>' \
                          '<li><a>Logout</a></li>' \
                          '</ul></div>'\

        if activePermission.__eq__("4"):
            if len(permissions) == 1:
                navHtml = '<div class="nav"><ul>' \
                          '<li><a>View Assistants</a></li>' \
                          '<li><a>View Contacts</a></li>' \
                          '<li><a>Edit Contact Info</a></li>' \
                          '<li><a>Logout</a></li>' \
                          '</ul></div>'
            else:
                navHtml = '<div class="nav"><ul>' \
                          '<li><a>View Assistants</a></li>' \
                          '<li><a>View Contacts</a></li>' \
                          '<li><a>Edit Contact Info</a></li>' \
                          '<li><a>Switch Permission</a></li>' \
                          '<li><a>Logout</a></li>' \
                          '</ul></div>'

        return navHtml
