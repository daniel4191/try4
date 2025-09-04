from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden

from .models import Post, Comment, PostImage
from .forms import CommentForm, PostForm

# Create your views here.
def feeds(request):
    user = request.user
    is_authenticated = user.is_authenticated
    
    if not user.is_authenticated:
        return redirect("/users/login2/")
    
    print("user:", user) # user는 현재 로그인 중인 계정
    print("is_authenticated:", is_authenticated) # 위에서 설정된 is_authenticated로 인해서 해당 user가 정상접근인지 확인,
    # 만약 로그인 되어있지 않으면 False가 나온다.
    
    # 모든 글 목록을 템플릿으로 전달
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts":posts,
        "comment_form": comment_form
        }
    return render(request, "posts/feeds.html", context)

@require_POST
@login_required(login_url="/users/login/")
def comment_add(request):
    #Commment 인스턴스 생성
    form = CommentForm(data = request.POST)
    if form.is_valid():
        # 메모리 상에 Comment 객체 생성
        comment = form.save(commit = False)
        
        #Comment 생성에 필요한 사용자 정보를 request에서 가져와 할당
        # 사용유저 자동입력기능
        comment.user = request.user

        # DB에 Comment 객체 저장
        comment.save()
        
        # 생성된 Comment 정보 확인
        print(comment.id)
        print(comment.content)
        print(comment.user)
        
        return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
    
@require_POST
def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id = comment_id)
        if comment.user == request.user:
            comment.delete()
            return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
        else:
            return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")
        
def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            for image_file in request.FILES.getlist("images"):
                # request.FILES로 가져온 파일은 models의 ImageField 부분에 바로 할당됨
                PostImage.objects.create(
                    post = post,
                    photo = image_file
                )
            # 모든 PostImage와 Post 생성이 완료되면
            # 피드 페이지로 이동하여 생성된 Post의 위치로 스크롤
            url = f"/posts/feeds/#post-{post.id}"
            return HttpResponseRedirect(url)
    # GET 요청일때는 빈 form을 보여준다.
    else:
        form = PostForm()
    context = {"form":form}
    return render(request, "posts/post_add.html", context)
    
    