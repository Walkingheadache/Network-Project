# This program Identifies the class of the Ip address that is passed to the function:
A_mask = "255.0.0.0"
A_slash = "8"
B_mask = "255.255.0.0"
C_mask = "255.255.255.0"

def Identify_c(ip):

    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return f"The Ip Address is A class, Mask:  {A_mask}/{A_slash}"
    elif 128 <= first_octet <= 191:
        return f"The Ip Address is B class, Mask: {B_mask}"
    elif 192 <= first_octet <= 223:
        return f"The Ip Address is C class, Mask: {C_mask}"
    else:
        return 0
    
