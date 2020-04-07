def main():
    while True:
        ip = input("Inserisci l'insirizzo ip: ").split(".")
        int_ip = [int(i) for i in ip]

        if (len(int_ip) == 4 and int_ip[0] <= 255 and int_ip[0] >= 0 and int_ip[1] <= 255 and int_ip[1] >= 0 and int_ip[
            2] <= 255 and int_ip[2] >= 0 and int_ip[3] <= 255 and int_ip[3] >= 0):
            break
        else:
            print("Invalid ip.")

    while True:
        mask = int(input("Inserisic la maschera: "))
        subnet = int(input("Inserisci il numero di subnet: "))
        if (mask <= 32 and mask >= 0 and subnet <= 32 and subnet >= 0):
            break
        else:
            print("Invalid mask. ")

    """
    ipaddress = "192.160.10.0"
    mask = 20

    ipaddress_splitted = [int(i) for i in ipaddress.split(".")]

    ipaddress_bin = 0
    for e, group in enumerate(ipaddress_splitted):
        ipaddress_bin = ipaddress_bin + group * (2 ** (((3 - e) * 8)))

    ipaddress_host = ipaddress_bin
    for c in range(1, 2 ** (32 - mask) - 1):
        ipaddress_host = ipaddress_host + 1
        l = '.'.join([str(int(bin(ipaddress_host)[i:i + 8], 2)) for i in range(2, 34, 8)])
        print(l)
    """

    n_host = pow(2, (32 - (mask + subnet))) - 2

    print(f"""
    ip = {int_ip}
    mask = {mask}
    n_host = {n_host}
    """)

    bin_ip = [bin(i) for i in int_ip]

    inc3 = 0
    inc2 = 0
    inc1 = 0
    inc0 = 0

    for i in range(0, pow(2, (subnet))):
        print(f"|SUBNET {i}|")
        if inc3 + int_ip[3] < 255:
            inc3 = inc3 + 1
        else:
            inc3 = 0
            int_ip[3] = 0
            if inc2 + int_ip[2] < 255:
                inc2 = inc2 + 1
            else:
                inc2 = 0
                int_ip[2] = 0
                if inc3 + int_ip[1] < 255:
                    inc1 = inc1 + 1
                else:
                    inc1 = 0
                    int_ip[1] = 0
                    if inc0 + int_ip[0] < 255:
                        inc0 = inc0 + 1
                    else:
                        inc0 = 0
                        int_ip[0] = 0

        print(f"""network: {int_ip[0] + inc0}.{int_ip[1] + inc1}.{int_ip[2] + inc2}.{int_ip[3] + inc3}
    host range:""")

        for k in range(1, n_host + 1):
            if inc3 + int_ip[3] < 255:
                inc3 = inc3 + 1
            else:
                inc3 = 0
                int_ip[3] = 0
                if inc2 + int_ip[2] < 255:
                    inc2 = inc2 + 1
                else:
                    inc2 = 0
                    int_ip[2] = 0
                    if inc3 + int_ip[1] < 255:
                        inc1 = inc1 + 1
                    else:
                        inc1 = 0
                        int_ip[1] = 0
                        if inc0 + int_ip[0] < 255:
                            inc0 = inc0 + 1
                        else:
                            inc0 = 0
                            int_ip[0] = 0

            print(f"{int_ip[0] + inc0}.{int_ip[1] + inc1}.{int_ip[2] + inc2}.{int_ip[3] + inc3}")

        if inc3 + int_ip[3] < 255:
            inc3 = inc3 + 1
        else:
            inc3 = 0
            int_ip[3] = 0
            if inc2 + int_ip[2] < 255:
                inc2 = inc2 + 1
            else:
                inc2 = 0
                int_ip[2] = 0
                if inc3 + int_ip[1] < 255:
                    inc1 = inc1 + 1
                else:
                    inc1 = 0
                    int_ip[1] = 0
                    if inc0 + int_ip[0] < 255:
                        inc0 = inc0 + 1
                    else:
                        inc0 = 0
                        int_ip[0] = 0
        print(f"broadcast: {int_ip[0] + inc0}.{int_ip[1] + inc1}.{int_ip[2] + inc2}.{int_ip[3] + inc3}")

if __name__ == "__main__":
    main()
