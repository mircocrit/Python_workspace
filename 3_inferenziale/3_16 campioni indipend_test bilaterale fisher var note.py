# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole


n=21
varx=2
m=31
vary=1

alfa=0.05


"""intervallo di fiducia per la varianza 1"""
print('------------------------------------------')
print('1a Intervallo di fiducia di livello α per la varianza x')
print('Varianza x:             {}\t'.format(varx))
print('n-1: {}\t'.format(n-1))

chialfa1=alfa/2
chialfa2=(1-(alfa/2))
print('Alfa/2 x:       {:1.3f}\t'.format(chialfa1))
print('1-Alfa/2 x:     {:1.3f}\t'.format(chialfa2))
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

chi1= chiq[i,j]#alfa/2

if   chialfa2==0.005:    j=0
elif chialfa2==0.010:    j=1
elif chialfa2==0.025:    j=2
elif chialfa2==0.050:    j=3
elif chialfa2==0.950:    j=4
elif chialfa2==0.975:    j=5
elif chialfa2==0.990:    j=6
elif chialfa2==0.995:    j=7

chi2= chiq[i,j]

print ('chiα/2(n-1) x:     {:1.3f}\t'.format(chi1))
print ('chi1-α/2(n-1) x:     {:1.3f}\t'.format(chi2))

Usigmax= ((n-1)*varx)/chi2
Vsigmax=((n-1)*varx)/chi1
print ('Usigma x:     {:1.3f}\t'.format(Usigmax))
print ('Vsigma x:     {:1.3f}\t'.format(Vsigmax))
print('Interv fiducia varianza :             {:1.3f},{:1.3f}\t'.format(Usigmax,Vsigmax))

print('')
"""intervallo di fiducia per la varianza 2"""
print('------------------------------------------')
print('1b Intervallo di fiducia di livello α per la varianza y')
print('Varianza y:             {:1.3f}\t'.format(vary))
print('m-1: {}\t'.format(m-1))

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

print ('chiα/2(m-1):     {:1.3f}\t'.format(chi1))
print ('chi1-α/2(m-1):     {:1.3f}\t'.format(chi2))


Usigmay= ((m-1)*vary)/chi2
Vsigmay=((m-1)*vary)/chi1
print ('Usigma:     {:1.3f}\t'.format(Usigmay))
print ('Vsigma:     {:1.3f}\t'.format(Vsigmay))
print('Interv fiducia varianza :             {:1.3f},{:1.3f}\t'.format(Usigmay,Vsigmay))










print('------------------------------------------')


print('')
print('3 Test bilaterale di Fisher(no varianza) di livello alfa')
Fo=varx/vary
print('Fo:             {}'.format(Fo))
print ('n-1: {}  m-1: {} \t'.format(n-1,m-1))
alfa1=alfa/2

print ('- alfa/2:     {:1.3f}\t'.format(alfa1))

if alfa1==0.025:    
    i=(n-1)-4               #1 indice
    if   (m-1)==15:    j=11 #2 indice
    elif (m-1)==20:    j=12
    elif (m-1)==30:    j=13
    elif (m-1)==60:    j=14
    else:              j=n-1
    j=j-1
    Fisheralfa2=fisher0975[i,j]
    print(('Fisher alfa/2 parziale:    {:1.2f}'.format(Fisheralfa2)))   
    Fisheralfa2=1/Fisheralfa2
print(('Fisher alfa/2:             {:1.2f}\n'.format(Fisheralfa2)))

alfa2=(1-(alfa/2))
print ('- 1-alfa/2:     {:1.3f}\t'.format(alfa2))

if alfa2==0.975:
    i=(m-1)-4  
    if   (n-1)==15:     j=11
    elif (n-1)==20:     j=12
    elif (n-1)==30:     j=13
    elif (n-1)==60:     j=14
    else:               j=n-1
    j=j-1
    Fisher1alfa= fisher0975[i,j]

print(('Fisher 1-alfa/2:             {:1.2f}'.format(Fisher1alfa)))
print('')
if Fo>Fisheralfa2 and Fo<Fisher1alfa : 
      print('accetto Ho')
else: 
    print('rifiuto Ho')



