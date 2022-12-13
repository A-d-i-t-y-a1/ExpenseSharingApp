from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

userToUserTransactionHistory={}
userToUserDue={}

# Create your views here.
def addExpense(request):
    if request.method=="POST":

        #fetching values from form
        paidByUser=request.POST.get('paidByUser')
        amount=request.POST.get('amount')
        userList=request.POST.get('userList')
        shareType=request.POST.get('shareType')
        expenseShare=request.POST.get('expenseShare')
        description=request.POST.get('description')

        users=[]
        expenses=[]
        #fetching the user and there share LAmounts
        if userList is not None and expenses is not None:
            users=userList.split(",")
            expenses=expenseShare.split(",")

        #checking weather the amount is a positive integer
        if amount.isdigit()==False and int(amount)<=0:
            print("Invalid Input")
            messages.error(request, 'Invalid Input-Amount Should be is a positive integer')
            return redirect('/')

        # Amount should be equal to exact amount 
        if shareType=="ExactAmount":
            sum=0
            for expense in expenses:
                if expense.isdigit()==False:
                    print("Invalid Input")
                    messages.error(request, 'Invalid Input- Indiviual expense is invalid')
                    return redirect('/')
                else:
                    sum+=int(expense)

            if sum!=int(amount) or len(users)!=len(expenses):
                print("Invalid Input")
                messages.error(request, 'Invalid Input- Amount is not equal to sum of indiviual amount or less number of people')
                return redirect('/')

        elif shareType=="Percent":
            sum=0
            for expense in expenses:
                if expense.isdigit()==False:
                    print("Invalid Input")
                    messages.error(request, 'Invalid Input- Indiviual percent is invalid')
                    return redirect('/')
                else:
                    sum+=int(expense)

            if sum!=100 or len(users)!=len(expenses):
                print("Invalid Input")
                messages.error(request, 'Invalid Input- Percentages not suming upto 100 or less/more expenses given')
                return redirect('/')
        else:
            print("Invalid Input")
            messages.error(request, 'Invalid Input- Share Type is not matching')
            return redirect('/')
        
        if shareType=="Percent":
            idx=0
            for user in users:
                if(user==paidByUser):
                    idx+=1
                    continue

            if userToUserDue.get((paidByUser,user))==None:
                userToUserDue[(paidByUser,user)]=0
                userToUserTransactionHistory[(paidByUser,user)]=[]
            userToUserDue[(paidByUser,user)]+=((int(expenses[idx])*int(amount))/100)
            userToUserTransactionHistory[(paidByUser,user)].append([((int(expenses[idx])*int(amount))/100),description])

            if userToUserDue.get((user,paidByUser))==None:
                userToUserDue[(user,paidByUser)]=0
                userToUserTransactionHistory[(user,paidByUser)]=[]
            userToUserDue[(user,paidByUser)]-=((int(expenses[idx])*int(amount))/100)
            userToUserTransactionHistory[(user,paidByUser)].append([-1*((int(expenses[idx])*int(amount))/100),description]) 
            idx+=1
        else:
            idx=0
            for user in users:

                if(user==paidByUser):
                    idx+=1
                    continue

                if userToUserDue.get((paidByUser,user))==None:
                    userToUserDue[(paidByUser,user)]=0
                    userToUserTransactionHistory[(paidByUser,user)]=[]
                userToUserDue[(paidByUser,user)]+=int(expenses[idx])
                userToUserTransactionHistory[(paidByUser,user)].append([int(expenses[idx]),description])

                if userToUserDue.get((user,paidByUser))==None:
                    userToUserDue[(user,paidByUser)]=0
                    userToUserTransactionHistory[(user,paidByUser)]=[]
                userToUserDue[(user,paidByUser)]-=int(expenses[idx])
                userToUserTransactionHistory[(user,paidByUser)].append([-1*int(expenses[idx]),description]) 
                idx+=1

        print(userToUserDue)
        print(userToUserTransactionHistory)
        messages.success(request, 'Expense Saved')
        return redirect('/')

    return render(request,'home.html')

def checkDue(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contextPay=[]
        contextTake=[]

        for userPair in userToUserDue:
            if userPair[0]==name:
                
                if userToUserDue[userPair]>0:
                    contextTake.append([userPair[1],userToUserDue[userPair]])
                elif userToUserDue[userPair]<0:
                    contextPay.append([userPair[1],-1*userToUserDue[userPair]])

        context={'pay':contextPay, 'take':contextTake}
        return render(request,"userDue.html",context)
    return render(request,"checkDue.html")
    

def userDue(request):
    return HttpResponse("you are great")