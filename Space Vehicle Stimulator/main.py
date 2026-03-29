from rocket_sim import run_rocket
from sat_tel import run_telemetry, plot_graph

def main():
    while True:
        print("\n---Space Vehicle Stimulator---")
        print("1. Rocket Simulator")
        print("2. Satellite Telemetry")
        print("3. Exit")

        choice = input("Enter the choice: ")

        if choice == "1":
            run_rocket()
        elif choice == "2":
            run_telemetry()
            plot_graph()
        elif choice == "3":
            print("Exiting stimulator...")
            break 
        else:
            print("Invalid choice entered")


if __name__ == "__main__":
    main()