import datetime
from pydantic import BaseModel

class CreateStudentReq(BaseModel):
    mssv: int
    fullName: str
    classCode: str


class AddPositiveReq(BaseModel):
    mssv: int