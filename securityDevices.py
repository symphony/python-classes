from enum import Enum


class SecurityDevice:
    def __init__(self, active=False):
        self.active = active

    def reset(self):
        print('Resetting device..')
        self.active = True

    def getDeviceStatus(self):
        print('Active: ', self.active)


class Sensor(SecurityDevice):
    def __init__(self, silent, distance):
        self.silent = silent
        self.distance = distance


class Camera(SecurityDevice):
    def __init__(self, serial, position, type):
        self.serial = serial
        self.position = position
        self.type = type

    def aboutCamera(self):
        print('Serial: ', self.serial,
              'Positon:', self.position.getPosition(),
              '\nCamera Type: ', self.type,)

    class CameraType(Enum): # TODO: fix enum
        a: 1
        b: 2
        c: 3


class Position:
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom

    def getPosition(self):
        return (self.pan, self.tilt, self.zoom)

        # test runner
device1 = SecurityDevice(False)
sensor1 = Sensor(False, 30)
cam1 = Camera('abc-123', Position(10, 11, 12), Camera.CameraType.a)
# sensor1.getDeviceStatus()
sensor1.reset()
sensor1.getDeviceStatus()
cam1.aboutCamera()
