from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import QuestionForm, AnswerForm
from main.forms import HashtagForm 
from django.utils import timezone
from QnA.models import Question, Answer 
from main.models import Hashtag
from django.http import request
from django.core.paginator import Paginator
# Create your views here.

#질문 작성
@login_required
def q_write(request, qna = None  , hashtag = None):
        if not request.user.is_authenticated:
            return redirect('main')
        if request.method == 'POST':
            form = QuestionForm(request.POST, request.FILES,instance = qna)
            if form.is_valid():
                    qna = form.save(commit=False)
                    qna.q_date = timezone.now()
                    qna.user = request.user
                    qna.save()
                    form.save_m2m()
                    return redirect('q_list')
        else:
            form = QuestionForm (instance= qna)
            return render(request, 'q_write.html' , {'form':form})

#질문 목록
def q_list(request):
    qnaobj = Question.objects
    q_sort = request.GET.get('q_sort','') #정렬
    if q_sort == 'q_clicks' :
        qnaobj = Question.objects.all().order_by('-q_clicks')#모델 오브젝트 templates에서 받고 싶은 요소만 추가
    else :
        qnaobj = Question.objects.all().order_by('-q_date')
    
    #페이지
    paginator = Paginator(qnaobj, 2)
    page = request.GET.get('page')
    qnaobj = paginator.get_page(page)
    return render(request, 'q_list.html' , {'qnaobj':qnaobj, 'q_sort':q_sort})

#질문글 상세페이지
@login_required
def q_detail(request, id):

    if not request.user.is_authenticated:
        return redirect('q_list')

    qna = get_object_or_404(Question, id=id)
   
    if request.method == "POST" :
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid() :
            answer = form.save(commit = False)
            answer.qna_id = qna
            answer.text = form.cleaned_data['text']
            answer.user = request.user
            answer.save()
            form.save_m2m()
            return redirect('q_detail' , id)
    else :
        form = AnswerForm()
        return render(request, 'q_detail.html' , {'qna' : qna , 'form':form})

#질문 수정하기
def q_edit(request , id):
        qna = get_object_or_404(Question, id=id)
        if request.method == "POST":
            form = QuestionForm(request.POST, request.FILES, instance=qna)
            if form.is_valid():
                    form.save(commit=False)
                    form.save()
                    return redirect('q_list')
        else:
            form = QuestionForm(instance=qna)
            return render(request, 'q_edit.html' , {'form':form})

#질문 삭제
def q_delete(request, id):
    qna = get_object_or_404(Question, id=id)           
    qna.delete()
    return redirect('q_list')

#좋아요 
def q_likes(request, id):
    like_q = get_object_or_404(Question, id=id)
    if request.user in like_q.q_like.all(): 
        like_q.q_like.remove(request.user)
        like_q.q_like_count -= 1
        like_q.save()
    else:
        like_q.q_like.add(request.user)
        like_q.q_like_count += 1
        like_q.save()
    return redirect('q_detail' , like_q.id) #redurect로 전달 하기 때문에 조회수 올라감..

#추천수 
# def q_clip(request, id):
#     like_b = get_object_or_404(Question, id=id)
#     if request.q_user in like_b.q_clip.all(): #q_user
#         like_b.q_clip.remove(request.q_user)
#         like_b.q_clips -= 1
#         like_b.save()
#     else:
#         like_b.q_clip.add(request.q_user)
#         like_b.q_clips += 1
#         like_b.save()
#     return redirect('/q_detail/' + str(id))

#검색하기
def q_search(request):
        if request.method == 'POST':
                q_searched = request.POST['q_searched']        
                q_serobj = Question.objects.filter(question__contains=q_searched)
                return render(request, 'q_search.html', {'q_searched': q_searched,'q_serobj':q_serobj})
        else:
                return render(request, 'q_search.html', {})
