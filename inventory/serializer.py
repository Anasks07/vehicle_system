from rest_framework import serializers
from .models import User,Vehicle,Booking 
from rest_framework.validators import ValidationError
from datetime import date

# User serializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User 
        fields = ['id','username','password']
    
    def validate_username(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("Username must be 4 characters long.")
        return value
    
    def validate_password(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("Password must be strong.") 
        return value
    
    def create(self,validated_data):
        user =  User.objects.create_user(**validated_data)
        return user


# Vehicle serializer

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle 
        fields = '__all__'


# Booking serializer 

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
    
    def validate(self,value):
        vehicle = value['vehicle']
        start_date = value['start_date']
        end_date = value['end_date']

        overlapping = vehicle.bookings.filter(start_date__lte=end_date, end_date__gte=start_date).exists()

        if overlapping:
            raise serializers.ValidationError("Vehicle is already booked for these dates.")


        if start_date < date.today():
            raise serializers.ValidationError("Start date cannot be in past.")
        
        if end_date <= start_date:
            raise serializers.ValidationError("End date must be after start date")
        
        return value
    
    def validate_customer_phone(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone must contain only digits.")
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits.")
        return value 

    def create(self,validated_data):
        vehicle = validated_data['vehicle']
        start_date = validated_data['start_date']
        end_date = validated_data['end_date']

        days = (end_date - start_date).days + 1 
        total_amount =  days* vehicle.price_per_day

        booking = Booking.objects.create(**validated_data, total_amount=total_amount)
        vehicle.is_available = False 
        vehicle.save()
        return booking
