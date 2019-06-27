import argparse

parser = argparse.ArgumentParser()
#args
parser.add_argument('--skel', required=True, help='Input path to the skeleton file.', type=str)
parser.add_argument('--video', help='Input path to the corresponding RGB video file.', type=str)
parser.add_argument('--frame_height', default=720, help='The height of the frame displayed.', type=int)
parser.add_argument('--frame_width', default=1280, help='The width of the frame displayed.', type=int)
parser.add_argument('--subject_ID', action='store_true', help='Use this arg to include the ID of the subject.')
parser.add_argument('--save', action='store_true', help='Use this arg to save the video on disk as output.avi.')
args = parser.parse_args()

#skeleton line between points based on the paper
skel_line_conf = [
					[1,13],
					[1,17],
					[1,2],
					[2,21],
					[21,5],
					[21,9],
					[21,3],
					[3,4],
					[5,6],
					[6,7],
					[7,8],
					[9,10],
					[10,11],
					[11,12],
					[13,14],
					[14,15],
					[15,16],
					[17,18],
					[18,19],
					[19,20]
					]