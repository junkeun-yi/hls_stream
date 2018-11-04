import sys

def make_ffmpeg(in_path_name):
	file = open('rec/stream.sh', 'w+')

	file.write('ffmpeg -stream_loop 1 -i %s -c:v libx264 \\\n' % in_path_name)
	file.write('-x264opts keyint=30:min-keyint=30:scenecut=-1 \\\n')
	file.write('-tune zerolatency -s 1280x720 \\\n')
	file.write('-b:v 1400k -bufsize 1400k \\\n')
	file.write('-hls_start_number_source epoch -f hls stream.m3u8 \\\n')

if __name__ == '__main__':
	make_ffmpeg(sys.argv[1])