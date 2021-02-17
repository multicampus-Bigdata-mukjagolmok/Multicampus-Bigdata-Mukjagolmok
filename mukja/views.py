from django.shortcuts import render, redirect
from mukja.models import Golmok, Restaurant, Menu, Comment
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
        useremail = request.POST.get('useremail')
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password',None)
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username = useremail,
                            first_name = firstname,
                            last_name = lastname,
                            password = password)
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect('/mukja/')
    return render(request, 'register.html', res_data)


def login(request):
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect("index")
        else :
            return render(request, 'login.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else :
        return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("index")
