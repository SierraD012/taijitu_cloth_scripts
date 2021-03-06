#Authors: Daniel Fuller, Brennan Mitchell, ### contact this guy: Trevor Barrus
import os

import maya
import maya.mel as mel #Allows for evaluation of MEL
import maya.cmds as mc

from byuam.project import Project
from byuam.environment import Department, Environment

STARTANIM = -5
STARTPRE = -25


############################
## PRE-ROLL BEOWULF ANIMATION ##
############################

#This code is brought to you in part by Daniel Fuller and the number 7

#Clears Rotation on a List of Objects
def clearRotate(list):
    print '>>ClearRotate() starting'
    for i in list:
    # check if attribute needs to be unlocked
        if (mc.getAttr(i + '.rotateX', lock=True) or mc.getAttr(i + '.rotateY', lock=True) or mc.getAttr(i + '.rotateZ',lock=True)):
            mc.setAttr(i + '.rotateX', lock=False)  # I hope force unlocking it is ok
            mc.setAttr(i + '.rotateY', lock=False)
            mc.setAttr(i + '.rotateZ', lock=False)
            print '******** Force unlocked ' + str(i) + '.rotate attributes'

        if mc.getAttr(i + '.rotateX', settable=True):
            mc.setAttr(i + '.rotateX', 0)
        else:
            print '************ Unable to clear ' + str(i) + '.rotateX'

        if mc.getAttr(i + '.rotateY', settable=True):
            mc.setAttr(i + '.rotateY', 0)
        else:
            print '************ Unable to clear ' + str(i) + '.rotateY'

        if mc.getAttr(i + '.rotateZ', settable=True):
            mc.setAttr(i + '.rotateZ', 0)
        else:
            print '************ Unable to clear ' + str(i) + '.rotateZ'

#Clears Translation on a List of Objects
def clearTranslate(list):
    print ">>ClearTranslate() starting"
    for i in list:
	# check if attribute needs to be unlocked
        if (mc.getAttr(i + '.translateX', lock=True) or mc.getAttr(i + '.translateY', lock=True) or mc.getAttr(i + '.translateZ',lock=True)):
            mc.setAttr(i + '.translateX', lock=False)  # I hope force unlocking it is ok
            mc.setAttr(i + '.translateY', lock=False)
            mc.setAttr(i + '.translateZ', lock=False)
            print '******** Force unlocked ' + str(i) + '.translate attributes'

        if mc.getAttr(i + '.translateX', settable=True):
            mc.setAttr(i + '.translateX', 0)
        else:
	    print '************ Unable to clear ' + str(i) + '.translateX' 
        
	if mc.getAttr(i + '.translateY', settable=True):   
            mc.setAttr(i + '.translateY', 0)
        else:
	    print '************ Unable to clear ' + str(i) + '.translateY'
       
	if mc.getAttr(i + '.translateZ', settable=True):
            mc.setAttr(i + '.translateZ', 0)
        else:
	    print '************ Unable to clear ' + str(i) + '.translateZ'


#Selects/Returns Full Rig
# The Hand/Foot "splaying" controls seem to be causing issues - they are connected and won't unlock
def selectRig():
    print ">>SelectRig() starting"

    beowulf_main = [
    'Beowulf_main_cc_01',
    'Beowulf_secondary_global_cc_01',
    'Beowulf_primary_global_cc_01']

    beowulf_head = [
    'Beowulf_head_cc_01',
    'Beowulf_jaw_cc_01',
    'Beowulf_head_settings_cc_01']

    beowulf_eyes = [
    'Beowulf_LFT_eye_rotate_cc_01', 	#Left
    'Beowulf_LFT_LOW_eyelid_cc_01',	
    'Beowulf_LFT_UPP_eyelid_cc_01',
    'Beowulf_LFT_OUT_eyebrow_cc_01',
    'Beowulf_LFT_MID_eyebrow_cc_01',
    'Beowulf_LFT_INN_eyebrow_cc_01',
    'Beowulf_LFT_MAIN_eyebrow_cc_01',
    'Beowulf_RGT_eye_rotate_cc_01',		#Right
    'Beowulf_RGT_LOW_eyelid_cc_01',	
    'Beowulf_RGT_UPP_eyelid_cc_01',
    'Beowulf_RGT_OUT_eyebrow_cc_01',
    'Beowulf_RGT_MID_eyebrow_cc_01',
    'Beowulf_RGT_INN_eyebrow_cc_01',
    'Beowulf_RGT_MAIN_eyebrow_cc_01',
    'Beowulf_LFT_eye_aim_cc_01',
    'Beowulf_RGT_eye_aim_cc_01',
    'Beowulf_both_eyes_aim_cc_01']
    
    beowulf_mouth = [
    'Beowulf_tongue_tip_cc_01',
    'Beowulf_tongue_middle_cc_01',
    'Beowulf_tongue_root_cc_01',
    'Beowulf_LOW_teeth_cc_01',
    'Beowulf_UPP_teeth_cc_01']

    beowulf_neck = [
    'Beowulf_UPP_neck_cc_01',
    'Beowulf_MID_neck_cc_01',
    'Beowulf_LOW_neck_cc_01',
    'Beowulf_neck_base_cc_01',
    'Beowulf_neck_settings_cc_01']

    beowulf_torso = [
    'Beowulf_spine_settings_cc_01',
    'Beowulf_chest_cc_01',
    'Beowulf_UPP_belly_cc_01',
    'Beowulf_MID_belly_cc_01',
    'Beowulf_LOW_belly_cc_01',
    'Beowulf_COG_cc_01']

    beowulf_arms = [
    'Beowulf_LFT_arm_settings_cc_01',	#Left
    'Beowulf_LFT_IK_arm_cc_01',
    'Beowulf_LFT_arm_pole_vector_cc_01',
    'Beowulf_LFT_clavicle_cc_01',
    'Beowulf_LFT_FK_wrist_cc_01',
    'Beowulf_LFT_FK_lower_arm_cc_01',
    'Beowulf_LFT_FK_upper_arm_cc_01',
    'Beowulf_LFT_upper_arm_bendy_cc_01',
    'Beowulf_LFT_upper_arm_bendy_low_tangent_cc_01',
    'Beowulf_LFT_upper_arm_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_elbow_bendy_cc_01',
    'Beowulf_LFT_elbow_bendy_low_tangent_cc_01',
    'Beowulf_LFT_elbow_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_lower_arm_bendy_cc_01',
    'Beowulf_LFT_lower_arm_bendy_low_tangent_cc_01',
    'Beowulf_LFT_lower_arm_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_wrist_bendy_cc_01',
    'Beowulf_LFT_wrist_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_shoulder_bendy_cc_01',
    'Beowulf_LFT_shoulder_bendy_low_tangent_cc_01',
    'Beowulf_RGT_arm_settings_cc_01',	#Right
    'Beowulf_RGT_IK_arm_cc_01',
    'Beowulf_RGT_arm_pole_vector_cc_01',
    'Beowulf_RGT_clavicle_cc_01',
    'Beowulf_RGT_FK_wrist_cc_01',
    'Beowulf_RGT_FK_lower_arm_cc_01',
    'Beowulf_RGT_FK_upper_arm_cc_01',
    'Beowulf_RGT_upper_arm_bendy_cc_01',
    'Beowulf_RGT_upper_arm_bendy_low_tangent_cc_01',
    'Beowulf_RGT_upper_arm_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_elbow_bendy_cc_01',
    'Beowulf_RGT_elbow_bendy_low_tangent_cc_01',
    'Beowulf_RGT_elbow_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_lower_arm_bendy_cc_01',
    'Beowulf_RGT_lower_arm_bendy_low_tangent_cc_01',
    'Beowulf_RGT_lower_arm_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_wrist_bendy_cc_01',
    'Beowulf_RGT_wrist_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_shoulder_bendy_cc_01',
    'Beowulf_RGT_shoulder_bendy_low_tangent_cc_01']    

    beowulf_hands = [
    'Beowulf_LFT_hand_cupping_splaying_cc_01',     #Left
    'Beowulf_LFT_thumb_primary_cc_01',
    'Beowulf_LFT_thumb_MED_secondary_cc_01',
    'Beowulf_LFT_thumb_DIS_secondary_cc_01',
    'Beowulf_LFT_index_finger_primary_cc_01',
    'Beowulf_LFT_index_finger_DIS_secondary_cc_01',
    'Beowulf_LFT_index_finger_MED_secondary_cc_01',
    'Beowulf_LFT_index_metacarpal_secondary_cc_01',
    'Beowulf_LFT_middle_finger_DIS_secondary_cc_01',
    'Beowulf_LFT_middle_finger_MED_secondary_cc_01',
    'Beowulf_LFT_middle_finger_primary_cc_01',
    'Beowulf_LFT_middle_metacarpal_secondary_cc_01',
    'Beowulf_LFT_ring_finger_DIS_secondary_cc_01',
    'Beowulf_LFT_ring_finger_MED_secondary_cc_01',
    'Beowulf_LFT_ring_finger_primary_cc_01',
    'Beowulf_LFT_ring_metacarpal_secondary_cc_01',
    'Beowulf_LFT_pinky_finger_DIS_secondary_cc_01',
    'Beowulf_LFT_pinky_finger_MED_secondary_cc_01',
    'Beowulf_LFT_pinky_finger_primary_cc_01',
    'Beowulf_LFT_pinky_metacarpal_secondary_cc_01',
    'Beowulf_RGT_hand_cupping_splaying_cc_01',	#Right
    'Beowulf_RGT_thumb_primary_cc_01',
    'Beowulf_RGT_thumb_MED_secondary_cc_01',
    'Beowulf_RGT_thumb_DIS_secondary_cc_01',
    'Beowulf_RGT_index_finger_primary_cc_01',
    'Beowulf_RGT_index_finger_DIS_secondary_cc_01',
    'Beowulf_RGT_index_finger_MED_secondary_cc_01',
    'Beowulf_RGT_index_metacarpal_secondary_cc_01',
    'Beowulf_RGT_middle_finger_DIS_secondary_cc_01',
    'Beowulf_RGT_middle_finger_MED_secondary_cc_01',
    'Beowulf_RGT_middle_finger_primary_cc_01',
    'Beowulf_RGT_middle_metacarpal_secondary_cc_01',
    'Beowulf_RGT_ring_finger_DIS_secondary_cc_01',
    'Beowulf_RGT_ring_finger_MED_secondary_cc_01',
    'Beowulf_RGT_ring_finger_primary_cc_01',
    'Beowulf_RGT_ring_metacarpal_secondary_cc_01',
    'Beowulf_RGT_pinky_finger_DIS_secondary_cc_01',
    'Beowulf_RGT_pinky_finger_MED_secondary_cc_01',
    'Beowulf_RGT_pinky_finger_primary_cc_01',
    'Beowulf_RGT_pinky_metacarpal_secondary_cc_01']

    beowulf_hips = [
    'Beowulf_hips_cc_01',
    'Beowulf_LFT_hip_bendy_low_tangent_cc_01',
    'Beowulf_LFT_hip_bendy_cc_01']

    beowulf_legs_feet = [
    'Beowulf_LFT_leg_settings_cc_01',	#Left
    'Beowulf_LFT_FK_ankle_cc_01',
    'Beowulf_LFT_FK_lower_leg_cc_01',
    'Beowulf_LFT_FK_upper_leg_cc_01',
    'Beowulf_LFT_leg_pole_vector_cc_01',
    'Beowulf_LFT_IK_leg_cc_01',
    'Beowulf_LFT_upper_leg_bendy_cc_01',
    'Beowulf_LFT_upper_leg_bendy_low_tangent_cc_01',
    'Beowulf_LFT_upper_leg_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_knee_bendy_cc_01',
    'Beowulf_LFT_knee_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_knee_bendy_low_tangent_cc_01',
    'Beowulf_LFT_lower_leg_bendy_cc_01',
    'Beowulf_LFT_lower_leg_bendy_low_tangent_cc_01',
    'Beowulf_LFT_lower_leg_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_ankle_bendy_cc_01',
    'Beowulf_LFT_ankle_bendy_upp_tangent_cc_01',
    'Beowulf_LFT_foot_splaying_cc_01',
    'Beowulf_LFT_foot_ball_cc_01',
    'Beowulf_LFT_big_toe_DIS_secondary_cc_01',
    'Beowulf_LFT_big_toe_MED_secondary_cc_01',
    'Beowulf_LFT_big_toe_primary_cc_01',
    'Beowulf_LFT_foot_ball_cc_01',
    'Beowulf_RGT_leg_settings_cc_01',	#Right
    'Beowulf_RGT_FK_ankle_cc_01',
    'Beowulf_RGT_FK_lower_leg_cc_01',
    'Beowulf_RGT_FK_upper_leg_cc_01',
    'Beowulf_RGT_leg_pole_vector_cc_01',
    'Beowulf_RGT_IK_leg_cc_01',
    'Beowulf_RGT_upper_leg_bendy_cc_01',
    'Beowulf_RGT_upper_leg_bendy_low_tangent_cc_01',
    'Beowulf_RGT_upper_leg_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_knee_bendy_cc_01',
    'Beowulf_RGT_knee_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_knee_bendy_low_tangent_cc_01',
    'Beowulf_RGT_lower_leg_bendy_cc_01',
    'Beowulf_RGT_lower_leg_bendy_low_tangent_cc_01',
    'Beowulf_RGT_lower_leg_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_ankle_bendy_cc_01',
    'Beowulf_RGT_ankle_bendy_upp_tangent_cc_01',
    'Beowulf_RGT_foot_splaying_cc_01',
    'Beowulf_RGT_foot_ball_cc_01',
    'Beowulf_RGT_big_toe_DIS_secondary_cc_01',
    'Beowulf_RGT_big_toe_MED_secondary_cc_01',
    'Beowulf_RGT_big_toe_primary_cc_01',
    'Beowulf_RGT_foot_ball_cc_01']

    fullRig = beowulf_main + beowulf_head + beowulf_mouth + beowulf_neck + beowulf_torso + beowulf_arms + beowulf_hands + beowulf_hips + beowulf_legs_feet
    
    #Create Selection from 'fullRig'
    mc.select(fullRig, replace=True)
    return fullRig


def keyArmFK():
    print ">>KeyArmFK() starting"
    #mc.setAttr('ten_rig_main_l_arm_switch_CTL.IKFK_Switch', 1)
    mc.setAttr('Beowulf_LFT_arm_settings_cc_01.FK_IK', 1)  #really not sure about this 

    if (mc.getAttr('Beowulf_LFT_arm_settings_cc_01.FK_IK', keyable=True) or mc.getAttr('Beowulf_LFT_arm_settings_cc_01.FK_IK', channelBox=True)):
        mc.setKeyframe('Beowulf_LFT_arm_settings_cc_01.FK_IK');
        

   # mc.setAttr('ten_rig_main_r_arm_switch_CTL.IKFK_Switch', 1) 
    mc.setAttr('Beowulf_RGT_arm_settings_cc_01.FK_IK', 1)  #really not sure about this 

    if (mc.getAttr('Beowulf_RGT_arm_settings_cc_01.FK_IK', keyable=True) or mc.getAttr('Beowulf_RGT_arm_settings_cc_01.FK_IK', channelBox=True)):
        mc.setKeyframe('Beowulf_RGT_arm_settings_cc_01.FK_IK');

def fingerNames():
    return [
    #'ten_rig_main_l_hand_CTL',
    #'ten_rig_main_l_thumb_CTL',
    #'ten_rig_main_l_index_CTL',
    #'ten_rig_main_l_middle_CTL',
    #'ten_rig_main_l_ring_CTL',
    #'ten_rig_main_l_pinky_CTL',
    #'ten_rig_main_r_hand_CTL',
    #'ten_rig_main_r_thumb_CTL',
    #'ten_rig_main_r_index_CTL',
    #'ten_rig_main_r_middle_CTL',
    #'ten_rig_main_r_ring_CTL',
    #'ten_rig_main_r_pinky_CTL'

    #'Beowulf_LFT_hand_cupping_splaying_cc_01',		#I'm not sure if these are the right controls for this
    'Beowulf_LFT_thumb_primary_cc_01',
    'Beowulf_LFT_index_metacarpal_secondary_cc_01',
    'Beowulf_LFT_middle_metacarpal_secondary_cc_01',
    'Beowulf_LFT_ring_metacarpal_secondary_cc_01',
    'Beowulf_LFT_pinky_metacarpal_secondary_cc_01',
    #'Beowulf_RGT_hand_cupping_splaying_cc_01',
    'Beowulf_RGT_thumb_primary_cc_01',
    'Beowulf_RGT_index_metacarpal_secondary_cc_01',
    'Beowulf_RGT_middle_metacarpal_secondary_cc_01',
    'Beowulf_RGT_ring_metacarpal_secondary_cc_01',
    'Beowulf_RGT_pinky_metacarpal_secondary_cc_01'
]
    
def scaleFingers():
    print ">>ScaleFingers() starting"
    for i in fingerNames():
        mc.setAttr(i + '.scaleX', 1)
        mc.setKeyframe(i, at='scaleX')

def keyFingers():
    print ">>KeyFingers() starting"
    for i in fingerNames():
	    mc.setKeyframe(i, at='scaleX')
    

def APose():
    print ">>APose() starting"
    #Handle Right Arm
    #   mc.rotate(0, 0, -45, 'ten_rig_main_r_armRoot_FK_CTL')
    mc.rotate(0, 0, -45, 'Beowulf_LFT_FK_upper_arm_cc_01') #check that this is the correct control to use - I'm pretty sure it is
    #Handle Left Arm
    #   mc.rotate(0, 0, -45, 'ten_rig_main_l_armRoot_FK_CTL')
    mc.rotate(0, 0, -45, 'Beowulf_RGT_FK_upper_arm_cc_01') 

def setRigKey(fullRig):
    print ">>SetRigKey() starting"
    #Key Translation
    mc.setKeyframe(fullRig, at='translateX')
    mc.setKeyframe(fullRig, at='translateY')
    mc.setKeyframe(fullRig, at='translateZ')
    #Key Rotation
    mc.setKeyframe(fullRig, at='rotateX')
    mc.setKeyframe(fullRig, at='rotateY')
    mc.setKeyframe(fullRig, at='rotateZ')
    
    keyFingers()


###########################################
#### MAIN ####
###########################################

#Keyframe Initial Frame
mc.currentTime(STARTANIM)
fullRig = selectRig()
setRigKey(fullRig)

#Set T-Pose (Clear Transformations)
mc.currentTime(STARTPRE)

selectRig()
keyArmFK()

clearRotate(fullRig)
clearTranslate(fullRig)

#scaleFingers() #Scale Fingers (Only Scalable Control)  #doesn't seem to be working right now - attrs are locked?

#Key APose (Adjust Arms, Keyframe)
APose()
setRigKey(fullRig)



mc.setKeyframe('Beowulf_COG_cc_01', at='translateX')
mc.setKeyframe('Beowulf_COG_cc_01', at='translateY')
mc.setKeyframe('Beowulf_COG_cc_01', at='translateZ')
#mc.setKeyframe('ten_rig_main_m_COG_CTL', at='translateX') #Hip Controller Not Working?  <-- existing comment
#mc.setKeyframe('ten_rig_main_m_COG_CTL', at='translateY')
#mc.setKeyframe('ten_rig_main_m_COG_CTL', at='translateZ')

mc.setKeyframe('Beowulf_COG_cc_01', at='rotateX')
mc.setKeyframe('Beowulf_COG_cc_01', at='rotateY')
mc.setKeyframe('Beowulf_COG_cc_01', at='rotateZ')
#mc.setKeyframe('ten_rig_main_m_COG_CTL', at='rotateX')
#mc.setKeyframe('ten_rig_main_m_COG_CTL', at='rotateY')
#mc.setKeyframe('ten_rig_main_m_COG_CTL', at='rotateZ')

# I'm not sure why these are in here, just the right shoulder?
#mc.setKeyframe('ten_rig_main_r_shoulder_CTL', at='translateX') #Shoulder Controller Not Working?   <-- existing comment
#mc.setKeyframe('ten_rig_main_r_shoulder_CTL', at='translateY')
#mc.setKeyframe('ten_rig_main_r_shoulder_CTL', at='translateZ')

#mc.setKeyframe('ten_rig_main_r_shoulder_CTL', at='rotateX')
#mc.setKeyframe('ten_rig_main_r_shoulder_CTL', at='rotateY')
#mc.setKeyframe('ten_rig_main_r_shoulder_CTL', at='rotateZ')


#Export Alembic (Requires User Input - Select Ten's Rig)
mc.playbackOptions(animationStartTime=STARTPRE)
import alembic_exporter
alembic_exporter.go()
