from django.shortcuts import render
from .serializer import UserSerializer,VehicleSerializer,BookingSerializer
from .models import User,Vehicle,Booking
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
# Create your views here.

# User endpoint 

class UserSigninView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username:
            return Response({"Error":"Username is not provided."},status=status.HTTP_400_BAD_REQUEST) 
        
        if not password:
            return Response({"Error":"Password is not provided."},status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username,password=password)
        if user is not None:
            token,created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=status.HTTP_200_OK)
        return Response({"Error":"Internal Server Error"})

        
            

# Vehicle endpoints
class ListVehicleView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        brand = request.query_params.get('brand')
        fuel_type = request.query_params.get('fuel_type')
        is_available = request.query_params.get('is_available')

        vehicles = Vehicle.objects.all()

        if brand:
            vehicles = vehicles.filter(brand__iexact=brand)
        
        if fuel_type:
            vehicles = vehicles.filter(fuel_type__iexact=fuel_type)
        
        if is_available is not None:
            is_available = is_available.lower() == 'true'
            vehicles = vehicles.filter(is_available=is_available)

        serializer = VehicleSerializer(instance = vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

class AddVehicleView(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        data = request.data 
        serializer = VehicleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,id):
        vehicle = get_object_or_404(Vehicle, id=id)
        serializer = VehicleSerializer(instance = vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateVehicleView(APIView):
    permission_classes = [IsAdminUser]
    def put(self,request,id):
        vehicle = get_object_or_404(Vehicle,id=id)
        serializer = VehicleSerializer(instance=vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteVehicleView(APIView):
    permission_classes = [IsAdminUser]
    def delete(self,request,id):
        vehicle_to_be_deleted = get_object_or_404(Vehicle,id=id)
        vehicle_to_be_deleted.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    


# Booking endpoints 

class ListBookingView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        bookings = Booking.objects.filter(customer_name = request.user)
        serializer = BookingSerializer(instance = bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateBookingView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data 
        serializer = BookingSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        booking = get_object_or_404(Booking, id=id, customer_name = request.user)
        serializer = BookingSerializer(instance=booking) 
        return Response(serializer.data, status=status.HTTP_200_OK)

