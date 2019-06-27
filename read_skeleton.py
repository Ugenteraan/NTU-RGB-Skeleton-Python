from conf import args as args
import utils
import cv2
import numpy as np


def read_skeleton():

	#open the skeleton file
	file = open(args.skel, 'r')

	read_lines = [] 

	for line in file:
		#strip away the '\n' characters and split the values by the spaces.
		#append each line to "read_lines" list.
	    read_lines.append(line.strip('\n').split(' '))


	num_of_frames = int(read_lines[0][0]) #get the number of frames


	skeleton_data = None

	if args.subject_ID : #to include the information about the subject.

		skeleton_data = utils.care_subject(num_of_frames, read_lines) #read the information from the list

	else:

		skeleton_data = utils.no_subject(num_of_frames, read_lines) #read the information from the list



	#if the video argument is present
	if args.video is not None:

		cap = cv2.VideoCapture(args.video)

		out = None

		#to save video
		if args.save:
			out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (args.frame_width,args.frame_height))

		frame_idx = 1 #frame number in dictionary starts from 1

		while cap.isOpened():

			ret, frame = cap.read()

			if ret is True:

				skel_info = skeleton_data[str(frame_idx)]
				num_subjects = len(skel_info)
				
				for sub in range(num_subjects):
					
					utils.draw_skeleton(skel_info[sub], frame) #draws the skeleton on the frame

				frame = cv2.resize(frame, (args.frame_width, args.frame_height))

				#to save video
				if args.save:
					out.write(frame)

				cv2.imshow("Frame", frame)

				if cv2.waitKey(25) & 0xff == ord('q'):
					break
				
				frame_idx += 1
			else:

				cap.release()
				if args.save:
					out.release()
				cv2.destroyAllWindows()


	return skeleton_data


if __name__=='__main__':

	_ = read_skeleton()









