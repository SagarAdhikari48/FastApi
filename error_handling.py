from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    "S001": {"name": "Sagar", "Marks": 85, "grade": "A"},
    "S002": {"name": "Ram", "Marks": 55, "grade": "D"},
    "S003": {"name": "Hari", "Marks": 65, "grade": "C"},
    "S004": {"name": "Shyam", "Marks": 75, "grade": "B"},
}


@app.get("/student/{student_id}")
def get_student(student_id: str):

    if student_id not in students:
        raise HTTPException(
            status_code=404, detail=f"student with ID {student_id} does not exists"
        )
    return students[student_id]


##{"detail":"student with ID S99 does not exists"} for - http://127.0.0.1:8000/student/S99
