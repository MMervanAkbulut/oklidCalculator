import math

# Öklid Mesafesi Hesaplayan Fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Kullanıcıdan Noktaları Alma
def get_point(prompt):
    x, y = map(float, input(prompt).split())
    return (x, y)

# Kullanıcıdan iki nokta girişi al
point1 = get_point("Birinci noktayı girin (x y formatında): ")
point2 = get_point("İkinci noktayı girin (x y formatında): ")

# Mesafeyi hesapla
distance = euclideanDistance(point1, point2)

# Sonucu yazdır
# print("İki nokta arasındaki mesafe:", distance)
print(f"İki nokta arasındaki mesafe: {distance:.2f}")