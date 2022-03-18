from fastapi import APIRouter, Depends
from server.models.reponse import Response
from server.models.request import CreateStudentReq
from server.models.database import Student
from sqlalchemy.orm import Session
from server.database import get_db
router = APIRouter()


@router.post("/add", response_description="Add new student", tags=["student"])
async def add_student(request: CreateStudentReq, db: Session = Depends(get_db)):
    to_add = Student(
        mssv=request.mssv,
        fullName=request.fullName,
        classCode=request.classCode
    )
    db.add(to_add)
    db.commit()
    return Response.ResponseModel(
        code=200,
        message="Add new student successfully",
        data= {
            "mssv": to_add.mssv,
            "fullName": to_add.fullName,
            "classCode": to_add.classCode
        }
    )

@router.get("/")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Student).filter(Student.mssv == id).first()


@router.delete("/")
async def delete(id: int, db: Session = Depends(get_db)):
    db.query(Student).filter(Student.mssv == id).delete()
    db.commit()
    return { "success": True }

@router.get("/all")
async def get_all_student( db: Session = Depends(get_db)):
    students = db.query(Student).filter().all()
    mssv = [student.mssv for student in students]
    db.commit()
    return Response.ResponseModel(
        code=200,
        message="Add new student successfully",
        data= {
            "students" : mssv
        }
    )


@router.get("/amount")
async def get_number_of_student( db: Session = Depends(get_db)):
    students = db.query(Student).filter().all()
    db.commit()
    return Response.ResponseModel(
        code=200,
        message="Add new student successfully",
        data= {
            "numberOfStudent" : len(students)
        }
    )

@router.post("/update")
def update(student: CreateStudentReq ,  db: Session = Depends(get_db)):
    # db.update(Student).where(Student.mssv == id).values(name=name, classCode=classCode)
    
    db.query(Student).filter(Student.mssv == student.mssv)\
        .update({"fullName": student.fullName , 'classCode' : student.classCode}, synchronize_session="fetch")
    
    db.commit()
    return { "success": True }



    
    
