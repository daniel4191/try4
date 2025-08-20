from django.shortcuts import render

# Create your views here.
def feeds(request):
    user = request.user
    
    is_authenticated = user.is_authenticated
    
    print("user:", user) # user는 현재 로그인 중인 계정
    print("is_authenticated:", is_authenticated) # 위에서 설정된 is_authenticated로 인해서 해당 user가 정상접근인지 확인,
    # 만약 로그인 되어있지 않으면 False가 나온다.
    
    return render(request, "posts/feeds.html")

