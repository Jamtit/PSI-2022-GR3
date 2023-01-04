import math
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_xyz():
    f = open('D:\PSI-Project\d2.json')
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
  f = open('D:\PSI-Project\d2.json')
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

x, y, z = get_xyz()
penX, penY, penZ = get_penetrations()


solarX = []
solarY = []
solarZ = []

solarX2 = []
solarY2 = []
solarZ2 = []

solarX3 = []
solarY3 = []
solarZ3 = []

solarX4 = []
solarY4 = []
solarZ4 = []

solarX.append(21)
solarX.append(27)
solarY.append(14.6)
solarY.append(14.7)
solarZ.append(15.7)
solarZ.append(15.7)

solarX.append(27)
solarX.append(27)
solarY.append(14.7)
solarY.append(12.7)
solarZ.append(15.7)
solarZ.append(14.7)

solarX.append(27)
solarX.append(21)
solarY.append(12.7)
solarY.append(12.7)
solarZ.append(14.7)
solarZ.append(14.7)

solarX.append(21)
solarX.append(21)
solarY.append(12.7)
solarY.append(14.7)
solarZ.append(14.7)
solarZ.append(15.7)

# Second panel

solarX.append(28)
solarX.append(34)
solarY.append(14.7)
solarY.append(14.7)
solarZ.append(15.7)
solarZ.append(15.7)

solarX.append(34)
solarX.append(34)
solarY.append(14.7)
solarY.append(12.7)
solarZ.append(15.7)
solarZ.append(14.7)

solarX.append(34)
solarX.append(28)
solarY.append(12.7)
solarY.append(12.7)
solarZ.append(14.7)
solarZ.append(14.7)

solarX.append(28)
solarX.append(28)
solarY.append(12.7)
solarY.append(14.7)
solarZ.append(14.7)
solarZ.append(15.7)

# Third solar

solarX.append(35)
solarX.append(41)
solarY.append(14.7)
solarY.append(14.7)
solarZ.append(15.7)
solarZ.append(15.7)

solarX.append(41)
solarX.append(41)
solarY.append(14.7)
solarY.append(12.7)
solarZ.append(15.7)
solarZ.append(14.7)

solarX.append(41)
solarX.append(35)
solarY.append(12.7)
solarY.append(12.7)
solarZ.append(14.7)
solarZ.append(14.7)

solarX.append(35)
solarX.append(35)
solarY.append(12.7)
solarY.append(14.7)
solarZ.append(14.7)
solarZ.append(15.7)

# Fourth panel

solarX.append(4)
solarX.append(10)
solarY.append(14.7)
solarY.append(14.7)
solarZ.append(15.7)
solarZ.append(15.7)

solarX.append(10)
solarX.append(10)
solarY.append(14.7)
solarY.append(12.7)
solarZ.append(15.7)
solarZ.append(14.7)

solarX.append(10)
solarX.append(4)
solarY.append(12.7)
solarY.append(12.7)
solarZ.append(14.7)
solarZ.append(14.7)

solarX.append(4)
solarX.append(4)
solarY.append(12.7)
solarY.append(14.7)
solarZ.append(14.7)
solarZ.append(15.7)

# Fifth panel

solarX2.append(21)
solarX2.append(27)
solarY2.append(12)
solarY2.append(12)
solarZ2.append(14.5)
solarZ2.append(14.5)

solarX2.append(27)
solarX2.append(27)
solarY2.append(12)
solarY2.append(10)
solarZ2.append(14.5)
solarZ2.append(13.5)

solarX2.append(27)
solarX2.append(21)
solarY2.append(10)
solarY2.append(10)
solarZ2.append(13.5)
solarZ2.append(13.5)

solarX2.append(21)
solarX2.append(21)
solarY2.append(10)
solarY2.append(12)
solarZ2.append(13.5)
solarZ2.append(14.5)

# Sixth panel

solarX2.append(34)
solarX2.append(40)
solarY2.append(12)
solarY2.append(12)
solarZ2.append(14.5)
solarZ2.append(14.5)

solarX2.append(40)
solarX2.append(40)
solarY2.append(12)
solarY2.append(10)
solarZ2.append(14.5)
solarZ2.append(13.5)

solarX2.append(40)
solarX2.append(34)
solarY2.append(10)
solarY2.append(10)
solarZ2.append(13.5)
solarZ2.append(13.5)

solarX2.append(34)
solarX2.append(34)
solarY2.append(10)
solarY2.append(12)
solarZ2.append(13.5)
solarZ2.append(14.5)

# Seventh panel

solarX3.append(21)
solarX3.append(27)
solarY3.append(9)
solarY3.append(9)
solarZ3.append(13)
solarZ3.append(13)

solarX3.append(27)
solarX3.append(27)
solarY3.append(9)
solarY3.append(7)
solarZ3.append(13)
solarZ3.append(12)

solarX3.append(27)
solarX3.append(21)
solarY3.append(7)
solarY3.append(7)
solarZ3.append(12)
solarZ3.append(12)

solarX3.append(21)
solarX3.append(21)
solarY3.append(7)
solarY3.append(9)
solarZ3.append(12)
solarZ3.append(13)

# Eight panel

solarX3.append(28)
solarX3.append(34)
solarY3.append(9)
solarY3.append(9)
solarZ3.append(13)
solarZ3.append(13)

solarX3.append(34)
solarX3.append(34)
solarY3.append(9)
solarY3.append(7)
solarZ3.append(13)
solarZ3.append(12)

solarX3.append(34)
solarX3.append(28)
solarY3.append(7)
solarY3.append(7)
solarZ3.append(12)
solarZ3.append(12)

solarX3.append(28)
solarX3.append(28)
solarY3.append(7)
solarY3.append(9)
solarZ3.append(12)
solarZ3.append(13)

# Ninth panel

solarX3.append(22)
solarX3.append(28)
solarY3.append(6)
solarY3.append(6)
solarZ3.append(11.6)
solarZ3.append(11.6)

solarX3.append(28)
solarX3.append(28)
solarY3.append(4)
solarY3.append(4)
solarZ3.append(10.6)
solarZ3.append(10.6)

solarX3.append(28)
solarX3.append(22)
solarY3.append(4)
solarY3.append(4)
solarZ3.append(10.6)
solarZ3.append(10.6)

solarX3.append(22)
solarX3.append(22)
solarY3.append(4)
solarY3.append(6)
solarZ3.append(10.6)
solarZ3.append(11.6)

# Tenth panel

solarX3.append(29)
solarX3.append(35)
solarY3.append(6)
solarY3.append(6)
solarZ3.append(11.6)
solarZ3.append(11.6)

solarX3.append(35)
solarX3.append(35)
solarY3.append(4)
solarY3.append(4)
solarZ3.append(10.6)
solarZ3.append(10.6)

solarX3.append(35)
solarX3.append(29)
solarY3.append(4)
solarY3.append(4)
solarZ3.append(10.6)
solarZ3.append(10.6)

solarX3.append(29)
solarX3.append(29)
solarY3.append(4)
solarY3.append(6)
solarZ3.append(10.6)
solarZ3.append(11.6)

# Eleventh panel

solarX4.append(49)
solarX4.append(55)
solarY4.append(16.6)
solarY4.append(16.6)
solarZ4.append(15.3)
solarZ4.append(15.3)

solarX4.append(55)
solarX4.append(55)
solarY4.append(16.6)
solarY4.append(14.8)
solarZ4.append(15.3)
solarZ4.append(14.3)

solarX4.append(55)
solarX4.append(49)
solarY4.append(14.8)
solarY4.append(14.8)
solarZ4.append(14.3)
solarZ4.append(14.3)

solarX4.append(49)
solarX4.append(49)
solarY4.append(14.8)
solarY4.append(16.6)
solarZ4.append(14.3)
solarZ4.append(15.3)

# Twelveth panel

solarX4.append(49)
solarX4.append(55)
solarY4.append(14.2)
solarY4.append(14.2)
solarZ4.append(14.1)
solarZ4.append(14.1)

solarX4.append(55)
solarX4.append(55)
solarY4.append(14.2)
solarY4.append(12.2)
solarZ4.append(14.1)
solarZ4.append(13.1)

solarX4.append(55)
solarX4.append(49)
solarY4.append(12.2)
solarY4.append(12.2)
solarZ4.append(13.1)
solarZ4.append(13.1)

solarX4.append(49)
solarX4.append(49)
solarY4.append(12.2)
solarY4.append(14.2)
solarZ4.append(13.1)
solarZ4.append(14.1)

# Thirteen panel

solarX4.append(49)
solarX4.append(55)
solarY4.append(11.8)
solarY4.append(11.8)
solarZ4.append(12.9)
solarZ4.append(12.9)

solarX4.append(55)
solarX4.append(55)
solarY4.append(11.8)
solarY4.append(9.8)
solarZ4.append(12.9)
solarZ4.append(11.9)

solarX4.append(55)
solarX4.append(49)
solarY4.append(9.8)
solarY4.append(9.8)
solarZ4.append(11.9)
solarZ4.append(11.9)

solarX4.append(49)
solarX4.append(49)
solarY4.append(9.8)
solarY4.append(11.8)
solarZ4.append(11.9)
solarZ4.append(12.9)

# Forteen panel

solarX4.append(49)
solarX4.append(55)
solarY4.append(9.1)
solarY4.append(9.1)
solarZ4.append(11.7)
solarZ4.append(11.7)

solarX4.append(55)
solarX4.append(55)
solarY4.append(9.1)
solarY4.append(7.1)
solarZ4.append(11.7)
solarZ4.append(10.7)

solarX4.append(55)
solarX4.append(49)
solarY4.append(7.1)
solarY4.append(7.1)
solarZ4.append(10.7)
solarZ4.append(10.7)

solarX4.append(49)
solarX4.append(49)
solarY4.append(7.1)
solarY4.append(9.1)
solarZ4.append(10.7)
solarZ4.append(11.7)

solarsD2 = {
  "lines0":
  {
    "X": solarX,
    "Y": solarY,
    "Z": solarZ
  },
  "lines1":
  {
    "X": solarX2,
    "Y": solarY2,
    "Z": solarZ2
  },
  "lines2":
  {
    "X": solarX3,
    "Y": solarY3,
    "Z": solarZ3
  },
  "lines3":
  {
    "X": solarX4,
    "Y": solarY4,
    "Z": solarZ4
  }
}

with open("solarsD2.json", "w") as write:
  json.dump(solarsD2, write)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot(x,y,z, color='r')
# ax.plot(penX, penY, penZ, color='r')
ax.plot(solarX, solarY, solarZ, color='b')
ax.plot(solarX2, solarY2, solarZ2, color='b')
ax.plot(solarX3, solarY3, solarZ3, color='b')
ax.plot(solarX4, solarY4, solarZ4, color='b')


fig.savefig('foo.png', bbox_inches='tight')



plt.show()


