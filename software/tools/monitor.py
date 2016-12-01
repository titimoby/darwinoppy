#from bottle import route, run, debug, template, get_url
from bottle import *
import pypot.dynamixel
import time

@route('/ports')
def port_list():
    return pypot.dynamixel.get_available_ports()

@route('/')
def motor_list():
    motors = {1 : {'id':1, 'name':"a", 'detected':False, 'position':None},
    2 : {'id':2, 'name':"a", 'detected':False, 'position':None},
    3 : {'id':3, 'name':"a", 'detected':False, 'position':None},
    4 : {'id':4, 'name':"a", 'detected':False, 'position':None},
    5 : {'id':5, 'name':"a", 'detected':False, 'position':None},
    6 : {'id':6, 'name':"a", 'detected':False, 'position':None},
    7 : {'id':7, 'name':"a", 'detected':False, 'position':None},
    8 : {'id':8, 'name':"a", 'detected':False, 'position':None},
    9 : {'id':9, 'name':"a", 'detected':False, 'position':None},
    10 : {'id':10, 'name':"a", 'detected':False, 'position':None},
    11 : {'id':11, 'name':"a", 'detected':False, 'position':None},
    12 : {'id':12, 'name':"a", 'detected':False, 'position':None},
    13 : {'id':13, 'name':"a", 'detected':False, 'position':None},
    14 : {'id':14, 'name':"a", 'detected':False, 'position':None},
    15 : {'id':15, 'name':"a", 'detected':False, 'position':None},
    16 : {'id':16, 'name':"a", 'detected':False, 'position':None}}
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
    motors = {1 : {'id':1, 'name':"a", 'detected':False, 'position':12},
    2 : {'id':2, 'name':"a", 'detected':False, 'position':25},
    3 : {'id':3, 'name':"a", 'detected':False, 'position':38},
    4 : {'id':4, 'name':"a", 'detected':False, 'position':52},
    5 : {'id':5, 'name':"a", 'detected':False, 'position':44},
    6 : {'id':6, 'name':"a", 'detected':False, 'position':10},
    7 : {'id':7, 'name':"a", 'detected':False, 'position':25},
    8 : {'id':8, 'name':"a", 'detected':False, 'position':4},
    9 : {'id':9, 'name':"a", 'detected':False, 'position':-50},
    10 : {'id':10, 'name':"a", 'detected':False, 'position':-12},
    11 : {'id':11, 'name':"a", 'detected':False, 'position':0},
    12 : {'id':12, 'name':"a", 'detected':False, 'position':32},
    13 : {'id':13, 'name':"a", 'detected':False, 'position':-8},
    14 : {'id':14, 'name':"a", 'detected':False, 'position':None},
    15 : {'id':15, 'name':"a", 'detected':False, 'position':2},
    16 : {'id':16, 'name':"a", 'detected':False, 'position':-3}}

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
