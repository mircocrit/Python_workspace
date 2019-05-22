# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per var""
"""""
import numpy as np
import tavole



arrx=np.array([4.83,-2.52,-1.79,-2.85,1.45,1.09,1.87,2.03,-2.60])
arry=np.array([-1.34,1.32,-0.96,0.29,-1.41,0.23,-0.56,-0.32,0.66,1.27])
n=len(arrx)
m=len(arry)
alfa=0.05

"""1_mediax """
i=0
buf=0
sum=0
while i<n:
    sum+=arrx[i]
    i=i+1
    if i%10==0:         
        print(sum-buf)
        buf=sum
print('sum:{:1.4f}\t'.format(sum))
medx=(1/n)*sum
print('Media x:                {:1.3f}\t'.format(medx))


"""1_mediay """
i=0
buf=0
sum=0
while i<m:
    sum+=arry[i]
    i=i+1
    if i%10==0:         
        print(sum-buf)
        buf=sum
print('sum:{:1.4f}\t'.format(sum))
medy=(1/m)*sum
print('Media y:                {:1.3f}\t'.format(medy))


"""2_media con i quadrati_x"""
i=0
sumq=0
buf=0
while i<n:
    sumq+=arrx[i]**2
    i=i+1
    if i%10==0:         
        print(sumq-buf)
        buf=sumq
sumqx=(1/n)*sumq

print('Media con quadrati x:      {:1.3f}\t'.format(sumqx))

"""2_media con i quadrati_y"""
i=0
sumq=0
buf=0
while i<m:
    sumq+=arry[i]**2
    i=i+1
    if i%10==0:         
        print(sumq-buf)
        buf=sumq
sumqy=(1/m)*sumq

print('Media con quadrati y:      {:1.3f}\t'.format(sumqy))

print('')

varx=sumqx-(medx**2)
print('Varianza x :             {:1.3f}\t'.format(varx))
vary=sumqy-(medy**2)
print('Varianza y :             {:1.3f}\t'.format(vary))


print('')
varcx=(n/(n-1))*(varx)
print('Varianza campionaria x:             {:1.3f}\t'.format(varcx))

varcy=(m/(m-1))*(vary)
print('Varianza campionaria y:             {:1.3f}\t'.format(varcy))

"""intervallo di fiducia per la varianza 1"""
print('------------------------------------------')
print('Intervallo di fiducia di livello α per la varianza x')
print('Varianza x:             {:1.3f}\t'.format(varx))
print('n-1: {}\t'.format(n-1))
chialfa1=alfa/2
chialfa2=(1-(alfa/2))
print('Alfa/2 x:       {:1.3f}\t'.format(chialfa1))
print('1-Alfa/2 x:     {:1.3f}\t'.format(chialfa2))
print('')

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

print ('chi1-α/2 x:     {:1.3f}\t'.format(chi2))
print ('chiα/2 x:     {:1.3f}\t'.format(chi1))
Usigmax= ((n-1)*varcx)/chi1
Vsigmax=((n-1)*varcx)/chi2
print ('Usigma x:     {:1.3f}\t'.format(Usigmax))
print ('Vsigma x:     {:1.3f}\t'.format(Vsigmax))
print('Interv fiducia varianza :             {:1.3f},{:1.3f}\t'.format(Vsigmax,Usigmax))


"""intervallo di fiducia per la varianza 2"""
print('------------------------------------------')
print('2 Intervallo di fiducia di livello α per la varianza y')
print('Varianza y:             {:1.3f}\t'.format(vary))
print('n-1: {}\t'.format(m-1))
chialfa1=alfa/2
chialfa2=(1-(alfa/2))
print('Alfa/2:       {:1.3f}\t'.format(chialfa1))
print('1-Alfa/2:     {:1.3f}\t'.format(chialfa2))
print('------------------------------------------')

i=m-2
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
Usigmay= ((m-1)*varcy)/chi1
Vsigmay=((m-1)*varcy)/chi2
print ('Usigma:     {:1.3f}\t'.format(Usigmay))
print ('Vsigma:     {:1.3f}\t'.format(Vsigmay))
print('Interv fiducia varianza :             {:1.3f},{:1.3f}\t'.format(Vsigmay,Usigmay))





print('------------------------------------------')
print('')


print('3 Test unilaterale di Fisher(no varianza) di livello alfa')
Fo=varcx/varcy
print('Fo:             {:1.3f}'.format(Fo))
print('')
print ('n-1: {}  m-1: {} \t'.format(n-1,m-1))
alfa1=1-alfa

print ('1-alfa:     {:1.3f}\t'.format(alfa1))

if alfa1==0.950:    
    i=(m-1)-3   #1 indice
    if   (n-1)==15:    j=11 #2 indice
    elif (n-1)==20:    j=12
    elif (n-1)==30:    j=13
    elif (n-1)==60:    j=14
    else:              j=n-1
    j=j-1
    Fisheralfa=fisher0950[i,j]
    print(('Fisher 1-alfa(n-1,m-1):             {:1.2f}\n'.format(Fisheralfa)))   

if Fo>Fisheralfa : 
      print('accetto Ho')
else: 
    print('rifiuto Ho')



