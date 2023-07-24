todo=[]

present=1

while True:
   
   user_choose = int(input('\n**** PELLA TO DO LIST****\n\n1. Add To Do \n2. Remove To Do\n 3. Update To Do\n 4. View To Do\n 5. Exit App\n\n Provide Option : '))

   if user_choose==1:
      add = input('Enter Title : ')
      if add in todo:
          print(" Title Already Exist")
      else:
       todo.append(add)
       print('To Do Saved Successfully')
   elif user_choose==2:
       if len(todo)<1:
           print('Empty Database')
       else:
        add = input('Enter Title To Remove : ')
        todo.remove(add)
        print("Removed Successfully")
   elif user_choose==3:
       add = input('Enter Title :')
       if add in todo:
        update = input('Enter New Update :')
        todo.remove(add)
        todo.append(update)
        print('Update Successfully')
       else:
          print('Invalid Title')
   elif user_choose==4:
       for i in todo:
           print(i,sep='\n')
       else:
           print('Database is Empty')    
   elif user_choose==5:
       break
   else:
       print('Invalid User Option, Try Again')










