# write your code here
person = {
'name': 'ali',
'age': '18',
'hobbies': ['video games' , 'football']
}
person["age"] = 20
person["country"] = "kuwait"
person["hobbies"] = 'video games' , 'football'

def check_hobbies(person):
    if len(person['hobbies']) >= 3:
        print(f"wow you are amazing")

check_hobbies(person)