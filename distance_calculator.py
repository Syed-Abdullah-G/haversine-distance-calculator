from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

if __name__ == "__main__":
    try:
        lat1 = float(input("Enter latitude of point 1: "))
        lon1 = float(input("Enter longitude of point 1: "))
        lat2 = float(input("Enter latitude of point 2: "))
        lon2 = float(input("Enter longitude of point 2: "))
        
        result = haversine(lat1, lon1, lat2, lon2)
        print(f"The distance between the two points is: {result:.2f} km")
    except ValueError:
        print("Please enter valid numerical input.")
