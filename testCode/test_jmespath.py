import jmespath

# Object Projections
# Whereas a list projection is defined for a JSON array, an object projection is defined for a JSON object. You can create an object projection using
# the * syntax.
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
result = jmespath.search("people[?general.age > `20`].general | [0]",source7)
print(result)