def language(name):
    names =("python", "java", "c", "c++", "html", "css", "js")
    name = input("Enter the language : ")
    if name in names:
        return f"{name} is a programming language"
    else:
        return f"{name} is not a programming lanuage"


    
    
    