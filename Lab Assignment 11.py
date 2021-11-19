import time
class Clock: 
    
    def __init__(self,hours,minutes,seconds,clock_type=0): 
        self.hours = hours 
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type

    def change(self): 
        self.seconds += 1 
        while(True):
            if self.seconds >= 60:
                self.seconds = 0  
                self.minutes += 1 
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1
            if self.hours >= 24:
                self.hours = 0
            break

    def __str__(self): 
        if self.clock_type == 0:
            return '{:02}:{:02}:{:02}'.format(self.hours,self.minutes,self.seconds)                                                                                          
        else:
            tz = "am" 
            while(True):
                if self.hours>=12: 
                    tz = "pm"  
                hours_1 = self.hours
                if self.hours==0: 
                    hours_1 = 12
                elif self.hours>12: 
                    hours_1 = self.hours-12 
                break

            return '{:02}:{:02}:{:02} {}'.format(hours_1,self.minutes,self.seconds,tz)

if __name__ == "__main__": 
    hours=int(input("What is the current hour ==> ")) 
    minutes=int(input("What is the current minute ==> ")) 
    seconds=int(input("What is the current second ==> ")) 
    changing=Clock(hours,minutes,seconds,1) 
    while (True):
        print(changing) 
        changing.change() 
        time.sleep(1)
