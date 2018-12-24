#Ranjan 24-12-2018
'''
This is very small project to build your own system monitoring application/pluggin.
It runs on Raspberry pi machine having python3
'''
from gpiozero import CPUTemperature
import time
import tkinter as kr
import os, sys, subprocess

cpu = CPUTemperature()
#print (cpu.temperature)


class app (kr.Frame):
    def __init__(self,master):
        kr.Frame.__init__(self,master)
        self.grid()
        self.widget()
        self.cal()
    
    def quitCmd(self):
        root.destroy()
    
    def updateCmd(self):
        #os.popen("sudo apt-get update")
        #subprocess.call("sudo apt-get update",shell=True)
        #subprocess.Popen("sudo apt-get update",shell=True)
        #subprocess.Popen("sudo apt-get upgrade -y",shell=True)
        #subprocess.Popen("sudo apt-get dist-upgrade -y", shell = True)
        cmd ="sudo apt-get update | sudo apt-get upgrade | sudo apt-get dist-upgrade -y -y"
        subprocess.Popen(cmd, shell = True)

    def widget(self):
        w1_1 = kr.Label (root, text = " RONNEY")
        #w1_2 = kr.Label (root, text = "UI")

        #CPU TEMP
        w2 = kr.Label (root, text = "CPU Temp :-" )
        timeDate = time.localtime()
        #Time
        w4 = kr.Label (root, text = "Time :-" )
        #Date
        w6 = kr.Label (root, text = "Date :-")
        
        #CPU usage
        w8 = kr.Label (root, text = "CPU Usage :-" )
        
        #Ram usage
        w10 = kr.Label (root, text = "RAM Usage :-" )
        #w11 = kr.Label (root, text = "Total RAM Space :-\t"+self.getRAMinfo()[0] )
        #w12 = kr.Label (root, text = ' '+self.getRAMinfo()[0]+' ' )
        #w13 = kr.Label (root, text = "Used RAM Space :-\t"+self.getRAMinfo()[1] )
        #w14 = kr.Label (root, text = ' '+self.getRAMinfo()[1]+' ' )
        #w15 = kr.Label (root, text = "Remaning RAM Space :-\t"+self.getRAMinfo()[2] )
        #w16 = kr.Label (root, text = ' '+self.getRAMinfo()[2]+' ' )
        #per = float("{0:.2f}".format(int(self.getRAMinfo()[1]) / int(self.getRAMinfo()[0])*100))
        #w17 = kr.Label (root, text = "Percentage RAM Space :-\t"+str(per)+'% ' )
        #w18 = kr.Label (root, text = ' '+str(per)+'% ' )

        #Disk Usage
        w19 = kr.Label (root, text = "Disk Usage :-" )
        #w20 = kr.Label (root, text = ' '+self.getDiskSpace()[3]+' ' )
        
        
        w50 = kr.Button ( root, text = "Full Update", command = self.updateCmd)
        w51 = kr.Button ( root, text = "Quit" , command = self.quitCmd)
        
        w1_1.grid( row = 0, column = 2 )
        #w1_2.grid( row = 0, column = 3 )
        w2.grid( row = 3, column = 1 )
        #w3.grid( row = 3, column = 3 )
        w4.grid( row = 1, column = 1 )
        #w5.grid( row = 1, column = 3 )
        w6.grid( row = 2, column = 1 )
        #w7.grid( row = 2, column = 3 )
        w8.grid( row = 4, column = 1 )
        #w9.grid( row = 4, column = 3 )
        w10.grid( row = 5, column = 1 )
        #w11.grid( row = 6, column = 1 )
        #w12.grid( row = 6, column = 3 )
        #w13.grid( row = 7, column = 1 )
        #w14.grid( row = 7, column = 3 )
        #w15.grid( row = 8, column = 1 )
        #w16.grid( row = 8, column = 3 )
        #w17.grid( row = 9, column = 1 )
        #w18.grid( row = 5, column = 3 )
        w19.grid( row = 6, column = 1 )
        #w20.grid( row = 6, column = 3 )
        
        
        w50.grid( row = 10, column = 1 )
        w51.grid( row = 10, column = 3 )
    
    def widget_data(self):
        w3 = kr.Label (root, text = ' '+str(cpu.temperature)+' ' )

        timeDate = time.localtime()
        #Time
        w5 = kr.Label (root, text =  str(timeDate.tm_hour) + ":" + str(timeDate.tm_min)+ ':' + str(timeDate.tm_sec) )
        #Date
        #w6 = kr.Label (root, text = "Date :-")
        w7 = kr.Label (root, text = str(timeDate.tm_mday) + '-' + str(timeDate.tm_mon) + '-' + str(timeDate.tm_year) )
        
        #CPU usage
        #w8 = kr.Label (root, text = "CPU Usage :-" )
        w9 = kr.Label (root, text = ' '+str(self.getCPUuse())+'% ' )

        #Ram usage
        #w10 = kr.Label (root, text = "RAM Usage :-" )
        #w11 = kr.Label (root, text = "Total RAM Space :-\t"+self.getRAMinfo()[0] )
        #w12 = kr.Label (root, text = ' '+self.getRAMinfo()[0]+' ' )
        #w13 = kr.Label (root, text = "Used RAM Space :-\t"+self.getRAMinfo()[1] )
        #w14 = kr.Label (root, text = ' '+self.getRAMinfo()[1]+' ' )
        #w15 = kr.Label (root, text = "Remaning RAM Space :-\t"+self.getRAMinfo()[2] )
        #w16 = kr.Label (root, text = ' '+self.getRAMinfo()[2]+' ' )
        per = float("{0:.2f}".format(int(self.getRAMinfo()[1]) / int(self.getRAMinfo()[0])*100))
        #w17 = kr.Label (root, text = "Percentage RAM Space :-\t"+str(per)+'% ' )
        w18 = kr.Label (root, text = ' '+str(per)+'% ' )

        #Disk Usage
        #w19 = kr.Label (root, text = "Disk Usage :-" )
        w20 = kr.Label (root, text = ' '+self.getDiskSpace()[3]+' ' )
        
        w3.grid( row = 3, column = 3 )
        w5.grid( row = 1, column = 3 )
        w7.grid( row = 2, column = 3 )
        w9.grid( row = 4, column = 3 )
        w18.grid( row = 5, column = 3 )
        w20.grid( row = 6, column = 3 )

    def getDiskSpace(self):
        '''
        Return information about disk space as a list (unit included)                     
        Index 0: total disk space                                                         
        Index 1: used disk space                                                          
        Index 2: remaining disk space                                                     
        Index 3: percentage of disk used
        '''
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i==2:
                return(line.split()[1:5])

    def getRAMinfo(self):
        '''
        Return RAM information (unit=kb) in a list
        Index 0: total RAM
        Index 1: used RAM
        Index 2: free RAM
        '''
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                return(line.split()[1:4])
        
    def getCPUuse(self):
        '''
        Return % of CPU used by user as a character string
        '''    
        return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

    def cal(self):
        self.widget_data()
        self.after(1000,self.cal)

root = kr.Tk()

root.title("Monitoring UI")
''' to hide the title bar '''
#root.overrideredirect(1)
#root.wm_attributes('-type', 'splash')
#root.wm_attributes('-fullscreen','true')

root.geometry("280x200")
#w1 = kr.Label (root, text = "Temperature")

ap = app(root)
#w1.pack()
root.mainloop()
