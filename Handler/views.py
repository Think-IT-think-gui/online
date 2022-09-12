from django.shortcuts import render,redirect
from .serializers import ClientInfoSerializer,SignUpSerializer,CartSerializer,ProductSerializer,AdminSerializer,MessageSerializer
from . models import Login_info,SignUp_info,Cart_info,Products,Admin,Contact
from rest_framework.response import Response
from rest_framework.views import APIView
import sqlite3
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q
import shutil
#============================================User name and password===========================================
BASE_DIR = Path(__file__).resolve().parent.parent

conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
c = conn1.cursor()
c.execute("SELECT * FROM  Handler_Products")
product_info = c.fetchmany(20)
conn1.commit()
product_info2 = product_info[3:12]
conn1.close()


class Login_Api(APIView):
    def get(self, request):
        return render(request, 'Login.html')
    def post(self, request):
          serializer = ClientInfoSerializer(data=request.data)
          if serializer.is_valid():
            user1_check = request.data['User']
            user2_check = request.data['Password']
            conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_SignUp_info WHERE  User='{user1_check}'")
            Clients_info = c.fetchone()
            conn1.commit()
            conn1.close()
            if Clients_info == None:
               return render(request, 'errors/invalid_credentials.html')
            else:
              if Clients_info[5] == user2_check:
                serializer.save()
                response =  redirect('defult')
                response.set_cookie('User', user1_check)
                return response
              else:
                 return render(request, 'errors/invalid_credentials.html')
          return render(request, 'errors/invalid_credentials.html')

class Account_Status(APIView):
    def get(self, request, pk):
        if pk ==  "user1_check":
          return redirect('login')
        else:
          return render(request,'logout.html', {"User":pk})


class Set_user(APIView):
    def get(self, request,pk):
       if pk == "user1_check":
            return  redirect('defult')
       else:
           return render(request, 'settings_tab.html', {'User':pk})


class Logout(APIView):
    def post(self, request):
       return redirect('defult')
#============================================User name and password===========================================

class Set_Image(APIView):
    def get(self,request,pk):
       return render(request, 'Profile_img.html', {'user':pk})

class Validate_action(APIView):
    def get(self,request,pk):
        return render(request, 'confirm_action.html', {'User':pk})
    def post(self,request,pk ):
            User = pk
            Password = request.data["Password"]
            conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_SignUp_info WHERE  User='{User}'")
            Clients_info = c.fetchone()
            conn1.commit()
            conn1.close()
            if Clients_info[5] == Password:
                return render(request, 'Delete_account.html', {'User':User})
            else:
                return render(request, 'settings_tab.html', {'User':User})

class Delete_account(APIView):
    def post(self, request):
        User = request.data["User"]
        conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn1.cursor()
        print(User)
        c.execute(f"DELETE from  Handler_SignUp_info WHERE  User='{User}'")
        conn1.commit()
        conn1.close()
        os.remove(f'{BASE_DIR}\\static\\media\\Clients\\{User}.jpg')
        response =   redirect('defult')
        response.delete_cookie('User')

        return response

class Set_basic(APIView):
    def get(self, request,pk):
       if pk == "user1_check":
            return redirect('defult')
       else:
            conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_SignUp_info WHERE  User='{pk}'")
            Clients_info = c.fetchone()
            conn1.commit()
            conn1.close()
            return render(request, 'edit_basic.html', {'User':pk,"All":Clients_info})
    def post(self, request, pk):
            User = request.data["User"]
            First_Name = request.data["First_Name"]
            Email = request.data["Email"]
            Gender = request.data["Gender"]
            conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn1.cursor()
            c.execute("""UPDATE Handler_SignUp_info set First_Name = :First_Name, Gender = :Gender, Email = :Email WHERE User = :User""",{"Email":Email,"User":User,"Gender":Gender,"First_Name":First_Name})
            conn1.commit()
            return render(request, 'settings_tab.html', {'User':User})
#=============================================================== settings ======================================================
class Set_pass(APIView):
    def get(self, request,pk):
       if pk == "user1_check":
           return redirect('defult')
       else:
            return render(request, 'edit_pass.html', {'User':pk})

    def post(self, request, pk):
            Password = request.data["Password"]
            conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_SignUp_info WHERE  User='{pk}'")
            Clients_info = c.fetchone()
            conn1.commit()
            if Clients_info[5] == Password:
                return render(request, 'new_password.html', {'User':pk})
            else:
                return render(request, 'settings_tab.html', {'User':pk})
class New_password(APIView):
    def post(self,request):
            User = request.data["User"]
            Password = request.data["Password"]
            conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn1.cursor()
            c.execute("""UPDATE Handler_SignUp_info set Password = :Password WHERE User = :User""",{"Password":Password,"User":User})
            conn1.commit()
            return render(request, 'settings_tab.html', {'User':User})




#================================================= payment =====================================================

class Pay(APIView):
    def post(self,request):
        User = request.data["User"]
        data = request.data
        print(data)
        conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn1.cursor()
        c.execute(f"SELECT * FROM  Handler_Cart_info WHERE User='{User}'")
        info = c.fetchall()
        conn1.commit()
        conn1.close()
        total_amount = 0
        for i in info:
            #print(i[2][0:-3])

            convert_data = str(i[2][0:-3]).replace(",","")
            amount = float(convert_data)

            quantity = float(data[i[1]+"-number"])

            total_amount += float(amount*quantity)

        return render(request, 'home/home_page.html', {'User':User})


       # return Response(total_amount)







#================================================= payment =====================================================






















#=============================================== create account =================================================
class Home(APIView):
    def get(self , request):
      if 'User' in request.COOKIES:
       user1_check = request.COOKIES['User']
       return render(request, 'start_home.html', {'product':product_info, 'User':user1_check ,'roll':product_info2})
      else:
       return render(request, 'start_home.html', {'product':product_info, 'User':"user1_check" ,'roll':product_info2})

class Home_content(APIView):
    def get(self , request,pk):
      
       return render(request, 'home/home_page.html', {'product':product_info, 'User':pk ,'roll':product_info2}) 


class All(APIView):
    def post(self , request):
       conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
       c = conn1.cursor()
       c.execute("SELECT * FROM  Handler_Products")
       product_info = c.fetchall()
       conn1.commit()
       product_info2 = product_info[3:12]
       conn1.close()
       return render(request, 'main.html', {'product':product_info, 'User':request.data["User"] ,'roll':product_info2})

class About(APIView):
    def get(self , request, pk):
       return render(request, 'about.html', { 'User':pk})

class Signup_Api(APIView):
    def get(self, request):
        return render(request, 'Signup.html')
    def post(self, request):
        user1_check = request.data["User"]
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
         conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
         c = conn1.cursor()
         c.execute(f"SELECT * FROM  Handler_SignUp_info WHERE  User='{user1_check}'")
         Clients_info = c.fetchone()
         conn1.commit()
         conn1.close()
         if Clients_info == None:
          serializer.save()
          shutil.copy(f'{BASE_DIR}/static/media/Clients/user1_check.jpg',f'{BASE_DIR}/static/media/Clients/{user1_check}.jpg')
          return redirect('defult')
         else:
          return render(request, 'errors/Already_exist.html')
        return render(request, 'errors/Input_error.html')


class Categories_Api(APIView):
    def get(self, request, pk):
        return render(request, 'services.html', {'User':pk} )

class Request_Product(APIView):
    def get(self, request, pk, pk2):

        conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn1.cursor()
        c.execute(f"SELECT * FROM  Handler_Products WHERE  Class='{pk2}' ")
        product_info = c.fetchall()
        print(product_info)
        conn1.commit()
        conn1.close()
        if product_info == []:
            data = f"No items found in {pk2}"
        else:
           data = f"Products of {pk2}"
        return render(request, 'category/cat.html', {"User":pk,"Info":product_info,"comment":data})

class Home_2(APIView):
    def get(self, request, pk):
      return redirect('defult')

class Log_out(APIView):
    def get(self, request, pk):

       response =  redirect('defult')
       response.delete_cookie('User')

       return response


class Profile_Api(APIView):

    def get(self, request):
        pass
    def post(self, request):
         print(request.data["User"])
         uploading_file = request.FILES['Img']
         fs = FileSystemStorage()
         user1_check = request.data["User"]
         os.remove(f'{BASE_DIR}/static/media/Clients/{user1_check}.jpg')
         fs.save("Clients//"+request.data['User']+".jpg",uploading_file)
         conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
         c = conn1.cursor()
         c.execute("""UPDATE Handler_Signup_info SET Img = :img WHERE User = :user """,{'img':request.data['User'],'user':request.data['User']})
         conn1.commit()
         conn1.close()
         return redirect('defult')


#=============================================== create account =================================================


#=============================================== create cart =================================================

class Rem_Cart(APIView):
    def post(self, request):
        user = request.data["User"]
        product = request.data["Product"]
        conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn1.cursor()
        c.execute(f"DELETE from  Handler_Cart_info WHERE Product='{product}'")
        conn1.commit()
        c.execute(f"SELECT * FROM  Handler_Cart_info WHERE User='{user}'")
        info = c.fetchall()
        print(product)
        conn1.commit()
        conn1.close()
        return render(request, 'cart.html' ,{'User':user, 'cart':info})

class Cart_Api(APIView):
    def get(self, request, pk):
        if pk == "user1_check":
            return redirect('login')
        conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
        c = conn1.cursor()
        c.execute(f"SELECT * FROM  Handler_Cart_info WHERE User='{pk}'")
        info = c.fetchall()
        conn1.commit()
        conn1.close()
        return render(request, 'cart.html' ,{'User':pk, 'cart':info})
    def post(self, request, pk):
        serializer = CartSerializer(data=request.data)
        user = request.data["User"]
        if serializer.is_valid():
         if request.data["User"] ==  "user1_check":
          return redirect('login')
         else:
          conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
          c = conn1.cursor()
          c.execute(f"SELECT * FROM  Handler_Cart_info WHERE User='{user}'")
          data = c.fetchall()
          conn1.commit()
          conn1.close()
          for i in data:
              if request.data["Product"] == i[1]:

                   return redirect('defult')
              else:
                   pass
          serializer.save()

          return redirect('defult')
        return Response("Error")



#=============================================== create cart =================================================


#=============================================== products =================================================

class Product_Api(APIView):

    def post(self, request, pk):
        pro = request.data["Product"]
        serializer = ProductSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():

         conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
         c = conn1.cursor()
         c.execute(f"SELECT * FROM  Handler_Products WHERE Product='{pro}'")
         Pro_info = c.fetchall()
         conn1.commit()
         conn1.close()
         print(Pro_info)
         if Pro_info == []:
          serializer.save()
          conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
          uploading_file = request.FILES['Img']
          fs = FileSystemStorage()



          fs.save("Product//"+request.data['Product']+".jpg",uploading_file)
         else:
                 pass
                 conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_SignUp_info")
                 Clients_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Products")
                 Pro_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Contact")
                 msg_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Login_info")
                 log_info = c.fetchall()
                 conn1.commit()
                 conn1.close()
                 return render(request, 'Admin_Tab/index.html', {"User":pk,"Info":Clients_info, "Product":Pro_info, "ask":msg_info, "logs":log_info})


class Search_Api(APIView):

     def get(self, request,pk1,pk2):
        Recieved = pk2
        data = Products.objects.filter(Q(Product__icontains=Recieved))
        if str(data) == "<QuerySet []>":
         tell="No result found!"   
         return render(request, 'search.html', {"User":pk1,"Info":[],"comment":tell})
        else:
         tell=f"Search result of '{Recieved}'"   
         Result = [] 
         for i in data:       
          conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')   
          c = conn1.cursor()
          c.execute(f"SELECT * FROM  Handler_Products WHERE Product='{i}' ")
          Pro_info = c.fetchone()
          conn1.commit()
          conn1.close()
          Result.append(Pro_info)
        return render(request, 'category/cat.html', {"User":pk1,"Info":Result,"comment":tell})


#=============================================== products =================================================

#=============================================== Admin account =================================================

class Admin_Api(APIView):

    def get(self, request):
        Recieved_data = Admin.objects.all()

        #return Response(serializer.data)
        return render(request, 'Admin_Tab/data.html')
    def post(self, request):

            user1_check = request.data['User']
            user2_check = request.data['Password']
            conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_Admin WHERE  User='{user1_check}'")
            Clients_info = c.fetchone()
            print(Clients_info)
            conn1.commit()
            conn1.close()
            if Clients_info == None:
               return render(request, 'errors/invalid_credentials.html')
            else:
             if Clients_info[2] == user2_check:
                 conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_SignUp_info")
                 Clients_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Products")
                 Pro_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Contact")
                 msg_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Login_info")
                 log_info = c.fetchall()
                 conn1.commit()
                 conn1.close()
                 return render(request, 'Admin_Tab/index.html', {"User":user1_check,"Info":Clients_info, "Product":Pro_info, "ask":msg_info, "logs":log_info})
             else:

                 return render(request, 'errors/invalid_credentials.html')



class Remove_Product(APIView):
    def post(self, request):

                 product = request.data["Product"]
                 conn1 = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')
                 c = conn1.cursor()
                 c.execute(f"DELETE from  Handler_Products WHERE Product='{product}'")
                 conn1.commit()
                 os.remove(f"/home/aminutahiru600/PZONE/online/static/media/Product/{product}.jpg")

                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_SignUp_info")
                 Clients_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Products")
                 Pro_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Contact")
                 msg_info = c.fetchall()
                 conn1.commit()
                 c = conn1.cursor()
                 c.execute("SELECT * FROM  Handler_Login_info")
                 log_info = c.fetchall()
                 conn1.commit()
                 conn1.close()
                 return render(request, 'Admin_Tab/index.html', {"User":request.data["User"],"Info":Clients_info, "Product":Pro_info, "ask":msg_info, "logs":log_info})



#=============================================== Admin account =================================================


#=============================================== messages =================================================

class Message_Api(APIView):

    def get(self, request, pk):
        return render(request, 'contact.html', {'User':pk})

    def post(self, request, pk):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return redirect('defult')


#=============================================== messages =================================================
