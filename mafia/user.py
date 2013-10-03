class User():
    def __init__(self, id, firstName, lastName, userName, hashedPassword, isAdmin):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.hashedPassword = hashedPassword
        self.isAdmin = isAdmin
    
    def getID():
        return id
    
    def setID(id):
        self.id = id
        
    def getFirstName():
        return firstName
    
    def getLastName():
        return lastName
        
    def setFirstName(firstName):
        self.firstName = firstName
        
    def setLastName(lastName):
        self.lastName = lastName
        
    def getUserName():
        return userName
        
    def setUserName(userName):
        self.userName = userName
        
    def getHashedPassword():
        return hashedPassword
        
    def setHashedPassword(hashedPassword):
        self.hashedPassword = hashedPassword