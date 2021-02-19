from django.shortcuts import render, redirect
from mukja.models import Golmok, Restaurant, Menu, Comment, Board
from .forms import CommentForm
from django.views.generic import UpdateView
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def golmok(request, pk):
    golmok_pk = pk
    mukjagolmok = Golmok.objects.get(id=pk)
    restaurants = Restaurant.objects.filter(golmok_id=golmok_pk)
    page = request.GET.get('page', 1)
    paginator = Paginator(restaurants, 3)
    restaurantspage = paginator.get_page(page)
    context = {
        'mukjagolmok': mukjagolmok,
        'restaurants': restaurantspage,
    }
    return render(request, "golmok.html", context)


def restaurant(request, fk, pk):
    golmok_pk = fk
    restaurant_pk = pk
    restaurant = Restaurant.objects.get(id=restaurant_pk)
    menus = Menu.objects.filter(restaurant_id=restaurant_pk)
    comment = Comment.objects.filter(restaurant_id=restaurant_pk)

    context = {
        'restaurant': restaurant,
        'menus': menus,
        'comment' : comment,
    }
    context['comment_form'] = CommentForm()

    return render(request, "restaurant.html", context)


def new_comment(request, fk, pk):
    restaurant = Restaurant.objects.get(id=pk)

    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid(): # 유효한 경우 필요한 것을 채워줘야함. 현재 form에는 text만 받아온 상태.. model 에 저장되어 있는 author 등을 받아와야함
            comment = comment_form.save(commit=False)
            comment.restaurant = restaurant
            comment.author = request.user
            comment.save()
            return redirect(comment.get_absolute_url()) # 해당 댓글로 바로 이동하기 위해 get absolute url 함수 만들었음 -> models에 있음
    else:
        return redirect('/mukja/')


class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_object(self, queryset = None):
        comment = super(CommentUpdate, self).get_object()  #super는 deleteview를 지칭
        if comment.author != self.request.user:
            raise PermissionError('Comment를 수정할 권한이 없습니다.')
        return comment




def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.user == comment.author:
        restaurant = comment.restaurant
        comment.delete()
        return redirect(restaurant.get_absolute_url() + '#comment-list')
    else:
        raise PermissionError('Comment를 삭제할 권한이 없습니다.')


def register(request):
    res_data = None
    if request.method =='POST':
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        firstname = request.POST.get('firstname', 'Unknown')
        lastname = request.POST.get('lastname', 'Unknown')
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password',None)
        res_data = {}
        if User.objects.filter(email=useremail):
            res_data['error']='Your Email address is already registered'
        elif User.objects.filter(username=username):
            res_data['error'] = 'Your username is already registered'
        elif password != re_password:
            res_data['error']='Re-password was not equal to password'
        else:
            user = User.objects.create_user(username = username,
                            email=useremail,
                            first_name = firstname,
                            last_name = lastname,
                            password = password)
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect('/mukja/')
    return render(request, 'register.html', res_data)


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect("index")
        else :
            return render(request, 'login.html', {'error': 'Your Username or Password is Incorrect.'})
    else :
        return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("index")

def board(request):
    page = request.GET.get('page', 1)
    datas = Board.objects.all().order_by('-id')
    paginator = Paginator(datas, 5)
    pagedatas = paginator.get_page(page)
    context ={"articles": pagedatas}
    return render(request, 'board.html', context)

def board_create(request):
    if request.method == "POST":
        author = request.user
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        text = request.POST['text']
        data = Board(author=author,subtitle=subtitle, title=title,text=text)
        if title=="" or text=="":
            msg = "You need to fill in first."
            context = {'msg': msg}
            return render(request, "new_article.html", context)
        else:
            data.save()
            return redirect("board")
    else:
        return render(request, 'new_article.html')

def board_delete(request):
    pk = request.GET['pk']
    data = Board.objects.get(pk=pk)
    data.delete()
    return redirect("board")

def board_edit(request, pk):
    if request.method == "POST" :
        data = Board.objects.get(pk=pk)
        data.title = request.POST['title']
        data.subtitle = request.POST['subtitle']
        data.text = request.POST['text']
        data.edited_or_not = "(Edited)"
        if data.title=="" or data.text=="":
            msg = "Either Title or Content is Empty."
            context = {'msg': msg}
            return render(request, "edit_article.html", context)
        else:
            data.save()
            return redirect("board")
    else:
        data = Board.objects.get(pk=pk)
        context = {'data': data}
        return render(request, "edit_article.html", context)
