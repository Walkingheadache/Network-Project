import IdentifyClass
import IdentifySlash

def main():
    print(IdentifyClass.Identify_c("172.12.0.1"))
    print(IdentifySlash.Identify_s_host("172.17.0.1",300))
    print(IdentifySlash.identify_s_subnet("220.190.156.0",37))


if __name__ == "__main__":
    main()