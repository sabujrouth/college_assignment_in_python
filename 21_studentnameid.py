def student_data(student_id, **DIATM):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in DIATM:
        print(f"Student Name: $ {DIATM['student_name']}")

 
student_data(student_name='Sabuj Routh',student_id='CS/21/96')