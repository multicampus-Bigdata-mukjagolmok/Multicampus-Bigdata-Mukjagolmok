from django.shortcuts import render, redirect
from mukja.models import Golmok, Restaurant, Menu, Comment
from .forms import CommentForm
from django.views.generic import UpdateView


# Create your views here.

def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def golmok(request, pk):
    golmok_pk = pk
    mukjagolmok = Golmok.objects.get(id=pk)
    restaurants = Restaurant.objects.filter(golmok_id=golmok_pk)
    context = {
        'mukjagolmok': mukjagolmok,
        'restaurants': restaurants,
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

