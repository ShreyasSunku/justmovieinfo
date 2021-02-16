from django.shortcuts import render, HttpResponse,redirect
from .models import Movies, LoginForm, Purchase
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    telugu_movies = Movies.objects.filter(language='Telugu')[:10]
    hindi_movies = Movies.objects.filter(language='Hindi')[:10]
    tamil_movies = Movies.objects.filter(language='Tamil')[:10]
    kannada_movies = Movies.objects.filter(language='Kannada')[:10]
    malayalam_movies = Movies.objects.filter(language='Malayalam')[:10]
    print('hindi_movies = ', hindi_movies)
    print('telugu_movies = ', telugu_movies)
    print('tamil_movies = ', tamil_movies)
    print('kannada_movies = ', kannada_movies)
    print('malayalam_movies = ', malayalam_movies)

    return render(request, 'home.html', {'telugu_movies': telugu_movies,
                                         'hindi_movies': hindi_movies,
                                         'tamil_movies': tamil_movies,
                                         'malayalam_movies': malayalam_movies,
                                         'kannada_movies': kannada_movies})


def display_category(request, language):
    print('Hello')
    movies_list = Movies.objects.filter(language=language)
    page = request.GET.get('page', 1)

    paginator = Paginator(movies_list, 12)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render(request, 'genres.html', {'movies': movies})


def disply_movie_info(request, mid):
    # check login or not
    # if request.session['id']
    movie = Movies.objects.get(movie_id=mid)
    if request.session.get('id'):
        try:
            user = Purchase.objects.get(user=request.session.get('id'))
            if user:
                print('user id = ', request.session.get('id'))

                return render(request, 'single.html', {'movie': movie})
            else:
                return render(request, 'paymentgateway.html', {'movie': movie})
        except:
            return render(request, 'paymentgateway.html', {'movie': movie})
    else:
        return HttpResponse('Please Login')



def login_form(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        Email = request.POST['Email']
        Phone = request.POST['Phone']

        LoginForm(user=Username,
                  password=Password,
                  mail=Email,
                  phone=Phone).save()
        return redirect('home_page')


def login(request):
    if request.method == 'POST':
        try:
            user = LoginForm.objects.get(mail=request.POST['email'], password=request.POST['password'])
            print('user= ', user)
            request.session['username'] = user.user
            request.session['email'] = user.mail
            request.session['id'] = user.id
            return redirect('home_page')
        except LoginForm.DoesNotExist as e:
            return HttpResponse('Please enter valid credentials')

    return redirect('home_page')


def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('home_page')
    return redirect('home_page')


def paid(request):
    if request.method == 'POST':
        userid = request.session.get('id')
        Purchase(purcased=1, user=userid).save()
        return render(request, 'success.html')


def handler404(request, *args, **argv):

    # response = render_to_response("404.html")
    # response.status_code = 404
    return redirect('errors')