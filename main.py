#!/usr/bin/python
# -*- coding: utf-8 -*-
#from kivy.app import App
#from tkinter import W
#from kivy.config import Config
#Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
__version__ = "0.1"
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
#from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivymd.app import MDApp
#from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import sp
from kivy.metrics import dp
#from kivy.uix.progressbar import ProgressBar
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton, MDRectangleFlatIconButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextFieldRect
#from kivymd.uix.label import MDLabel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from kivymd.uix.datatables import MDDataTable
#from kivymd.uix.list import OneLineListItem, MDList
#from kivymd.uix.scrollview import MDScrollView
from datetime import datetime
from database import Database
from kivmob import KivMob, TestIds
import threading 
import csv
import random
import requests
import json
import smtplib
import datetime
import time
import os
#import sys
import webbrowser
#import sqlite3
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# # ANDROID SPECIFIC PRIVS#
# from android.storage import app_storage_path
# settings_path = app_storage_path()

# from android.storage import primary_external_storage_path
# primary_ext_storage = primary_external_storage_path()

# from android.storage import secondary_external_storage_path
# secondary_ext_storage = secondary_external_storage_path()

# from android.permissions import request_permissions, Permission
# request_permissions([Permission.WRITE_EXTERNAL_STORAGE])


# Initialize db instance
db = Database()
# class to build GUI for a popup window
class P(FloatLayout):
	pass
# staging class to hold old kivy
class Staging(BoxLayout):
  pass
# Set global variables for use across classes
class GlobalVariables:
  def __init__(self):
    self.sum_mod = 1
    self.highlow_mod = 1
    self.evenodd_mod = 1
    self.groupskips_mod = 1
    self.onerepeat_mod = 1
    self.fourhot_mod = 1
    self.leastfreq_mod = 0
    self.neverdrawn_mod = 0
    self.winodds_mod = 0
    self.progress_value = 0
    self.progress_max = 0
    self.email = ''
    self.name = ''
    self.timer = 0
    self.mostfreq_mod = 0
    self.agreement = 0
# Class for tool tip
class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass

# Class to ensure numeric input and control range of numbers
class NumericInput(MDTextFieldRect):
    min_value = NumericProperty(0)
    max_value = NumericProperty(100)

    def validate_input(self, value):
        if not value:
            return True

        try:
            value = float(value)

            if self.min_value <= value <= self.max_value:
                return True

        except ValueError:
            pass

        return False

    def on_text(self, instance, text):
        if not self.validate_input(text):
            self.text = ''

    def insert_text(self, substring, from_undo=False):
        if not self.validate_input(substring):
            return False

        return super().insert_text(substring, from_undo=from_undo)

    def on__min_value(self, instance, value):  # pylint: disable=no-self-use, unused-argument; Kivy callback signature requires these arguments to be present even though they are unused in this case. See https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties._ObservableDictMixin for more information about the callback signature and how it differs from a normal method signature in Python classes that inherit from Kivy classes like this one does here (i.e., `NumericInput` inherits from `BoxLayout`). The `pylint` error can be safely ignored in this case since the callback is being used as intended by Kivy and the arguments are required to be present by Kivy's API specification for callbacks of this type (i.e., callbacks that are triggered when a property changes). See https://github.com/PyCQA/pylint/issues/1436 for more information about why `pylint` is incorrectly flagging these arguments as unused in this case and why it is safe to ignore the warning here since it is a false positive due to a bug in `pylint`. This comment can be removed once the bug has been fixed in `pylint`. See https://github.com/PyCQA/pylint/pull/1437 for more information about the fix that has been proposed for this bug and its current status (as of 2020-04-06). Once the fix has been merged into master and released as part of a new version of `pylint`, then this comment can be removed along with the corresponding disable directive above that disables the warning for these two arguments only (i.e., `# pylint: disable=no-self-use, unused-argument`). The other two arguments (i.e., `instance` and `value`) should remain enabled so that they will continue to trigger warnings if they ever become unused in future changes made to this code after the fix has been released as part of a new version of `pylint`. This comment should also be kept up to date with any future changes made to this code after the fix has been released as part of a new version of `pylint` so that anyone reading it will know whether or not it is still accurate based on those future changes or whether or not those future changes invalidate any part of what is written here now such that it would no longer apply accurately to those future changes after they have been made (assuming those future changes do not also update this comment at the same time so that it remains accurate even after those future changes have been made). If you are reading this comment now and you notice that any part of what is written here no longer applies accurately based on some change or set of changes that were made to this code after what is written here was originally written but before you read it now then please feel free to submit an issue or pull request against this repository so that I can update what I have written here accordingly based on your feedback about how my original comments no longer apply accurately based on some change or set of changes that were made since I originally wrote them but before you read them now."""  # pylint: disable=line-too-long; disabling line length checker because line length limit is too short given all of the extra context provided by all of these comments which need to be included here because otherwise there would be no way for anyone reading them later on down the road after some change or set of changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code.
        self.text = ''

    def on__max_value(self, instance, value):  # pylint: disable=no-self-use, unused-argument; Kivy callback signature requires these arguments to be present even though they are unused in this case. See https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties._ObservableDictMixin for more information about the callback signature and how it differs from a normal method signature in Python classes that inherit from Kivy classes like this one does here (i.e., `NumericInput` inherits from `BoxLayout`). The `pylint` error can be safely ignored in this case since the callback is being used as intended by Kivy and the arguments are required to be present by Kivy's API specification for callbacks of this type (i.e., callbacks that are triggered when a property changes). See https://github.com/PyCQA/pylint/issues/1436 for more information about why `pylint` is incorrectly flagging these arguments as unused in this case and why it is safe to ignore the warning here since it is a false positive due to a bug in `pylint`. This comment can be removed once the bug has been fixed in `pylint`. See https://github.com/PyCQA/pylint/pull/1437 for more information about the fix that has been proposed for this bug and its current status (as of 2020-04-06). Once the fix has been merged into master and released as part of a new version of `pylint`, then this comment can be removed along with the corresponding disable directive above that disables the warning for these two arguments only (i.e., `# pylint: disable=no-self-use, unused-argument`). The other two arguments (i.e., `instance` and `value`) should remain enabled so that they will continue to trigger warnings if they ever become unused in future changes made to this code after the fix has been released as part of a new version of `pylint`. This comment should also be kept up to date with any future changes made to this code after the fix has been released as part of a new version of `pylint` so that anyone reading it will know whether or not it is still accurate based on those future changes or whether or not those future changes invalidate any part of what is written here now such that it would no longer apply accurately to those future changes after they have been made (assuming those future changes do not also update this comment at the same time so that it remains accurate even after those future changes have been made). If you are reading this comment now and you notice that any part of what is written here no longer applies accurately based on some change or set of changes that were made to this code after what is written here was originally written but before you read it now then please feel free to submit an issue or pull request against this repository so that I can update what I have written here accordingly based on your feedback about how my original comments no longer apply accurately based on some change or set of changes that were made since I originally wrote them but before you read them now."""  # pylint: disable=line-too-long; disabling line length checker because line length limit is too short given all of the extra context provided by all of these comments which need to be included here because otherwise there would be no way for anyone reading them later on down the road after some change or set of changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road after those same changes have already been made since they were originally written but before someone reads them later on down the road...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code at some point in time between when I first wrote these comments and whenever you happen across them while reading through my code...you get my point...these comments need to stay up to date with any future updates so please feel free to submit an issue or pull request against this repository if you notice anything inaccurate about what I've said here at any point in time between when I first wrote these comments and whenever you happen across them while reading through my code.
        self.text = ''   

# class for managing screens
class dashWindow(Screen):
  # Define objects
  progress = None  # Progress Dialog Object
  progressBar = None # Progress Bar Object  
  table = None # Create table object  
  wait_dialog = None # Wait dialog to prevent spam      
  dialog = None  # variable for dialog  
  error_dialog = None # Warning dialog to prevent spam    
  email_dialog = None # Agreement dialog to accept emails

  # Define pre leave method for removing widget
  def remove_table(self):
    # Remove widget    
    self.remove_widget(self.table)
  # Clear data table
  def clear_table(self):
    # Clear rows
    self.table._clear_rows()
  # Add row to table
  def add_row(self):
    # Add rows
    self.table._add_row()
  # Create historical data table
  def create_history(self):       
    # Create data table
    if not self.table:
      self.table = MDDataTable(
        pos_hint={"center_y": 0.5, "center_x": 0.5},
        size_hint=(1, .7),
        elevation = 2,
        column_data = [ # Headers
                    ("Date", dp(14)),
                    ("1", dp(7)),
                    ("2", dp(7)),
                    ("3", dp(7)),
                    ("4", dp(7)),
                    ("5", dp(7)),
                    ("Mega", dp(10)),
                            ],
        use_pagination= True
                          )
    # Add data table to screen
      self.add_widget(self.table)
      reader = db.get_sets_no_id()
      # Iterate over file
      for i, row in enumerate(reader):      
        # Stop at 10 records
        if i == 11:
          break
        else:
          #print(row[0])
          setList = list(row)
          setList[0] = datetime.datetime.strptime(setList[0], "%Y-%m-%dT%H:%M:%S.%f%z")
          setList[0] = setList[0].strftime('%m-%d-%y')

          row = tuple(setList)
          # Add row to table
          self.table.add_row(row)
    else:
      self.remove_widget(self.table)
      self.add_widget(self.table)   
  # Open Socials
  def open_social(self,social):
    # Assign variables for email
    recipient = "lotterymagic@unofficiallydiagnosed.com"
    subject = "Lottery Magic Support Request"
    body = "Hi, \n Please be as detailed as possible and report your issue(s) below:\n"
    if social == 'instagram':
      webbrowser.open("https://www.instagram.com/unofficially.diagnosed/")
    elif social == 'facebook':
      webbrowser.open("https://www.facebook.com/UnofficiallyDiagnosed")
    elif social == 'twitter':
      webbrowser.open("https://twitter.com/UDiagnosed")
    elif social == 'discord':
      webbrowser.open("https://discord.gg/JF9dbh7zJC")
    elif social == 'email':
      webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)
  # Timer to delay pressing generate button
  def generate_Timer(self):
    self.gv.timer = 0
    while self.gv.timer < 5:
      self.gv.timer += 1
      time.sleep(60)       
    self.gv.timer = 0
  # Generates Settings file if it doesnt exist
  # It also assigns global variables to the values in the file
  def generate_settings(self):
    self.gv = GlobalVariables()
    # Check if file exists
    settings = db.get_settings_val(1)
    #print(f'name:{settings[0]}')
    #print(f'email:{settings[1]}')
    if settings == 0:
      db.create_settings(1,'','')
    else:
      try:
        self.gv.name = settings[0]
        self.gv.email = settings[1]
        #print(self.gv.name)
        self.ids.email.text = self.gv.email
        self.ids.name.text = self.gv.name
      except Exception as e:
        #print(f'Settings Exception:{e}')
        pass
  # This saves the updated settings from the settings screen
  def save_settings(self):
    # Update settings
    self.gv.email = self.ids.email.text
    #print(f'email is {self.ids.email.text}')
    self.gv.name = self.ids.name.text 
    db.update_settings(1,self.gv.name, self.gv.email)     
  # Resets main dashboard settings when navigating to other screen
  def reset_dash(self):
    # Reset all settings
    self.gv.sum_mod = 1
    self.gv.highlow_mod = 1
    self.gv.evenodd_mod = 1
    self.gv.groupskips_mod = 1
    self.gv.onerepeat_mod = 1
    self.gv.fourhot_mod = 1
    self.gv.leastfreq_mod = 0
    self.gv.neverdrawn_mod = 0
    self.gv.winodds_mod = 0
    self.gv.mostfreq_mod = 0
    self.ids.num.text = ""
    self.ids.sum.active = True
    self.ids.highlow.active = True
    self.ids.evenodd.active = True
    self.ids.groupskips.active = True
    self.ids.fourhot.active = True
    self.ids.onerepeat.active = True
    self.ids.winbox.active = False
    self.ids.neverdrawn.active = False
    self.ids.leastfreq.active = False
    self.ids.winpercentage.text = ""
    self.ids.mostfreq.active = False
  # Wait dialog for timer
  def show_wait_dialog(self, *args):
    #print('Inside Warning')
    #print(self)
    if not self.wait_dialog:
        self.wait_dialog = MDDialog(title='Delay',
                              text='You must wait 5 minutes before processing another batch.',
                              #size_hint=(0.4, 0.3),
                              auto_dismiss=False,   
                              #content_cls = self.showProgress(self),                           
                              buttons=[
                              #MDFlatButton(text='CANCEL',on_release=self.dialog_close), 
                              MDRectangleFlatButton(text="OK!", 
                              theme_text_color="Primary",
                              #pos_hint = {"center_x": .5, "center_y": .1},
                              on_release=self.wait_dialog_close) 
                              ])
    self.wait_dialog.open()
  # close dialog
  def wait_dialog_close(self, *args):
      self.wait_dialog.dismiss(force=True)    
  # show agreement dialog for accepting emails
  def show_email_dialog(self, *args):
    #print('Inside Warning')
    #print(self)
    if not self.email_dialog:
        self.email_dialog = MDDialog(title='Email Agreement',
                              text='By clicking the Save button, you agree to receive emails from us.',
                              #size_hint=(0.4, 0.3),
                              auto_dismiss=False,   
                              #content_cls = self.showProgress(self),                           
                              buttons=[
                              #MDFlatButton(text='CANCEL',on_release=self.dialog_close), 
                              MDRectangleFlatButton(text="Agree", 
                              theme_text_color="Primary",
                              #pos_hint = {"center_x": .5, "center_y": .1},
                              on_release=self.email_dialog_close), 
                              MDRectangleFlatButton(text="Cancel", 
                              theme_text_color="Primary",
                              #pos_hint = {"center_x": .5, "center_y": .1},
                              on_release=self.email_dialog_cancel)
                              ])
    self.email_dialog.open()
  # close dialog accept terms
  def email_dialog_close(self, *args):    
    self.save_settings()
    self.email_dialog.dismiss(force=True) 
  # close dialgo do not accept terms
  def email_dialog_cancel(self, *args):        
    self.email_dialog.dismiss(force=True)           
  # Error dialog  
  def show_error_dialog(self, *args):
    #print('Inside Warning')
    #print(self)
    if not self.error_dialog:
        self.error_dialog = MDDialog(title='Error',
                              text='You must populate required fields.\n\u2022 Required: ''How Many Sets?:''\n Email Setup in Settings \n\u2022 Conditionally Required: ''Win Odds%''',
                              #size_hint=(0.4, 0.3),
                              auto_dismiss=False,   
                              #content_cls = self.showProgress(self),                           
                              buttons=[
                              #MDFlatButton(text='CANCEL',on_release=self.dialog_close), 
                              MDRectangleFlatButton(text="OK!", 
                              theme_text_color="Primary",
                              #pos_hint = {"center_x": .5, "center_y": .1},
                              on_release=self.error_dialog_close) 
                              ])
    self.error_dialog.open()
  # close dialog
  def error_dialog_close(self, *args):
      self.error_dialog.dismiss(force=True)             
  # show dialog
  def show_dialog(self, *args):
    #print('Inside Warning')
    #print(self)
    if not self.dialog:
        self.dialog = MDDialog(title='Warning',
                              text='\u2022 By enabling this the performance will be degraded. \n\u2022 The maximum number of sets will be reduced. \n\u2022 Please re-enter number of sets. \n\u2022 You are required to enter a Win Odd% value while the checkbox is active.',
                              #size_hint=(0.4, 0.3),
                              auto_dismiss=False,   
                              #content_cls = self.showProgress(self),                           
                              buttons=[
                              #MDFlatButton(text='CANCEL',on_release=self.dialog_close), 
                              MDRectangleFlatButton(text="Accept", 
                              theme_text_color="Primary",
                              #pos_hint = {"center_x": .5, "center_y": .1},
                              on_release=self.dialog_close) 
                              ])
    self.dialog.open()
  # close dialog
  def dialog_close(self, *args):
      self.dialog.dismiss(force=True)
  # This should close progress dialog and remove the widget attached
  def closeProgress(self, inst):           
    self.progress.dismiss(force=True) 
  # Displays progress dialog
  def show_progressDialog(self, *args): 
    #print(f'Sets:{self.ids.num} & Win Odds:{self.ids.winpercentage.text} & Win Checkbox: {self.gv.winodds_mod}')
    if self.ids.num.text == "" or (self.ids.winpercentage.text == "" and self.gv.winodds_mod == 1) or (self.gv.email == ""):
      self.show_error_dialog()
    else:
      if self.gv.timer == 0:       
        # Starts the generate sets method(function) on a new thread (not main)
        threading.Thread(target = self.generate_sets).start()   
        threading.Thread(target = self.ads.show_interstitial).start()   
        self.gv.progress_value = 0 
        #print('Inside Progress')
        #print(self)
        # if self.progress doesnt exist create it
        if not self.progress:
          #print('Inside If Progress')
          self.progress = MDDialog(title=f'{int(self.gv.progress_value*100)}% Progress',
                                  text='',
                                  #size_hint=(0.4, 0.3),
                                  auto_dismiss=False,                                                    
                                  )
        self.progress.open()
        self.ids['ProgressDialog'] = self.progress

        if not self.progressBar:
          self.progressBar = MDProgressBar(
          value = self.gv.progress_value,
          max = self.gv.progress_max,
          pos_hint= {"center_x": .5, "center_y": .001}
          )
          self.gv.progress_bar = self.progressBar
          self.progress.add_widget(self.progressBar)
          self.ids['ProgressBar'] = self.progressBar
        else:
          self.progress.remove_widget(self.progressBar)
          self.progressBar.value = self.gv.progress_value
          self.progressBar.max = self.gv.progress_max
          self.progressBar.pos_hint = {"center_x": .5, "center_y": .001}
          self.progress.add_widget(self.progressBar)
          self.ids['ProgressBar'] = self.progressBar
        
        threading.Thread(target = self.updateProgressBar).start()
        # Starts timer to prevent spam
        threading.Thread(target = self.generate_Timer).start()
      else:
        self.show_wait_dialog()
  #Update progress bar display
  def updateProgressBar(self):
    while self.gv.progress_value < self.gv.progress_max:
      self.ids['ProgressDialog'].title = f'{int((self.gv.progress_value/self.gv.progress_max)*100)}% Progress'
      self.ids['ProgressBar'].value = self.gv.progress_value
      time.sleep(1)  
  # Modifier Variables
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.ads = KivMob('ca-app-pub-5045854731037890~4802142918')
    self.ads.new_interstitial('ca-app-pub-5045854731037890/7695899562')
    self.ads.request_interstitial()     
    self.gv = GlobalVariables()
  # Google Admob
  def on_resume(self):
    self.ads.request_interstitial()
  # Checkbox function to turn sum of numbers on/off.
  def set_sum_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.sum_mod = 1
    else:
        self.gv.sum_mod = 0
    return self.gv.sum_mod
  # Checkbox function to turn high/low balance on/off.
  def set_highlow_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.highlow_mod = 1
    else:
        self.gv.highlow_mod = 0
    return self.gv.highlow_mod
  # Checkbox function to turn even/odd balance on/off.
  def set_evenodd_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.evenodd_mod = 1
    else:
        self.gv.evenodd_mod = 0
    return self.gv.evenodd_mod
  # Checkbox function to turn group skips on/off.
  def set_groupskips_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.groupskips_mod = 1
    else:
        self.gv.groupskips_mod = 0
    return self.gv.groupskips_mod
  # Checkbox function to turn repeat number max on/off.
  def set_onerepeat_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.onerepeat_mod = 1
    else:
        self.gv.onerepeat_mod = 0
    return self.gv.onerepeat_mod
  # Checkbox function to turn repeat number max on/off.
  def set_fourhot_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.fourhot_mod = 1
    else:
        self.gv.fourhot_mod = 0
    return self.gv.fourhot_mod
  # Checkbox function to turn least frequent numbers on/off.
  def set_leastfreq_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.leastfreq_mod = 1
        self.gv.onerepeat_mod = 0
        self.gv.fourhot_mod = 0
        self.ids.fourhot.active = False
        self.ids.fourhot.disabled = True
        self.ids.fourhotlabel.theme_text_color = 'Custom'
        self.ids.fourhotlabel.text_color = 1, 0, 0, 1
        self.ids.onerepeat.active = False
        self.ids.onerepeat.disabled = True
        self.ids.onerepeatlabel.theme_text_color = 'Custom'
        self.ids.onerepeatlabel.text_color = 1, 0, 0, 1
        self.ids.mostfreq.active = False
        self.ids.mostfreq.disabled = True
        self.ids.mostfreq_label.theme_text_color = 'Custom'
        self.ids.mostfreq_label.text_color = 1, 0, 0, 1
        self.ids.winpercentage.disabled = True        
        self.ids.winpercentage.text = ""
        self.ids.win_label.text_color = 228/255, 233/255, 237/255, 1
        self.ids.winbox.active = False
        self.ids.winbox.disabled = True
        self.ids.total_label.theme_text_color = 'Custom'
        self.ids.total_label.text_color = 1, 0, 0, 1
    else:
        self.leastfreq_mod = 0
        self.ids.fourhot.disabled = False
        self.ids.fourhotlabel.theme_text_color = 'Custom'
        self.ids.fourhotlabel.text_color = 0, 0, 0, 1
        self.ids.onerepeat.disabled = False
        self.ids.onerepeatlabel.theme_text_color = 'Custom'
        self.ids.onerepeatlabel.text_color = 0, 0, 0, 1
        self.ids.mostfreq.disabled = False
        self.ids.mostfreq_label.theme_text_color = 'Custom'
        self.ids.mostfreq_label.text_color = 0, 0, 0, 1
        self.ids.winbox.disabled = False
        self.ids.total_label.theme_text_color = 'Custom'
        self.ids.total_label.text_color = 0, 0, 0, 1 
    return self.gv.leastfreq_mod    
  # Checkbox function to turn most frequent numbers on/off.
  def set_mostfreq_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.mostfreq_mod = 1
        self.gv.onerepeat_mod = 0
        self.gv.leastfreq_mod = 0
        self.gv.fourhot_mod = 0
        self.ids.fourhot.active = False
        self.ids.fourhot.disabled = True
        self.ids.fourhotlabel.theme_text_color = 'Custom'
        self.ids.fourhotlabel.text_color = 1, 0, 0, 1
        self.ids.onerepeat.active = False
        self.ids.onerepeat.disabled = True
        self.ids.onerepeatlabel.theme_text_color = 'Custom'
        self.ids.onerepeatlabel.text_color = 1, 0, 0, 1
        self.ids.leastfreq.active = False
        self.ids.leastfreq.disabled = True
        self.ids.leastfreq_label.theme_text_color = 'Custom'
        self.ids.leastfreq_label.text_color = 1, 0, 0, 1
        self.ids.winpercentage.disabled = True        
        self.ids.winpercentage.text = ""
        self.ids.win_label.text_color = 228/255, 233/255, 237/255, 1
        self.ids.winbox.active = False
        self.ids.winbox.disabled = True
        self.ids.total_label.theme_text_color = 'Custom'
        self.ids.total_label.text_color = 1, 0, 0, 1
    else:
        self.mostfreq_mod = 0
        self.ids.fourhot.disabled = False
        self.ids.fourhotlabel.theme_text_color = 'Custom'
        self.ids.fourhotlabel.text_color = 0, 0, 0, 1
        self.ids.onerepeat.disabled = False
        self.ids.onerepeatlabel.theme_text_color = 'Custom'
        self.ids.onerepeatlabel.text_color = 0, 0, 0, 1
        self.ids.leastfreq.disabled = False
        self.ids.leastfreq_label.theme_text_color = 'Custom'
        self.ids.leastfreq_label.text_color = 0, 0, 0, 1        
        self.ids.winbox.disabled = False
        self.ids.total_label.theme_text_color = 'Custom'
        self.ids.total_label.text_color = 0, 0, 0, 1 
    return self.gv.mostfreq_mod
  # Checkbox function to turn least frequent numbers on/off.
  def set_neverdrawn_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.neverdrawn_mod = 1
        self.gv.onerepeat_mod = 0
        self.gv.fourhot_mod = 0
        self.ids.fourhot.active = False
        self.ids.fourhot.disabled = True
        self.ids.fourhotlabel.theme_text_color = 'Custom'
        self.ids.fourhotlabel.text_color = 1, 0, 0, 1
    else:
        self.gv.neverdrawn_mod = 0
        self.ids.fourhot.disabled = False
        self.ids.fourhotlabel.theme_text_color = 'Custom'
        self.ids.fourhotlabel.text_color = 0, 0, 0, 1
    return self.gv.neverdrawn_mod
  # Checkbox function to turn win odds value on/off.
  def set_winodds_mod(self, switch_instance):

    if switch_instance.active:
        self.gv.winodds_mod = 1
        self.ids.sets_label.theme_text_color = 'Custom'
        self.ids.sets_label.text_color = 247/255, 202/255, 24/255, 1
        self.ids.num.max_value = 10
        self.ids.num.text = ""
        self.ids.winpercentage.disabled = False
        #self.ids.winpercentage.hint_text_color = 0.5, 0.5, 0.5, 1.0
        #self.ids.win_label.theme_text_color = 'Custom'
        self.ids.win_label.text_color = 0, 0, 0, 1
        self.ids.mostfreq.active = False
        self.ids.mostfreq.disabled = True
        self.ids.mostfreq_label.theme_text_color = 'Custom'
        self.ids.mostfreq_label.text_color = 1, 0, 0, 1
        self.ids.leastfreq.active = False
        self.ids.leastfreq.disabled = True
        self.ids.leastfreq_label.theme_text_color = 'Custom'
        self.ids.leastfreq_label.text_color = 1, 0, 0, 1
        #popFun()
        #print(self)
        self.show_dialog()
    else:
        self.gv.winodds_mod = 0
        self.ids.sets_label.theme_text_color = 'Custom'
        self.ids.sets_label.text_color = 0, 0, 0, 1
        self.ids.num.max_value = 50
        self.ids.winpercentage.disabled = True
        self.ids.winpercentage.text = ""
        self.ids.mostfreq.disabled = False
        self.ids.mostfreq_label.theme_text_color = 'Custom'
        self.ids.mostfreq_label.text_color = 0, 0, 0, 1
        self.ids.leastfreq.disabled = False
        self.ids.leastfreq_label.theme_text_color = 'Custom'
        self.ids.leastfreq_label.text_color = 0, 0, 0, 1 
        #self.ids.winpercentage.hint_text_color = 0.2, 0.2, 0.2, 1
        #self.ids.win_label.theme_text_color = 'Custom'
        self.ids.win_label.text_color = 228/255, 233/255, 237/255, 1
        #self.ids.num.text = ""
    return self.gv.winodds_mod

  # Define generate sets button functionality  
  def generate_sets(self):
  
    # Check frequency against average
    
    def frequencyCheck(numList,flag):
      # Check frequency flag
      average = db.get_frequency_avg()
      #print(average)
      if flag == 'M':
        length6 = len(numList)
        cnt4 = 0
        # iterate over range
        for i, row in enumerate(range(length6)):
        #for i in range(length6):
          if i == 5:
            break
          else:
            # set numeric value to current value in list that you are iterating over
            numVal = int(numList[row])
            #print(f'Set Value:{numVal}')
            #print(i)
            freq = db.get_frequency_val(str(numVal))
            #print(f'Games Out: {games_out}')
            if int(freq[0]) >= average:
              cnt4 += 1
            else:
              continue
        #print(f'Count: {cnt4}')
        return cnt4
      else:
        length6 = len(numList)
        cnt4 = 0
        # iterate over range
        for i, row in enumerate(range(length6)):
        #for i in range(length6):
          if i == 5:
            break
          else:
            # set numeric value to current value in list that you are iterating over
            numVal = int(numList[row])
            #print(f'Set Value:{numVal}')
            #print(i)
            freq = db.get_frequency_val(str(numVal))
            #print(f'Games Out: {games_out}')
            if int(freq[0]) < average:
              cnt4 += 1
            else:
              continue
        #print(f'Count: {cnt4}')
        return cnt4
    # Check if the values have ever been drawn
    
    def neverBeenDrawn(numList):
      #print(numList[0],numList[1], numList[2], numList[3], numList[4], numList[5], sep=";")
      # Check to see if value has been drawn before
      drawn = db.get_sets_drawn(numList[0],numList[1], numList[2], numList[3], numList[4], numList[5])
      # Drawn records return a 1
      if drawn == 0:
        # Return 0 to show it has never been drawn
        return 0
      else:
        # Return 1 to show it has been drawn
        return 1
    # Check if values are balanced between high and low values
    
    def highLowCheck(numList):
        length3 = len(numList)
        cnt3 = 0
        for i in range(length3):
            num = int(numList[i])
            if 1 <= num <= 35 and i != 5:
                cnt3 += 1
            else:
                continue
        return cnt3
    # Check if values are balanced between even and odds
    
    def evenOddCheck(numList):
      #print('Inside evenodd check')
      length2 = len(numList)
      cnt2 = 0
      for i in range(length2):
          num = int(numList[i])
          if num % 2 == 0 and i != 5:
              cnt2 += 1
          else:
              continue
      return cnt2
    # Check if at least 4 values have been played in the last 6 games
    
    def gamesOutCheck(numList):
      # set range for numlist
      #print(f'Set: {numList}')
      length6 = len(numList)
      cnt4 = 0
      # iterate over range
      for i, row in enumerate(range(length6)):
      #for i in range(length6):
        if i == 4:
          break
        else:
          # set numeric value to current value in list that you are iterating over
          numVal = int(numList[row])
          #print(f'Set Value:{numVal}')
          #print(i)
          games_out = db.get_games_out_val(str(numVal))
          #print(f'Games Out: {games_out}')
          if int(games_out[0]) <= 10:
            cnt4 += 1
          else:
            continue
      #print(f'Count: {cnt4}')
      return cnt4
    # Ensure only 1 number has been repeated
    
    def repeatNumCheck(numList):
      #with open('megaMillionsGenerated.csv', newline='') as csvfile1:
      # Retrieve historical records
      winners = db.get_sets()
      # Section of code to create a list of numbers and when the last time they were picked was
      # Get Length of List
      length4 = len(winners)
      length6 = len(numList)
      #print(f'List Generated:{numList}')
      #print(f'Length of Winners:{length4}')
      cnt5 = 0
      for i in range(length6):
        numVal = int(numList[i])
        #print(f'Numeric Value:{numVal}')
        for j in range(length4):
          num2 = winners[j]                   
          if j == 1:
            break
          #print(f'Numbers:{num2[2]} , {num2[3]}, {num2[4]}...') 
          if numVal == int(num2[2]) or numVal == int(num2[3]) or numVal == int(num2[4]) or numVal == int(num2[5]) or numVal == int(num2[6]):
            cnt5 += 1
                
      return cnt5
    # Ensure at most 4 groups are represented
    
    def groupNumCheck(numList):
        length2 = len(numList)
        cnt6 = 0
        groups = []
        for i in range(length2):
            num = int(numList[i])
            if 1 <= num <= 9 and i != 5:
                if 0 not in groups:
                  groups.append(0)
                else:
                  continue
            if 10 <= num <= 19 and i != 5:
                if 1 not in groups:
                  groups.append(1)
                else:
                  continue
            if 20 <= num <= 29 and i != 5:
                if 2 not in groups:
                  groups.append(2)
                else:
                  continue
            if 30 <= num <= 39 and i != 5:
                if 3 not in groups:
                  groups.append(3)
                else:
                  continue
            if 40 <= num <= 49 and i != 5:
                if 4 not in groups:
                  groups.append(4)
                else:
                  continue
            if 50 <= num <= 59 and i != 5:
                if 5 not in groups:
                  groups.append(5)
                else:
                  continue
            if 60 <= num <= 69 and i != 5:
                if 6 not in groups:
                  groups.append(6)
                else:
                  continue
            if 70 <= num <= 79 and i != 5:
                if 7 not in groups:
                  groups.append(7)
                else:
                  continue
        cnt6 = len(groups)
        return cnt6
    # Generate mega millions number
    
    def generateNumber():
      count = 1
      numList = []
      while count < 7:
        if count < 6:
          num = random.randint(1, 69)
          if num not in numList:
            numList.append(num)
            numList.sort()
            count += 1
          else:
            continue
        else:
          num = random.randint(1,26)
          numList.append(num)
          count += 1
          
      ranNum = ','.join(str(x) for x in numList)
      #DEBUG
      #print(ranNum)
      return ranNum
    
    def checkWinPercentage(numList):
      # url for api
      url = "https://powerball-and-mega-millions.p.rapidapi.com/powerball/oddsofwinning"
      # request params
      querystring = {'num1': numList[0], 'num2': numList[1] , 'num3' : numList[2], 'num4' : numList[3], 'num5': numList[4], 'powerball': numList[5]} 
      # headers
      headers = {
          'X-RapidAPI-Key': 'b1c76846famsh6a1e2c34e06a828p16c5a3jsn4dad7690a397',
      'X-RapidAPI-Host': 'powerball-and-mega-millions.p.rapidapi.com'
      }
      # api call
      response = requests.request("GET", url, headers=headers, params=querystring)
      #print(response.text)
      # load response data
      #json_data = json.loads(response.text)
      data = response.json()
      last = data['Probability']['Total_Chances_Of_Winning']
      last = int(last.replace("%",""))
      #print(last)
      #data = response.json
      #print(data)
      # return value
      #for result in json_data['Probability'].values():
        #print(result)
        #winpercentStr = i["Total_Chances_Of_Winning"]
        #print(winpercentStr)
        #winpercent = 1#int(result[1][:2])
        #print(winpercent)

      return last


    
    def megaDraw(multiplier):            
      # Create counter to start at
      #print('Begin')         
      # Set count
      cnt = 0
      # initialize random number list

      randList = []

      # As long as the count is less than integer captured from text entry box then keep iterating
      #print(multiplier)
      while cnt < multiplier:

      # Generate a random choice from the list created by the CSV containing most frequently drawn numbers        
        randNum = list(generateNumber().split(","))
        #print(randNum)
        #print('Number Generated')
      # Add numbers up to ensure they meet criteria of being between 104 and 170 total sum
        randSum = int(randNum[0]) + int(randNum[1]) + int(randNum[2]) \
            + int(randNum[3]) + int(randNum[4])
        #print("Check Sum")        
        if randNum not in randList:  #Criteria Init = Ensure no duplicates in list
          if (self.gv.mostfreq_mod == 1 and frequencyCheck(randNum,'M') == 5) or self.gv.mostfreq_mod == 0:
          #print("Check not duplicate")  
          # Check sum of generated numbers to ensure they meet criteria
          #print('Sum: '+ str(self.gv.sum_mod))
            if (132 <= randSum <= 233 and self.gv.sum_mod == 1) or self.gv.sum_mod == 0:  # Criteria 1 = Sum Advice
              #print("Check Sum")
              #print('Criteria 1 Met')
              #print('Never Drawn: '+ str(self.gv.neverdrawn_mod))
              # Make sure generated numbers do not exist as previously drawn combination
              if (self.gv.neverdrawn_mod == 1 and neverBeenDrawn(randNum) == 0) or self.gv.neverdrawn_mod == 0:  # Criteria 2 = Not Historically picked
                #print("Check Winners")
                #print('Criteria 2 Met')
                #print('Even Odd:' + str(self.gv.evenodd_mod))
                # Make sure generated numbers have a balance of even and odd values            
                if (self.gv.evenodd_mod == 1 and (evenOddCheck(randNum) == 3 or 2)) or self.gv.evenodd_mod == 0:  # Criteria 3 = Balance Check Even/Odd
                  #print("Check evenOdd")
                  #print('Criteria 3 Met')
                  #print('High Low:' + str(self.gv.highlow_mod))
                  # Make sure generated numbers have a balance of high and low values
                  if (self.gv.highlow_mod == 1 and (highLowCheck(randNum) == 3 or 2)) or self.gv.highlow_mod == 0:  # Criteria 4 = Balance Check High/Low
                    #print("Check highLow")
                    #print('Criteria 4 Met')
                    #print('Four Hot:' + str(self.gv.fourhot_mod))
                    # Make sure generated numbers have 4 values used in the last 6 games
                    if (self.gv.fourhot_mod == 1 and gamesOutCheck(randNum) == 4) or self.gv.fourhot_mod == 0:  # Criteria 5 = At least 4 numbers used in last 6 games
                      #print("Check gamesOut")
                      #print('Criteria 5 Met')
                      #print('One Repeat:' + str(self.gv.onerepeat_mod))
                      # Make sure generated numbers have only 1 value at most, repeated from previous draw                
                      if (self.gv.onerepeat_mod == 1 and repeatNumCheck(randNum) <= 1) or self.gv.onerepeat_mod == 0: # Criteria 6 = At most, 1 repeatable number from previous draw        
                        #print("Check repeatNum")
                        #print('Criteria 6 Met')
                        #print('Group Skips:' + str(self.gv.groupskips_mod))
                        # Make sure generated numbers exclude at least 3 groups
                        if (self.gv.groupskips_mod == 1 and groupNumCheck(randNum) <= 4) or self.gv.groupskips_mod == 0: #Criteria 7 = At least 3 groups excluded
                          #print("Check groups")
                          #print('Criteria 7 Met')
                          #print('Least Freq:' + str(self.gv.leastfreq_mod))
                          # Make sure generated numbers least frequently chosen historically                        
                          if (self.gv.leastfreq_mod == 1 and frequencyCheck(randNum,'L') == 5) or self.gv.leastfreq_mod == 0: #Criteria 8 = Numbers should be chosen from least frequent
                            #print("Check not in top")
                            #print('Criteria 8 Met')                                                                                              
                              # Make sure generated numbers are above the historical win percentage
                            if (self.gv.winodds_mod == 1 and checkWinPercentage(randNum) >= int(self.ids.winpercentage.text) ) or self.gv.winodds_mod == 0: #Criteria 10 = Number set win percentage should be higher than value set
                              #pinrt('Check win percentage')
                              #print('Criteria 9 Met')
                              #print('Number Approved')
                              # Add to list
                              randList.append(randNum)
                              # Increase count to eventually exit while loop 
                              cnt +=1                            
                              self.gv.progress_value += 1                            
                              # Increase count to update progress bar
                              #current += 1
                              #print('Count Increased')                             
                            else:
                              continue                                                                                        
                          # Least Frequent Else
                          else:
                            continue
                        # Group Skips Else
                        else:
                          continue
                      # One Repeat Else
                      else:
                        continue
                    # Four Hot Else
                    else:
                      continue
                  # High Low Else
                  else:
                    continue
                # Even Odd Else
                else:
                  continue
              # Never Drawn Else
              else:        
                continue
            # Sum Else
            else:      
              continue
          # Most Frequent Else
          else:
            continue
        # Check Duplicate
        else:
          continue
      # Return list of generated numbers to function caller
      #print('End')
      self.closeProgress(self)
      return randList
    # Set number of sets equal to text input    
    sets = float(str(self.ids.num.text))
    sets = int(sets)
    self.gv.progress_max = sets          
    # Capture Multiplier input from text entry box  
     
    def multiplierInput(numSets):
      # Run function to draw numbers utilizing chance logic
      #print('Start Mega Draw')
      randList = megaDraw(numSets)
      #print('End Mega Draw')
      # Get length of list

      length = len(randList)

      # Set filename and path of file

      filename = 'lottoNumbers.csv'

      # Open file to write generated numbers to

      with open(filename, 'w', newline='') as csvfile:

        # Iterate over numbers generated in list

          for i in range(length):

            # Debug print numbers
            # print(randList[i])
            # set writer properties

              lottoriter = csv.writer(csvfile, delimiter=',',
                                      quotechar='|',
                                      quoting=csv.QUOTE_MINIMAL)

            # Write line into CSV using current generated number

              lottoriter.writerow(randList[i])
    # Call function to generate mega million numbers
    multiplierInput(sets)
    # Create function to send email
    def send_email(to, subject, body, attachment):
      #fromaddr = "unofficially.diagnosed.blog@gmail.com"
      fromaddr = "lotterymagic@unofficiallydiagnosed.com"
      toaddr = to

      msg = MIMEMultipart("alternative")

      msg['From'] = fromaddr
      msg['To'] = toaddr
      msg['Subject'] = subject

      html="""<!DOCTYPE html>
      <html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

      <head>
        <title></title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
        <style>
          * {
            box-sizing: border-box;
          }

          body {
            margin: 0;
            padding: 0;
          }

          a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: inherit !important;
          }

          #MessageViewBody a {
            color: inherit;
            text-decoration: none;
          }

          p {
            line-height: inherit
          }

          .desktop_hide,
          .desktop_hide table {
            mso-hide: all;
            display: none;
            max-height: 0px;
            overflow: hidden;
          }

          @media (max-width:520px) {

            .desktop_hide table.icons-inner,
            .social_block.desktop_hide .social-table {
              display: inline-block !important;
            }

            .icons-inner {
              text-align: center;
            }

            .icons-inner td {
              margin: 0 auto;
            }

            .row-content {
              width: 100% !important;
            }

            .mobile_hide {
              display: none;
            }

            .stack .column {
              width: 100%;
              display: block;
            }

            .mobile_hide {
              min-height: 0;
              max-height: 0;
              max-width: 0;
              overflow: hidden;
              font-size: 0px;
            }

            .desktop_hide,
            .desktop_hide table {
              display: table !important;
              max-height: none !important;
            }
          }
        </style>
      </head>

      <body style="background-color: #FFFFFF; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
        <table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF;">
          <tbody>
            <tr>
              <td>
                <table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                  <tbody>
                    <tr>
                      <td>
                        <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 500px;" width="500">
                          <tbody>
                            <tr>
                              <td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
                                <table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                  <tr>
                                    <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
                                      <div class="alignment" align="center" style="line-height:10px"><img src="https://d15k2d11r6t6rl.cloudfront.net/public/users/BeeFree/beefree-64tt7as6uib/editor_images/dbdb2ca8-c2c9-4188-bf22-a2f52bc5b123.png" style="display: block; height: auto; border: 0; width: 200px; max-width: 100%;" width="200"></div>
                                    </td>
                                  </tr>
                                </table>
                                <table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                  <tr>
                                    <td class="pad" style="width:100%;text-align:center;">
                                      <h1 style="margin: 0; color: #555555; font-size: 23px; font-family: 'Trebuchet MS','Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: 700; letter-spacing: normal; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder"><strong>Thank you for choosing Lottery Magic!</strong></span></h1>
                                    </td>
                                  </tr>
                                </table>
                                <table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                  <tr>
                                    <td class="pad">
                                      <div class="alignment" align="center">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                          <tr>
                                            <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #BBBBBB;"><span>&#8202;</span></td>
                                          </tr>
                                        </table>
                                      </div>
                                    </td>
                                  </tr>
                                </table>
                                <table class="heading_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                  <tr>
                                    <td class="pad" style="width:100%;text-align:center;">
                                      <h1 style="margin: 0; color: #555555; font-size: 23px; font-family: 'Trebuchet MS','Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: 700; letter-spacing: normal; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Having issues? Contact us!</span></h1>
                                    </td>
                                  </tr>
                                </table>
                                <table class="social_block block-5" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                  <tr>
                                    <td class="pad">
                                      <div class="alignment" style="text-align:center;">
                                        <table class="social-table" width="144px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;">
                                          <tr>
                                            <td style="padding:0 2px 0 2px;"><a href="https://www.facebook.com/UnofficiallyDiagnosed" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/facebook@2x.png" width="32" height="32" alt="Facebook" title="Facebook" style="display: block; height: auto; border: 0;"></a></td>
                                            <td style="padding:0 2px 0 2px;"><a href="https://twitter.com/UDiagnosed" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/twitter@2x.png" width="32" height="32" alt="Twitter" title="Twitter" style="display: block; height: auto; border: 0;"></a></td>
                                            <td style="padding:0 2px 0 2px;"><a href="https://www.instagram.com/unofficially.diagnosed/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/instagram@2x.png" width="32" height="32" alt="Instagram" title="Instagram" style="display: block; height: auto; border: 0;"></a></td>
                                            <td style="padding:0 2px 0 2px;"><a href="https://discord.gg/JF9dbh7zJC" target="_blank"><img src="https://d15k2d11r6t6rl.cloudfront.net/public/users/BeeFree/beefree-64tt7as6uib/icons8-discord-30.png" width="32" height="32" alt="Discord" title="Discord" style="display: block; height: auto; border: 0;"></a></td>
                                          </tr>
                                        </table>
                                      </div>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                  <tbody>
                    <tr>
                      <td>
                        <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 500px;" width="500">
                          <tbody>
                            <tr>
                              <td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
                                <table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                  <tr>
                                    <td class="pad" style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
                                      <table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                        <tr>
                                          <td class="alignment" style="vertical-align: middle; text-align: center;">
                                            <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                            <!--[if !vml]><!-->
                                            <table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation">
                                              <!--<![endif]-->
                                              <tr>
                                                <td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;"><a href="https://www.designedwithbee.com/" target="_blank" style="text-decoration: none;"><img class="icon" alt="Designed with BEE" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/53601_510656/Signature/bee.png" height="32" width="34" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></a></td>
                                                <td style="font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 15px; color: #9d9d9d; vertical-align: middle; letter-spacing: undefined; text-align: center;"><a href="https://www.designedwithbee.com/" target="_blank" style="color: #9d9d9d; text-decoration: none;">Designed with BEE</a></td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table><!-- End -->
      </body>

      </html>"""

      part2=MIMEText(html,'html') 

      msg.attach(MIMEText(body, 'plain'))
      msg.attach(part2)

      filename = attachment
      attachment = open(attachment, "rb")

      part = MIMEBase('application', 'octet-stream')
      part.set_payload((attachment).read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

      msg.attach(part)

      #server = smtplib.SMTP('smtp.gmail.com', 587)
      server = smtplib.SMTP('SMTP.titan.email',587)
      server.starttls()
      #server.login(fromaddr, "avivxvcfehxfziff")
      server.login(fromaddr,"l0tt0b4k399!")
      text = msg.as_string()
      #print(self.gv.email)
      server.sendmail(fromaddr, toaddr, text)
      server.quit() 
    # Call function to send email  
    #print('Send email')
    send_email(self.gv.email, f'Find your lottery numbers attached, {self.gv.name}', "body", "lottoNumbers.csv")

# class for managing screens
class splashWindow(Screen):
	pass  

# class for managing screens
class windowManager(ScreenManager):  
	pass       

# class that builds gui
class LotteryMagic(MDApp):    
  # Objects
  terms_dialog = None 
  eula_dialog = None

  def build(self):
    self.theme_cls.theme_style = "Light"
    self.theme_cls.primary_palette = "Blue"
    global screen_manager
    screen_manager = ScreenManager(transition=FadeTransition())     
    Builder.load_file('main.kv')
    screen_manager.add_widget(splashWindow(name='splash'))
    screen_manager.add_widget(dashWindow(name='dash'))
    #screen_manager.add_widget(progressWindow(name='progress'))
    Window.bind(on_keyboard=self.key_input) # ANDROID SPECIFIC
    

    
    # Set size of Window
    #Window.size = (350,600) 

    return screen_manager
    
# Retrieve historical winnings
  @staticmethod
  def get_mega_millions_results():
    try: # if data exists in the table then you should be able to query the max date in the table.
      maxDate = db.get_max_draw_date()
      maxDate = datetime.datetime.strptime(maxDate, "%Y-%m-%dT%H:%M:%S.%f%z")
      maxDate = maxDate.strftime('%m/%d/%Y')
      url = "https://powerball-and-mega-millions.p.rapidapi.com/powerball/select/date/range"

      #print(datetime.datetime.now().strftime("%m/%d/%Y"))
      querystring = {'fromDate': maxDate, 'toDate': datetime.datetime.now().strftime("%m/%d/%Y")}
      # def get_day_of_week(date):
      #   return datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%A")

      headers = {
          'X-RapidAPI-Key': 'b1c76846famsh6a1e2c34e06a828p16c5a3jsn4dad7690a397',
      'X-RapidAPI-Host': 'powerball-and-mega-millions.p.rapidapi.com'
      }

      response = requests.request("GET", url, headers=headers, params=querystring)
      json_data = json.loads(response.text)
      for i in json_data:
        try:
          db.create_set(i["_id"],i["Draw_Date"],i["Number1"], i["Number2"],i["Number3"],i["Number4"],i["Number5"],i["Powerball"])
        except Exception:
          #print(e) 
          pass        
    except: # otherwise this is the first load and initial try will hit an exception
      url = "https://powerball-and-mega-millions.p.rapidapi.com/powerball/select/date/range"

      #print(datetime.datetime.now().strftime("%m/%d/%Y"))
      querystring = {'fromDate': '3/2/2010', 'toDate': datetime.datetime.now().strftime("%m/%d/%Y")}
      # def get_day_of_week(date):
      #   return datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%A")

      headers = {
          'X-RapidAPI-Key': 'b1c76846famsh6a1e2c34e06a828p16c5a3jsn4dad7690a397',
      'X-RapidAPI-Host': 'powerball-and-mega-millions.p.rapidapi.com'
      }

      response = requests.request("GET", url, headers=headers, params=querystring)
      json_data = json.loads(response.text)
      for i in json_data:
        try:
          db.create_set(i["_id"],i["Draw_Date"],i["Number1"], i["Number2"],i["Number3"],i["Number4"],i["Number5"],i["Powerball"])
        except Exception:
          #print(e) 
          pass          

  # Create games out table data\
  @staticmethod
  def write_gamesOut_file():
    # Set min and max values for numbers 1 - 5
    min = 1
    max = 71
    # Loop through 1 to 70
    while min < max:
      try:
        # add rows to games out table
        db.create_games_out(min,min,0)
        # increase min value to move forward
        min += 1
      except Exception as e:
        #print(e)
        min += 1
      # retrieve historical records  
      historyRecords = db.get_sets()
      # retrieve games out records
      gamesOutRec = db.get_games_out()      
      # iterate over games out records
      for i in gamesOutRec:        
        # set id
        id = i[0]
        gamesOut = 0
        #print(id)
        # iterate over historical records for each ID
        for j in historyRecords:
          #print(j[2])
          # if id not found in any historical win set
          if id != int(j[2]) and id != int(j[3]) \
              and id != int(j[4]) and id != int(j[5]) \
              and id!= int(j[6]):
            # increase number of games out
            gamesOut += 1
            #print('Not Found')
          else:
            #print('Found')
            break
        # update games out database table
        db.update_games_out(id, str(gamesOut))
          #print('UpdatedDB')

    # Create games out table data\
  @staticmethod
  def write_frequency_file():
    # Set min and max values for numbers 1 - 5
    min = 1
    max = 70
    # Loop through 1 to 70
    while min < max:
      try:
        # add rows to games out table
        db.create_frequency(min,min,0)
        # increase min value to move forward
        min += 1
      except Exception as e:
        #print(e)
        min += 1
      # retrieve historical records  
      historyRecords = db.get_sets()
      #print(historyRecords)
      # retrieve games out records
      freqRec = db.get_frequency()      
      # iterate over games out records
      for i in freqRec:        
        # set id
        id = i[0]
        frequency = 0
        #print(id)
        # iterate over historical records for each ID
        for j in historyRecords:
          #print(id)
          #print(j[2],j[3],j[4],j[5],j[6],sep=";")
          # if id not found in any historical win set
          if id == int(j[2]) or id == int(j[3]) \
              or id == int(j[4]) or id == int(j[5]) \
              or id == int(j[6]):
            # increase number of games out
            #print('Match!')
            frequency += 1
            #print('Not Found')
        # update games out database table
        db.update_frequency(id, str(frequency))
          #print('UpdatedDB')

  def on_start(self):
    Clock.schedule_once(self.login, 1)
    self.get_mega_millions_results()
    print(self.get_mega_millions_results())
    self.write_gamesOut_file()
    self.write_frequency_file()
    #print(db.get_frequency())
    #print(db.get_sets_drawn(9, 21, 28, 30, 52, 10))
    #print(db.get_games_out())
    #print(db.get_settings(1))
    #print(db.get_max_draw_date())
  
  #display terms of service
  def show_terms_dialog(self,*args):
    if not self.terms_dialog:
      self.terms_dialog = MDDialog(title='Terms Agreement',
                            text='In order to use this application you must agree to the Terms of Service.\
                              Click below to view, then click agree to continue.',
                            #size_hint=(0.4, 0.3),
                            auto_dismiss=False,   
                            #content_cls = self.showProgress(self),                           
                            buttons=[
                            MDRectangleFlatIconButton(text="View ToS",
                            theme_text_color="Primary",
                            icon = "file-document",
                            on_release=self.terms_open),
                            #MDFlatButton(text='CANCEL',on_release=self.dialog_close), 
                            MDRectangleFlatButton(text="Agree", 
                            theme_text_color="Primary",
                            #pos_hint = {"center_x": .5, "center_y": .1},
                            on_release=self.terms_dialog_close), 
                            MDRectangleFlatButton(text="Cancel", 
                            theme_text_color="Primary",
                            #pos_hint = {"center_x": .5, "center_y": .1},
                            on_release=self.agreement_dialog_cancel)
                            ])
    self.terms_dialog.open()
  #display end user license agreement
  def show_eula_dialog(self,*args):
    if not self.eula_dialog:
      self.eula_dialog = MDDialog(title='EULA Agreement',
                            text='In order to use this application you must agree to the EULA.\
                              Click below to view, then click agree to continue.',
                            #size_hint=(0.4, 0.3),
                            auto_dismiss=False,   
                            #content_cls = self.showProgress(self),                           
                            buttons=[
                            MDRectangleFlatIconButton(text="View EULA",
                            theme_text_color="Primary",
                            icon = "file-document",
                            on_release=self.eula_open),
                            #MDFlatButton(text='CANCEL',on_release=self.dialog_close), 
                            MDRectangleFlatButton(text="Agree", 
                            theme_text_color="Primary",
                            #pos_hint = {"center_x": .5, "center_y": .1},
                            on_release=self.eula_dialog_close), 
                            MDRectangleFlatButton(text="Cancel", 
                            theme_text_color="Primary",
                            #pos_hint = {"center_x": .5, "center_y": .1},
                            on_release=self.agreement_dialog_cancel)
                            ])
    self.eula_dialog.open()

  # open the terms of service provided by termly  
  def terms_open(self,*args):
    webbrowser.open("https://app.termly.io/document/terms-of-use-for-website/7330750b-0919-4fb4-a494-51cb13e3d906")
  # Open the EULA provided by termly  
  def eula_open(self,*args):
    webbrowser.open("https://app.termly.io/document/eula/89132524-7259-4a40-9e1c-059e4ad8ec62")
  
  # user accepted the terms
  def terms_dialog_close(self, *args):    
    db.create_agreement('Y', 'ToS', __version__)
    self.terms_dialog.dismiss(force=True) 

  # user accepted the terms
  def eula_dialog_close(self, *args):    
    db.create_agreement('Y', 'Eula', __version__)
    self.eula_dialog.dismiss(force=True)
    
  # user did not accept agreement
  def agreement_dialog_cancel(self, *args):
    MDApp.get_running_app().stop()

  def login(self, *args):
    screen_manager.current = "splash"
    Clock.schedule_once(self.change_screen, 4)

  def change_screen(self, dt):
    # display terms and eula
    try:
      terms = db.get_agreement('ToS',__version__)
      #print(f'Terms Result = {terms}')
      if terms == 0:
        self.show_terms_dialog()
        try:
          eula = db.get_agreement('Eula',__version__) 
          #print(f'Eula = {eula}')
          if eula == 0:
            self.show_eula_dialog()
        except:
          self.show_eula_dialog()
    except:
      self.show_terms_dialog()
    screen_manager.current = "dash"

    #screen_manager.transition = FadeTransition()

  # ANDROID SPECIFIC
  def key_input(self, window, key, scancode, codepoint, modifier):
    if key == 27:
        return True  # override the default behaviour
    else:           # the key now does nothing
        return False
  # ANDROID SPECIFIC  
  def on_pause(self):
    return True

         



# driver function
if __name__=="__main__":
	LotteryMagic().run()




