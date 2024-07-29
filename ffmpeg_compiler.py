import ffmpeg
import glob
import os
import tempfile

print('Folder name:')
folderDir = input()
input_pattern = os.path.join(folderDir, '*LRR.JPG')

# Get the list of files matching the pattern
input_files = sorted(glob.glob(input_pattern))

if not input_files:
    print("No matching files found.")
    exit()

print(f"Found {len(input_files)} files.")
print("First file:", input_files[0])
print("Last file:", input_files[-1])

# Create a temporary file with the list of input files
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
    for file in input_files:
        temp_file.write(f"file '{file}'\n")
    temp_file_name = temp_file.name

def niceName(s):
  print(s)
  return int(s)

# Use the concat demuxer with the temporary file list
input_stream = ffmpeg.input(temp_file_name, format='concat', safe=0)

input_stream = ffmpeg.filter(input_stream, 'drawtext', text='%{metadata:file_basename}', x=10, y=10, fontfile='C:/Windows/Fonts/Arial.ttf', fontsize=150, fontcolor='white')

outputVideo = (
    input_stream
    .output('./sources/1.mp4', vcodec='libx264', crf=20, s='1300*1920')
    .overwrite_output()
)

print("FFmpeg command:")
print(' '.join(ffmpeg.compile(outputVideo)))

try:
    ffmpeg.run(outputVideo)
finally:
    os.unlink(temp_file_name)  # Delete the temporary file