from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon!")


def main(request):
    path = request.path
    return HttpResponse(path, content_type="text/html", charset="utf-8")


def header(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META["REMOTE_ADDR"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path_info = request.path_info

    response = HttpResponse()
    response.headers["Age"] = 20
    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Sceme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br> Response header: {response.headers}
        """
    return HttpResponse(msg, content_type="text/html", charset="utf-8")


def index(request):
    path = request.path
    method = request.method
    content = """
    <center>
        <h2>Testing Django Request Response Objects</h2>
        <p>Request path : " {}</p>
        <p>Request Method : {}</p>
    </center>
    """.format(
        path, method
    )
    return HttpResponse(content)


def pathview(request, name, id):
    return HttpResponse("Name:{} UserID:{}".format(name, id))


def qryview(request):
    name = request.GET["name"]
    id = request.GET["id"]
    return HttpResponse("Name:{} UserID: {}".format(name, id))


def showform(request):
    return render(request, "form.html")


def getform(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
    return HttpResponse("Name: {} UserID: {}".format(name, id))


def menuitems(request, dish):
    items = {
        "pasta": "an italian dish",
        "falafel": "an israeli dish",
        "cheesecake": "a french dessert",
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)


# source venv/Scripts/activate
# python manage.py runserver
