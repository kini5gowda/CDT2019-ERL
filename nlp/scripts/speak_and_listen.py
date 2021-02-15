#!/usr/bin/env python

import rospy

from actionlib import SimpleActionClient

from pal_interaction_msgs.msg import TtsAction, TtsGoal

from nlp.srv import Say

class NLP:

    def __init__(self):

        # speak
        self.tts_client = SimpleActionClient('/tts', TtsAction)
        self.tts_client.wait_for_server()

        self.goal = TtsGoal()
        self.goal.rawtext.lang_id = "en_GB"

        s = rospy.Service('say', Say, self.say)

        rospy.loginfo("Ready to talk")

        # listen

    def say(self, msg):
        self.goal.rawtext.text = msg.text

        self.tts_client.send_goal(self.goal)

        # wait and return result TODO

    def step(self):
        return

if __name__ == '__main__':
    
    rospy.init_node('nlp', anonymous=True)
    rate = rospy.Rate(1)
    nlp = NLP() 

    while(True):

        nlp.step()
        rate.sleep()