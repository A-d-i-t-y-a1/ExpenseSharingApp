--------------------------------Expense Sharing App------------------------------------------------------------

Here is a link to the App : http://aditya1211.pythonanywhere.com/

Note: That database is not added

Commands to run on local server
1. clone the Git repository
2. Use the command "python manage.py runserver" to run on your local host

Assumptions
1. paidByUser is the name of user who paid 
2. Amount in the form has to be positive integer
3. ShareType should be either "Percent" or "ExactAmount" (Case Sensitive)
4. User names are case sensitive
5. User involved in a transaction should be seperated by ','
6. Percentage of expense and exact amount should also be seperated by ',' and '%' symbol is not required
7. Description contains the description of expense

Example of a valid inputs----------

PaidByUser: user1
Amount:  10
Share Type (Percent/ExactAmount): ExactAmount
User Involved: user1,user2
Share of Expense Among user: 5,5
Description: choclate

PaidByUser: user5
Amount:  100
Share Type (Percent/ExactAmount): Percent
User Involved: user1,user5
Share of Expense Among user: 40,60
Description: Lunch Bill

------------------------------------------------------------------------------------
1.To check your dues you must click on "Check Your Dues" appering on top-left side of 
home page. 
2. A new page will be prompted, It will ask for your name
3. Enter your name (Case Sensitive) and submit
4. New page will be prompted, showing the net balance with other user
5. A user will appear on above only if it some non zero balance
