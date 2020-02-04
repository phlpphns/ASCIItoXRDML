#!/usr/bin/python3

#
#   ASCSynchMythen_toXRDML.py
#

import numpy
import sys
import datetime
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


waveLength   = sys.argv[1]
#waveLength   = 0.826060 # sys.argv[1]
timePerPoint = 1


skipLinesStart = 0#17
skipLinesEnd   = 0
for fileName in sys.argv[2:]:
    thetas = numpy.genfromtxt(fileName, dtype=float, skip_header=skipLinesStart, skip_footzer=skipLinesEnd, usecols=(0),comments='#')
    intensities_raw = numpy.genfromtxt(fileName, dtype=float, skip_header=skipLinesStart, skip_footer=skipLinesEnd, usecols=(1),comments='#')
    startPosition = thetas[0]
    endPosition =   thetas[-1]
    stepSize = abs(startPosition-endPosition)/(len(thetas)-1)/40
    f = interp1d(thetas, intensities_raw, kind='slinear')
    x_new = numpy.arange(startPosition, endPosition, stepSize)
    #x_new = numpy.linspace(startPosition, endPosition, num=len(thetas), endpoint=True)
    intensities = f(x_new)
    plt.plot(thetas, intensities_raw, label="raw")
    plt.plot(x_new, intensities, label="inter")
    plt.legend()
    plt.show()

    print(stepSize)
    print(thetas)
    print(x_new)
    print(len(thetas))
    print(len(x_new))

    print('processing:   ',fileName,'      range in 2theta:   ',startPosition,' - ',endPosition, sep =' ')
    print('saving file as %sxrdml' % fileName.strip(fileName.split(sep='.')[-1]))
    with open("%sxrdml" % fileName.strip(fileName.split(sep='.')[-1]), 'w') as file:
        print('<?xml version="1.0" encoding="UTF-8"?>', file=file)
        print('<xrdMeasurements xmlns="http://www.xrdml.com/XRDMeasurement/1.3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.xrdml.com/XRDMeasurement/1.3 http://www.xrdml.com/XRDMeasurement/1.3/XRDMeasurement.xsd" status="Completed">', file=file)
        
        print('        <comment>', file=file)
        print('		<entry>Configuration=SynchrotronMeasurement - Mythen</entry>', file=file)
        print('		<entry>Goniometer=PW3050/60 (Theta/Theta); Minimum step size 2Theta:0.001; Minimum step size Omega:0.001</entry>', file=file)
        print('		<entry>Sample stage=Capillary</entry>', file=file)
        print('		<entry>Diffractometer system=Diamond Beamline I11</entry>', file=file)
        print('		<entry>Measurement program=Hans_XCEL_5_136_30min_rot, Owner=Hans, Creation date=21.04.2015 20:53:27</entry>', file=file)
        print('        </comment>', file=file)
        
        print('        <sample type="To be analyzed">', file=file)
        print('                <id>',fileName.split(sep='.')[0],'</id>', sep='',  file=file)
        print('                <name>',fileName.split(sep='.')[0],'</name>', sep='', file=file)
        print('                <preparedBy>Nevzat Yigit and Philipp Hans</preparedBy>', file=file)
        print('        </sample>', file=file)
        
        print('        <xrdMeasurement measurementType="Scan" status="Completed" sampleMode="Reflection">', file=file)
        print('                <comment>', file=file)
        print('                        <entry/>', file=file)
        print('                </comment>', file=file)
        print('                <usedWavelength intended="K-Alpha 1">', file=file)
        print('                        <kAlpha1 unit="Angstrom">',waveLength,'</kAlpha1>', sep='', file=file)
        print('                        <kAlpha2 unit="Angstrom">',waveLength,'</kAlpha2>', sep='', file=file)
        print('                        <kBeta unit="Angstrom">',waveLength,'</kBeta>', sep='', file=file)
        print('                        <ratioKAlpha2KAlpha1>1.0000</ratioKAlpha2KAlpha1>', file=file)
        print('                </usedWavelength>', file=file)
        
        print('                <incidentBeamPath>', file=file)
        print('                        <radius unit="mm">200.00</radius>', file=file)
#        print('                        <xRayTube id="1010041" name="Diamond Synchrotron Radiation">', file=file)
#        print('                                <tension unit="kV">40</tension>', file=file)
#        print('                                <current unit="mA">40</current>', file=file)
#        print('                                <anodeMaterial>Eu</anodeMaterial>', file=file)
#        print('                                <focus type="Line">', file=file)
#        print('                                        <length unit="mm">1.0</length>', file=file)
#        print('                                        <width unit="mm">1.4</width>', file=file)
#        print('                                        <takeOffAngle unit="deg">6.0</takeOffAngle>', file=file)
#        print('                                </focus>', file=file)
#        print('                        </xRayTube>', file=file)
#        print('                        <sollerSlit id="21010002" name="Soller 0.001 rad.">', file=file)
#        print('                                <opening unit="rad">0.001</opening>', file=file)
#        print('                        </sollerSlit>', file=file)
#        print('                        <mask id="22080002" name="no mask">', file=file)
#        print('                                <distanceToSample unit="mm">140.00</distanceToSample>', file=file)
#        print('                                <width unit="mm">6.60</width>', file=file)
#        print('                        </mask>', file=file)
#        print('                        <antiScatterSlit id="22010003" name="no slit°" xsi:type="fixedAntiScatterSlitType">', file=file)
#        print('                                <height unit="mm">1.52</height>', file=file)
#        print('                        </antiScatterSlit>', file=file)
#        print('                        <divergenceSlit id="22010012" name="none">', file=file)
#        print('                                <distanceToSample unit="mm">100.00</distanceToSample>', file=file)
#        print('                                <angle unit="deg">0.5</angle>', file=file)
#        print('                        </divergenceSlit>', file=file)
        print('                </incidentBeamPath>', file=file)
        
#        print('                <sampleMovement xsi:type="spinningSampleMovementType">', file=file)
#        print('                        <spinnerRevolutionTime unit="seconds">4.0</spinnerRevolutionTime>', file=file)
#        print('                </sampleMovement>', file=file)
        
        print('                <diffractedBeamPath>', file=file)
        print('				<radius unit="mm">240.00</radius>', file=file)
#    print('			<antiScatterSlit id="22060009" name="Programmable anti-scatter slit" xsi:type="fixedAntiScatterSlitType">
#    print('				<height unit="mm">2.00</height>
#    print('			</antiScatterSlit>
#    print('			<sollerSlit id="21010002" name="Soller slits 0.04 rad.">
#    print('				<opening unit="rad">0.0400</opening>
#    print('			</sollerSlit>
#    print('			<filter id="20010006" name="Beta-filter Rhodium">
#    print('				<material>Rh</material>
#    print('				<thickness unit="mm">0.050</thickness>
#    print('			</filter>
#    print('			<receivingSlit id="22020009" name="Programmable receiving slit">
#    print('				<height unit="mm">2.00</height>
#    print('			</receivingSlit>

        print('			<detector id="7010002" name="Scintillation detector" xsi:type="pointDetectorType">', file=file)
        print('				<phd>', file=file)
        print('					<lowerLevel unit="%">36.0</lowerLevel>', file=file)
        print('					<upperLevel unit="%">81.0</upperLevel>', file=file)
        print('				</phd>', file=file)
        print('			</detector>', file=file)
        print('                </diffractedBeamPath>', file=file)
        
        print('                <scan appendNumber="0" mode="Continuous" scanAxis="Gonio" status="Completed">', file=file)
        print('                        <header>', file=file)
        print('                                <startTimeStamp>',datetime.datetime.now(),'</startTimeStamp>', sep='', file=file)
        print('                                <endTimeStamp>',datetime.datetime.now(),'</endTimeStamp>', sep='', file=file)
        print('                                <author>', file=file)
        print('                                        <name>pulver</name>', file=file)
        print('                                </author>', file=file)
        print('                                <source>', file=file)
        print('                                        <applicationSoftware version="1">Diamond</applicationSoftware>', file=file)
        print('                                        <instrumentControlSoftware version="1">Diamond</instrumentControlSoftware>', file=file)
        print('                                        <instrumentID>1</instrumentID>', file=file)
        print('                                </source>', file=file)
        print('                        </header>', file=file)
        print('                        <dataPoints>', file=file)
        print('                                <positions axis="2Theta" unit="deg">', file=file)
        print('                                        <startPosition>',startPosition,'</startPosition>', sep='', file=file)
        print('                                        <endPosition>',endPosition,'</endPosition>', sep='', file=file)
        print('                                </positions>', file=file)
        print('                                <positions axis="Omega" unit="deg">', file=file)
        print('                                        <commonPosition>0.0000</commonPosition>', file=file)
        print('                                </positions>', file=file)
        print('                                <commonCountingTime unit="seconds">',timePerPoint,'</commonCountingTime>', sep='', file=file)
        print('                                <intensities unit="counts">', end='', file=file)
##############################################################################################################################################
        for intensity in intensities:
            print('%.2f'%intensity, sep=' ', end=' ', file=file)
##############################################################################################################################################
        print('</intensities>', file=file)
        print('                        </dataPoints>', file=file)
        print('                </scan>', file=file)
        print('        </xrdMeasurement>', file=file)
        print('</xrdMeasurements>', file=file)
        
#    plt.plot(x_new, intensities)
"""        plt.xlabel('2 theta')
        plt.ylabel('Intensities')
        plt.title('Diffractogramme')
        plt.grid(True)a
"""
#    plt.show()
