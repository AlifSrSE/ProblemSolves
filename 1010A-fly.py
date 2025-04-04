# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

EPSILON = 1e-6

def solve(a, b, m):
    # The binary search for the minimal amount of fuel
    lower = 0.0
    upper = 1000000001.0
    
    while upper - lower > EPSILON:
        middle = (lower + upper) / 2.0
        
        if check(a, b, m, middle):
            upper = middle  # if it's possible, try smaller fuel
        else:
            lower = middle  # if not, try larger fuel
    
    return lower

def check(a, b, m, fuel):
    n = len(a)
    current_fuel = fuel
    
    # Simulate the journey to all planets and back
    for i in range(n):
        # The amount of fuel needed for takeoff from planet i
        takeoff_fuel = (m + current_fuel) / a[i]
        if current_fuel < takeoff_fuel:
            return False  # Not enough fuel for takeoff
        current_fuel -= takeoff_fuel
        
        # The amount of fuel needed for landing at planet (i + 1) % n
        landing_fuel = (m + current_fuel) / b[(i + 1) % n]
        if current_fuel < landing_fuel:
            return False  # Not enough fuel for landing
        current_fuel -= landing_fuel
    
    return True

def main():
    n = int(input())  # number of planets
    m = int(input())  # weight of the payload (cargo)
    
    a = list(map(int, input().split()))  # takeoff coefficients
    b = list(map(int, input().split()))  # landing coefficients
    
    # Output the result of the binary search
    print(f"{solve(a, b, m):.10f}")

if __name__ == "__main__":
    main()
