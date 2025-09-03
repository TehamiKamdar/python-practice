marks = {
  "Tehami": 53,
  "Mohib": 69,
  "Zayan": 98
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Tehami": 99});
print(marks.values())

print(marks.get("Harry"))