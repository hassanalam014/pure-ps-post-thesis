# Date: April 2017
#
# Description: The purpose of this file is to plot PMMA density information based on experiment and theory for comparison.
#

import os,sys,math,matplotlib.pyplot as plt,numpy as npy
from matplotlib.ticker import AutoMinorLocator
from all_p_params import *
from loadExperimentalData import *
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from loadPhysicalConstants import *
from findVectors import findVectors
from calculatePureVariables import calculateNewMolecularParameters,calculateCharacteristicParametersGamma
from wrapperFunctions import calculatePressure,calculateTemperature,calculateDensity

#Setting which set of parameters to use for calculation.
param_set = 'Data4'

if param_set == 'Data1':
	Pstar = Pstar_1
	Tstar = Tstar_1
	Rstar = Rstar_1
	# temp = ['303','312','321','332','343','354','364','373','383','393','402','412','422','432','442','452','463','473','482','492','503','513','524']
	temp = ['402','412','422','432','442','452','463','473','482','492','503','513','524']

elif param_set == 'Data2':
	Pstar = Pstar_2
	Tstar = Tstar_2
	Rstar = Rstar_2
	temp = ['383','393','403','413','423','433','443','453','463','473','483','493','503','513','523']

elif param_set == 'Data3':
	Pstar = Pstar_3
	Tstar = Tstar_3
	Rstar = Rstar_3
	temp = ['453','473','493']

elif param_set == 'Data4':
	Pstar = Pstar_4
	Tstar = Tstar_4
	Rstar = Rstar_4
	temp = ['378','383','388','393','398','403','408','413','418','423','428','433','438','443','448','453']
	# temp = ['378','383','388','393','398','403','408','413','418','423','428','433','438','443','448','453']

P_exp_min = min(P0)
P_exp_max = max(P0)
T_exp_min = min(T0)
T_exp_max = max(T0)
R_exp_min = min(R0)
R_exp_max = max(R0)

#Initializing the array of densities.
R0 = npy.linspace(0.01,0.99*Rstar,300)

gamma,vh,epsilon = calculateNewMolecularParameters(Pstar,Tstar,Rstar,M0[0])
vh = vh/NA
epsilon = epsilon/NA
print('The molecular parameters are: gamma = {}, vh = {}, and epsilon = {}.'.format(gamma,vh,epsilon))

Pmin = min(P0)
Pmax = max(P0)
Tmin = min(T0)
Tmax = max(T0)

print('The pressure range is {}-{}MPa and the temperature range is {}-{}K.'.format(Pmin,Pmax,Tmin,Tmax))

#==============================================================================================================
#Calculating Isotherms.
#==============================================================================================================

for i in range(0,len(temp)):
	exec "result = calculatePressure(T0_%sK[0],R0,M0_%sK[0],Pstar=Pstar,Tstar=Tstar,Rstar=Rstar)" % (temp[i],temp[i])
	exec "T%sK_P = result[0]" % (temp[i])
	# exec "vector_%sK = findVectors(T%sK_P,R0,P0_%sK,R0_%sK)" % (temp[i],temp[i],temp[i],temp[i])

#Below is only at EXP Points.
# for i in range(0,len(temp)):
# 	exec "result = calculatePressure(T0_%sK[0],R0_%sK,M0_%sK[0],Pstar=Pstar,Tstar=Tstar,Rstar=Rstar)" % (temp[i],temp[i],temp[i])
# 	exec "T%sK_P = result[0]" % (temp[i])
# 	# exec "vector_%sK = findVectors(T%sK_P,R0,P0_%sK,R0_%sK)" % (temp[i],temp[i],temp[i],temp[i])

# T493_P,R0 = calculatePressure(493.3,R0,M0[0],Pstar=Pstar,Tstar=Tstar,Rstar=Rstar)

#Setting font size
axis_size = 20
title_size = 20
size = 14
label_size = 20
plt.rcParams['xtick.labelsize'] = label_size
plt.rcParams['ytick.labelsize'] = label_size

#Setting saved image properties
img_extension = '.png'
img_dpi = None
output_folder = 'plot_density'

#Checking for existence of output directory. If such a directory doesn't exist, one is created.
if not os.path.exists('./'+output_folder):
    os.makedirs('./'+output_folder)

#Defining linetype
line_style = ['-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':']
dot_style= ['ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk']

#General line properties.
linewidth = 3
markersize = 8


arrow_ls = 'dashdot'
show_arrows = True

#==================================================================================
#P versus R plots.
figPUREPMMA=plt.figure(num=None, figsize=(12, 10), dpi=img_dpi, facecolor='w', edgecolor='k')
ax = plt.axes()

for i in range(0,len(temp)):
	exec "plt.plot(T%sK_P,R0,'k',lw=linewidth,ls='%s',label='%sK theory')" % (temp[i],line_style[i],temp[i])
	exec "plt.plot(P0_%sK,R0_%sK,'%s',ms=markersize,label='%sK experiment')" % (temp[i],temp[i],dot_style[i],temp[i])

# #Below is only at EXP Points
# for i in range(0,len(temp)):
# 	exec "plt.plot(T%sK_P,R0_%sK,'k',lw=linewidth,ls='%s',label='%sK theory')" % (temp[i],temp[i],line_style[i],temp[i])
# 	exec "plt.plot(P0_%sK,R0_%sK,'%s',ms=markersize,label='%sK experiment')" % (temp[i],temp[i],dot_style[i],temp[i])

# plt.plot(T2_P,R0,'k',lw=linewidth,ls=T2_line,label='T2 theory')
# plt.plot(T3_P,R0,'k',lw=linewidth,ls=T3_line,label='T3 theory')

# plt.plot(P0_T2,R0_T2,'^k',ms=markersize,label='T2 experiment')
# plt.plot(P0_T3,R0_T3,'sk',ms=markersize,label='T3 experiment')

plt.xlabel('Pressure P (MPa)',fontsize=axis_size)
plt.ylabel(r'Density $\rho$ ($g/cm^3$)',fontsize=axis_size)
plt.axis([0.80*P_exp_min,1.15*P_exp_max,0.98*R_exp_min,1.02*R_exp_max])
plt.legend(loc=4,fontsize=size,numpoints=1)

#minorLocator = AutoMinorLocator()
#ax.xaxis.set_minor_locator(minorLocator)
#plt.tick_params(which='both', width=1)
#plt.tick_params(which='major', length=7)
#plt.tick_params(which='minor', length=4)
#minorLocator = AutoMinorLocator()
#ax.yaxis.set_minor_locator(minorLocator)
#plt.tick_params(which='both', width=1)
#plt.tick_params(which='major', length=7)
#plt.tick_params(which='minor', length=4)

figPUREPMMA.savefig('./'+output_folder+r'\pure_PMMA_density'+img_extension,dpi=img_dpi)

plt.show()
