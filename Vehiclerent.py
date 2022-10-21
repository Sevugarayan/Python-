#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:00:19 2022

@author: sevugarayan
"""
import datetime
#Parent class

class VehicleRent:
    
    def __init__(self,stock):
        self.stock = stock
        self.now = 0
        
        
    def displayStock(self):
        print("{} Vehicle available for rent".format(self.stock) )
        return self.stock
    
    
    def rentHourly(self,n):
        """ 
        Rent Hourly
        """
        if n <= 0:
            print("Invalid Input")
            return None
            
        elif n > self.stock:
            print("Sorry, only {} left".format(self.stock))
            return None
            
        else:
            self.now = datetime.datetime.now()
            print("Rented {} Vehicle for hourly at {} hours".format(n,self.now.hour))
            self.stock -= n
            return self.now
        
        
    def rentDaily(self,n):
        
        if n <= 0:
            print("Invalid Input")
            return None
            
        elif n > self.stock:
            print("Sorry, only {} left".format(self.stock))
            return None
            
        else:
            self.now = datetime.datetime.now()
            print("Rented {} Vehicle for daily at {} hours".format(n,self.now.hour))
            self.stock -= n
            return self.now
    
    def returnVehicle(self,request,brand):
        """
        Return a Bill
        """
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        
        rentalTime, rentalBasis, numofVeh = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numofVeh:
                self.stock += numofVeh
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numofVeh
                
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numofVeh
                    
                if (2 <= numofVeh):
                    print("you have 20% discount")
                    bill = bill*0.8
                    
                print("Thank you for returning your car")
                print("Price = $ {}".format(bill))
                return bill
        
        
        elif brand == "bike":
            if rentalTime and rentalBasis and numofVeh:
                self.stock += numofVeh
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds/3600*bike_h_price*numofVeh
                
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numofVeh
                    
                if (4 <= numofVeh):
                    print("you have 20% discount")
                    bill = bill*0.8
                    
                print("Thank you for returning your car")
                print("Price = $ {}".format(bill))
                return bill
                    
        else:
            print ("you do not rent a vehicle")
            return None
                
                
        
#child class
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self,stock):
        super().__init__(stock)
    
    def Discount(self,b):
        bill = b - (b*discount_rate)/100
        return bill 
    
#Child Class
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)
    
#Customer Class
class Customer:
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        
        self.car = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    
    def requestVehicle(self, brand):
        
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")
            
            try:
                bikes = int(bikes)
            
            except ValueError:
                print("Input should be a number")
                return -1
        
            if bikes < 1:
                print("number of bikes should be greater than 0")
                return -1
            else:
                self.bikes = bikes
                return self.bikes
        
        elif brand == "car":
            car = input("How many cars would you like to rent?")
            
            try:
                car = int(car)
            
            except ValueError:
                print("Input should be a number")
                return -1
        
            if car < 1:
                print("number of cars should be greater than 0")
                return -1
            else:
                self.car = car
                return self.car
            
        else:
            print("Request Vehicle Error")
            
        
    def returnVehicle(self, brand):
        
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
            
        
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.car:
                return self.rentalTime_c, self.rentalBasis_c, self.car
            else:
                return 0,0,0
        else:
            print("Return Vehicle Error")
        