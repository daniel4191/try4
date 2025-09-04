from django.shortcuts import render, redirect

def index(request):
    
    # 로그인 되어있는 경우 피드 페이지로
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    # 로그인 되어있지 않은 경우, 로그인 페이지로
    else:
        return redirect("users:login")
    # return render(request, "index.html")