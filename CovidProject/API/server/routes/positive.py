from fastapi import APIRouter, Depends
from server.models.request import AddPositiveReq
from server.models.reponse import Response
from server.models.request import CreateStudentReq
from server.models.database import Student, Positive
from sqlalchemy.orm import Session
from server.database import get_db
import datetime


router = APIRouter()


@router.get("/add", response_description="Add new positive case", tags=["positive"])
async def add_positive(mssv: int, db: Session = Depends(get_db)):
    exist_student = db.query(Positive).filter(Positive.mssv == mssv)
    add_date = datetime.date.today()
    if exist_student.first():
        exist_student.update({'firstTestDay' : add_date , 'negativeDay' : None}\
            , synchronize_session="fetch")
        db.commit()
        return Response.ResponseModel(
        code=200,
        message="Update new positive successfully",
        data= {
            "mssv": mssv,
            "firstTestDay": add_date,
        }
    )
    else:
        to_add = Positive(
            mssv = mssv,
            firstTestDay = add_date,
            negativeDay = None
        )

        db.add(to_add)
        db.commit()

        return Response.ResponseModel(
        code=200,
        message="Add new positive successfully",
        data= {
            "mssv": mssv,
            "firstTestDay": to_add.firstTestDay,
        }
    )

    

    

@router.get("/negative", response_description="Update to negative case", tags=["positive"])
async def update_negative(mssv : int ,  db: Session = Depends(get_db)):
    student = db.query(Positive).filter(Positive.mssv == mssv)

    if student.first():
        student.update({"negativeDay": datetime.date.today()}, synchronize_session="fetch")
        db.commit()
        return Response.ResponseModel(
            code=200,
            message="Update negative successfully",
            data= {
                "mssv": mssv,
                "negativeDay": datetime.date.today(),
            }
        )
    else:
        return Response.ResponseModel(
            code=404,
            message="Positive case not found",
            data = []
        )
        
    

@router.get("/", response_description="Get positive case", tags=["positive"])
async def get_positive(db: Session = Depends(get_db)):
    positive = db.query(Positive).filter(Positive.negativeDay.is_(None)).all()
        
    return Response.ResponseModel(
        code=200,
        message="Get case sucessfully",
        data= {
            "totalCase" : len(positive)
        }
    )