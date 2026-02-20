def main():
    seed = input("enter seed key >> ")

    def gen_part(seed):
        part = (seed[0:3], seed[3:])
        return part

    part = gen_part(seed)

    def print_part(part):
        return " ".join(part)

    print(print_part(part))

    for i in range(5):
        seed = seed[1:] + seed[0]
        print(print_part(gen_part(seed)))


main()
