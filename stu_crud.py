from db_config import get_db_connection

# 1️⃣ Create
def create_student(id, name, course, marks):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO student_info (id, name, course, marks) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, name, course, marks))
    conn.commit()
    print("✅ Student record created successfully.")
    cursor.close()
    conn.close()

# 2️⃣ Read
def read_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_info")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# 3️⃣ Update
def update_student(id, name=None, course=None, marks=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    fields = []
    values = []

    if name:
        fields.append("name=%s")
        values.append(name)
    if course:
        fields.append("course=%s")
        values.append(course)
    if marks is not None:
        fields.append("marks=%s")
        values.append(marks)

    if fields:
        query = "UPDATE student_info SET " + ", ".join(fields) + " WHERE id=%s"
        values.append(id)
        cursor.execute(query, tuple(values))
        conn.commit()
        print("✅ Student record updated successfully.")
    else:
        print("⚠️ No fields provided to update.")

    cursor.close()
    conn.close()

# 4️⃣ Delete
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student_info WHERE id=%s", (id,))
    conn.commit()
    print("✅ Student record deleted successfully.")
    cursor.close()
    conn.close()

# 5️⃣ Exit
def exit_program():
    print("👋 Exiting program...")
    exit()
