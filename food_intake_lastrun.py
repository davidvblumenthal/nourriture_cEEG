#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Dezember 06, 2021, at 18:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'food_intake'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Lukas Stingl\\OneDrive\\Desktop\\EMUB\\nourriture_cEEG\\food_intake_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Welcome!\n\n',
    font='Open Sans',
    pos=(0, 0.35), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button = visual.ButtonStim(win, 
    text='Start', font='Arvo',
    pos=(0.4, -0.4),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor=None, borderColor=None,
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()
Description = visual.TextStim(win=win, name='Description',
    text='1. Task: Reading a text out loud\n2. Task: Yawning\n3. Task: Resting\n4. Task: Eating soup\n5. Task: Eating solid food',
    font='Open Sans',
    pos=(0.17, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Description_Speaking"
Description_SpeakingClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please read the following text aloud and clearly. If you reach the end before the time runs out, please start again from the beginning (duration: 2 intervals of 40 seconds each).',
    font='Open Sans',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_2 = visual.ButtonStim(win, 
    text='Start', font='Arvo',
    pos=(0.4, -0.4),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor=None, borderColor=None,
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_2'
)
button_2.buttonClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Bilder/sprechen.jpg', mask=None,
    ori=0.0, pos=(0, 0.25), size=(0.4, 0.266),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Speaking_40s"
Speaking_40sClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Zu Frühlingsbeginn machte man plötzlich eine alarmierende Entdeckung. Schneeball suchte nachts heimlich die Farm auf! Die Tiere waren so beunruhigt, dass sie in ihren Ställen kaum noch Schlaf fanden. Jede Nacht, so hieß es, schleiche er sich im Schutze der Dunkelheit herein und verübe alle möglichen Missetaten. Er stahl das Korn, er stießt die Milchkübel um, er zerbrach die Eier, er zertrampelte die Saatbeete, er knabberte die Rinde der Obstbäume ab. Wenn irgendetwas schiefging, wurde dies in der Regel Schneeball zugeschrieben. War ein Fenster zerbrochen oder Abfluss verstopft, durfte man sicher sein, dass irgendjemand erklärte, Schneeball sei in der Nacht gekommen und habe es getan, und als der Schlüssel zur Futterkammer verloren ging, da war die ganze Farm überzeugt davon, dass Schneeball ihn in den Brunnen geworfen hatte.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Description_Yawning"
Description_YawningClock = core.Clock()
text_Yawning = visual.TextStim(win=win, name='text_Yawning',
    text='Please yawn as naturally as possible (duration: 20 intervals of 3 seconds each).\n',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_yawning = visual.ButtonStim(win, 
    text='Start', font='Arvo',
    pos=(0.4, -0.4),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor=None, borderColor=None,
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_yawning'
)
button_yawning.buttonClock = core.Clock()

# Initialize components for Routine "Yawning_40s"
Yawning_40sClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='Bilder/gähnen.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.333),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Description_Resting"
Description_RestingClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Look at the cross and try to relax your facial muscles as much as possible (duration: 1 interval of 60 seconds).',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_3 = visual.ButtonStim(win, 
    text='Start', font='Arvo',
    pos=(0.4, -0.4),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor=None, borderColor=None,
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_3'
)
button_3.buttonClock = core.Clock()

# Initialize components for Routine "Resting"
RestingClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='Bilder/cross.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Description_Resting_Eyes_closed"
Description_Resting_Eyes_closedClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Close your eyes and try to relax your facial muscles as much as possible until you hear a sound (duration: 1 interval of 60 seconds).',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_6 = visual.ButtonStim(win, 
    text='Start', font='Arvo',
    pos=(0.4, -0.4),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor=None, borderColor=None,
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_6'
)
button_6.buttonClock = core.Clock()

# Initialize components for Routine "Resting_eyes_closed"
Resting_eyes_closedClock = core.Clock()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(0.6)

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Description_Eating_NSF"
Description_Eating_NSFClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Please eat the soup (duration: 2 intervals of 40 seconds each).\n',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_4 = visual.ButtonStim(win, 
    text='Start', font='Arvo',
    pos=(0.4, -0.4),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor=None, borderColor=None,
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_4'
)
button_4.buttonClock = core.Clock()

# Initialize components for Routine "Eating_NSF"
Eating_NSFClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='Bilder/Suppe.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.336),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Description_Eating_SF"
Description_Eating_SFClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Please eat nuts in the first and second interval and bread in the second and fourth interval (duration: 4 intervals of 40 seconds each).\n',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_5 = visual.ButtonStim(win, 
    text='Start', font='Arvo',
    pos=(0.4, -0.4),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor=None, borderColor=None,
    color='green', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_5'
)
button_5.buttonClock = core.Clock()

# Initialize components for Routine "Eating_SF_nuts"
Eating_SF_nutsClock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='Bilder/nuts.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.329),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Eating_SF_nuts"
Eating_SF_nutsClock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='Bilder/nuts.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.329),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Eating_SF_bread"
Eating_SF_breadClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='Bilder/Brot.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.333),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "blank4"
blank4Clock = core.Clock()
text_blank4 = visual.TextStim(win=win, name='text_blank4',
    text='To be continued soon',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Eating_SF_bread"
Eating_SF_breadClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='Bilder/Brot.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.333),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "GoodbyeScreen"
GoodbyeScreenClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Thank you for participating. \n\nThe experiment is finished now. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
Description.alignText='left'
# keep track of which components have finished
WelcomeScreenComponents = [Welcome, button, Description]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.tStart = t  # local t and not account for scr refresh
        Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        Welcome.setAutoDraw(True)
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
    # *Description* updates
    if Description.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Description.frameNStart = frameN  # exact frame index
        Description.tStart = t  # local t and not account for scr refresh
        Description.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Description, 'tStartRefresh')  # time at next scr refresh
        Description.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome.started', Welcome.tStartRefresh)
thisExp.addData('Welcome.stopped', Welcome.tStopRefresh)
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn)
   thisExp.addData('button.timesOff', button.timesOff)
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
thisExp.addData('Description.started', Description.tStartRefresh)
thisExp.addData('Description.stopped', Description.tStopRefresh)
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank4"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank4Components = [text_blank4]
for thisComponent in blank4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank4* updates
    if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank4.frameNStart = frameN  # exact frame index
        text_blank4.tStart = t  # local t and not account for scr refresh
        text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
        text_blank4.setAutoDraw(True)
    if text_blank4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_blank4.tStop = t  # not accounting for scr refresh
            text_blank4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank4"-------
for thisComponent in blank4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_blank4.started', text_blank4.tStartRefresh)
thisExp.addData('text_blank4.stopped', text_blank4.tStopRefresh)

# ------Prepare to start Routine "Description_Speaking"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Description_SpeakingComponents = [text_2, button_2, image]
for thisComponent in Description_SpeakingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Description_SpeakingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Description_Speaking"-------
while continueRoutine:
    # get current time
    t = Description_SpeakingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Description_SpeakingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *button_2* updates
    if button_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        button_2.frameNStart = frameN  # exact frame index
        button_2.tStart = t  # local t and not account for scr refresh
        button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
        button_2.setAutoDraw(True)
    if button_2.status == STARTED:
        # check whether button_2 has been pressed
        if button_2.isClicked:
            if not button_2.wasClicked:
                button_2.timesOn.append(button_2.buttonClock.getTime()) # store time of first click
                button_2.timesOff.append(button_2.buttonClock.getTime()) # store time clicked until
            else:
                button_2.timesOff[-1] = button_2.buttonClock.getTime() # update time clicked until
            if not button_2.wasClicked:
                continueRoutine = False  # end routine when button_2 is clicked
                None
            button_2.wasClicked = True  # if button_2 is still clicked next frame, it is not a new click
        else:
            button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    else:
        button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Description_SpeakingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Description_Speaking"-------
for thisComponent in Description_SpeakingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('button_2.started', button_2.tStartRefresh)
thisExp.addData('button_2.stopped', button_2.tStopRefresh)
thisExp.addData('button_2.numClicks', button_2.numClicks)
if button_2.numClicks:
   thisExp.addData('button_2.timesOn', button_2.timesOn)
   thisExp.addData('button_2.timesOff', button_2.timesOff)
else:
   thisExp.addData('button_2.timesOn', "")
   thisExp.addData('button_2.timesOff', "")
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "Description_Speaking" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Speaking_40s"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Speaking_40sComponents = [text]
    for thisComponent in Speaking_40sComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Speaking_40sClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Speaking_40s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Speaking_40sClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Speaking_40sClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Speaking_40sComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Speaking_40s"-------
    for thisComponent in Speaking_40sComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "blank4"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank4Components = [text_blank4]
    for thisComponent in blank4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_blank4* updates
        if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blank4.frameNStart = frameN  # exact frame index
            text_blank4.tStart = t  # local t and not account for scr refresh
            text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(True)
        if text_blank4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_blank4.tStop = t  # not accounting for scr refresh
                text_blank4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
                text_blank4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank4"-------
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_blank4.started', text_blank4.tStartRefresh)
    trials.addData('text_blank4.stopped', text_blank4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials'


# ------Prepare to start Routine "Description_Yawning"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Description_YawningComponents = [text_Yawning, button_yawning]
for thisComponent in Description_YawningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Description_YawningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Description_Yawning"-------
while continueRoutine:
    # get current time
    t = Description_YawningClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Description_YawningClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Yawning* updates
    if text_Yawning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Yawning.frameNStart = frameN  # exact frame index
        text_Yawning.tStart = t  # local t and not account for scr refresh
        text_Yawning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Yawning, 'tStartRefresh')  # time at next scr refresh
        text_Yawning.setAutoDraw(True)
    
    # *button_yawning* updates
    if button_yawning.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        button_yawning.frameNStart = frameN  # exact frame index
        button_yawning.tStart = t  # local t and not account for scr refresh
        button_yawning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_yawning, 'tStartRefresh')  # time at next scr refresh
        button_yawning.setAutoDraw(True)
    if button_yawning.status == STARTED:
        # check whether button_yawning has been pressed
        if button_yawning.isClicked:
            if not button_yawning.wasClicked:
                button_yawning.timesOn.append(button_yawning.buttonClock.getTime()) # store time of first click
                button_yawning.timesOff.append(button_yawning.buttonClock.getTime()) # store time clicked until
            else:
                button_yawning.timesOff[-1] = button_yawning.buttonClock.getTime() # update time clicked until
            if not button_yawning.wasClicked:
                continueRoutine = False  # end routine when button_yawning is clicked
                None
            button_yawning.wasClicked = True  # if button_yawning is still clicked next frame, it is not a new click
        else:
            button_yawning.wasClicked = False  # if button_yawning is clicked next frame, it is a new click
    else:
        button_yawning.wasClicked = False  # if button_yawning is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Description_YawningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Description_Yawning"-------
for thisComponent in Description_YawningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Yawning.started', text_Yawning.tStartRefresh)
thisExp.addData('text_Yawning.stopped', text_Yawning.tStopRefresh)
thisExp.addData('button_yawning.started', button_yawning.tStartRefresh)
thisExp.addData('button_yawning.stopped', button_yawning.tStopRefresh)
thisExp.addData('button_yawning.numClicks', button_yawning.numClicks)
if button_yawning.numClicks:
   thisExp.addData('button_yawning.timesOn', button_yawning.timesOn)
   thisExp.addData('button_yawning.timesOff', button_yawning.timesOff)
else:
   thisExp.addData('button_yawning.timesOn', "")
   thisExp.addData('button_yawning.timesOff', "")
# the Routine "Description_Yawning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Yawning_40s"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Yawning_40sComponents = [image_2]
    for thisComponent in Yawning_40sComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Yawning_40sClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Yawning_40s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Yawning_40sClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Yawning_40sClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Yawning_40sComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Yawning_40s"-------
    for thisComponent in Yawning_40sComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('image_2.started', image_2.tStartRefresh)
    trials_2.addData('image_2.stopped', image_2.tStopRefresh)
    
    # ------Prepare to start Routine "blank4"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank4Components = [text_blank4]
    for thisComponent in blank4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_blank4* updates
        if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blank4.frameNStart = frameN  # exact frame index
            text_blank4.tStart = t  # local t and not account for scr refresh
            text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(True)
        if text_blank4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_blank4.tStop = t  # not accounting for scr refresh
                text_blank4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
                text_blank4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank4"-------
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_blank4.started', text_blank4.tStartRefresh)
    trials_2.addData('text_blank4.stopped', text_blank4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_2'


# ------Prepare to start Routine "Description_Resting"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Description_RestingComponents = [text_3, button_3]
for thisComponent in Description_RestingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Description_RestingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Description_Resting"-------
while continueRoutine:
    # get current time
    t = Description_RestingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Description_RestingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *button_3* updates
    if button_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        button_3.frameNStart = frameN  # exact frame index
        button_3.tStart = t  # local t and not account for scr refresh
        button_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
        button_3.setAutoDraw(True)
    if button_3.status == STARTED:
        # check whether button_3 has been pressed
        if button_3.isClicked:
            if not button_3.wasClicked:
                button_3.timesOn.append(button_3.buttonClock.getTime()) # store time of first click
                button_3.timesOff.append(button_3.buttonClock.getTime()) # store time clicked until
            else:
                button_3.timesOff[-1] = button_3.buttonClock.getTime() # update time clicked until
            if not button_3.wasClicked:
                continueRoutine = False  # end routine when button_3 is clicked
                None
            button_3.wasClicked = True  # if button_3 is still clicked next frame, it is not a new click
        else:
            button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click
    else:
        button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Description_RestingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Description_Resting"-------
for thisComponent in Description_RestingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('button_3.started', button_3.tStartRefresh)
thisExp.addData('button_3.stopped', button_3.tStopRefresh)
thisExp.addData('button_3.numClicks', button_3.numClicks)
if button_3.numClicks:
   thisExp.addData('button_3.timesOn', button_3.timesOn)
   thisExp.addData('button_3.timesOff', button_3.timesOff)
else:
   thisExp.addData('button_3.timesOn', "")
   thisExp.addData('button_3.timesOff', "")
# the Routine "Description_Resting" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
RestingComponents = [image_3]
for thisComponent in RestingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RestingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Resting"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = RestingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RestingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    if image_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_3.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            image_3.tStop = t  # not accounting for scr refresh
            image_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
            image_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RestingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting"-------
for thisComponent in RestingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)

# ------Prepare to start Routine "blank4"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank4Components = [text_blank4]
for thisComponent in blank4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank4* updates
    if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank4.frameNStart = frameN  # exact frame index
        text_blank4.tStart = t  # local t and not account for scr refresh
        text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
        text_blank4.setAutoDraw(True)
    if text_blank4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_blank4.tStop = t  # not accounting for scr refresh
            text_blank4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank4"-------
for thisComponent in blank4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_blank4.started', text_blank4.tStartRefresh)
thisExp.addData('text_blank4.stopped', text_blank4.tStopRefresh)

# ------Prepare to start Routine "Description_Resting_Eyes_closed"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Description_Resting_Eyes_closedComponents = [text_7, button_6]
for thisComponent in Description_Resting_Eyes_closedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Description_Resting_Eyes_closedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Description_Resting_Eyes_closed"-------
while continueRoutine:
    # get current time
    t = Description_Resting_Eyes_closedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Description_Resting_Eyes_closedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *button_6* updates
    if button_6.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        button_6.frameNStart = frameN  # exact frame index
        button_6.tStart = t  # local t and not account for scr refresh
        button_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_6, 'tStartRefresh')  # time at next scr refresh
        button_6.setAutoDraw(True)
    if button_6.status == STARTED:
        # check whether button_6 has been pressed
        if button_6.isClicked:
            if not button_6.wasClicked:
                button_6.timesOn.append(button_6.buttonClock.getTime()) # store time of first click
                button_6.timesOff.append(button_6.buttonClock.getTime()) # store time clicked until
            else:
                button_6.timesOff[-1] = button_6.buttonClock.getTime() # update time clicked until
            if not button_6.wasClicked:
                continueRoutine = False  # end routine when button_6 is clicked
                None
            button_6.wasClicked = True  # if button_6 is still clicked next frame, it is not a new click
        else:
            button_6.wasClicked = False  # if button_6 is clicked next frame, it is a new click
    else:
        button_6.wasClicked = False  # if button_6 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Description_Resting_Eyes_closedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Description_Resting_Eyes_closed"-------
for thisComponent in Description_Resting_Eyes_closedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('button_6.started', button_6.tStartRefresh)
thisExp.addData('button_6.stopped', button_6.tStopRefresh)
thisExp.addData('button_6.numClicks', button_6.numClicks)
if button_6.numClicks:
   thisExp.addData('button_6.timesOn', button_6.timesOn)
   thisExp.addData('button_6.timesOff', button_6.timesOff)
else:
   thisExp.addData('button_6.timesOn', "")
   thisExp.addData('button_6.timesOff', "")
# the Routine "Description_Resting_Eyes_closed" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_eyes_closed"-------
continueRoutine = True
routineTimer.add(41.000000)
# update component parameters for each repeat
sound_1.setSound('A', secs=1.0, hamming=True)
sound_1.setVolume(0.6, log=False)
# keep track of which components have finished
Resting_eyes_closedComponents = [sound_1]
for thisComponent in Resting_eyes_closedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Resting_eyes_closedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Resting_eyes_closed"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Resting_eyes_closedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Resting_eyes_closedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    if sound_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            sound_1.tStop = t  # not accounting for scr refresh
            sound_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
            sound_1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_eyes_closedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_eyes_closed"-------
for thisComponent in Resting_eyes_closedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStartRefresh)
thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)

# ------Prepare to start Routine "blank4"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank4Components = [text_blank4]
for thisComponent in blank4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank4* updates
    if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank4.frameNStart = frameN  # exact frame index
        text_blank4.tStart = t  # local t and not account for scr refresh
        text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
        text_blank4.setAutoDraw(True)
    if text_blank4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_blank4.tStop = t  # not accounting for scr refresh
            text_blank4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank4"-------
for thisComponent in blank4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_blank4.started', text_blank4.tStartRefresh)
thisExp.addData('text_blank4.stopped', text_blank4.tStopRefresh)

# ------Prepare to start Routine "Description_Eating_NSF"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Description_Eating_NSFComponents = [text_4, button_4]
for thisComponent in Description_Eating_NSFComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Description_Eating_NSFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Description_Eating_NSF"-------
while continueRoutine:
    # get current time
    t = Description_Eating_NSFClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Description_Eating_NSFClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *button_4* updates
    if button_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        button_4.frameNStart = frameN  # exact frame index
        button_4.tStart = t  # local t and not account for scr refresh
        button_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
        button_4.setAutoDraw(True)
    if button_4.status == STARTED:
        # check whether button_4 has been pressed
        if button_4.isClicked:
            if not button_4.wasClicked:
                button_4.timesOn.append(button_4.buttonClock.getTime()) # store time of first click
                button_4.timesOff.append(button_4.buttonClock.getTime()) # store time clicked until
            else:
                button_4.timesOff[-1] = button_4.buttonClock.getTime() # update time clicked until
            if not button_4.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                None
            button_4.wasClicked = True  # if button_4 is still clicked next frame, it is not a new click
        else:
            button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    else:
        button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Description_Eating_NSFComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Description_Eating_NSF"-------
for thisComponent in Description_Eating_NSFComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('button_4.started', button_4.tStartRefresh)
thisExp.addData('button_4.stopped', button_4.tStopRefresh)
thisExp.addData('button_4.numClicks', button_4.numClicks)
if button_4.numClicks:
   thisExp.addData('button_4.timesOn', button_4.timesOn)
   thisExp.addData('button_4.timesOff', button_4.timesOff)
else:
   thisExp.addData('button_4.timesOn', "")
   thisExp.addData('button_4.timesOff', "")
# the Routine "Description_Eating_NSF" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Eating_NSF"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Eating_NSFComponents = [image_4]
    for thisComponent in Eating_NSFComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Eating_NSFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Eating_NSF"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Eating_NSFClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Eating_NSFClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        if image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                image_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Eating_NSFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Eating_NSF"-------
    for thisComponent in Eating_NSFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('image_4.started', image_4.tStartRefresh)
    trials_3.addData('image_4.stopped', image_4.tStopRefresh)
    
    # ------Prepare to start Routine "blank4"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank4Components = [text_blank4]
    for thisComponent in blank4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_blank4* updates
        if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blank4.frameNStart = frameN  # exact frame index
            text_blank4.tStart = t  # local t and not account for scr refresh
            text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(True)
        if text_blank4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_blank4.tStop = t  # not accounting for scr refresh
                text_blank4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
                text_blank4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank4"-------
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('text_blank4.started', text_blank4.tStartRefresh)
    trials_3.addData('text_blank4.stopped', text_blank4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_3'


# ------Prepare to start Routine "Description_Eating_SF"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Description_Eating_SFComponents = [text_6, button_5]
for thisComponent in Description_Eating_SFComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Description_Eating_SFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Description_Eating_SF"-------
while continueRoutine:
    # get current time
    t = Description_Eating_SFClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Description_Eating_SFClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *button_5* updates
    if button_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_5.frameNStart = frameN  # exact frame index
        button_5.tStart = t  # local t and not account for scr refresh
        button_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_5, 'tStartRefresh')  # time at next scr refresh
        button_5.setAutoDraw(True)
    if button_5.status == STARTED:
        # check whether button_5 has been pressed
        if button_5.isClicked:
            if not button_5.wasClicked:
                button_5.timesOn.append(button_5.buttonClock.getTime()) # store time of first click
                button_5.timesOff.append(button_5.buttonClock.getTime()) # store time clicked until
            else:
                button_5.timesOff[-1] = button_5.buttonClock.getTime() # update time clicked until
            if not button_5.wasClicked:
                continueRoutine = False  # end routine when button_5 is clicked
                None
            button_5.wasClicked = True  # if button_5 is still clicked next frame, it is not a new click
        else:
            button_5.wasClicked = False  # if button_5 is clicked next frame, it is a new click
    else:
        button_5.wasClicked = False  # if button_5 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Description_Eating_SFComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Description_Eating_SF"-------
for thisComponent in Description_Eating_SFComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('button_5.started', button_5.tStartRefresh)
thisExp.addData('button_5.stopped', button_5.tStopRefresh)
thisExp.addData('button_5.numClicks', button_5.numClicks)
if button_5.numClicks:
   thisExp.addData('button_5.timesOn', button_5.timesOn)
   thisExp.addData('button_5.timesOff', button_5.timesOff)
else:
   thisExp.addData('button_5.timesOn', "")
   thisExp.addData('button_5.timesOff', "")
# the Routine "Description_Eating_SF" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Eating_SF_nuts"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Eating_SF_nutsComponents = [image_6]
for thisComponent in Eating_SF_nutsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Eating_SF_nutsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Eating_SF_nuts"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Eating_SF_nutsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Eating_SF_nutsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_6.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            image_6.tStop = t  # not accounting for scr refresh
            image_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
            image_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Eating_SF_nutsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Eating_SF_nuts"-------
for thisComponent in Eating_SF_nutsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)

# ------Prepare to start Routine "blank4"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank4Components = [text_blank4]
for thisComponent in blank4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank4* updates
    if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank4.frameNStart = frameN  # exact frame index
        text_blank4.tStart = t  # local t and not account for scr refresh
        text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
        text_blank4.setAutoDraw(True)
    if text_blank4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_blank4.tStop = t  # not accounting for scr refresh
            text_blank4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank4"-------
for thisComponent in blank4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_blank4.started', text_blank4.tStartRefresh)
thisExp.addData('text_blank4.stopped', text_blank4.tStopRefresh)

# ------Prepare to start Routine "Eating_SF_nuts"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Eating_SF_nutsComponents = [image_6]
for thisComponent in Eating_SF_nutsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Eating_SF_nutsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Eating_SF_nuts"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Eating_SF_nutsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Eating_SF_nutsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_6.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            image_6.tStop = t  # not accounting for scr refresh
            image_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
            image_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Eating_SF_nutsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Eating_SF_nuts"-------
for thisComponent in Eating_SF_nutsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)

# ------Prepare to start Routine "blank4"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank4Components = [text_blank4]
for thisComponent in blank4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank4* updates
    if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank4.frameNStart = frameN  # exact frame index
        text_blank4.tStart = t  # local t and not account for scr refresh
        text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
        text_blank4.setAutoDraw(True)
    if text_blank4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_blank4.tStop = t  # not accounting for scr refresh
            text_blank4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank4"-------
for thisComponent in blank4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_blank4.started', text_blank4.tStartRefresh)
thisExp.addData('text_blank4.stopped', text_blank4.tStopRefresh)

# ------Prepare to start Routine "Eating_SF_bread"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Eating_SF_breadComponents = [image_5]
for thisComponent in Eating_SF_breadComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Eating_SF_breadClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Eating_SF_bread"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Eating_SF_breadClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Eating_SF_breadClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Eating_SF_breadComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Eating_SF_bread"-------
for thisComponent in Eating_SF_breadComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)

# ------Prepare to start Routine "blank4"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank4Components = [text_blank4]
for thisComponent in blank4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank4* updates
    if text_blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank4.frameNStart = frameN  # exact frame index
        text_blank4.tStart = t  # local t and not account for scr refresh
        text_blank4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank4, 'tStartRefresh')  # time at next scr refresh
        text_blank4.setAutoDraw(True)
    if text_blank4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank4.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_blank4.tStop = t  # not accounting for scr refresh
            text_blank4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank4, 'tStopRefresh')  # time at next scr refresh
            text_blank4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank4"-------
for thisComponent in blank4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_blank4.started', text_blank4.tStartRefresh)
thisExp.addData('text_blank4.stopped', text_blank4.tStopRefresh)

# ------Prepare to start Routine "Eating_SF_bread"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Eating_SF_breadComponents = [image_5]
for thisComponent in Eating_SF_breadComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Eating_SF_breadClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Eating_SF_bread"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Eating_SF_breadClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Eating_SF_breadClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Eating_SF_breadComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Eating_SF_bread"-------
for thisComponent in Eating_SF_breadComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)

# ------Prepare to start Routine "GoodbyeScreen"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GoodbyeScreenComponents = [text_5]
for thisComponent in GoodbyeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GoodbyeScreen"-------
while continueRoutine:
    # get current time
    t = GoodbyeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GoodbyeScreen"-------
for thisComponent in GoodbyeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "GoodbyeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='semicolon')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
