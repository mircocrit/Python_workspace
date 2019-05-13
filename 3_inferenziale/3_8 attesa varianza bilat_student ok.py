# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

arr=np.array([2.02,-0.87,-1.68,-1.39,-0.05,-2.69,3.14,-2.46,-0.05,1.83])
n=len(arr)
alfa=0.05

print('1 Intervallo di fiducia di livello α per la media')
"""1_media """
i=0
sum=0
while i<n:
    sum+=arr[i]
    i=i+1
med=(1/n)*sum
print('Media:                {:1.3f}\t'.format(med))

"""2_media con i quadrati"""
i=0
sumq=0
while i<n:
    sumq+=arr[i]**2
    i=i+1
sumq=(1/n)*sumq
print('Media con quadrati:      {:1.3f}\t'.format(sumq))
print('Media al quadrato:             {:1.3f}\t'.format(med**2))
varc=(n/(n-1))*(sumq-(med**2))
print('Varianza campionaria:             {:1.3f}\t'.format(varc))


"""3_deviazione standard"""
devstdd=np.sqrt(varc)
print('Deviazione standard camp:     {:1.3f}\t'.format(devstdd))
print('')
"""4_Student"""
studalfa=1-(alfa/2)
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n-1))
i=n-2
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3

student= studen[i,j]
print('student:     {:1.5f}  \t'.format(student))

"""5_delta"""
delta=((devstdd)/(np.sqrt(n)))*student
print('Delta:      {:1.3f}\t'.format(delta))
print('Intervallo:      {:1.3f} +/- {:1.3f} \t'.format(med,delta))


"""intervallo di fiducia per la varianza"""
print('------------------------------------------')
print('2 Intervallo di fiducia di livello α per la varianza')
print('Varianza campionaria:             {:1.3f}\t'.format(varc))
print('n-1: {}\t'.format(n-1))
chialfa1=alfa/2
chialfa2=(1-(alfa/2))
print('Alfa/2:       {:1.3f}\t'.format(chialfa1))
print('1-Alfa/2:     {:1.3f}\t'.format(chialfa2))
print('------------------------------------------')

i=n-2
if   chialfa1==0.005:    j=0
elif chialfa1==0.010:    j=1
elif chialfa1==0.025:    j=2
elif chialfa1==0.050:    j=3
elif chialfa1==0.950:    j=4
elif chialfa1==0.975:    j=5
elif chialfa1==0.990:    j=6
elif chialfa1==0.995:    j=7

chi1= chiq[i,j]

if   chialfa2==0.005:    j=0
elif chialfa2==0.010:    j=1
elif chialfa2==0.025:    j=2
elif chialfa2==0.050:    j=3
elif chialfa2==0.950:    j=4
elif chialfa2==0.975:    j=5
elif chialfa2==0.990:    j=6
elif chialfa2==0.995:    j=7

chi2= chiq[i,j]

print ('chi1-α/2:     {:1.3f}\t'.format(chi2))
print ('chiα/2:     {:1.3f}\t'.format(chi1))
Usigma= ((n-1)*varc)/chi1
Vsigma=((n-1)*varc)/chi2
print ('Usigma:     {:1.3f}\t'.format(Usigma))
print ('Vsigma:     {:1.3f}\t'.format(Vsigma))
print('Interv fiducia varianza :             {:1.3f},{:1.3f}\t'.format(Usigma,Vsigma))

print('------------------------------------------')

print('3 Test bilaterale di student(no varianza) di livello alfa')
med_o=0
print('uo:             {}'.format(med_o))
To=((med-med_o)/devstdd)*np.sqrt(n)
print('|To|:                     {:1.3f}  \t'.format(np.abs(To)))
print('quantile normale gauss: {:1.3f}  \t'.format(student))

if np.abs(To)<student: 
      print('accetto Ho')
else: 
    print('rifiuto Ho')

"""3__calcolabilita test alfa di s"""


