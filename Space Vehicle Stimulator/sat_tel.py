import sqlite3
import random 
import time 
import matplotlib.pyplot as plt

time_data = []
temp_data = []
vol_data = []


def get_db():
    return sqlite3.connect("databases/telemetry.db")

def start_db():
    con = get_db()
    cursor = con.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS simulation_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                voltage REAL,
                temperature REAL,
                altitude REAL,
                velocity REAL,
                radiation REAL
    )
    """)

    con.commit()
    con.close()

def save_to_db(vol,temp,alti,vel,rad):
    con = get_db()
    cursor = con.cursor()

    cursor.execute("""
    INSERT INTO simulation_runs (timestamp, voltage, temperature, altitude, velocity, radiation)
    VALUES(datetime('now'), ?, ?, ?, ?, ?)
""", (vol,temp,alti,vel,rad))
    
    con.commit()
    con.close()

    print("Data saved to telemetry.db")


def run_telemetry():
    print("\n Satellite Telemetry")
    
    for i in range(10):
        vol = random.uniform(3.0,5.0)
        temp = random.randint(-20,100)
        alti = random.randint(-20,100)
        vel = random.randint(2000,8000)
        rad = random.uniform(0.1,5.0)

        time_data.append(i)
        temp_data.append(temp)
        vol_data.append(vol)

        print(f"Temperature={temp} | Voltage={vol:.2f}")
        
        if temp>80:
            print("WARNING: System Overheat")

        save_to_db(vol,temp,alti,vel,rad)


def plot_graph(time_data, temp_data, vol_data):
    plt.figure()
    plt.plot(time_data, temp_data, marker='o')
    plt.title("Temperature vs Time")
    plt.xlabel("Time(s)")
    plt.ylabel("Temprature(C)")
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(time_data, vol_data, marker='o')
    plt.title("Voltage vs Time")
    plt.xlabel("Time(s)")
    plt.ylabel("Voltage(V)")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    start_db()
    run_telemetry()
    plot_graph(time_data, temp_data, vol_data)
