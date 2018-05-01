#!/usr/bin/env python2

from rosbag_recorder.srv import *
import rospy
import psutil
import subprocess
import signal
from os.path import expanduser

pidDict = {}
 
def recordTopics(req):
	global pidDict

	command = "rosbag record -b 512 -o " + expanduser("~") + "/" + req.name
	print "Recording to bag named %s. Topics:"%(req.name)
	for t in req.topics:
		print t
		command += " " + t

	pidDict[req.name] = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd="/tmp/")

	return RecordTopicsResponse(True)
 
def stopRecording(req):
	global pidDict

	if req.name in pidDict:
		print "Stop recording to bag named %s"%(req.name)
		p = pidDict[req.name]
		process = psutil.Process(p.pid)
		for subProcess in process.children(recursive=True):
			subProcess.send_signal(signal.SIGINT)
		p.wait()
	else:
		print "No current recording with name %s!"%req.name

	return StopRecordingResponse(True)
 
def rosbagRecorder():
	rospy.init_node('rosbag_recorder_server')
	recordServ = rospy.Service('record_topics', RecordTopics, recordTopics)
	stopServ = rospy.Service('stop_recording', StopRecording, stopRecording)
	print "Ready to record topics"
	rospy.spin()

if __name__ == "__main__":
	rosbagRecorder()
