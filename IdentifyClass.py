# This program Identifies the class of the Ip address that is passed to the function:
A_mask = "255.0.0.0"
A_slash = "8"
B_mask = "255.255.0.0"
B_slash = "16"
C_mask = "255.255.255.0"
C_slash = "24"

def Identify_c(ip = None): #this function takes in ip address and determiens the class,mask and slash.

    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return A_mask,"/", A_slash
    elif 128 <= first_octet <= 191:
        return B_mask,"/", B_slash
    elif 192 <= first_octet <= 223:
        return C_mask,"/", C_slash
    else:
        return 0
    
