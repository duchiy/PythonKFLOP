import clr
clr.AddReference(R'C:\KMotion433x64\KMotion\Debug\KMotion_dotNet.dll') 
# The R lets python interpret the string RAW so you can put in Windows paths easy
from KMotion_dotNet import KM_Controller
_KM = KM_Controller()
result=_KM.CompileAndLoadCoff(1, R'C:\KMotion433x64\C Programs\SnapAmp\InitSnapAmp3Axis.c', 0)
x = _KM.GetAxis(0, "X")
y = _KM.GetAxis(1, "Y")
z = _KM.GetAxis(2, "Z")

x.Enable()
y.Enable()
z.Enable()

xpos = _KM.CoordMotion.GetAxisPosition(0)
ypos = _KM.CoordMotion.GetAxisPosition(1)
zpos = _KM.CoordMotion.GetAxisPosition(2)