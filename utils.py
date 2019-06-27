import numpy as np 
import cv2
import conf

args = conf.args

def care_subject(num_of_frames, read_lines):
	'''
	Reads the skeleton file line by line and returns a dictionary with the following format :
	{
		'frame 1' : {'subject_id_1' : np.array of the 1-st subject's skeletal position on frame 1 (25,2),
						. ,
						. ,
						. ,
					   'subject_id_m  : np.array of the m-th subject's skeletal position on frame 1 (25,2)},
			. ,
			. ,
			. ,
		'frame n' : {'subject_id 1' : np.array of the 1-st subject's skeletal position on frame n (25,2),
							. ,
							. ,
							. ,
					 'subject_id m': np array of the m-th subject's skeletal position on frame n (25,2)}

	}

	Parameter
	---------
	num_of_frames   : number of frames in the video that the skeletal data appears.   | integer
	read_lines      : list consisting of values from the .skeleton file line by line. | list

	'''

	frame_skel = {}

	idx = 0
	for frame in range(1, num_of_frames+1): # +1 since the loop iterates only till num_of_frames - 1
		idx += 1 #next line 
		num_subjects = int(read_lines[idx][0])
		
		temp_sub = {}
		
		for sub in range(num_subjects):
			idx += 1 #next line 
			sub_id = read_lines[idx][0]
			idx += 1 #next line 
			
			temp_skel = []
			for skeleton in range(int(read_lines[idx][0])):
				
				idx += 1 #next line 
				jointx = float(read_lines[idx][5]) #5th index is where the x-coordinate of the skeleton is stored.
				jointy = float(read_lines[idx][6]) #6th index is where the y-coordinate of the skeleton is stored.
				
				temp_skel.append((jointx, jointy))
			
			#use the subject id as the key to the dictionary.
			temp_sub[sub_id] = np.asarray(temp_skel) #store the list as np array.
		
		frame_skel[str(frame)] = temp_sub

	return frame_skel




def no_subject(num_of_frames, read_lines):
	'''
	Reads the skeleton file line by line and returns a dictionary with the following format :
	{
		'frame 1' : [[np.array of the 1-st subject's skeletal position on frame 1 (25,2)],
						. ,
						. ,
						. ,
					[np.array of the m-th subject's skeletal position on frame 1 (25,2)], (m, 25, 2)],
			. ,
			. ,
			. ,
		'frame n' : [[np.array of the 1-st subject's skeletal position on frame n (25,2)],
							. ,
							. ,
							. ,
					 [np array of the m-th subject's skeletal position on frame n (25,2)], (m, 25, 2)]

	}
	In this format, each subject's skeletal position information can be extracted using index value instead of specifying the
	subject's ID in previous format.

	Parameter
	---------
	num_of_frames   : number of frames in the video that the skeletal data appears.   | integer
	read_lines      : list consisting of values from the .skeleton file line by line. | list

	'''

	frame_skel = {}

	idx = 0
	for frame in range(1, num_of_frames+1):
		idx += 1 #next line 
		num_subjects = int(read_lines[idx][0])
		
		temp_sub = []
		
		for sub in range(num_subjects):
			idx += 1 #next line 
			sub_id = read_lines[idx][0]
			idx += 1 #next line 
			
			temp_skel = [] #a list instead of a dictionary
			for skeleton in range(int(read_lines[idx][0])):
				
				idx += 1 #next line 
				jointx = float(read_lines[idx][5]) #5th index is where the x-coordinate of the skeleton is stored.
				jointy = float(read_lines[idx][6]) #6th index is where the x-coordinate of the skeleton is stored.
				
				temp_skel.append((jointx, jointy))
			
			#must convert to float32 since cv2 circle does not accept float 64 data type.
			temp_sub.append(np.asarray(temp_skel).astype('float32')) #append each subject's skeletal information into the list.
		
		frame_skel[str(frame)] = temp_sub

	return frame_skel



def draw_skeleton(skeleton_data, frame):

	#to draw the lines joining the points
	for idx in range(len(conf.skel_line_conf)):

		#get the index of the points from the skeleton configuration list. -1 since index position starts from 0.
		first_xy  = conf.skel_line_conf[idx][0] - 1
		second_xy = conf.skel_line_conf[idx][1] - 1

		x1 = skeleton_data[first_xy][0]
		y1 = skeleton_data[first_xy][1]

		x2 = skeleton_data[second_xy][0]
		y2 = skeleton_data[second_xy][1]

		#use the index to get the x-y coordinate of the first point and the second point
		cv2.line(frame, (x1, y1), (x2, y2), (20,215,20), 2)

		#draw cirlces on the points
		cv2.circle(frame, (x1, y1), 4, (20,215,20), -1)





