import psycopg2
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

connection = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

cursor = connection.cursor()
cursor=connection.cursor()

"""CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary NUMERIC(10,2)
);"""

def add_employees():
    try:
        num = int(input("👥 How many employees do you want to add? "))
    except (ValueError,TypeError):
        print("⚠️ Please enter a valid number.")
        return

    employees=[]
    query="""insert into employees(
            name,department,salary)
            values(%s,%s,%s)"""
    
    for i in range(num):
        print(f"\n📝 Entering Employee {i + 1} Details")
        print("-" * 35)
        name = input("👤 Enter employee name: ").strip().capitalize()
        department = input("🏢 Enter department: ").strip().upper()
        try:
            salary = float(input("💰 Enter salary: "))
        except(ValueError,TypeError):
            print("⚠️ Please enter a valid salary amount.")
            return
        print("")
        employees.append((name,department,salary))
    for employee in employees:
        cursor.execute(query,employee)
    connection.commit()
    print("✅ Employees added successfully!")

def view_employees():
    cursor=connection.cursor()
    query="select id,name,department,salary from employees"
    cursor.execute(query)
    result=cursor.fetchall()
    if not result:
        print("📭 No employees found.")
    else:    
        print(f"{'ID':<8}{'Employee name':<25}{'Department':<15}{'Salary':<10}")
        print("-"*60)
        for row in result: 
            print(f"{row[0]:<8}{row[1]:<25}{row[2]:<15}{row[3]:<10}")

def update_employees():
    try:
        sal = float(input("💰 Enter new salary: "))
        id = int(input("🆔 Enter employee ID: "))
    except (ValueError,TypeError):
        print("⚠️ Please enter a valid number.")
        return
    query="""update employees
            set salary=%s
            where id=%s"""
    cursor.execute(query,(sal,id))
    connection.commit()
    if cursor.rowcount==1:
        print("✅ Employee salary updated successfully!")
    else:
        print("❌ Employee ID not found.")
def delete_employees():
    try:
        employee_id = int(input("🆔 Enter employee ID to delete: "))
    except (ValueError,TypeError):
        print("⚠️ Please enter a valid employee ID.")
        return
    query="""delete from employees
            where id=%s"""
    cursor.execute(query,(employee_id,))
    connection.commit()
    if cursor.rowcount==1:
        print("🗑️ Employee deleted successfully!")
    else:
        print("❌ Employee ID not found.")


def analytics():
    while True:
        print("")
        print("╔══════════════════════════════════════════╗")
        print("║           📊 ANALYTICS MENU              ║")
        print("╠══════════════════════════════════════════╣")
        print("║  1️⃣  Salary Analytics                     ║")
        print("║  2️⃣  Department Analysis                  ║")
        print("║  3️⃣  Top Employees                        ║")
        print("║  4️⃣  Salary Increase Analysis             ║")
        print("║  5️⃣  🔙 Back                              ║")
        print("╚══════════════════════════════════════════╝")
        try:
            choice = int(input("👉 Enter your choice (1-5): "))
        except(ValueError,TypeError):
            print("⚠️ Please enter a valid number.")
            continue

        if choice==1:
            cursor.execute("select avg(salary),sum(salary) from employees")
            result=cursor.fetchone()
            print(f"📊 Average Salary : ₹{result[0]:,.2f}")
            print(f"💰 Total Salary   : ₹{result[1]:,.2f}")
            cursor.execute("select name,salary from employees order by salary desc limit 1")
            max_result=cursor.fetchone()
            
            if max_result:
                print(f"🏆 Highest Salary : {max_result[0]} — ₹{max_result[1]:,.2f}")
            cursor.execute("select name,salary from employees order by salary asc limit 1")
            min_result=cursor.fetchone()
            if min_result:
                print(f"📉 Lowest Salary  : {min_result[0]} — ₹{min_result[1]:,.2f}")

        elif choice==2:
            query="select department,count(id),avg(salary),max(salary),min(salary)from employees group by department"
            cursor.execute(query)
            result=cursor.fetchall()
            for row in result:
                print("\n" + "-" * 40)
                print(f"🏢 Department       : {row[0]}")
                print(f"👥 Employees        : {row[1]}")
                print(f"📊 Average Salary   : ₹{row[2]:,.2f}")
                print(f"💰 Maximum Salary   : ₹{row[3]:,.2f}")
                print(f"📉 Minimum Salary   : ₹{row[4]:,.2f}")
                print("-" * 40)
        elif choice==3:
            try:
                num = int(input("🏆 How many top employees do you want? "))
            except (ValueError,TypeError):
                print("⚠️ Please enter a valid number.")
                continue
            if num>0:
                query="""select id,name,salary 
                        from employees order by salary desc limit %s"""
                cursor.execute(query,(num,))
                result=cursor.fetchall()
                if not result:
                    print("📭 No employees found.")
                else:    
                    for row in result:
                        print(f"🏆 ID: {row[0]} | {row[1]} | Salary: ₹{row[2]:,.2f}")
            else:
                print("⚠️ Please enter a valid number.")
        elif choice==4:
            query="select name,salary from employees"
            cursor.execute(query)
            result=cursor.fetchall()

            names=[row[0] for row in result]
            salaries=[float(row[1])for row in result]

            salary_array=np.array(salaries)
            salary_in=salary_array*1.10 

            for name,ori_sal,inc_sal in zip(names,salaries,salary_in):
                print(
                        f"👤 {name:<15} "
                        f"Original: ₹{ori_sal:,.2f}  →  "
                        f"After 10%: ₹{inc_sal:,.2f}"
                    )
        
        elif choice==5:
            break  
        else:
            print("⚠️ Please enter a valid number.")  

def exit_app():
    print("\n👋 Thank you for using Employee Salary Analytics!")
    print("🚪 Exiting application...")     
    connection.close()
def main():

    while True:
        print("")
        print("╔══════════════════════════════════════════╗")
        print("║       👨‍💼 EMPLOYEE SALARY ANALYTICS      ║")
        print("╠═════════════════════════════════════════╣")
        print("║  1️⃣  Add Employee                        ║")
        print("║  2️⃣  View Employees                      ║")
        print("║  3️⃣  Update Employee Salary              ║")
        print("║  4️⃣  Delete Employee                     ║")
        print("║  5️⃣  📊 Analytics                        ║")
        print("║  6️⃣  🚪 Exit                             ║")
        print("╚═════════════════════════════════════════╝")
        print("")
        try:
            choice = int(input("👉 Enter your choice (1-6): "))
        except(ValueError,TypeError):
            print("⚠️ Please enter a valid number.")
            continue
        if choice==1:
            add_employees()
        elif choice==2:
            view_employees()
        elif choice==3:
            update_employees()
        elif choice==4:
            delete_employees()
        elif choice==5:
            analytics()
        elif choice==6:
            exit_app() 
            break
        else:
            print("❌ Invalid choice! Please select an option from 1-6.")
if __name__=="__main__":
    main()