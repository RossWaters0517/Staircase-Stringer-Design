from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from matplotlib.patches import Polygon, Rectangle
import matplotlib as mpl
import numpy as np
import pathlib
import os
import re
import math
import subprocess
root=tk.Tk()
# PopUp Menu
popup=Menu(root, tearoff=0)
#Add PopUp Menu Items
popup.add_command(label="View I.R.C. pdf File", background='aqua', command=lambda:open_pdf())
popup.add_separator(background='lightgray')
popup.add_command(label="About", background='aqua', command=lambda:about())
popup.add_separator(background='lightgray')
popup.add_command(label="Exit Program", background='aqua', command=root.destroy)
#
# display the popup menu
def menu_popup(event):
       try:popup.tk_popup(event.x_root, event.y_root)
       finally:popup.grab_release()
root.bind("<Button-3>", menu_popup)
#
def about():
       messagebox.showinfo('About', 'Creator: Ross Waters\nEmail: RossWatersjr@gmail.com'\
              '\nProgram: Staircase Stringer Designer\nRevision: 2.2.0'\
              '\nLast Revision Date: 11/19/2021\nLanguage: Python 3.9.7 64-bit'\
              '\nOperating System: Windows 11 21H2')
#
def open_pdf():
       try:
              dir=pathlib.Path(__file__).parent.absolute()
              filename='StairIRC.pdf'
              path=os.path.join(dir, filename)
       finally:subprocess.Popen([path], shell=True)
# 
# Enter Key Pressed On Entry Textbox Widgets
# Examine Entries Per I.R.C. Specs.
def enterkey_pressed(event):
       try:
              if (event.keysym)=='Return':
                     if event.widget['text']=='PY_VAR1': #hgt, Staircase Height
                            value=hgt_txtbx.get()
                            if value=='': raise Exception('Staircase Height Value Is Null.')
                            if float(value)<14 or float(value)>150:
                                   msg1='Allowable Staircase Height Range Is From\n'
                                   msg2= '14 inches (2 Steps) to 150 inches (@20 Steps).\n'
                                   msg3='Please Correct Entry Values!'
                                   messagebox.showwarning('Limit Violation', msg1+msg2+msg3)
                                   hgt_txtbx.delete(0,END)
                                   hgt_txtbx.insert(0,'')
                                   return
                     elif event.widget['text']=='PY_VAR2': # run, Run Per Step
                            value=run_txtbx.get()
                            tread_overhang=float(tdoverhang.get())
                            if float(value) <11.00 : #Examine Overhang >=0.75-1.25
                                   if float(tread_overhang)< 0.75:
                                          tread_overhang=0.75
                                          tdoverhang.set(tread_overhang)
                            if value=='': raise Exception('Run Per Step Value Is Null.')
                            if float(value)<10.00 or float(value)>30.00:
                                   msg1='Allowable Staircase Run Length Is From\n'
                                   msg2= '10.00 inches to 30.00 inches.\n'
                                   msg3='Please Correct Entry Values!'
                                   messagebox.showwarning('(Application Limit)', msg1+msg2+msg3)
                                   run_txtbx.delete(0,END)
                                   run_txtbx.insert(0,'')
                                   return
                            tread_depth=float(value)
                            tddepth.set(tread_depth)
                     elif event.widget['text']=='PY_VAR3': # toekick, Toe Kick Angle
                            value=toekick_txtbx.get()
                            if value=='': raise Exception('Toe Kick Angle Value Is Null.')
                            if float(value)<0 or float(value)>30:
                                   msg1='Allowable Toe Kick Angel Is From\n'
                                   msg2= '0 Degrees to 30 Degrees (I.R.C) Specs.\n'
                                   msg3='Please Correct Entry Values!'
                                   messagebox.showwarning('(I.R.C) Spec. Violation', msg1+msg2+msg3)
                                   toekick_txtbx.delete(0,END)
                                   toekick_txtbx.insert(0,'')
                                   return
                     elif event.widget['text']=='PY_VAR4': # tdthickness, Tread Thickness
                            value=tdthickness_txtbx.get()
                            if value=='': raise Exception('Tread Thickness Value Is Null.')
                            if float(value)<0 or float(value)>3:
                                   msg1='Allowable Tread Thickness Is From\n'
                                   msg2= '0 inches to 3 inches. \n'
                                   msg3='Please Correct Entry Values!'
                                   messagebox.showwarning('Application Limit', msg1+msg2+msg3)
                                   tdthickness_txtbx.delete(0,END)
                                   tdthickness_txtbx.insert(0,'') 
                                   return
                     elif event.widget['text']=='PY_VAR5': # ttdthickness, Top Tread Thickness
                            value=ttdthickness_txtbx.get()
                            if value=='': raise Exception('Top Tread Thickness Value Is Null.')
                            if float(value)<0 or float(value)>3:
                                   msg1='Allowable Top Tread Thickness Is From\n'
                                   msg2= '0 inches to 3 inches.\n'
                                   msg3='Please Correct Entry Values!'
                                   messagebox.showwarning('Application Limit', msg1+msg2+msg3)
                                   ttdthickness_txtbx.delete(0,END)
                                   ttdthickness_txtbx.insert(0,'')
                                   return
                     elif event.widget['text']=='PY_VAR6': # tddepth, Tread Depth
                            run_per_step=float(run_txtbx.get())
                            tread_depth=float(tddepth.get())
                            run.set(str(tread_depth))
                            tread_overhang=float(tdoverhang.get())
                            if tread_depth<11.00:
                                   if float(tread_overhang)< 0.75:
                                          tread_overhang=0.75
                                          tdoverhang.set(tread_overhang)
                            minval=10.0
                            maxval=30.0       
                            value=tddepth.get()
                            if value=='': raise Exception('Tread Depth Value Is Null.')
                            if float(value)<minval or float(value)>maxval:
                                   msg1='Allowable Tread Depth Is '+str(minval)+' inches\n'
                                   msg2='To '+str(maxval)+' inches.'
                                   messagebox.showwarning('(Application Limit)', msg1+msg2)
                                   tddepth_txtbx.delete(0,END)
                                   tddepth_txtbx.insert(0,'')
                                   return
                     elif event.widget['text']=='PY_VAR7': # tdoverhang, Tread Overhang
                            run_per_step=float(run_txtbx.get())
                            tread_wid=float(treadwid.get())
                            tread_depth=float(tddepth.get())
                            if run_per_step>=11: minval=0.0
                            if run_per_step<11: minval=0.75
                            maxval=1.25       
                            value=tdoverhang.get()
                            if value=='': raise Exception('Tread Overhang Value Is Null.')
                            if float(value)<minval or float(value)>maxval:
                                   msg1='Allowable Tread Overhang Is From '+str(minval)+' inches To\n'
                                   msg2= str(maxval)+' inches (I.R.C) Specs.'
                                   messagebox.showwarning('(I.R.C) Spec. Violation', msg1+msg2)
                                   tdoverhang_txtbx.delete(0,END)
                                   tdoverhang_txtbx.insert(0,'')
                                   return
              plot()
       except Exception as e:
              msg1='Exception occurred while code execution:\n'
              msg2= repr(e)+' '+event.widget['text']
              msg3='\nPlease Check Entry Values!'
              messagebox.showerror('Exeption Error', msg1+msg2+msg3)
#
# Radio Button Choices
def ShowChoice():
       #top_pos=top_position.get() # Not Used, Only For Test
       plot()
#
# Allow Only Positive Numeric values and decimal point for Entry Widgets
def validate_Entries(entry_text):
       regex=re.compile(r'[(0-9)(.)]*$') # Allow
       result=regex.match(entry_text)
       return (entry_text == '' 
       # Prevent duplicates
       or (entry_text.count('.') <= 1 # allow only one period
              and result is not None
              and result.group(0) != ''))
def on_validate(P):
       return validate_Entries(P)
#       
def plot():
       try:
              fig.clear(True) # Start Fresh
              viewport = fig.add_subplot(111) # Create The Figure
              viewport.set_title('Staircase Stringer Calculator (I.R.C. Specs.)',
                     ha='center', color='mediumblue', fontsize=14, weight='normal', style='italic')# Centered on graph
              # X and Y Axis Labels
              viewport.set_xlabel('Required Floor Space (inches)', ha='center', color='firebrick',
                     fontsize=10, weight='normal', style='italic')
              viewport.set_ylabel('Distance To Top Landing (inches)', ha='center', color='firebrick',
              fontsize=10, weight='normal', style='italic')
              # Define and Set Plot Limits
              stringer_hgt = float(hgt_txtbx.get())
              total_rise=stringer_hgt
              pos=top_position.get() #Returns Integer
              run_per_step=float(run_txtbx.get())
              #Plot Facecolor
              viewport.set_facecolor('lightcyan')
              top_tread_thickness=float(ttdthickness_txtbx.get())
              tread_depth=float(tddepth_txtbx.get())
              finished_hgt=stringer_hgt+top_tread_thickness
              tread_thickness=float(tdthickness_txtbx.get())
              num_of_steps=int(finished_hgt/7.5)
              toekick_angle=float(toekick.get())
              stringer_width=float(stringerwid.get())
              tread_overhang=float(tdoverhang_txtbx.get())
              if pos==0: # Flush With Top Sub-Floor
                     num_of_risers=num_of_steps
                     num_of_runners=num_of_risers
                     rise_per_step=finished_hgt/num_of_risers
                     # If Rise > Spec, Add Step To Reduce Rise
                     if rise_per_step >7.75: #Max Riser Hgt
                            num_of_risers += 1
                            rise_per_step=finished_hgt/num_of_risers
                            num_of_runners=num_of_risers
                            rise_per_step=finished_hgt/num_of_risers
                     num_of_steps=num_of_risers
                     top_riser_rise=rise_per_step-top_tread_thickness+tread_thickness
                     totalrise.set(total_rise)
                     stringer_hgt = float(hgt_txtbx.get())
                     req_floor_space=run_per_step*num_of_steps
                     xmax=req_floor_space+(run_per_step*2)
                     ymax=xmax/aspect_ratio
                     ylimits=0, ymax
                     xlimits=0, xmax
                     viewport.set(xlim=xlimits, ylim=ylimits, autoscale_on=False)
                     x1=0.0
                     x2=x1+run_per_step
                     y1=stringer_hgt
                     y2=y1
                     # Upper Landing Annotation
                     # Try Keeping Arrow Head Constant size
                     arrow_x=(1.75*run_per_step)+tread_overhang
                     viewport.arrow(arrow_x, stringer_hgt, -run_per_step*0.5, 0, 
                            head_width=ymax/116, head_length=(xmax*2)/158, fc='k', ec='k')
                     viewport.annotate('Upper Landing Subfloor = '+ str(stringer_hgt) +' in.',
                           xy=(arrow_x+1, stringer_hgt-0.1), xycoords='data', fontsize=6, color='k')
              else: # 1 Step Down From Top Sub-Floor
                     # Top Overhang
                     viewport.add_patch(Rectangle((0, stringer_hgt), tread_overhang, top_tread_thickness,
                     facecolor = 'lime', ec='darkgreen',lw=1,fill=True))
                     rise_per_step=finished_hgt/num_of_steps
                     num_of_runners=num_of_steps-1
                     num_of_risers=num_of_steps-1  
                     if rise_per_step >7.75: #Max Riser Hgt
                            num_of_risers += 1
                            num_of_steps=num_of_risers+1
                            num_of_runners=num_of_steps-1
                            rise_per_step=finished_hgt/num_of_steps
                     req_floor_space=run_per_step*num_of_risers
                     xmax=req_floor_space+(run_per_step*3)
                     ymax=xmax/aspect_ratio
                     ylimits=0, ymax
                     xlimits=0, xmax
                     viewport.set(xlim=xlimits, ylim=ylimits, autoscale_on=False)
                     x1=0.0
                     x2=x1+run_per_step
                     total_rise=finished_hgt-rise_per_step-tread_thickness
                     top_riser_rise=rise_per_step-top_tread_thickness+tread_thickness
                     totalrise.set(round(total_rise,4))
                     y1=total_rise
                     y2=y1
                     # Upper Landing Annotation
                     # 116 And 158 Represents Viewport Height and Width
                     # At a Standard 9 Feet Staircasing With Arrow Dimensions
                     # At Approximately L=2, W=1
                     viewport.arrow(run_per_step*0.85, stringer_hgt, -run_per_step*0.5, 0, 
                            head_width=ymax/116, head_length=(xmax*2)/158, fc='k', ec='k')      
                     viewport.annotate('Upper Landing Subfloor = '+ str(stringer_hgt) +' in.',
                            xy=(run_per_step+1, stringer_hgt-0.1), xycoords='data', fontsize=6, 
                            color='k', clip_on=True)
                     # Total Rise Annotation
                     arrow_x=(1.75*run_per_step)+tread_overhang
                     viewport.arrow(arrow_x, total_rise, -run_per_step*0.5, 0, 
                            head_width=ymax/116, head_length=(xmax*2)/158, fc='k', ec='k')      
                     viewport.annotate('Stringer Rise = '+ str(round(total_rise,4)) +' in.',
                            xy=(arrow_x+1, total_rise-0.1), xycoords='data', fontsize=6, 
                            color='k', clip_on=True)
              # Set Tick Label Font Size And Grid/Ticks
              viewport.tick_params(axis='both', which='major', labelsize=8)
              # Change Major And Minor Ticks Depending On Height Of Staircase
              if stringer_hgt<=90:
                     xmajor_tick=run_per_step
                     ymajor_tick=rise_per_step
                     xminor_tick=2
                     yminor_tick=2
              elif stringer_hgt>90:
                     xmajor_tick=run_per_step*2
                     ymajor_tick=rise_per_step*2
                     xminor_tick=2
                     yminor_tick=2
              viewport.xaxis.set_major_locator(MultipleLocator(xmajor_tick))
              viewport.xaxis.set_minor_locator(AutoMinorLocator(xminor_tick))
              viewport.yaxis.set_major_locator(MultipleLocator(ymajor_tick))
              viewport.yaxis.set_minor_locator(AutoMinorLocator(yminor_tick))
              # Turn Both Major and Minor Ticks On
              viewport.grid(which='major', color='lightgray', linestyle='dashed')
              viewport.grid(which='minor', color='lightgray', linestyle='dashed')
              # Get Things Ready To Plot The Stringer Risers And Runners
              if toekick_angle > 0: # Toe Kick Angle > 0
                     toekick_tan=math.tan(toekick_angle/(180/math.pi))
                     run_diff=toekick_tan*rise_per_step #Correction For Runs With Riser Angle
                     riser_len=math.sqrt(pow(rise_per_step,2)+pow(run_diff,2))
                     runner_len=run_per_step+run_diff
                     tread_top_adj = toekick_tan * tread_thickness
              else:
                     run_diff=0
                     riser_len=rise_per_step
                     runner_len=run_per_step
                     tread_top_adj=0
              while x1 < req_floor_space: # Plot The Stringer Risers And Runners
                     viewport.plot([x1-run_diff,x2], [y1,y2],'saddlebrown', lw=2) #Plot Runners
                     x1=x2
                     y1=y2
                     if y2==stringer_hgt:
                            y2-=top_riser_rise
                     else:        
                            y2-=rise_per_step
                     viewport.plot([x1,x2-run_diff], [y1,y2],'saddlebrown', lw=2) #Plot Risers
                     y1=y2
                     x2+=run_per_step
              # Get Things Ready To Plot Tread
              x1=0
              y1=total_rise
              x2=x1+tread_depth+tread_overhang
              y2=y1
              x3=x2
              y3=y2+tread_thickness
              if x1==0:
                     x4=x1 # No toekick_angle For Top Step
                     y3=y2+top_tread_thickness # Top Tread May Differ From Tread
                     y4=y3
              else:
                     x4=x1+tread_top_adj
                     x1=0
                     y1=total_rise
                     y3=y2+tread_thickness
                     y4=y3
              while y1 > 3: # Plot The Tread
                     p = np.array([[x1-run_diff,y1], [x2,y2], [x3,y3], [x4,y4]])
                     viewport.add_patch(Polygon(p, facecolor = 'lime',closed=True,
                            ec='darkgreen',lw=1,fill=True))
                     x1+=run_per_step
                     y1-=rise_per_step
                     x2=x1+tread_depth+tread_overhang
                     if y2==stringer_hgt:
                            y2-=top_riser_rise
                     else:        
                            y2-=rise_per_step
                     y1=y2
                     x3=x2
                     y3=y2+tread_thickness
                     x4=x1-run_diff+tread_top_adj
                     y4=y3
              # Top Riser Rise Annotations
              if pos==0: arrow_y=stringer_hgt-(0.65*rise_per_step)
              else: arrow_y=stringer_hgt-(1.65*rise_per_step)
              arrow_x=(run_per_step*1.75)-0.75*run_diff 
              viewport.arrow(arrow_x, arrow_y, -run_per_step*0.5, 0, head_width=ymax/116, 
                     head_length=(xmax*2)/158, fc='k', ec='k')      
              viewport.annotate('Top Riser Rise = '+ str(round(top_riser_rise,4)) +' in.',
                     xy=(arrow_x+1, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
              # Rise Per Step Annotations
              if num_of_risers>2:
                     if pos==0: arrow_y=stringer_hgt-(1.65*rise_per_step)
                     else: arrow_y=stringer_hgt-(2.65*rise_per_step)
                     arrow_x=(run_per_step*2.75)-0.75*run_diff 
                     viewport.arrow(arrow_x, arrow_y, -run_per_step*0.5, 0, head_width=ymax/116, 
                            head_length=(xmax*2)/158, fc='k', ec='k')      
                     viewport.annotate('Rise = '+ str(round(rise_per_step,4)) +' in.',
                            xy=(arrow_x+1, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
              # Bottom Riser Rise Annotations
              arrow_x=(req_floor_space-(run_per_step/aspect_ratio))-run_diff*0.75
              arrow_y=0.3*(rise_per_step-tread_thickness)
              viewport.arrow(arrow_x, arrow_y, 0.5*run_per_step, 0, head_width=ymax/116, 
                     head_length=(xmax*2)/158, fc='k', ec='k')
              # This Annotation Is Used To Only Obtain Text Dimensions.
              # Will Be Removed And Replaced Below.      
              txt=viewport.annotate('Bottom Riser Rise = '+ str(round(rise_per_step-tread_thickness,4)) +' in.',
                     xy=((xmax)*0.5, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
              r = canvas.get_renderer()
              # Get Text Properties in Data Coords.
              bbox = viewport.transData.inverted().transform_bbox(txt.get_window_extent(renderer=r))
              x0=arrow_x-bbox.width-1
              txt.remove() # Remove Original Annotation And Replace With New
              # Place Annotation Along Left Side Of Arrow According To Data Dimensions
              txt=viewport.annotate('Bottom Riser Rise = '+ str(round(rise_per_step-tread_thickness,4)) +' in.',
                     xy=(x0, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
              # Set Variables To Move Arrows And Annotations According To Number Of Steps
              if num_of_risers<=7:
                     redarrow_x=req_floor_space-run_per_step+tread_overhang
                     redarrow_y=(3.2*rise_per_step)+1
                     runarrow_x=req_floor_space+tread_overhang
                     runarrow_y=(2.5*rise_per_step)+1
                     runnotation_x=(req_floor_space-run_per_step)+2
                     runnotation_y=(2.5*rise_per_step)+1.5
                     overhang_x=(req_floor_space-run_per_step)+2
                     overhang_y=(2.5*rise_per_step)+3.5
                     tdarrow_x=(req_floor_space)-((run_per_step*2)-tread_overhang)
                     tdarrow_y=(3.5*rise_per_step)+1
                     tdannotation_x=(req_floor_space-((run_per_step*2)-tread_overhang))+1
                     tdannotation_y=3.5*rise_per_step
                     twarrow_x=(req_floor_space)-(run_per_step*2)-run_diff
                     twarrow_y=(3.7*rise_per_step)
                     twannotation_x=(req_floor_space-(run_per_step*2))-(run_diff-1)
                     twannotation_y=(3.7*rise_per_step)
              elif num_of_risers<=12:
                     redarrow_x=(req_floor_space-(2*run_per_step))+tread_overhang
                     redarrow_y=(4.2*rise_per_step)+1
                     runarrow_x=(req_floor_space-run_per_step)+tread_overhang
                     runarrow_y=(3.5*rise_per_step)+1
                     runnotation_x=(req_floor_space-(2*run_per_step))+2
                     runnotation_y=(3.5*rise_per_step)+1.5
                     overhang_x=(req_floor_space-(2*run_per_step))+2
                     overhang_y=(4.5*rise_per_step)-3
                     tdarrow_x=(req_floor_space)-((run_per_step*3)-tread_overhang)
                     tdarrow_y=(4.5*rise_per_step)+1
                     tdannotation_x=(req_floor_space-((run_per_step*3)-tread_overhang))+1
                     tdannotation_y=4.5*rise_per_step
                     twarrow_x=(req_floor_space)-(run_per_step*3)-run_diff
                     twarrow_y=(4.8*rise_per_step)+1
                     twannotation_x=(req_floor_space-(run_per_step*3))-(run_diff-1)
                     twannotation_y=(4.8*rise_per_step)+1
              else: 
                     redarrow_x=(req_floor_space-(3*run_per_step))+tread_overhang
                     redarrow_y=(5.2*rise_per_step)+1
                     runarrow_x=(req_floor_space-2*run_per_step)+tread_overhang
                     runarrow_y=(4.5*rise_per_step)+1
                     runnotation_x=(req_floor_space-(3*run_per_step))+2
                     runnotation_y=(4.5*rise_per_step)+1.5
                     overhang_x=(req_floor_space-(3*run_per_step))+2
                     overhang_y=(5.5*rise_per_step)-2.5
                     tdarrow_x=(req_floor_space)-((run_per_step*4)-tread_overhang)
                     tdarrow_y=(5.5*rise_per_step)+1
                     tdannotation_x=(req_floor_space-((run_per_step*4)-tread_overhang))+1
                     tdannotation_y=5.5*rise_per_step
                     twarrow_x=(req_floor_space)-(run_per_step*4)-run_diff
                     twarrow_y=(5.8*rise_per_step)+1
                     twannotation_x=(req_floor_space-(run_per_step*4))-(run_diff-1)
                     twannotation_y=(5.8*rise_per_step)+1
              # Use The Variables And Move Arrows And Annotation Accordingly
              viewport.arrow(redarrow_x, redarrow_y, 0,
                     (-1.2*rise_per_step)+tread_thickness, head_width=ymax/116,
                     head_length=(xmax*2)/158, fc='k', ec='red')      
              # Run Per Step Arrow And Annotation             
              viewport.arrow(runarrow_x, runarrow_y, 0,
                     (-rise_per_step*1.5)+tread_thickness, head_width=ymax/116,
                     head_length=(xmax*2)/158, fc='k', ec='k')
              txt=viewport.annotate('Run Per Step = '+ str(round(run_per_step,3)) +' in.', xy=(runnotation_x,
                     runnotation_y), xycoords='data', fontsize=6, color='k', clip_on=True)
              # Overhang Annotation Only
              txt=viewport.annotate('Overhang = '+ str(round(tread_overhang,3)) +' in.', xy=(overhang_x,
                     overhang_y), xycoords='data', fontsize=6, color='k', clip_on=True)
              # Tread Depth Arrow And Annotation       
              viewport.arrow(tdarrow_x, tdarrow_y, 0, 
                     (-rise_per_step*1.5)+tread_thickness, head_width=ymax/116, 
                     head_length=(xmax*2)/158, fc='k', ec='k')
              txt=viewport.annotate('Tread Depth = '+ str(round(tread_depth,3)) +' in.', xy=(tdannotation_x,
                     tdannotation_y), xycoords='data', fontsize=6, color='k', clip_on=True)
              if toekick_angle > 0:
                     viewport.arrow(twarrow_x, twarrow_y, 0, 
                            (-rise_per_step*1.8)+tread_thickness, head_width=ymax/116, 
                            head_length=(xmax*2)/158, fc='k', ec='k')      
                     txt=viewport.annotate('Tread Width = '+ str(round(runner_len+tread_overhang,3)) +' in.', 
                            xy=(twannotation_x, twannotation_y),
                            xycoords='data', fontsize=6, color='k', clip_on=True)
              # Draw The Strnger Material
              x1=0
              if pos==0: y1=stringer_hgt+rise_per_step
              if pos==1: y1=stringer_hgt
              # peaks_valleys, Top Cut Length, Floor Cut Length And Staircase Angle
              peaks_valleys=round(math.sqrt(pow(rise_per_step,2)+pow(run_per_step,2)),4)#Hyp
              topanglesin=run_per_step/peaks_valleys
              topcutlength= stringer_width/topanglesin
              x2=x1              
              y2=y1-topcutlength
              stair_angle=math.atan(rise_per_step/run_per_step)*(180/math.pi)
              hyp=y2/math.sin(stair_angle/(180/math.pi))
              x3=math.sqrt(pow(hyp,2)-pow(y2,2))
              y3=0
              floor_sin=rise_per_step/peaks_valleys
              floor_cutlength=stringer_width/floor_sin
              x4=x3+floor_cutlength
              y4=0
              # Plot Stringer Material
              p = np.array([[x1,y1], [x2,y2], [x3,y3], [x4,y4]])
              viewport.add_patch(Polygon(p, closed=True,
                     ec='saddlebrown',lw=1,ls='--', fill=False))
              # Stringer Length Required
              if pos==0: y1=stringer_hgt
              if pos==1: y1=stringer_hgt-rise_per_step
              stringer_len=math.sqrt(pow(y1,2)+pow(req_floor_space,2))
              tread_wid=runner_len+tread_overhang # Total Tread Width
              fig.canvas.draw() # Refresh The Canvas
              # Update Entry Widgets
              numrisers.set(num_of_risers)
              numsteps.set(num_of_steps)
              riseperstep.set(round(rise_per_step,4))
              numrunners.set(num_of_runners)
              totalrun.set(round(req_floor_space,4))
              runnerlength.set(round(runner_len,4))
              riserlength.set(round(riser_len,4))
              toprise.set(round(top_riser_rise,4))
              bot_riser_rise=rise_per_step-tread_thickness
              botrise.set(round(bot_riser_rise,4))
              stairangle.set(round(stair_angle,4))
              # Stringer Floor And Top Cut Angles
              floor_cutangle=90-stair_angle
              botangle.set(round(floor_cutangle,4))
              peakvalley.set(peaks_valleys)
              stringerlen.set(round(stringer_len,4))
              treadwid.set(round(tread_wid,4)) 
       except Exception as e:
              msg1='Exception occurred while code execution:\n'
              msg2= repr(e)
              msg3='\nPlease Check Entry Values!'
              messagebox.showerror('Exeption Error', msg1+msg2+msg3)
# Entry widgets StringVar() with Local float assignments, 23 total 
top_position = tk.IntVar() #PY_VAR0 Location Of Top Step, 0=Flush, 1=Down 1 Step
hgt=tk.StringVar() #PY_VAR1, stringer_hgt
run=tk.StringVar() #PY_VAR2, run_per_step
toekick=tk.StringVar() #PY_VAR3, toekick_angle
tdthickness=tk.StringVar() #PY_VAR4, tread_thickness
ttdthickness=tk.StringVar() #PY_VAR5, top_tread_thickness
tddepth=tk.StringVar() #PY_VAR6, tread_depth
tdoverhang=tk.StringVar() #PY_VAR7, tread_overhang
totalrise=tk.StringVar() #PY_VAR8, total_rise
riseperstep=tk.StringVar() #PY_VAR9, rise_per_step
numrisers=tk.StringVar() #PY_VAR10, num_of_risers
toprise=tk.StringVar() #PY_VAR11, top_riser_rise
botrise=tk.StringVar() #PY_VAR12, bot_riser_rise
totalrun=tk.StringVar() #PY_VAR13, req_floor_space
numrunners=tk.StringVar() #PY_VAR14, num_of_runners
numsteps=tk.StringVar() #PY_VAR15, num_of_steps
runnerlength=tk.StringVar() #PY_VAR16, runner_len
stairangle=tk.StringVar() #PY_VAR17, stair_angle
botangle=tk.StringVar() #PY_VAR18, floor_cutangle
peakvalley=tk.StringVar() #PY_VAR19, peaks_valleys
stringerlen=tk.StringVar() #PY_VAR20, stringer_len
stringerwid=tk.StringVar() #PY_VAR21, stringer_width
treadwid=tk.StringVar() #PY_VAR22, tread_wid
riserlength=tk.StringVar() #PY_VAR23, riser_len
# Program icon
dir=pathlib.Path(__file__).parent.absolute()
filename='Stringer.ico'
path=os.path.join(dir, filename)
root.iconbitmap(path)  
# Set Tk main Dimensions
root.title('Staircase Stringer Designer')
screen_width=root.winfo_screenwidth() # Width of the screen
screen_height=root.winfo_screenheight() # Height of the screen
root_wid=int(screen_width/2.0)
root_hgt=int(screen_height/1.8)
x=(screen_width/2)-(root_wid/2)
y=(screen_height/2)-(root_hgt/2)
# Position Center Of Screen
root.geometry('%dx%d+%d+%d' % (root_wid, root_hgt, x, y, ))
root.configure(bg='lightgray') # Set main backcolor to aqua
# Create And Position The Figure
fig_width=7
fig_height=5
fig = mpl.figure.Figure(figsize=(fig_width, fig_height), dpi=113)
aspect_ratio=fig_width/fig_height
fig.patch.set_facecolor('lightgray')# Set the figure facecolor
fig_x, fig_y, fig_wid, fig_hgt=fig.bbox.bounds
fig_wid, fig_hgt = int(fig_wid), int(fig_hgt)
# Create The Canvas
canvas=FigureCanvasTkAgg(fig, master=root)
canvas_wid=int(root_wid*0.78) # Covers 78% of fig Width
canvas_hgt=int(root_hgt*0.74) # Covers 74% of fig Height
canvas.get_tk_widget().pack(side=TOP, anchor=NW)#place(x=0, y=0)
# creating the Matplotlib toolbar
toolbar=NavigationToolbar2Tk(canvas, root).update()
# placing the toolbar on the Tkinter window
canvas.get_tk_widget().pack()
entry_font=font.Font(family='Times New Romans', size=9, weight='bold', slant='italic')
# Create Frame with Label and place 2 radio buttons inside
# Create the frame Label
fra_lbl=tk.Label(root, background='lightgray', foreground='mediumblue', font=entry_font,
       text="Stringer Position At Top")
lbl_wid=fra_lbl.winfo_reqwidth()
x_centered=fig_wid-lbl_wid/5
lbl_hgt=fra_lbl.winfo_reqheight()
y_centered=7
fra_lbl.place(x=x_centered, y=y_centered)
# Create the Frame
lbl_font=font.Font(family='lucidas', size=8, weight='bold', slant='italic')
fra1=Frame(root, background='lightgray', relief='raised', 
       highlightbackground="#696969", highlightthickness=1)
fra1.place(x=x_centered-13, y=y_centered+lbl_hgt)
# Radio Buttons For Staircase Location At Top   
top_position.set(0)  # initializing the choice, i.e. Python
rdo1=tk.Radiobutton(fra1, text='Flush with Top Subfloor', indicatoron=0, width=20, height=1, activebackground='aqua',
       background='lightgray', font=lbl_font, padx=10, variable=top_position, command=ShowChoice, value=0).pack()
rdo2=tk.Radiobutton(fra1, text='Down 1 Step from Top', indicatoron=0, width=20, height=1,  activebackground='aqua',
       background='lightgray', font=lbl_font, padx=10, variable=top_position, command=ShowChoice, value=1).pack()
# Staircase Height and Label
txtbx_font=font.Font(family='lucidas', size=10, weight='normal', slant='italic')
# Variables For Size And Position
# Of Entry Widgets And Labels
x_centered=745
lbl_wid=147
tb_wid=65
x_space=x_centered+lbl_wid
y_space=80
#
root.bind('<Return>', enterkey_pressed) # Enter Key Was Pressed On Entry Widgets
hgt_txtbx=tk.Entry(root, background='lightcyan', textvariable=hgt, font=txtbx_font,)
hgt_txtbx['validatecommand']=(hgt_txtbx.register(validate_Entries),'%P','%d')
val_cmd=(hgt_txtbx.register(on_validate), '%P')
hgt_txtbx.config(validate="key", validatecommand=val_cmd)
hgt_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
hgt_txtbx.insert(0, '60.0')
#
hgt_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Staircase Height (in.)', justify='left', anchor=E)
hgt_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Run Per Step and Label
run_txtbx=tk.Entry(root, background='lightcyan', textvariable=run, font=txtbx_font,)
run_txtbx['validatecommand']=(run_txtbx.register(validate_Entries),'%P','%d')
run_cmd=(run_txtbx.register(on_validate), '%P')
run_txtbx.config(validate="key", validatecommand=val_cmd)
run_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
run_txtbx.insert(0, '10.25')
#
run_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Run per Step (in.)', justify='left', anchor=E)
run_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Riser Toe Kick Angle and Label
toekick_txtbx=tk.Entry(root, background='lightcyan', textvariable=toekick, font=txtbx_font,)
toekick_txtbx['validatecommand']=(toekick_txtbx.register(validate_Entries),'%P','%d')
toekick_cmd=(toekick_txtbx.register(on_validate), '%P')
toekick_txtbx.config(validate="key", validatecommand=val_cmd)
toekick_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
toekick_txtbx.insert(0, '0.0')
#
toekick_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Riser Toe Kick Angle', justify='left', anchor=E)
toekick_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Tread Thickness and Label
tdthickness_txtbx=tk.Entry(root, background='lightcyan', textvariable=tdthickness, font=txtbx_font,)
tdthickness_txtbx['validatecommand']=(tdthickness_txtbx.register(validate_Entries),'%P','%d')
tdthickness_cmd=(tdthickness_txtbx.register(on_validate), '%P')
tdthickness_txtbx.config(validate="key", validatecommand=val_cmd)
tdthickness_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
tdthickness_txtbx.insert(0, '1.0')
#
tdthickness_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Tread Thickness (in.)', justify='left', anchor=E)
tdthickness_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Top Tread Thickness and Label
ttdthickness_txtbx=tk.Entry(root, background='lightcyan', textvariable=ttdthickness, font=txtbx_font,)
ttdthickness_txtbx['validatecommand']=(ttdthickness_txtbx.register(validate_Entries),'%P','%d')
ttdthickness_cmd=(ttdthickness_txtbx.register(on_validate), '%P')
ttdthickness_txtbx.config(validate="key", validatecommand=val_cmd)
ttdthickness_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
ttdthickness_txtbx.insert(0, '1.0')
#
ttdthickness_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Top Tread Thickness (in.)', justify='left', anchor=E)
ttdthickness_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Tread Depth and Label
tddepth_txtbx=tk.Entry(root, background='lightcyan', textvariable=tddepth, font=txtbx_font,)
tddepth_txtbx['validatecommand']=(tddepth_txtbx.register(validate_Entries),'%P','%d')
tddepth_cmd=(tddepth_txtbx.register(on_validate), '%P')
tddepth_txtbx.config(validate="key", validatecommand=val_cmd)
tddepth_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
tddepth_txtbx.insert(0, '10.25')
tread_depth='10.25'
#
tddepth_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Tread Depth (in.)', justify='left', anchor=E)
tddepth_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Tread Overhang and Label
tdoverhang_txtbx=tk.Entry(root, background='lightcyan', textvariable=tdoverhang, font=txtbx_font,)
tdoverhang_txtbx['validatecommand']=(tdoverhang_txtbx.register(validate_Entries),'%P','%d')
tdoverhang_cmd=(tdoverhang_txtbx.register(on_validate), '%P')
tdoverhang_txtbx.config(validate="key", validatecommand=val_cmd)
tdoverhang_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
tdoverhang_txtbx.insert(0, '1.0')
#
tdoverhang_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Tread Overhang (in.)', justify='left', anchor=E)
tdoverhang_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Stringer Width
stringerwid_txtbx=tk.Entry(root, background='lightcyan', textvariable=stringerwid, font=txtbx_font,)
stringerwid_txtbx['validatecommand']=(stringerwid_txtbx.register(validate_Entries),'%P','%d')
stringerwid_cmd=(tdoverhang_txtbx.register(on_validate), '%P')
stringerwid_txtbx.config(validate="key", validatecommand=val_cmd)
stringerwid_txtbx.place(x=x_space, y=y_space, width=tb_wid, height=18)
stringerwid_txtbx.insert(0, '11.5')
#
sw_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Stringer Width (in.)', justify='left', anchor=E)
sw_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Tread Width
treadwid_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=treadwid, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
treadwid_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
tw_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Tread Width (in.)', justify='left', anchor=E)
tw_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Stringer Total Rise
totalrise_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=totalrise, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
totalrise_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
trise_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Stringer Total Rise (in.)', justify='left', anchor=E)
trise_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Rise Per Step
riseperstep_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=riseperstep, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
riseperstep_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
rps_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Rise per Step (in.)', justify='left', anchor=E)
rps_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Number Of Risers
numrisers_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=numrisers, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
numrisers_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
nrisers_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Number of Risers', justify='left', anchor=E)
nrisers_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Top Riser Rise
toprise_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=toprise, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
toprise_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
trr_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Top Riser Rise (in.)', justify='left', anchor=E)
trr_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Bottom Riser Rise
botrise_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=botrise, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
botrise_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
br_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Bottom Riser Rise (in.)', justify='left', anchor=E)
br_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Stringer Total Run
totalrun_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=totalrun, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
totalrun_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
trun_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Required Floor Space (in.)', justify='left', anchor=E)
trun_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Number Of Runners
numrunners_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=numrunners, anchor=W,  
       justify='left', borderwidth=1, relief="ridge")
numrunners_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
nrunners_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Number of Runners', justify='left', anchor=E)
nrunners_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Number of Steps
numsteps_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=numsteps, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
numsteps_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
nsteps_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Number of Steps', justify='left', anchor=E)
nsteps_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Runner Length
runnerlength_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=runnerlength, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
runnerlength_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
runl_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Runner Cut Length (in.)', justify='left', anchor=E)
runl_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Riser Length
riserlength_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=riserlength, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
riserlength_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
risl_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Riser Cut Length (in.)', justify='left', anchor=E)
risl_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Staircase Angle
stairangle_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=stairangle, anchor=W,  
       justify='right', borderwidth=1, relief="ridge")
stairangle_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
sa_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Staircase Angle', justify='left', anchor=E)
sa_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
y_space+=21
# Bottom Cut Angle
botangle_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=botangle, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
botangle_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
ba_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Bottom Cut Angle', justify='left', anchor=E)
ba_lbl.place(x=x_centered+20, y=y_space, width=lbl_wid-20, height=18)
y_space+=21
# peaks_valleys and Valleys
peakvalley_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=peakvalley, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
peakvalley_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
pv_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Peaks/Valleys (in.)', justify='left', anchor=E)
pv_lbl.place(x=x_centered+20, y=y_space, width=lbl_wid-20, height=18)
y_space+=21
# Stringer Length
stringerlen_lbl=tk.Label(root, background='whitesmoke', font=txtbx_font, textvariable=stringerlen, anchor=W, 
       justify='right', borderwidth=1, relief="ridge")
stringerlen_lbl.place(x=x_space, y=y_space, width=tb_wid, height=18)
#
sl_lbl=tk.Label(root, background='lightgray', font=lbl_font, text='Stringer Length Req. (in.)', justify='left', anchor=E)
sl_lbl.place(x=x_centered, y=y_space, width=lbl_wid, height=18)
plot()
root.mainloop()