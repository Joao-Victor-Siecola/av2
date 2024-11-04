from database import Database
from teacher_crud import TeacherCRUD

db = Database("bolt://3.236.41.76:7687", "neo4j", "pushes-winters-fences")


teacher_crud = TeacherCRUD(db)


teacher_crud.create(name="Jake", ano_nasc=2003, cpf="126.203.666-66")


teacher = teacher_crud.read(name="Jake")
print("Teacher found:", teacher)


teacher_crud.update(name="Jake", new_cpf="126.203.666-66")

db.close()