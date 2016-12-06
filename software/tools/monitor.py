#from bottle import route, run, debug, template, get_url
from bottle import *
import pypot.dynamixel
import time

@route('/ports')
def port_list():
    return pypot.dynamixel.get_available_ports()

@route('/')
def motor_list():
    motors = {1 : {'id':1, 'name':"r_shoulder_y", 'detected':False, 'position':None},
    2 : {'id':2, 'name':"l_shoulder_y", 'detected':False, 'position':None},
    3 : {'id':3, 'name':"r_shoulder_x", 'detected':False, 'position':None},
    4 : {'id':4, 'name':"l_shoulder_x", 'detected':False, 'position':None},
    5 : {'id':5, 'name':"r_elbow_x", 'detected':False, 'position':None},
    6 : {'id':6, 'name':"l_elbow_x", 'detected':False, 'position':None},
    7 : {'id':7, 'name':"r_hip_x", 'detected':False, 'position':None},
    8 : {'id':8, 'name':"l_hip_x", 'detected':False, 'position':None},
    9 : {'id':9, 'name':"r_hip_y", 'detected':False, 'position':None},
    10 : {'id':10, 'name':"l_hip_y", 'detected':False, 'position':None},
    11 : {'id':11, 'name':"r_knee_y", 'detected':False, 'position':None},
    12 : {'id':12, 'name':"l_knee_y", 'detected':False, 'position':None},
    13 : {'id':13, 'name':"r_ankle_y", 'detected':False, 'position':None},
    14 : {'id':14, 'name':"l_ankle_y", 'detected':False, 'position':None},
    15 : {'id':15, 'name':"r_ankle_x", 'detected':False, 'position':None},
    16 : {'id':16, 'name':"l_ankle_x", 'detected':False, 'position':None}}
    dxl_io = pypot.dynamixel.Dxl320IO('/dev/ttyAMA0')
    detected = (dxl_io.scan(range(60)))

    for id in detected:
        motors[id]['detected']=True
        motors[id]['position']=dxl_io.get_present_position({id})

    dxl_io.close()
    return template('monitor.tpl', motors=motors)

@route('/simulates')
def simulates():
    print("simulates")
    motors = {1 : {'id':1, 'name':"r_shoulder_y", 'detected':False, 'position':2},
    2 : {'id':2, 'name':"l_shoulder_y", 'detected':False, 'position':45},
    3 : {'id':3, 'name':"r_shoulder_x", 'detected':False, 'position':-4},
    4 : {'id':4, 'name':"l_shoulder_x", 'detected':False, 'position':None},
    5 : {'id':5, 'name':"r_elbow_x", 'detected':False, 'position':-54},
    6 : {'id':6, 'name':"l_elbow_x", 'detected':False, 'position':21},
    7 : {'id':7, 'name':"r_hip_x", 'detected':False, 'position':124},
    8 : {'id':8, 'name':"l_hip_x", 'detected':False, 'position':-100},
    9 : {'id':9, 'name':"r_hip_y", 'detected':False, 'position':24},
    10 : {'id':10, 'name':"l_hip_y", 'detected':False, 'position':78},
    11 : {'id':11, 'name':"r_knee_y", 'detected':False, 'position':-54},
    12 : {'id':12, 'name':"l_knee_y", 'detected':False, 'position':None},
    13 : {'id':13, 'name':"r_ankle_y", 'detected':False, 'position':-54},
    14 : {'id':14, 'name':"l_ankle_y", 'detected':False, 'position':24},
    15 : {'id':15, 'name':"r_ankle_x", 'detected':False, 'position':8},
    16 : {'id':16, 'name':"l_ankle_x", 'detected':False, 'position':78}}

    return template('monitor.tpl', motors=motors)

@route('/minus')
def minus():
    print("minus")
    print(request)
    return "";

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/incrementServoPosition')
def incrementServoPosition():
    print("incrementServoPosition")
    return "OK"

debug(True)
BaseTemplate.defaults['get_url'] = default_app().get_url  # reference to function, not function call!
run(reloader=True, host="0.0.0.0", port=8066)
