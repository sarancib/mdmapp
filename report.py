import database
import reports.user_report

connection = database.get_connection()
cur = connection.cursor()
# User count report
user_report = reports.user_report.UserReport(cur)
user_report_data = user_report.process()
print(f'We have {user_report_data} users')
#get users findings
findings= user_report.countAlbumsTodos()
print("Users Report:\n")
for row in findings:
            print("User_name: ", row[0])
            print("Albums: ", row[1])
            print("Unfinished_todos: ", row[2])
            print("\n")
