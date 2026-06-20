from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    "S001": {"name": "Sagar", "Marks": 85, "grade": "A"},
    "S002": {"name": "Ram", "Marks": 55, "grade": "D"},
    "S003": {"name": "Hari", "Marks": 65, "grade": "C"},
    "S004": {"name": "Shyam", "Marks": 75, "grade": "B"},
}


# Input schema


class MarksSubmission(BaseModel):
    student_id: str
    marks: int
    subject: str


@app.get("/student/{student_id}")
def get_student(student_id: str):

    if student_id not in students:
        raise HTTPException(
            status_code=404, detail=f"student with ID {student_id} does not exists"
        )
    return students[student_id]


##{"detail":"student with ID S99 does not exists"} for - http://127.0.0.1:8000/student/S99


@app.post("/submit-makes")
def submit_marks(submission: MarksSubmission):
    # Error 1
    if submission.student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {submission.student_id} doesnot found!",
        )
    # Error 2 valid range 0-100
    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Marks nust be between 0 and 100",
                "marks_received": submission.marks,
                "fix": "Enter a valid range between 0 and 100",
            },
        )
    if submission.subject.strip() == "":
        raise HTTPException(status_code=400, detail="Subject cannot be empty")

    try:
        students[submission.student_id]["marks"] = submission.marks
        return {
            "message": "Marks submitted successfully",
            "student": students[submission.student_id]["name"],
            "subject": submission.subject,
            "marks": submission.marks,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Something went wrong from our side: {str(e)} "
        )
