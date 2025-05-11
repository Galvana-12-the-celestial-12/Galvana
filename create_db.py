from main import app, db

app.app_context().push()
db.create_all
print("База данных создана")