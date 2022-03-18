from fastapi import APIRouter, Depends
from server.models.request import AddPositiveReq
from server.models.reponse import Response
from server.models.request import CreateStudentReq
from server.models.database import Student, Positive
from sqlalchemy.orm import Session
from server.database import get_db
import datetime


router = APIRouter()


@router.post("/add", response_description="Add new positive case", tags=["positive"])
async def add_positive(request: AddPositiveReq, db: Session = Depends(get_db)):
    print(request)
    mssv = request.mssv
    testDate = datetime.date.today()

    to_add = Positive(
        mssv = mssv,
        firstTestDay = testDate,
        negativeDay = None
    )

    db.add(to_add)
    db.commit()

    return Response.ResponseModel(
        code=200,
        message="Add new positive successfully",
        data= {
            "mssv": to_add.mssv,
            "firstTestDay": to_add.firstTestDay,
        }
    )

@router.post("/negative", response_description="Update to negative case", tags=["positive"])
async def update_negative(request : AddPositiveReq ,  db: Session = Depends(get_db)):
    db.query(Positive).filter(Positive.mssv == request.mssv)\
        .update({"negativeDay": datetime.date.today()}, synchronize_session="fetch")
    db.commit()
    return Response.ResponseModel(
        code=200,
        message="Update negative successfully",
        data= {
            "mssv": request.mssv,
            "negativeDay": datetime.date.today(),
        }
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