#!/usr/bin/python

"""

::

	This program loads calibration data from a directory, processes it, and loads it into a connected device
	Not for regular users!
	Maybe dont include this in the main package

"""
from __future__ import print_function
from SEEL_Apps.utilitiesClass import utilitiesClass
from templates import calibration_loader

import numpy as np
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,os,random,struct,time

params = {
'image' : 'sensors.png',
'name':'Calibration\nLoader',
'hint':'A utility to process the calibration data obtained using calibrator utility, and write them to flash. Not for regular users!'

}


class AppWindow(QtGui.QMainWindow, calibration_loader.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.I.__ignoreCalibration__()
		self.hexid = hex(self.I.device_id())
		self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8")+' : '+self.hexid)
		self.plot=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Error -->', units='V',**labelStyle)
		self.plot.setLabel('bottom','Actual Voltage -->', units='V',**labelStyle)
		self.plot.setYRange(-.06,.06)

		self.region = pg.LinearRegionItem([-1.,1.])
		self.region.setZValue(-10)
		self.plot.addItem(self.region)		

		self.opendir = QtGui.QPushButton('open')
		self.opendir.clicked.connect(self.loadDir)
		self.WidgetLayout.addWidget(self.opendir)
		
		self.uploadButton = QtGui.QPushButton('Upload')
		self.uploadButton.clicked.connect(self.uploadCalibration)
		self.WidgetLayout.addWidget(self.uploadButton)
		
		self.results={}
		self.DAC_POLYS=[]
		self.INL_SLOPE=0
		self.INL_INTERCEPT=0
		self.adc_shifts=[]
		self.DAC_FILES=[]
		self.DAC_TABLES=[]
		self.dirname = ''
		self.ADDITIONAL_FILE = 'CAP_PCS.csv'
		
	def addLabel(self,name,color=None):
		item = QtGui.QListWidgetItem()
		if color:
			brush = QtGui.QBrush(color)
			brush.setStyle(QtCore.Qt.SolidPattern)
			item.setBackground(brush)
			brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
			brush.setStyle(QtCore.Qt.SolidPattern)
			item.setForeground(brush)
		item.setText(name)
		self.listWidget.addItem(item)
		return item

	def selected(self,item):
		c=self.cleanCurves.get(str(item),None)
		r=self.rawCurves.get(str(item),None)
		if c and r:
			for a in self.cleanCurves:
				self.cleanCurves[a].curve.opts['shadowPen'] = None
				self.rawCurves[a].opts['shadowPen'] = None

			c.setShadowPen(color=[255,255,255], width=3)
			r.setShadowPen(color=[255,255,255], width=3)
	
	def selectItem(self,item):
		self.listWidget.setCurrentItem(item)
		

	def crop(self):
		text = self.listWidget.currentItem()
		if text:
			start,end=self.region.getRegion()
			fn = str(text.text())
			self.loadADCFile(fn,[start,end])
			print ('Cropping %s within [%.2f,%.2f]'%(fn,start,end))

	def loadADCFile(self,filename,newLimits=[-30,30]):
			print ('Loading ',filename)
			INPUTNAME = filename.split('_')[1]
			GAIN = filename.split('_')[2].split('x')[0]

			data = np.loadtxt('%s/%s'%(self.dirname,filename))
			X=data[:,0];Y=data[:,1];
			source=self.analogInputSource(INPUTNAME)
			source.setGain(int(GAIN))
			X2=[];Y2=[]
			for B in range(len(X)):
				if source.__conservativeInRange__(X[B]) and X[B]>newLimits[0] and X[B]<newLimits[1]:
					X2.append(X[B]);Y2.append(Y[B])
			X=np.array(X2);Y=np.array(Y2)
			RAW = source.voltToCode12(Y)  								#convert back to ADC codes for testing
			avg_shifts=(self.adc_shifts[np.int16(np.floor(RAW))]+self.adc_shifts[np.int16(np.ceil(RAW))])/2. # Find mean shift(in code units) of ADC INL at each code,
			# so it can be removed (Next line) , before calculating slope & intercept for the channel under process
			OFFSET_REMOVED = RAW-4095*(avg_shifts*self.INL_SLOPE - self.INL_INTERCEPT)/3.3  #apply calibration of the ADC. no slope correction yet. 
			#OFFSET_REMOVED = source.calPoly12(OFFSET_REMOVED)	#convert to voltage values
			
			fitvals = np.polyfit(OFFSET_REMOVED[1:],X[1:],3)
			self.results[INPUTNAME][int(GAIN)]=fitvals
			fitfn = np.poly1d(fitvals)
			print (filename,fitvals,fitfn(0),fitfn(4095))

			self.rawCurves[filename].setData(np.array(X),X-Y)
			self.cleanCurves[filename].setData(np.array(X),X-fitfn(OFFSET_REMOVED))	
			#tmpfit = np.polyfit(X[1:],Y[1:],3)
			#tmppoly = np.poly1d(tmpfit)		

	def loadDir(self):
		from os.path import expanduser
		dirname = QtGui.QFileDialog.getExistingDirectory(self,  "Load a calibration folder", expanduser("./%s"%(self.hexid)),  QtGui.QFileDialog.ShowDirsOnly)
		if dirname:
			self.dirname = dirname
			all_files=os.listdir('%s/'%(dirname))
			
			files=[a for a in all_files if 'csv' in a]  #sort out the csv files
			self.DAC_FILES = [a for a in files if 'PV' in a] #extract dac files based on the occurence of PV in the filename
			self.ADC_FILES = [a for a in files if 'CALIB_CH' in a] #extract ADC files based on the occurence of CALIB_CH in the filename
			if self.ADDITIONAL_FILE in files:
				self.CAP_AND_PCS  =  np.loadtxt('%s/%s'%(dirname,self.ADDITIONAL_FILE))
			else:
				self.CAP_AND_PCS = ''

			print (self.ADC_FILES,self.DAC_FILES)

			'''
			First calculate INL errors from the raw data obtained from AN3.
			There will be 4096 data pairs of actual(AD7718) and measured(AN8) values
			stored in CALIB_INL.csv

			process this data to generate an array of 4096 corrections. one for each code of the 12-bit uC ADC.
			The offsets will be stored in one byte each. two extra variables (SLOPE, INTERCEPT stored separately 0) are used for baseline
			correction so that maximum correction resolution can be obtained.

			'''
			try:
				inldata = np.loadtxt('%s/CALIB_INL.csv'%(dirname))
			except:
				QtGui.QMessageBox.about(self,'Unable to find INL calibration file',"Is CALIB_INL.csv present?")

			ADC24=inldata[:,0];ADCINL=inldata[:,1];

			Y2=ADCINL-ADC24
			print (max(Y2),min(Y2),len(ADCINL))
			self.adc_shifts = np.zeros(4096)
			self.INL_INTERCEPT = Y2.min()
			self.INL_SLOPE = (Y2.max()-Y2.min())/255.


			for a in range(len(ADCINL)):
				code = np.int16(4095*(ADCINL[a])/3.3)
				self.adc_shifts[np.clip(code,0,4095)] = np.int16(((Y2[a]-self.INL_INTERCEPT)/self.INL_SLOPE))

			print (min(self.adc_shifts),max(self.adc_shifts))
			for n in range(1,len(self.adc_shifts)-2):
				if self.adc_shifts[n]==0:
					self.adc_shifts[n] = (self.adc_shifts[n+1]+self.adc_shifts[n-1])/2


			self.rawCurves={}
			self.cleanCurves={}

			self.cleanCurves['INL(AN8)']=self.addCurve(self.plot,pen='w',name='Direct ADC. AN8')
			self.cleanCurves['INL(AN8)'].setData(ADC24,ADCINL-ADC24)

			self.rawCurves['INL(AN8)']=self.addCurve(self.plot,pen='w',name='Direct ADC. AN8')
			self.rawCurves['INL(AN8)'].setData(ADC24,ADCINL-ADC24)

			self.addLabel('INL(AN8)',[255,255,255])
			
			inputSources={}
			from SEEL.achan import analogInputSource
			self.analogInputSource = analogInputSource
			self.results={}

			for a in self.ADC_FILES:
				INPUTNAME = a.split('_')[1]
				GAIN = a.split('_')[2].split('x')[0]
				if INPUTNAME not in self.results:
					self.results[INPUTNAME]={}
				col=QtGui.QColor(random.randint(20,255),random.randint(20,255),random.randint(20,255))
				self.cleanCurves[a]=self.addCurve(self.plot,pen=pg.mkPen(col, width=1, style=QtCore.Qt.DashLine),name=INPUTNAME+':'+GAIN+'x')
				self.rawCurves[a]=self.addCurve(self.plot,pen=pg.mkPen(col, width=1))
				item = self.addLabel(a,col)
				self.rawCurves[a].setClickable(True)
				self.rawCurves[a].sigClicked.connect(functools.partial(self.selectItem,item))
				self.loadADCFile(a)

			'''
			Calibrate DAC if file found
			'''
			self.DAC_TABLES={}
			self.DAC_POLYS = {}
			for DAC_FILE in self.DAC_FILES:
				NAME = DAC_FILE[:3]
				col=QtGui.QColor(random.randint(20,255),random.randint(20,255),random.randint(20,255))
				self.cleanCurves[NAME]=self.addCurve(self.plot,pen=pg.mkPen(col, width=1, style=QtCore.Qt.DashLine),name=NAME)
				self.rawCurves[NAME]=self.addCurve(self.plot,pen=col)
				self.addLabel(NAME,col)
				
				#
				DAC_LOOKAHEAD=100;DAC_LOOKBEHIND=100
				dacdata = np.loadtxt('%s/%s'%(dirname,DAC_FILE))
				Ydata=dacdata[:,0]#;Ydata=dacdata[:,1];

				CHAN = self.I.DAC.CHANS[DAC_FILE.split('_')[0]]
				X= np.linspace(CHAN.range[0],CHAN.range[1],4096)
				
				fitvals = np.polyfit(X,Ydata,3)
				fitfn = np.poly1d(fitvals)
				print(NAME,fitvals,fitfn(0),fitfn(4095))

				self.rawCurves[NAME].setData(np.array(X),X-Ydata)
				#OFF=[np.argmin(np.fabs(Ydata[max(a-DAC_LOOKBEHIND,0):min(4095,a+DAC_LOOKAHEAD)]-X[a]) )- (a-max(a-DAC_LOOKBEHIND,0)) for a in range(0,4096)]
				#
				DIFF = (fitfn(X)-Ydata)
				intercept = DIFF.min()
				slope = (DIFF.max()-DIFF.min())/255.

				OFF = np.int16((( DIFF-intercept)/slope)) # compress the errors into an unsigned BYTE each
				
				print (min(OFF),max(OFF),len(OFF))
				#OFF=np.array(OFF)+127
				#X=[(int(OFF[n])&0xF)|(int(OFF[n+1])<<4) for n in range(len(OFF)/2)]
				#S.write_bulk_flash(10+DAC_CHAN,X)
				X2=np.linspace(0,4095,4096)
				

				self.cleanCurves[NAME].setData(np.linspace(CHAN.range[0],CHAN.range[1],4096),fitfn(CHAN.CodeToV(X2))-(OFF*slope+intercept)-Ydata)
				self.DAC_TABLES[DAC_FILE]=OFF  #offset
				self.DAC_POLYS [DAC_FILE]=[slope,intercept,fitvals[0],fitvals[1],fitvals[2],fitvals[3]]
				print ('fitvals',fitvals)

			print('Capacitance and current source : ' ,self.CAP_AND_PCS)
			#print ([int(x) for x in self.adc_shifts])

	def stoa(self,s):
		return [ord(a) for a in s]
	def atos(self,a):
		return ''.join(chr(e) for e in a)

	def uploadCalibration(self):
		final_fitstr=self.stoa('SEELablet SLOPES and OFFSETS\nCSpark Research\n')
		for channel in self.results:
			keys=np.sort(self.results[channel].keys())
			final_fitstr+=self.stoa('>|'+channel+'|<')
			for b in keys:
				fitstr=struct.pack('4f',*self.results[channel][b])
				print (channel,b,self.results[channel][b],len(fitstr),fitstr)
				print (':',struct.unpack('4f',fitstr))
				print ([ord(a) for a in fitstr])
				final_fitstr+=self.stoa(fitstr)

		final_fitstr+=self.stoa('STOP')
		for a in self.DAC_POLYS:
			print ('############',self.atos(final_fitstr),len(final_fitstr))
			l1 = len(final_fitstr)
			final_fitstr+=self.stoa('>|'+a[:3]+'|<')
			fitstr=struct.pack('6f',*self.DAC_POLYS[a])
			final_fitstr+=self.stoa(fitstr)
			print ('############',self.atos(final_fitstr),len(final_fitstr), len(final_fitstr)-l1)

		print ('########---------------------#########',self.atos(final_fitstr))
		final_fitstr+=self.stoa('STOP')
		final_fitstr+=self.stoa(struct.pack('2f',self.INL_SLOPE,self.INL_INTERCEPT))
		final_fitstr+=self.stoa('STOP')
		if len(self.CAP_AND_PCS)==4:final_fitstr+=self.stoa(struct.pack('4f',*self.CAP_AND_PCS))
		final_fitstr+=self.stoa('STOP')

		self.adc_shifts=[int(a) for a in self.adc_shifts]  #Convert to regular list
		print('Writing adc shifts to Flash.....(first half)')
		self.I.write_bulk_flash(self.I.ADC_SHIFTS_LOCATION1,self.adc_shifts[:2048])

		print( 'Writing adc shifts to Flash.....(second half)')
		self.I.write_bulk_flash(self.I.ADC_SHIFTS_LOCATION2,self.adc_shifts[2048:])

		print('Writing adc slopes and offsets to Flash.....'+str(len(final_fitstr)))
		self.I.write_bulk_flash(self.I.ADC_POLYNOMIALS_LOCATION,final_fitstr)
		
		for FILE in self.DAC_FILES:
			name = FILE[:3]
			print ('Writing DAC offsets and tables....',name)
			if name == 'PV1':
				LOCA= self.I.DAC_SHIFTS_PV1A;LOCB= self.I.DAC_SHIFTS_PV1B;
			elif name == 'PV2':
				LOCA= self.I.DAC_SHIFTS_PV2A;LOCB= self.I.DAC_SHIFTS_PV2B;
			elif name == 'PV3':
				LOCA= self.I.DAC_SHIFTS_PV3A;LOCB= self.I.DAC_SHIFTS_PV3B;
			else:
				print ('unknown DAC file',FILE)
				continue
			TABLE = self.atos( self.DAC_TABLES[FILE] )
			print('DAC WRITING',name,LOCA,LOCB,TABLE[:50])
			print('Writing DAC shifts to Flash.....(first half)')
			self.I.write_bulk_flash(LOCA,TABLE[:2048])
			print('Writing DAC shifts to Flash.....(second half)')
			self.I.write_bulk_flash(LOCB,TABLE[2048:])
		
		self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8")+' : FINISHED CALIBRATION WRITE')
		

	def __del__(self):
		print('bye')

if __name__ == "__main__":
    from SEEL import interface
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=interface.connect(load_calibration=False))
    myapp.show()
    sys.exit(app.exec_())

