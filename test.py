import IdentifyClass
import IdentifySlash

def main():
    print(IdentifyClass.Identify_c("172.12.0.1"))
    print(IdentifySlash.Identify_s("172.17.0.1",200))
    print(IdentifyClass.A_mask)


if __name__ == "__main__":
    main()