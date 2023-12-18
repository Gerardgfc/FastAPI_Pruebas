def get_full_name(first_name: str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe")) #john doe
#print(get_full_name("john", 0))   #AttributeError: 'int' object has no attribute 'title'
print(get_full_name("julia" "ortiz"))
