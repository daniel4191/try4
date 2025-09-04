from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignForm
from .models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    
    # 만약 request 메서드가 post라면(templates의 html에서)
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        
        # 바로 위에서 온 POST가 유효한 값이라면
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            # 중복되는 유저가 없는지 한번 더 검사
            user = authenticate(username = username, password = password)
            
            # 만약 해당 사용자가 존재한다면
            if user:
                # 로그인 처리 후 피드페이지로 리다이렉트
                login(request, user)
                return redirect("posts:feeds")
            # 사용자가 없다면 실패 출력
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")
                
        # 데이터 검증 후에 다시 loginform 사용하도록 로그인 페이지 렌더링
        context = {"form": form}
        return render(request, "arm/login.html", context)
    
    form = LoginForm()
    context = {"form":form}
    return render(request, "arm/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect("users:login")

def signup(request):
    if request.method == "POST":
        form = SignForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("posts:feeds")
    else:    
        form = SignForm()
        context = {"form": form}
        return render(request, "arm/signup.html", context)