class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price is: $ " + str(self.price)
        print "Max Speed: " + str(self.max_speed) + " mph"
        print "Total Miles " + str(self.miles) + " miles"
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self


bike1 = Bike(199.99, 12)
bike1.ride().ride().ride().reverse().displayinfo();

# bike1 = Bike(199.99, 12)
# bike1.ride()
# bike1.ride()
# bike1.ride()
# bike1.reverse()
# bike1.displayinfo()

bike2 = Bike(299.99, 15)
bike2.ride().ride().reverse().reverse().displayinfo();

# bike2 = Bike(299.99, 15)
# bike2.ride()
# bike2.ride()
# bike2.reverse()
# bike2.reverse()
# bike2.displayinfo()

bike3 = Bike(399.99, 20)
bike3.reverse().reverse().reverse().displayinfo();

# bike3 = Bike(399.99, 20)
# bike3.reverse()
# bike3.reverse()
# bike3.reverse()
# bike3.displayinfo()
