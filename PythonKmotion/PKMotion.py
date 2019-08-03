from flask import Flask
from flask import render_template, request
# import RPi.GPIO as GPIO
import time
import clr
clr.AddReference(R'C:\KMotion433x64\KMotion\Debug\KMotion_dotNet.dll') 
# The R lets python interpret the string RAW so you can put in Windows paths easy
from KMotion_dotNet import KM_Controller
app = Flask(__name__)


_KM = KM_Controller()
result=_KM.CompileAndLoadCoff(1, r'C:\KMotion433x64\C Programs\SnapAmp\InitSnapAmp3Axis.c', 0)
_KM.WriteLine("Execute1")
print ("CompileAndLoadCoff="+result)
_XAxis = _KM.GetAxis(0, "X")
_YAxis = _KM.GetAxis(1, "Y")
_ZAxis = _KM.GetAxis(2, "Z")

_MotionParams = _KM.CoordMotion.MotionParams
_MotionParams.CountsPerInchX = 14000
_MotionParams.CountsPerInchY = 14000
_MotionParams.CountsPerInchZ = 13220
_KM.CoordMotion.SetTPParams()

_XAxis.Enable()
_YAxis.Enable()
_ZAxis.Enable()
_XAxis.ZeroAxis()
_YAxis.ZeroAxis()
_ZAxis.ZeroAxis()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/turnon_machine')
def turnon_machine():
   print ("MACHINE ON")
   return 'true'


@app.route('/left_side')
def left_side():
   _XAxis.Velocity = 3000.0
   xpos = _KM.CoordMotion.GetAxisPosition(0)
   _XAxis.StartRelativeMoveTo(-500)
   print("left side = "+str(xpos))
   return 'true'

@app.route('/right_side')
def right_side():
   _XAxis.Velocity = 3000.0
   xpos = _KM.CoordMotion.GetAxisPosition(0)
   _XAxis.StartRelativeMoveTo(500)
   print("left side = "+str(xpos))
   return 'true'

@app.route('/up_side')
def up_side():
   _YAxis.Velocity = 3000.0
   ypos = _KM.CoordMotion.GetAxisPosition(1)
   _YAxis.StartRelativeMoveTo(500)
   print("up side = "+str(ypos))   
   return 'true'

@app.route('/down_side')
def down_side():
   _YAxis.Velocity = 3000.0
   ypos = _KM.CoordMotion.GetAxisPosition(1)
   _YAxis.StartRelativeMoveTo(-500)
   print("down side = "+str(ypos))   
   return 'true'

@app.route('/stop')
def stop():
   print("STOP")
   _XAxis.Stop()
   _YAxis.Stop()
   _ZAxis.Stop()

   return  'true'

if __name__ == "__main__":
 print ("Start")
 app.run(host='<your IP>',port=5010)