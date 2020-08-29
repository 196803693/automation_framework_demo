import jmespath

# Object Projections
# Whereas a list projection is defined for a JSON array, an object projection is defined for a JSON object. You can create an object projection using
# the * syntax.
source0={"a":"foo","b":"bar","c":"baz"}
source7 = {
  "people": [
    {
      "general": {
        "id": 100,
        "age": 20,
        "other": "foo",
        "name": "Bob"
      },
      "history": {
        "first_login": "2014-01-01",
        "last_login": "2014-01-02"
      }
    },
    {
      "general": {
        "id": 101,
        "age": 30,
        "other": "bar",
        "name": "Bill"
      },
      "history": {
        "first_login": "2014-05-01",
        "last_login": "2014-05-02"
      }
    }
  ]
}
result0 = jmespath.search('a',source0)
print('简单查找',result0)
result1 = jmespath.search('people[0].general.age',source7)
print('下层定位查找',result1)
result = jmespath.search("people[?general.age > `20`].general | [0]",source7)
print(result)