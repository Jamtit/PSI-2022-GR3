import math

fireCode = 50
gapBetweenPanels = 10 / 2
gapFromRoofEdges = 15
stogoPlotis = 1000
stogoIlgis = 2000
panelIlgis = 165 + gapBetweenPanels
panelPlotis = 99 + gapBetweenPanels

def test_howManyFits():
    
    solarPanelKiekis = 106
    solarPanelPlotas = (panelIlgis * panelPlotis) * solarPanelKiekis
    stogoPlotas = (stogoPlotis - 2 * gapFromRoofEdges) * (stogoIlgis - fireCode - gapFromRoofEdges)
    assert (stogoPlotas >= solarPanelPlotas)

def test_vertical():

    solarPanelKiekis = 90
    galimasEiliuSkaicius = math.floor((stogoPlotis - 2 * gapFromRoofEdges) / panelIlgis)
    realusStogoIlgis = stogoIlgis - fireCode - gapFromRoofEdges
    MAXBaterijuKiekisVienojEilej = math.floor(realusStogoIlgis / panelPlotis)
    assert (MAXBaterijuKiekisVienojEilej * galimasEiliuSkaicius >= solarPanelKiekis)

def test_horizontal():

    solarPanelKiekis = 99
    galimasEiliuSkaicius = math.floor((stogoPlotis - 2 * gapFromRoofEdges) / panelPlotis)
    realusStogoIlgis = stogoIlgis - fireCode - gapFromRoofEdges
    MAXBaterijuKiekisVienojEilej = math.floor(realusStogoIlgis / panelIlgis)
    assert (MAXBaterijuKiekisVienojEilej * galimasEiliuSkaicius >= solarPanelKiekis)
