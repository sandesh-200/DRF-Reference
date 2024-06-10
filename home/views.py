from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer,BookSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({"status":200, "payload":serializer.data})

class RegisterUser(APIView):
    def post(self,request):
        serializer= UserSerializer(data=request.data)



class StudentAPI(APIView):
    def get(Self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs,many=True)
        return Response({"status":200,"payload":serializer.data})

    def post(self,request):
        serializer  = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"payload":serializer.data,"message":"You have successfully sent data"})
        else:
            return Response({"status":403,"error":serializer.error,"message":"Not sent"})


    def put(self,request):
        pass

    def patch(self,request):
        try: 
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data,partial=True)
            if not serializer.is_valid():
                print("Validation errors:", serializer.errors)
                return Response({"error":serializer.errors,"message":"Something Went Wrong"})
        
            serializer.save()
            return Response({"payload":serializer.data,"message":"You have successfully UPDATED data"})
    
    
        except Exception as e:
            return Response({"status":403,"message":"An unexpected error occurred:"+ str(e)})
    

    def delete(self,request):
        pass


































# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)
#     return Response({"status":200, "about student":serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"payload":serializer.data,"message":"You have successfully sent"})
#     return Response({"error":serializer.errors,"message":"Something Went Wrong"})

# @api_view(['PUT'])
# def update_Student(request, id):
#     try: 
#         student_obj = Student.objects.get(id=id)
#         print(student_obj)

#         serializer = StudentSerializer(student_obj, data=request.data,partial=True)
#         if not serializer.is_valid():
#             print("Validation errors:", serializer.errors)
#             return Response({"error":serializer.errors,"message":"Something Went Wrong"})
        
#         serializer.save()
#         return Response({"payload":serializer.data,"message":"You have successfully sent"})
    
    
#     except Exception as e:
#         return Response({"status":403,"message":"An unexpected error occurred:"+ str(e)})
    
# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#          student_obj = Student.objects.get(id=id)
#          student_obj.delete()
#          return Response({"msg":"deleted"})
#     except Exception as e:
#         print(e)
#         return Response({"message":"an error occured"+str(e)})
    
