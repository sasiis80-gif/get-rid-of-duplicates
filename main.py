#Dictionary of students (Id-> details)
student_data = {
    "id1" : {"name":"Sasi", "class":"B", "subject_integration":"English, Math, Sinahla"},
    "id2" : {"name":"Sanuli", "class":"B", "subject_integration":"English, Math, Sinahla"},
    "id3" : {"name":"Chathu", "class":"B", "subject_integration":"English, Math, Sinahla"},
#Duplicate of id1 
    "id4" : {"name":"Rhea", "class":"B", "subject_integration":"English, Math, Sinahla"},
}

result = {}
seen_keys = [] #using a list instead of a set
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

#print the output line by line
for k, v in result.items():
    print(k,":", v)        