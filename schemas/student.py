
def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item['student_email'],
        "phone": db_item['student_phone']
    }

def listOfStudentEntities(list_db_items) -> list:
    list_student_entities = []
    for item in list_db_items:
        list_student_entities.append(studentEntity(item))

    return list_student_entities
