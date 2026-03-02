import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth's surface.
    
    Parameters:
    lat1 (float): Latitude of the first point in decimal degrees.
    lon1 (float): Longitude of the first point in decimal degrees.
    lat2 (float): Latitude of the second point in decimal degrees.
    lon2 (float): Longitude of the second point in decimal degrees.
    
    Returns:
    float: Distance between the two points in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert decimal degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance

def main():
    # Example coordinates: Rio de Janeiro and São Paulo
    lat1, lon1 = -22.9068, -43.1729  # Rio de Janeiro
    lat2, lon2 = -23.5505, -46.6333   # São Paulo
    
    distance = haversine_distance(lat1, lon1, lat2, lon2)
    print(f"The distance between the two points is {distance:.2f} kilometers.")

if __name__ == '__main__':
    main()