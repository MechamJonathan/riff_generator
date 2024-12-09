
from scale import Scale


def main():
    print("\nWelcome to the Simple Guitar Riff Generator!\n")
    key = input("Choose one of the available keys: (E) ")
    scale_type = input("Choose a scale: (Major, Minor, Random) ")
    tuning = input("Choose tuning: (E_Standard, Drop_D) ")

    chosen_scale = Scale(key="E", scale_type="Minor")

if __name__ == '__main__':
    main()

