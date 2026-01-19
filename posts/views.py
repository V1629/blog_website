from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view,APIView, permission_classes
from rest_framework import mixins
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import  get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import ReadOnly,AuthorOrReadOnly


###a MOCK POSTS DATABSE
# posts = [
#     {
#         "id" : 1,
#         "title" : "Why it is difficult to learn programming",
#         "content" : "THis is to give reason why it is hard"
#     },
#     {
#         "id" : 2,
#         "title" : "Learn Javascript",
#         "content" : "This is a course on JS"
#     },
#     {
#         "id" : 3,
#         "title":"Why it is difficult to learn programming?",
#         "content" : "this is to give reason why it is hard"
#     }
# ]

###Homepage
@api_view(http_method_names =["GET","POST"])
@permission_classes([AllowAny])
def homepage(request :Request):

    if request.method == "POST":
        data = request.data
        response = {"message":"Hello world","data":data}
        return Response(data = response,status = status.HTTP_201_CREATED)
    repsonse = {"message":"Hello world"}
    return Response(data=repsonse,status = status.HTTP_200_OK)


###A class based view for creating and listing the posts
class PostListCreateView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    def get(self,request:Request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request:Request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # def get(self,request:Request,*args,**kwargs):
    #     posts = Post.objects.all()

    #     serializer = PostSerializer(instance=posts,many=True)
    #     return Response(data=serializer.data,status=status.HTTP_200_OK)
    # def post(self,request:Request,*args,**kwargs):
    #     data= request.data


    #     serializer = self.serializer_class(data=data)


    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {
    #             "message" : "Post created successfully",
    #             "data" : serializer.data
    #         }

    #         return Response(data=response,status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
        


class PostRetrieveUpdateDeleteView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]
    

    def get(self,request:Request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request:Request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request:Request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)

    
# @api_view(http_method_names=["GET","POST"])
# def list_posts(request : Request):
#     posts = Post.objects.all()

#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()

#             response = {
#                 "message" : "Post created",
#                 "data" : serializer.data
#             }
#             return Response(data=response,status=status.HTTP_201_CREATED)
        
#         return Response(data = serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    # serializer = PostSerializer(instance = posts, many=True)
    # response = {
    #     "message":"posts",
    #     "data" : serializer.data
    # }

    # return Response(data=response,status=status.HTTP_200_OK)


##View for returning the post by its id through serializer
# @api_view(http_method_names=["GET"])
# def post_detail(request:Request,post_id:int):
#     post = get_object_or_404(Post,pk = post_id)

#     serializer = PostSerializer(instance = post)

#     response = {
#         "message" : "post",
#         "data" : serializer.data
#     }

    
#     return Response(data=response,status=status.HTTP_200_OK)


# ###UPDATING THE POSTS
# @api_view(http_method_names=["PUT"])
# def update_post(request:Request,post_id: int):
#     post = get_object_or_404(Post,pk = post_id)

#     data = request.data

#     serializer = PostSerializer(instance=post,data=data)

#     if serializer.is_valid():
#         serializer.save()

#         response = {
#             "message" : "Post updates successfully",
#             "data" : serializer.data
#         }
#         return Response(data=response,status=status.HTTP_200_OK)
#     return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

# ###Deleting the posts
# @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request,post_id: int):
#     post = get_object_or_404(Post,pk = post_id)

#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)
    