
from graphics import *
import math

roofPoint = [
  [0, 0],
  [0, 300],
  [300, 0],
  [300, 300],
]
changedRoofPoint = []
changedRoofPoint.extend(roofPoint)

chimneys = []
skylights =[]
fireCode = 20
gapBetweenPanel = 5
gapFromRoofEdges = 15

def panelPlot():
  panelIlgis = 165 + gapBetweenPanel
  panelPlotis = 99 + gapBetweenPanel

  plotOfPanel = panelIlgis * panelPlotis
  return plotOfPanel
# TODO: make this function more optimized for the calculations
def roofPlotWithLimitations():
  if(fireCode):
    changedRoofPoint[1][1] = changedRoofPoint[1][1] - fireCode
    changedRoofPoint[3][1] = changedRoofPoint[3][1] - fireCode
  
  
  changedRoofPoint[0][0] = changedRoofPoint[0][0] + gapFromRoofEdges
  changedRoofPoint[1][0] = changedRoofPoint[1][0] + gapFromRoofEdges
  changedRoofPoint[2][0] = changedRoofPoint[2][0] - gapFromRoofEdges
  changedRoofPoint[3][0] = changedRoofPoint[3][0] - gapFromRoofEdges

  changedRoofPoint[0][1] = changedRoofPoint[0][1] + gapFromRoofEdges
  changedRoofPoint[2][1] = changedRoofPoint[2][1] + gapFromRoofEdges
  changedRoofPoint[1][1] = changedRoofPoint[1][1] - gapFromRoofEdges
  changedRoofPoint[3][1] = changedRoofPoint[3][1] - gapFromRoofEdges

  siena1 = (changedRoofPoint[1][0] - changedRoofPoint[0][0]) + (changedRoofPoint[1][1] - changedRoofPoint[0][1])
  siena2 = (changedRoofPoint[2][0] - changedRoofPoint[0][0]) + (changedRoofPoint[2][1] - changedRoofPoint[0][1])
  roofPlot = siena1 * siena2
  panelPlotas = panelPlot()

  panelAmount = math.floor(roofPlot / panelPlotas)

  print("Amount of panels: ", panelAmount)

# TODO: check why the original array for roofPoint is being changed inside the function - it shouldn't
print("Changed: ",changedRoofPoint)
print("RoofPoint: ", roofPoint)
roofPlotWithLimitations()
print("RoofPoint: ", roofPoint)
print("Changed: " ,changedRoofPoint)



# TODO: fix this function too

def main():
  win = GraphWin("Solar Panel Placement Tool - Area3", 700, 800)
  roof = Rectangle(Point(0,0), Point(300,300))
  roof1 = Rectangle(Point(changedRoofPoint[0][0], changedRoofPoint[0][1]), Point(changedRoofPoint[3][0], changedRoofPoint[3][1]))
  solarPanel = Rectangle(Point(changedRoofPoint[0][0], changedRoofPoint[0][1]), Point(99, 165))
  solarPanel1 = Rectangle(Point(changedRoofPoint[0][0] + (99 + gapBetweenPanel), changedRoofPoint[0][1]), Point(99 + (99 + gapBetweenPanel), 165))
  # rec2.setFill('red')
  roof1.setFill('green')
  roof.draw(win)
  roof1.draw(win)
  solarPanel.draw(win)
  solarPanel1.draw(win)
  # rec2.draw(win)
  win.getMouse()
  win.close()

main()