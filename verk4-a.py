from math import sqrt, acos, cos, degrees as deg
class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Þinn kóði hér

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        print(f"[{self.x} {self.y}]")
    # Fall sem skilar lengd
    def lengd(self):
        return round(sqrt(self.x**2 + self.y**2),2)

    # Fall sem skilar hallatölu
    def halli(self):
        return self.y/self.x
    # Þinn kóði hér

    # Fall sem skilar þvervigri
    def þvervigur(self):
        return Vigur(-self.y,self.x)

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self): # cos-1(((self.x*1)+0)/(self.lengd*1))
        return f"{round(deg(acos((self.x+0)/self.lengd())),1)}*"
    # Þinn kóði hér

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self, v): # cos((a.x*v.x+a.y*v.y)//(a.lengd*b.lengd))
        a = self
        b = v
        return f"{deg(acos(((a.x*b.x)+(a.y*b.y))/(a.lengd() * b.lengd())))}*"
    # Þinn kóði hér

    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self, v):
        return Vigur(self.x+v.x,self.y+v.y)


# Keyrsluforrit
v1 = Vigur(1, 3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: ", end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3, 1)
print("Horn milli vigra: ", v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: ", end=" ")
v3.prenta()

