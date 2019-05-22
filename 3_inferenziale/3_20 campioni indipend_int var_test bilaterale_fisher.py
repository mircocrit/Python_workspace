# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole


arrx=np.array([1.13,0.11,0.74,0.97,0.10,1.14,0.68,0.21,0.70,0.41,
               0.82,0.04,0.85,0.85,0.84,0.11,0.55,0.09,1.01,0.34,
              1.04])
arry=np.array([0.85,0.62,0.21,0.22,0.34,0.13,0.93,0.38,0.01,0.65,
               0.97,0.79,0.42,0.09,0.44,0.31])
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
#print('Varianza x :             {:1.3f}\t'.format(varx))
vary=sumqy-(medy**2)
#print('Varianza y :             {:1.3f}\t'.format(vary))


print('')
varcx=(n/(n-1))*(varx)
print('Varianza campionaria x:             {:1.3f}\t'.format(varcx))

varcy=(m/(m-1))*(vary)
print('Varianza campionaria y:             {:1.3f}\t'.format(varcy))


"""intervallo di fiducia per la varianza sigmax"""
print('------------------------------------------')
print('Intervallo di fiducia di livello α per la varianza x')
print('Varianza x:             {:1.3f}\t'.format(varcx))
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
print('Interv fiducia varianza :             {:1.2f},{:1.2f}\t'.format(Vsigmax,Usigmax))

print('')
"""intervallo di fiducia per la varianza sigmay"""
print('------------------------------------------')
print('2 Intervallo di fiducia di livello α per la varianza y')
print('Varianza y:             {:1.3f}\t'.format(varcy))
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
print('Interv fiducia varianza :             {:1.2f},{:1.2f}\t'.format(Vsigmay,Usigmay))




print('')
print('------------------------------------------')
print('3 Test bilaterale di Fisher(no varianza) di livello alfa')
Fo=varcx/varcy
print('Fo:             {:1.2f}'.format(Fo))
print ('n-1: {}  m-1: {} \t'.format(n-1,m-1))
alfa1=alfa/2

print ('alfa1:     {:1.3f}\t'.format(alfa1))

if alfa1==0.025:    
    i=(n-1)-4               #1 indice
    if   (m-1)==15:    j=11 #2 indice
    elif (m-1)==20:    j=12
    elif (m-1)==30:    j=13
    elif (m-1)==60:    j=14
    else:              j=n-1
    j=j-1
    Fisheralfa2=fisher0975[i,j]
    print(('Fisher alfa/2 parziale:             {:1.3f}\n'.format(Fisheralfa2)))   
    Fisheralfa2=1/Fisheralfa2
print(('Fisher alfa/2:             {:1.2f}\n'.format(Fisheralfa2)))

alfa2=(1-(alfa/2))
print ('alfa2:     {:1.3f}\t'.format(alfa2))

if alfa2==0.975:
    i=(m-1)-4  
    if   (n-1)==15:     j=11
    elif (n-1)==20:     j=12
    elif (n-1)==30:     j=13
    elif (n-1)==60:     j=14
    else:               j=n-1
    j=j-1
    Fisher1alfa= fisher0975[i,j]

print(('Fisher 1-alfa/2:             {}'.format(Fisher1alfa)))
if Fo>Fisheralfa2 and Fo<Fisher1alfa : 
      print('accetto Ho')
else: 
    print('rifiuto Ho')



