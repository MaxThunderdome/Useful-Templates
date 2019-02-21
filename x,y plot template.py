import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot(111)
tau = 5.0
t = np.arange(0.0, 25.0, 0.01)
s = (1/tau)*np.exp(-t/tau)
line, = plt.plot(t, s, lw=2,color="blue")
SecondLineX=[0,0]
SecondLineY=[0,0.2]
ThirdLineX=[-5,0]
ThirdLineY=[0,0]
plt.plot(SecondLineX,SecondLineY,lw=2,color="blue")
plt.plot(ThirdLineX,ThirdLineY,lw=2,color="blue")
plt.annotate('fluorescence decay curve', xy=(5,0.075), xytext=(10,0.075),
arrowprops=dict(facecolor='black', shrink=0.05),
)
plt.ylabel("f(t)")
plt.xlabel("t(ns)")
plt.text(6,0.175,r'$\tau$ = 5')
plt.title("5 nsec fluorescence decay")
plt.grid(True,color="green")
plt.ylim(0,0.25)
plt.xlim(-5,30)
plt.show()