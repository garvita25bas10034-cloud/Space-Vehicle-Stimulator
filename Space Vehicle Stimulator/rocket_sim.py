import sqlite3
import time 



def get_db():
    return sqlite3.connect("databases/rocket.db")

def start_db():
    con = get_db()
    cursor = con.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS simulation_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                mass REAL,
                thrust REAL,
                max_altitude REAL,
                max_velocity REAL
    )
    """)

    con.commit()
    con.close()

def save_to_db(m,th,max_alt,max_vel):
    con = get_db()
    cursor = con.cursor()

    cursor.execute("""
    INSERT INTO simulation_runs (timestamp, mass, thrust, max_altitude, max_velocity)
    VALUES(datetime('now'), ?, ?, ?, ?)
""", (m,th,max_alt,max_vel))
    
    con.commit()
    con.close()

    print("Data saved to rocket.db")


def run_rocket():
    print("\n Rocket Stimulator")

    m = float(input("Enter the mass of the rocket: "))
    th = float(input("Enter the thrust: "))

    g = 9.81
    acc = (th-m*g)/m

    velo = 0
    alt = 0 
    max_alt = 0
    max_vel = 0 

    for t in range(10):
        velo += acc
        alt += velo 

        max_alt = max(max_alt, alt)
        max_vel = max(max_vel, velo)

        print(f"t={t}s  | Altitude={alt:.2f}   | Velocity={velo:.2f}")
        time.sleep(0.5)

    save_to_db(m,th,max_alt,max_vel)


if __name__ == "__main__":
    start_db()
    run_rocket()
