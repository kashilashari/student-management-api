from sqlalchemy.orm import Session
from sqlalchemy import and_

from models import Student
from schemas import StudentCreate


# ----------------------------
# Create Student
# ----------------------------
def create_student(db: Session, student: StudentCreate):

    db_student = Student(
        name=student.name,
        age=student.age,
        department=student.department,
        cgpa=student.cgpa
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


# ----------------------------
# Get Student By ID
# ----------------------------
def get_student(db: Session, student_id: int):

    return db.query(Student).filter(
        Student.id == student_id
    ).first()


# ----------------------------
# Get All Students
# ----------------------------
def get_students(
    db: Session,
    name: str = None,
    department: str = None,
    age: int = None,
    min_cgpa: float = None,
    max_cgpa: float = None
):

    query = db.query(Student)

    if name:
        query = query.filter(Student.name.ilike(name))

    if department:
        query = query.filter(Student.department.ilike(department))

    if age:
        query = query.filter(Student.age == age)

    if min_cgpa is not None:
        query = query.filter(Student.cgpa >= min_cgpa)

    if max_cgpa is not None:
        query = query.filter(Student.cgpa <= max_cgpa)

    return query.all()


# ----------------------------
# Update Student
# ----------------------------
def update_student(
    db: Session,
    student_id: int,
    updated_student: StudentCreate
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        return None

    student.name = updated_student.name
    student.age = updated_student.age
    student.department = updated_student.department
    student.cgpa = updated_student.cgpa

    db.commit()
    db.refresh(student)

    return student


# ----------------------------
# Delete Student
# ----------------------------
def delete_student(
    db: Session,
    student_id: int
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        return None

    db.delete(student)
    db.commit()

    return student