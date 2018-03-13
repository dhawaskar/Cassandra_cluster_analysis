import matplotlib.pyplot as plt
import csv

x=[]
y=[]
z=[]
with open('readings.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    count=0
    for row in plots:
        if(count>1):
            x.append(float(row[2]))
            y.append(float(row[4]))#delay
            z.append(float(row[5]))#offeset
        count+=1
plt.plot(x,y,lw=3.0)
plt.plot(x,z,lw=3.0)
plt.legend(['delay','offset']);
plt.title('server time versus client delay and offeset')
plt.xlabel('delay and offset in ms')
plt.ylabel('server time in s')
plt.savefig('delay_offset.pdf')
