# -*- coding: UTF-8 -*-
import wiringpi as gpio

#gpio.wiringPiSetup() #wiringPi 
#gpio.wiringPiSetupGpio() #BCM
#gpio.wiringPiSetupSys() #board

class GPIO:
    pin:int
    pinmode = None
    INPUT = LOW = PUD_OFF = PWM_MODE_MS = 0
    OUTPUT = HIGH = PUD_DOWN = PWM_MODE_BAL = 1
    PWM_OUTPUT = PUD_UP =  2
    _dict_ = {
        'INPUT':INPUT,'OUTPUT':OUTPUT,'PWM_OUTPUT':PWM_OUTPUT,
        'LOW':LOW,'HIGH':HIGH,
        'PUD_OFF':PUD_OFF,'PUD_DOWN':PUD_DOWN,'PUD_UP':PUD_UP,
        'PWM_MODE_BAL':PWM_MODE_BAL,'PWM_MODE_MS':PWM_MODE_MS,
    }
    
    
    def __init__(self,pin:int,pinmode:str,pwmRangeValue = 1024):
        gpio.wiringPiSetupGpio() 
        self.pin = pin
        if pinmode in _dict_:
            self.pinmode = _dict_[pinmode]
        else:
            self.pinmode = _dict_['OUTPUT']
        gpio.pwmSetRange(pwmRangeValue)
        gpio.pinMode(self.pin,self.pinmode)

    def input(self):
        if self.pinmode == INPUT:
            gpio.input(self.pin)
            return True
        return False

    def open(self): #打开端口
        try:
            if self.pinmode == OUTPUT:
                gpio.digitalWrite(self.pin,self.HIGH)
                return True
            return False
        except Exception as e :
            print(str(e))
        return False
        
    def close(self): #关闭端口
        try:
            if self.pinmode == OUTPUT:
                gpio.digitalWrite(self.pin,self.LOW)
                return True
            return False
        except Exception as e :
            print(str(e))
        return False

    def setPwm(self,pwmValue:int):
        try:
            if self.pinmode == PWM_OUTPUT:
                if pwmValue >= 0 and pwmValue <= 1024 :
                    gpio.pwmWrite(self.pin,pwmValue)
                    return True
        except Exception as e :
            print(str(e))
        return False

    def setPwmMode(self,pwmMode:str):
        if pwmMode in _dict_:
            gpio.pwmWrite(self.pin,pwmMode)
            return True
        return False

    def setPwmRange(self,pwmRangeValue:int):
        if pwmRangeValue >= 0 and pwmRangeValue <= 1024 :
            gpio.pwmSetRange(pwmRangeValue)
            return True
        return False

    def setPwmClock(self,divisor:int):
        gpio.pwmSetClock(divisor)
        return True

    def delay(self,howLong:int): # 1ms = 1/1000s
        gpio.delay(thowLongime)
        return True

    def delayMicroSeconds(self,howLong:int): # 1μs = 1/1000ms
        gpio.delayMicroseconds(howLong)
        return True

    def pullUpDnControl(self,pud:str):
        try:
            if self.pinmode == INPUT:
                if pud in _dict_:
                    gpio.pullUpDnControl(self.pin,_dict_[pud])
                    return True
        except Exception as e :
            print(str(e))
        return False

    @property
    def value(self):
        try:
            return gpio.digitalRead(self.pin)
        except Exception as e :
            print(str(e))
        return False
    #Interrupts todo


class Serial:
    pin:int
    def __init__(self, device='/dev/ttyAMA0', baudrate=9600):
        if not device.startswith('/dev/'):
            device = '/dev/%s' % device
        
        if isinstance(baudrate, str):
            baudrate = int(baudrate)

        aname = 'B%d' % baudrate
        if not hasattr(termios, aname):
            raise Exception('Unsupported baudrate')
        self.baudrate = baudrate

        Bus.__init__(self, 'UART', device, os.O_RDWR | os.O_NOCTTY)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, os.O_NDELAY)
        
        #backup  = termios.tcgetattr(self.fd)
        options = termios.tcgetattr(self.fd)
        # iflag
        options[0] = 0

        # oflag
        options[1] = 0

        # cflag
        options[2] |= (termios.CLOCAL | termios.CREAD)
        options[2] &= ~termios.PARENB
        options[2] &= ~termios.CSTOPB
        options[2] &= ~termios.CSIZE
        options[2] |= termios.CS8

        # lflag
        options[3] = 0

        speed = getattr(termios, aname)
        # input speed
        options[4] = speed
        # output speed
        options[5] = speed
        
        termios.tcsetattr(self.fd, termios.TCSADRAIN, options)