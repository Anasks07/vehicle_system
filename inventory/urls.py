from django.urls import path
from .views import * 

urlpatterns = [
    path('api/vehicles/',ListVehicleView.as_view()),
    path('api/vehicles/createvehicle/',AddVehicleView.as_view()),
    path('api/vehicles/vehicledetail/<id>/',VehicleDetailView.as_view()),
    path('api/vehicles/updatevehicle/<id>/',UpdateVehicleView.as_view()),
    path('api/vehicles/deletevehicle/<id>/',DeleteVehicleView.as_view()),

    path('api/bookings/',ListBookingView.as_view()),
    path('api/bookings/createbooking/',CreateBookingView.as_view()),
    path('api/bookings/<id>/',BookingDetailsView.as_view()),

    path('api/usersignin/',UserSigninView.as_view()),
    path('api/userlogin/',UserLoginView.as_view())
]