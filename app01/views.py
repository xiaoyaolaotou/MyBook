from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse
from django.http import JsonResponse,HttpResponse
from app01 import models

# def user_list(request):
#     """
#     展示所有用户
#     :param request:
#     :return:
#     """
#     ret = models.UserInfo.objects.all()
#     return render(request,"user_list.html",{'user_list':ret})
#
#
# def add_user(request):
#     """
#     添加用户
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         new_name = request.POST.get("username",None)
#         models.UserInfo.objects.create(name=new_name)
#         return redirect('/user_list/')
#     return render(request,'add_user.html')


def publisher_list(request):
    """FBV方式查看出版社列表"""
    ret = models.Publisher.objects.all().order_by("id")
    return render(request,"publisher_list.html",{"publisher_list":ret})


# def add_publisher(request):
#     """添加出版社"""
#     error_msg = ""
#     if request.method == "POST":
#         publisher_name = request.POST.get("publisher_name")
#         if publisher_name:
#             models.Publisher.objects.create(name=publisher_name)
#             return redirect("/publisher_list/")
#         else:
#             error_msg = "不能为空！"
#     return render(request,"add_publisher.html",{"error":error_msg})


class AddPublisher(View):
    """CBV方式添加出版社"""
    def get(self,request):
        print(request.path_info)
        return render(request, "add_publisher.html")

    def post(self,request):
        print(request.body)
        print("=" *120)
        error_msg = ""
        publisher_name = request.POST.get("publisher_name")
        if publisher_name:
            models.Publisher.objects.create(name=publisher_name)
            return redirect("/publisher_list/")
        else:
            error_msg = "不能为空！"
            return render(request,"add_publisher.html",{"error":error_msg})



def delete_publisher(request):
    """删除出版社"""
    del_id = request.GET.get("id",None)
    #如果能取到ID值
    if del_id:
        #根据ID值查找到数据
        del_obj = models.Publisher.objects.filter(id=del_id).delete()
        return redirect("/publisher_list")
    else:
        return HttpResponse("error")



def edit_publisher(request):
    """编辑出版社"""
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()
        url = reverse('publisher_test')
        return redirect(url)

    edit_id = request.GET.get("id",None)
    if edit_id:
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request,"edit_publisher.html",{'publisher':publisher_obj})


def book_list(request):
    """书列表"""
    if request.method == "GET":
        all_book = models.Book.objects.all()
        return render(request,"book_list2.html",{"all_book":all_book})


def add_book(request):
    """添加书"""
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title,publisher_id=new_publisher_id)
        return redirect("/book_list/")
    ret = models.Publisher.objects.all()
    return render(request,"add_book.html",{'publisher_list':ret})


def delete_book(request):
    """删除书籍"""
    delete_id = request.GET.get("id")
    models.Book.objects.get(id=delete_id).delete()
    return redirect('/book_list/')


def edit_book(request):
    """编辑书籍"""
    if request.method == "GET":
        edit_id = request.GET.get("id")
        edit_book_obj = models.Book.objects.get(id=edit_id)
        ret = models.Publisher.objects.all()
        return render(request,"edit_book.html",{"publisher_list":ret,"book_obj":edit_book_obj})

    else:
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title
        edit_book_obj.publisher_id = new_publisher_id
        edit_book_obj.save()
        return redirect("/book_list/")


def author_list(request):
    """展示作者列表"""
    if request.method == "GET":
        all_author = models.Author.objects.all().order_by("id")
        return render(request,"author_list.html",{"author_list":all_author})


def add_author(request):
    """添加作者"""
    if request.method == "POST":
        #取到提交的数据
        new_author = request.POST.get("author_name")
        books = request.POST.getlist("books")
        new_author_obj = models.Author.objects.create(name=new_author)
        new_author_obj.book.set(books) #多对多进行创建数据
        new_author_obj.save()
        return redirect('/author_list/')

    ret = models.Book.objects.all()
    return render(request,"add_author.html",{"book_list":ret})


def delete_author(request):
    """删除作者"""
    #根据ID值取到要删除的ID
    delete_id = request.GET.get('id')
    models.Author.objects.get(id=delete_id).delete()
    return redirect("/author_list/")


def edit_author(request):
    """修改作者"""
    if request.method == "POST":
        #根据当关编辑的ID
        edit_author_id = request.POST.get("author_id")
        #拿到提交过来的数据
        new_author_name = request.POST.get("author_name")
        #拿到编辑后作者关联的书籍信息
        new_books = request.POST.getlist("books")
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_name #更新作者
        edit_author_obj.book.set(new_books) #更新作者关联的书籍
        edit_author_obj.save()
        return redirect("/author_list/")


    #从URL里取到要编辑的作者信息
    edit_id = request.GET.get('id')
    # 找到要编辑的作者对象
    edit_author_obj = models.Author.objects.get(id=edit_id)

    #查询所有的书籍对象
    ret = models.Book.objects.all()
    return render(request,"edit_author.html",{"book_list":ret,"author":edit_author_obj})



def upload(request):
    if request.method == "GET":
        return render(request,'upload.html')
    elif request.method == "POST":
        print(request.FILES)
        filename = request.FILES['upload_file'].name
        with open(filename,'wb') as f:
            for chunk in request.FILES["upload_file"].chunks():
                f.write(chunk)
        return HttpResponse("OK")







