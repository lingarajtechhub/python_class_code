import simplejson

x = '{"name":"Rahul","age":30,"city":"Kolkata"}'

#parse the x
y = simplejson.loads(x)

print(y["age"])
print(y["name"])

q = {
    "name":"John",
    "age":45,
    "city":"New York"
}

y = simplejson.dumps(q)

print(y)