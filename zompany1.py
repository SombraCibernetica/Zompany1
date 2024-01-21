from fastapi import FastAPI

app = FastAPI()

students = [
    {
        "id": 1,
        "username": "felixOchoa"
},
        {
        "id": 2,
        "username": "camiloPerez"
},
    {
        "id": 3,
        "username": "andresPerez"
} 
]
@app.get("/")
async def root():
    return {"memsaje":"felix Ochoa es bacano"}

@app.get("/students/{id}")
async def getStudentById(id:int):
    studentSearch = student

    studentSearch = {}
    for student in student:
        if(student["id"] == id):
            studentSearch = student


    return {
        "mensaje":studentSearch,}

@app.get("/estudent-by-name/{username}")
async def getStudentByName(username: str):

    studentSearch = {}
    for student in students:
        if(student[username] == username):
            studentSearch = student

    return {
        "mensaje":studentSearch,
}

@app.post("/create-students")
async def createStudent(id: int, username: str):
    studentCreate = {
        "id":id,
        "username":username
    }
students.append(studentCreate):
    return("message": "El estudiante se a creado")


@app.put("/edit-student")
async def editStuden(id:int, username: str):
    for studen in studens:
        if (studen["id"] == id ):
            studen["id"] = id 
            studen["username"] = useraname

    return(
        "mensaje": "se edito el estudiante"
        )

@app.delete("/delete-studen")
async def deletreStuden(id: int):
    for student in students:
        if(student["id"] == id):
            students.remove(student)
    return(
        "mensaje": "se a eliminado el estudiante"
        )


