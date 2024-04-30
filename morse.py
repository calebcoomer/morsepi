from gpiozero import Buzzer, LED
from time import sleep

## buzzer is currently in gen gpio22 (physical board 15)
## green LED currently in gen gpio23 (physical board 16)
buzzer = Buzzer(22)
led = LED(23)

## these list values are called for the buzzer.beep() function
## time unit is 1/16 of a second
## dot = 1 unit; dash = 3 units; space between = 1 unit
## between letters = 3 units; between words = 7 units
dot = [.0625,.0625,1,False] ## 1/16 on, 1/16 off .
dash = [.1875,.0625,1,False]## 3/16 on, 1/16 off _
lspace = [0,.125,1,False]   ## 0/16 on, 2/16 off '' UNUSED
wspace = [0, .25, 1,False] ## 0/16 on, 4/16 off '  'UNUSED

## letter library
charset = {
'a' : [dot, dash],
'b' : [dash, dot, dot, dot],
'c' : [dash, dot, dash, dot],
'd' : [dash, dot, dot],
'e' : [dot],
'f' : [dot, dot, dash, dot],
'g' : [dash, dash, dot],
'h' : [dot, dot, dot, dot],
'i' : [dot, dot],
'j' : [dot, dash, dash, dash],
'k' : [dash, dot, dash],
'l' : [dot, dash, dot, dot],
'm' : [dash, dash],
'n' : [dash, dot],
'o' : [dash, dash, dash],
'p' : [dot, dash, dash, dot],
'q' : [dash, dash, dot, dash],
'r' : [dot, dash, dot],
's' : [dot, dot, dot],
't' : [dash],
'u' : [dot, dot, dash],
'v' : [dot, dot, dot, dash],
'w' : [dot, dash, dash],
'x' : [dash, dot, dot, dash],
'y' : [dash, dot, dash, dash],
'z' : [dash, dash, dot, dot],
'1' : [dot, dash, dash, dash],
'2' : [dot, dot, dash, dash, dash],
'3' : [dot, dot, dot, dash, dash],
'4' : [dot, dot, dot, dot, dash],
'5' : [dot, dot, dot, dot, dot],
'6' : [dash, dot, dot, dot, dot],
'7' : [dash, dash, dot, dot, dot],
'8' : [dash, dash, dash, dot, dot],
'9' : [dash, dash, dash, dash, dot],
'0' : [dash, dash, dash, dash, dash],
' ' : [wspace]}

def main():
    while True:
## ask for input
        message = input("Enter your message. Numbers, letters, and spaces only.\n").lower()
## check for alphanumeric input by checking message with spaces removed
        precheck = message.replace(' ','')
        if (precheck.isalnum()) == True:
## if space, wait
            for letter in message:
                if letter == ' ':
                    print('space')
                    sleep(.25)
## else, play dots and dashes
                else:
                    print(letter)
                    for unit in charset[letter]:
                        led.on()
                        buzzer.beep(*unit)
                        led.off()
                sleep(.125)
## if alphanumeric check fails, inform user and alert
        else:
            print('Alphanumeric messages only')
            led.on()
            buzzer.beep(.5,.5,2,False)
            led.off()

main()
