from bson import ObjectId
from fastapi import APIRouter

from config.database import connection
from models.student import Student
from schemas.student import studentEntity, listOfStudentEntities

student_router = APIRouter()


@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntities(connection.local.student.find())


@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntities(connection.local.student.find())


@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
