from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post



@api_view(["GET", 'POST'])
def posts(request):
    
    if request.method == "GET":
        all_post = Post.objects.all()
                
        serializer = PostSerializer(all_post, many=True)
        
        data = {
            "message":"success",
            "data":serializer.data
        }
                
        return Response(data=data, status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            data = {
            "message":"success",
            "data":serializer.data
            }
                    
            return Response(data=data, status=status.HTTP_201_CREATED)
        
        else:
            errors = {
                "message":"failed",
                "error" : serializer.errors
            }
            
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)
        



@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        data = {
            "message":f"post with id {post_id} does not exist."
        }
                
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer = PostSerializer(post)
        
        data = {
            "message":"success",
            "data":serializer.data
        }
                
        return Response(data=data, status=status.HTTP_200_OK)
    
    elif request.method=="PUT":
        serializer = PostSerializer(post,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            data = {
            "message":"success",
            "data":serializer.data
            }
                    
            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        
        else:
            errors = {
                "message":"failed",
                "error" : serializer.errors
            }
            
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        post.delete()
        
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        
        