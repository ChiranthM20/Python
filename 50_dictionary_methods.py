tools = {
    "Python" : "PyCharm",
    "Java" : "NetBeans",
    "C" : "VS Code",
}


print(tools)

# keys() --> prints only keys

print(tools.keys())


# values() --> prints only values

print(tools.values())


# items() --> returns key-value as tuple

print(tools.items())


# update()  --> updates the dictionary with another dictionary

new_tools = {
    "chat bot" : "ChatGPT",
    "ppt" : "Gamma"
}

tools.update(new_tools)

print(tools)


