#in this function  we recieve number of hosts we need in a subnet and return on what slash is the network going to be.
import IdentifyClass


def Identify_s_host(ip = None ,host = None):
    
    count = 0
    start =  0

    while host > start:
        new_num = pow(2,count) - 2
        start = new_num
        if host > start:
            count += 1

    slash = 32 - count
  
    return f"The slash for {ip} with {host} hosts is {slash}"

def identify_s_subnet(ip = None ,subnet = None ): #this function helps us identify slash for 
    count = 0
    start = 0
    while subnet > start:
        new_num = pow(2,count)
        start = new_num
        if subnet > start:
            count += 1

    identify_result = IdentifyClass.Identify_c(ip) #storing the value to avoid calling the function repeteadly 

    if int(identify_result[2]) == 8: #checks if the slash is 8 so we can define slash for subnets
        slash  = 8 + count
        hosts = pow(2,32 - slash) - 2
        return f"The slash for {ip} with {subnet} subnets is {slash}.Available hosts {hosts}"
    elif int(identify_result[2]) == 16: #same logic here
        slash = 16 + count
        hosts = pow(2,32 - slash) - 2
        return f"The slash for {ip} with {subnet} subnets is {slash},Available hosts {hosts}"
    elif int(identify_result[2]) == 24: #and here too
        slash = 24 + count
        hosts = pow(2,32 - slash) - 2
        return f"The slash for {ip} with {subnet} subnets is {slash},Available hosts {hosts}"
    elif  identify_result == 0: #if the result is 0, to avoid further issues.
        return f"Invalid IP address: {ip}"