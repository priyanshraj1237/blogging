from django.shortcuts import render,redirect
import json
from django.contrib import messages
from django.http import HttpResponse, JsonResponse , HttpResponseNotAllowed
from .mongodb import db
from . firebase import auth
from datetime import datetime
from bson import ObjectId

user_detail=db['user_details']
blog=db['datas']


# Create your views here.
def testing(request):
    return HttpResponse('testing in views.py')


def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email, password)
        try:
            user = auth.create_user_with_email_and_password(email, password)
            print("data got sucessfully....")

            return redirect('login')
        except:
            return render(request, 'signup.html', {'error': 'Signup failed'})
        
    return render(request,'app/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            if user:
                print("TRUE")
            else:
                print("FALSE")
            request.session['uid'] = str(user['idToken'])
            request.session['email']=email
            request.session['password']=password
            return render(request,'app/index.html',{'user': email})
        except:
            return render(request, 'app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'app/login.html')


def tes(request):
    print(request.session['uid'])
    return HttpResponse("session info is stored in chromr")

def load_user_details(request):
    if request.method=='GET':
        email=request.session['email']
        # password=request.session['password']
        print("i love you")
        results=db['datas'].find({'email':email})

        blogs = []
        for blog in results:
            blog['id'] = str(blog['_id'])   # ✅ Create new field 'id'
            del blog['_id']                 # ✅ Optional: remove '_id' if you don't need it
            blogs.append(blog)
        print(blogs)

    return render(request,'app/user_detail.html',{'results':blogs,'email':email})



def delete_data(request, blog_id):
    if request.method == 'GET':  # Or 'POST' if you're sending from a form
        try:
            result = db['datas'].delete_one({"_id": ObjectId(blog_id)})
            if result.deleted_count == 1:
                return render(request,'app/user_detail.html')
            else:
                return JsonResponse({'error': 'Blog not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return HttpResponseNotAllowed(['GET']) 

def update_data(request, document_id):
    print(document_id)
    print("this function hits at atime.......")
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        db['datas'].update_one(
            {'_id': ObjectId(document_id)},
            {'$set': {'title': title, 'content': content}}
        )
        print("Data updated successfully....")
        return redirect('load_user_details')
    return render(request,'app/update.html')


def create_dummy(request):
    if request.method =='POST':
        try:
            user = json.loads(request.body)  # Parse incoming JSON data
            data = {
                "title": user.get("title"),
                "content": user.get("content"),
                "email":request.session['email'],
            }
 
            result=db['datas'].insert_one(data)
            return JsonResponse({'message':"data send to database sucessfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return render(request,'app/index.html')   

def testing(request):
      return render(request,'app/index.html')        

def edit(request, blog_id):
    if request.method == 'GET':
        print("work till this.....")  # Use GET to render the edit form
        document = db['datas'].find_one({'_id': ObjectId(blog_id)})
        document_id = str(document['_id'])
        print(document)
        print(document['_id'])
      

        if document:
            return render(request, 'app/update.html', {'document': document,'document_id':document_id})
        else:
            return HttpResponse("Document not found", status=404)


























































































    #     data = json.loads(request.body)
    #     blog_id = data.get('id')
    #     new_title = data.get('title')
    #     new_content = data.get('content')
    #     print(new_title, new_content)
    #     db['your_collection'].update_one(
    #         {"_id": ObjectId(blog_id)},
    #         {"$set": {"title": new_title, "content": new_content}}
    #     )
    #     return JsonResponse({'message': 'Blog updated successfully!'})
    # return render(request,'app/user_detail.html')