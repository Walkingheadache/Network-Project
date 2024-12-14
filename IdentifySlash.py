#in this function  we recieve number of hosts we need in a subnet and return on what slash is the network going to be.



def Identify_s(ip,host):
    
    count = 0
    start =  0

    while host > start:
        new_num = pow(2,count) - 2
        start = new_num
        count += 1

    slash = 32 - count
  
    return f"The slash for {ip} with {host}'s is {slash}"

