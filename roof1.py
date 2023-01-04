
from graphics import *
import math
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.proj3d as pj3D
import numpy as np

def get_xyz():
    f = open('D:\PSI-Project\d1.json')
    templates = json.load(f)

    x=[]
    y=[]
    z=[]

    for key, value in templates.items():
        # print(value)
        for i in value:
            # print(i["@type"])
            if(i["@type"] == "ROOF"):
              a = i["POLYGON"]["@path"]
              for j_key, j_value in a.items():
                  for k_key, k_value in j_value.items():
                      if "C" in k_key:
                          x.append(k_value["X"])
                          y.append(k_value["Y"])
                          z.append(k_value["Z"])
    # print(x)
    # print("-----------------------------------\n")
    # print(y)
    # print("-----------------------------------\n")
    # print(z)
    return x, y, z

def get_penetrations():
  f = open('D:\PSI-Project\d1.json')
  templates = json.load(f)

  penX=[]
  penY=[]
  penZ=[]

  for key, value in templates.items():
        # print(value)
        for i in value:
            # print(i["@type"])
            if(i["@type"] == "ROOFPENETRATION"):
              a = i["POLYGON"]["@path"]
              for j_key, j_value in a.items():
                  for k_key, k_value in j_value.items():
                      if "C" in k_key:
                          penX.append(k_value["X"])
                          penY.append(k_value["Y"])
                          penZ.append(k_value["Z"])
  print(penX)
  print("-----------------------------------\n")
  print(penY)
  print("-----------------------------------\n")
  print(penZ)
  return penX, penY, penZ

penX, penY, penZ = get_penetrations()

x, y, z = get_xyz()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot(x,y,z, color='r')


fig.savefig('foo.png', bbox_inches='tight')



newX = []
newY = []
newZ = []
for items in range(math.floor(len(x) / 2)):
  newX.append(x[items])
  newY.append(y[items])
  newZ.append(z[items])
  print(str(items + 1))
  print("X: " + str(newX) + " , Y: " + str(newY) + " ,Z: " + str(newZ))
  print("-------------------------------------")


def changeAreaSize(x, y, z):
  for j in range(len(x)):
    if(j <= 2 or j == len(x) - 1):
      x[j] = x[j] + 2
    else:
       x[j] = x[j] - 2
  for i in range(len(y)):
    if(i == 0 or i > 4):
      y[i] = y[i] + 2
    else:
      y[i] = y[i] - 2

  for l in range(len(z)):
    if(l >= 3 and l < 7):
      z[l] = z[l] + 3
    else:
      z[l]= z[l] - 3


print("Before: ", newX)
changeAreaSize(newX, newY, newZ)
print("After: ", newX)
print("After", newY)

solarX = []
solarY = []
solarZ = []

solarX1 = []
solarY1 = []
solarZ1 = []

solarX2 = []
solarY2 = []
solarZ2 = []

solarX.append(2)
solarX.append(2.6)
solarY.append(2)
solarY.append(7)
solarZ.append(26.8)
solarZ.append(26.8)

solarX.append(2.6)
solarX.append(5.8)
solarY.append(7)
solarY.append(6.5)
solarZ.append(26.8)
solarZ.append(21.6)

solarX.append(5.8)
solarX.append(5.3)
solarY.append(6.5)
solarY.append(1.5)
solarZ.append(21.6)
solarZ.append(21.6)

solarX.append(5.3)
solarX.append(2)
solarY.append(1.5)
solarY.append(2)
solarZ.append(21.6)
solarZ.append(26.8)

# Second solar

solarX.append(3)
solarX.append(3.6)
solarY.append(8)
solarY.append(13)
solarZ.append(26.8)
solarZ.append(26.8)

solarX.append(3.6)
solarX.append(6.6)
solarY.append(13)
solarY.append(12.6)
solarZ.append(26.8)
solarZ.append(21.6)

solarX.append(6.6)
solarX.append(6)
solarY.append(12.6)
solarY.append(7.5)
solarZ.append(21.6)
solarZ.append(21.6)

solarX.append(6)
solarX.append(3)
solarY.append(7.5)
solarY.append(8)
solarZ.append(21.6)
solarZ.append(26.8)

# Third Solar
solarX.append(4)
solarX.append(4.6)
solarY.append(14)
solarY.append(19)
solarZ.append(26.8)
solarZ.append(26.8)

solarX.append(4.6)
solarX.append(7.6)
solarY.append(19)
solarY.append(18.6)
solarZ.append(26.8)
solarZ.append(21.6)

solarX.append(7.6)
solarX.append(7)
solarY.append(18.6)
solarY.append(13.6)
solarZ.append(21.6)
solarZ.append(21.6)

solarX.append(7)
solarX.append(4)
solarY.append(13.6)
solarY.append(14)
solarZ.append(21.6)
solarZ.append(26.8)

# Fourth Solar

solarX.append(5)
solarX.append(5.6)
solarY.append(20)
solarY.append(25)
solarZ.append(26.8)
solarZ.append(26.8)

solarX.append(5.6)
solarX.append(8.6)
solarY.append(25)
solarY.append(24.6)
solarZ.append(26.8)
solarZ.append(21.6)

solarX.append(8.6)
solarX.append(8)
solarY.append(24.6)
solarY.append(19.6)
solarZ.append(21.6)
solarZ.append(21.6)

solarX.append(8)
solarX.append(5)
solarY.append(19.6)
solarY.append(20)
solarZ.append(21.6)
solarZ.append(26.8)

# Fifth Solar

solarX.append(6)
solarX.append(6.6)
solarY.append(26)
solarY.append(31)
solarZ.append(26.8)
solarZ.append(26.8)

solarX.append(6.6)
solarX.append(9.6)
solarY.append(31)
solarY.append(30.6)
solarZ.append(26.8)
solarZ.append(21.6)

solarX.append(9.6)
solarX.append(9)
solarY.append(30.6)
solarY.append(25.6)
solarZ.append(21.6)
solarZ.append(21.6)

solarX.append(9)
solarX.append(6)
solarY.append(25.6)
solarY.append(26)
solarZ.append(21.6)
solarZ.append(26.8)

# Sixth Solar

solarX1.append(6)
solarX1.append(6.6)
solarY1.append(1.3)
solarY1.append(7)
solarZ1.append(21)
solarZ1.append(21)

solarX1.append(6.6)
solarX1.append(9.6)
solarY1.append(7)
solarY1.append(6.5)
solarZ1.append(21)
solarZ1.append(16)

solarX1.append(9.6)
solarX1.append(9)
solarY1.append(6.5)
solarY1.append(1)
solarZ1.append(16)
solarZ1.append(16)

solarX1.append(9)
solarX1.append(6)
solarY1.append(1)
solarY1.append(1.3)
solarZ1.append(16)
solarZ1.append(21)

# Seventh Solar

solarX2.append(8)
solarX2.append(8.6)
solarY2.append(19.5)
solarY2.append(24.5)
solarZ2.append(21)
solarZ2.append(21)

solarX2.append(8.6)
solarX2.append(11.6)
solarY2.append(24.5)
solarY2.append(24)
solarZ2.append(21)
solarZ2.append(16)

solarX2.append(11.6)
solarX2.append(11)
solarY2.append(24)
solarY2.append(19.5)
solarZ2.append(16)
solarZ2.append(16)

solarX2.append(11)
solarX2.append(8)
solarY2.append(19.5)
solarY2.append(19.8)
solarZ2.append(16)
solarZ2.append(21)


solarsD1 = {
  "lines0":
  {
    "X": solarX,
    "Y": solarY,
    "Z": solarZ
  },
  "lines1":
  {
    "X": solarX1,
    "Y": solarY1,
    "Z": solarZ1
  },
  "lines2":
  {
    "X": solarX2,
    "Y": solarY2,
    "Z": solarZ2
  }
}

with open("solarsD1.json", "w") as write:
  json.dump(solarsD1, write)

# print("SolarX: " + str(solarX) + " SolarY: " + str(solarY) + " SolarZ: " + str(solarZ))

# ax.plot(penX, penY, penZ, color='r')
ax.plot(newX, newY, newZ, color='g')
ax.plot(solarX, solarY, solarZ, color='b')
ax.plot(solarX1, solarY1, solarZ1, color='b')
ax.plot(solarX2, solarY2, solarZ2, color='b')

plt.show()


