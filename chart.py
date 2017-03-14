'''
    Chart Features
    --------------

    This is an Area Chart that contains a Legend Widget to compare cost of living in paris.

'''
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, Rect
from reportlab.graphics.charts.axes import XValueAxis, YValueAxis, AdjYValueAxis, NormalDateXValueAxis
from reportlab.lib import colors
from reportlab.lib.colors import PCMYKColor
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.rl_config import defaultPageSize
from reportlab.graphics.charts.lineplots import LinePlot, AreaLinePlot
from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, Rect, String
from reportlab.lib.formatters import DecimalFormatter


PAGE_HEIGHT=defaultPageSize[1]
styles = getSampleStyleSheet()
Title = Paragraph("COST OF LIVING IN  PARIS &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp $3214.12/mo", styles["Heading1"])


drawing = Drawing(400, 200)

# chart
my_colors = PCMYKColor(50,0,100,20, alpha=40) ,PCMYKColor(0,100,100,40) ,PCMYKColor(100,0,90,50) ,PCMYKColor(0,0,0,40) ,PCMYKColor(10,0,100,11) ,PCMYKColor(15,0,0,0) ,PCMYKColor(0,0,0,50)
lp = LinePlot()
lp.x = 0
lp.y = 0
lp.width = 400
lp.height = 120
lp.lines[0].inFill=True
lp.lines[0].strokeColor = my_colors[0]
# x axis
lp.xValueAxis = NormalDateXValueAxis() # we change the axis type here
lp.xValueAxis.bottomAxisLabelSlack = 0
lp.xValueAxis.dailyFreq = 0
lp.xValueAxis.forceEndDate = True
lp.xValueAxis.forceFirstDate = True
lp.xValueAxis.gridEnd = 0
lp.xValueAxis.gridStart = 0
lp.xValueAxis.gridStrokeWidth = 1
lp.xValueAxis.joinAxisMode='bottom'
lp.xValueAxis.labels.angle = 30
lp.xValueAxis.labels.boxAnchor = 'e'
lp.xValueAxis.labels.dx = -2
lp.xValueAxis.labels.dy = -10
lp.xValueAxis.labels.fontName = 'Times-Roman'
lp.xValueAxis.labels.fontSize = 10
lp.xValueAxis.maximumTicks = 13
lp.xValueAxis.minimumTickSpacing = 20 # in points
lp.xValueAxis.strokeWidth = 1
lp.xValueAxis.tickDown =  10
lp.xValueAxis.visibleAxis = True
lp.xValueAxis.valueSteps = None
lp.xValueAxis.visibleGrid = True
lp.xValueAxis.xLabelFormat = '{mm},{dd},{yyyy}'
# y axis
lp.yValueAxis.avoidBoundFrac = 0.1
lp.yValueAxis.drawGridLast          = True
lp.yValueAxis.forceZero = True
lp.yValueAxis.gridStrokeWidth = 0.5
lp.yValueAxis.labels.dy = 0
lp.yValueAxis.labels.fontName = 'Times-Roman'
lp.yValueAxis.labels.fontSize = 10
lp.yValueAxis.labels.rightPadding   = 10
lp.yValueAxis.labelTextFormat = DecimalFormatter(places=0,thousandSep=',',decimalSep='.',prefix='$')
lp.yValueAxis.maximumTicks = 7
lp.yValueAxis.rangeRound='floor'
lp.yValueAxis.strokeWidth = 0.5
lp.yValueAxis.tickLeft = 5
lp.yValueAxis.tickRight = 0
lp.yValueAxis.valueMax = None
lp.yValueAxis.valueMin = None
lp.yValueAxis.valueStep = None
lp.yValueAxis.visibleAxis = True
lp.yValueAxis.visibleGrid = True
lp.yValueAxis.visibleTicks = True
lp.data = [[(19960901, 100000.0), (19961201, 109034.00000000001), (19970301, 110105.00000000001), (19970601, 127487.0), (19970901, 134702.0), (19971201, 136920.0), (19980301, 153788.0), (19980601, 158997.0), (19980901, 141245.0), (19981201, 171859.0), (19990301, 179215.0), (19990601, 193963.0), (19990901, 181679.0), (19991201, 202828.0), (20000301, 216832.0), (20000601, 218377.0), (20000901, 222553.0), (20001201, 220915.00000000003), (20010301, 204568.0), (20010601, 212621.0), (20010901, 185524.0), (20011201, 202977.0), (20020301, 204425.0), (20020601, 176716.0), (20020901, 143573.0), (20021201, 158079.0), (20030301, 153953.0), (20030601, 181898.0), (20030901, 186917.0), (20031201, 210109.0), (20040301, 214340.99999999997), (20040601, 217241.00000000003), (20040901, 207773.0), (20041201, 226420.99999999997), (20050301, 219802.0), (20050601, 224784.0), (20050901, 234346.0), (20051201, 238378.99999999997), (20060301, 244329.99999999997), (20060601, 237279.00000000003), (20060901, 250893.0)]]
lp.lines.strokeWidth     = .5

drawing.add(lp)
Elements = [Title, drawing]
def go():
   doc = SimpleDocTemplate('chart.pdf')
   doc.build(Elements)

go()
