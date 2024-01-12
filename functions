#save user inf
h=float(input('type working hours:'))
r=float(input('type rate:'))
#define function computepay whit parameters a,b
def computepay(a,b):
    #op with hours+1.5rate after 40 working hours 
    if a>40:
        extra=b*1.5
        hextra=a-40
        pay=(a-hextra)*b+(hextra*extra)
    #normal op with 40 working hours or less    
    else:
        pay=a*b
    return pay
#invoke and print the function computepay with arguments h,r
print('Pay',computepay(h,r))
