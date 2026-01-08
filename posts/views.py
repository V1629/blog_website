from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


###a MOCK POSTS DATABSE
posts = [
    {
        "id" : 1,
        "title" : "Why it is difficult to learn programming",
        "content" : "THis is to give reason why it is hard"
    },
    {
        "id" : 2,
        "title" : "Learn Javascript",
        "content" : "This is a course on JS"
    },
    {
        "id" : 3,
        "title":"Why it is difficult to learn programming?",
        "content" : "this is to give reason why it is hard"
    }
]


@api_view(http_method_names =["GET","POST"])
def homepage(request :Request):

    if request.method == "POST":
        data = request.data
        response = {"message":"Hello world","data":data}
        return Response(data = response,status = status.HTTP_201_CREATED)
    repsonse = {"message":"Hello world"}
    return Response(data=repsonse,status = status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def list_posts(request : Request):
    return Response(data=posts,status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def post_detail(request:Request,post_index:int):
    post = posts[post_index]

    if post:
        return Response(data=post,status=status.HTTP_200_OK)
    return Response(data={"error":"Posts not found"},status=status.HTTP_204_NO_CONTENT)