from fastapi import APIRouter, Query, HTTPException, Depends
from sqlalchemy.orm import Session

import crud

from schemas import StudentCreate, StudentResponse
from database import get_db

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.get("/", response_model=list[StudentResponse])
def get_students(
    name: str = Query(default=None),
    department: str = Query(default=None),
    age: int = Query(default=None, ge=16, le=40),
    min_cgpa: float = Query(default=None, ge=0, le=4),
    max_cgpa: float = Query(default=None, ge=0, le=4),
    db: Session = Depends(get_db)
):

    return crud.get_students(
        db=db,
        name=name,
        department=department,
        age=age,
        min_cgpa=min_cgpa,
        max_cgpa=max_cgpa
    )


@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    return crud.create_student(db, student)


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    updated_student: StudentCreate,
    db: Session = Depends(get_db)
):

    student = crud.update_student(
        db,
        student_id,
        updated_student
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = crud.delete_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student Deleted Successfully",
        "student": student
    }