from pydantic import BaseModel, Field


class StudentBase(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Student Full Name"
    )

    age: int = Field(
        ...,
        ge=16,
        le=40,
        description="Student Age"
    )

    department: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Department Name"
    )

    cgpa: float = Field(
        ...,
        ge=0.0,
        le=4.0,
        description="Student CGPA"
    )


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True