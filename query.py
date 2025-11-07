import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row #以字典形式输出
    cursor = conn.cursor()



    # 1. SHOW ALL TESTS
    print('\n')
    print('All TESTS')
    cursor.execute('SELECT project_name,test_date,required_strength,actual_strength,passed FROM concrete_tests')
    while row:=cursor.fetchone():
        projectname = row['project_name']
        test_date = row['test_date']
        required_strength=row['required_strength']
        acutal_strength=row['actual_strength']
        if row['passed']==0:
            pass1='Fail'
        else:
            pass1='Pass'
        print(f"{projectname}: {acutal_strength} PSI - {pass1}")
    
    print('\n')

    

    # 2. Show ONLY failed tests
    print('Failed Tests')
    cursor.execute('SELECT * From concrete_tests where passed=0 ')
    while row:=cursor.fetchone():
        projectname = row['project_name']
        test_date = row['test_date']
        required_strength=row['required_strength']
        acutal_strength=row['actual_strength']
        pass1=row['passed']
        print(f'{projectname} on {test_date}')
        print(f'  Required:{required_strength} PSI')
        print(f'  Actual:{acutal_strength} PSI')
        print('\n')
   
    # 3. Count tests by project
    # cursor.execute('SELECT * From concrete_tests where project_name=Bridge Repair')
    print('Tests Per Project')
    cursor.execute("""
        SELECT 
            project_name,
            SUM(passed) AS passed,     
            COUNT(*) AS total        
        FROM concrete_tests
        GROUP BY project_name;
    """)

    results = cursor.fetchall()

print("TESTS PER PROJECT")
for row in results:
    project_name, passed, total = row
    print(f"{project_name}: {passed}/{total} passed")

