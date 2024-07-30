import ffmpeg
import glob
import os
import tempfile

print('Folder name:')
folderDir = input()+'/'
input_pattern_left = os.path.join(folderDir, '*LRL.JPG')
input_pattern_right = os.path.join(folderDir, '*LRR.JPG')

# Get the list of files matching the pattern
input_files_right = sorted(glob.glob(input_pattern_right))
input_files_left = sorted(glob.glob(input_pattern_left))

if not input_files_right and not input_files_left:
    print("No matching files found.")
    exit()

print(f"Found {len(input_files_right) + len(input_files_left)} files.")

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
    for file in input_files_right:
        temp_file.write(f"file '{file}'\n")
    temp_file_name_right = temp_file.name

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
    for file in input_files_left:
        temp_file.write(f"file '{file}'\n")
    temp_file_name_left = temp_file.name

def timeStampElement(i):
    start = i
    end = (i+1)
    first_part = f"{int(start//3600):02d}:{int(start//60):02d}:{int(start%60):02d},{int((start%1)*1000):03d}"
    second_part = f"{int(start//3600):02d}:{int(end//60):02d}:{int(end%60):02d},{int((start%1)*1000):03d}"
    return f"{first_part} --> {second_part}\n"

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.srt', dir='./') as temp_file:
    for i in range(len(input_files_right)):
        temp_file.write(f"{i}\n")
        temp_file.write(timeStampElement(i))
        temp_file.write(f"{input_files_right[i].split('\\')[-1]}\n\n")
    temp_subtitles_right = temp_file.name

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.srt', dir='./') as temp_file:
    for i in range(len(input_files_left)):
        temp_file.write(f"{i}\n")
        temp_file.write(timeStampElement(i))
        temp_file.write(f"{input_files_left[i].split('\\')[-1]}\n\n")
    temp_subtitles_left = temp_file.name

input_right_stream = ffmpeg.input(temp_file_name_right, format='concat', safe=0, r=1)
input_left_stream = ffmpeg.input(temp_file_name_left, format='concat', safe=0, r=1)

input_right_stream = input_right_stream.filter('subtitles', temp_subtitles_right.split('\\')[-1])
input_left_stream = input_left_stream.filter('subtitles', temp_subtitles_left.split('\\')[-1])

final_stream = ffmpeg.filter([input_left_stream, input_right_stream], 'hstack')

outputVideo = (
    final_stream
    .output(f'{folderDir}video.mp4', vcodec='libx264', crf=20, s='3167*1080')
    .overwrite_output()
)

framerate = f'{input("Framerate: ")}'

try:
    ffmpeg.run(outputVideo)
finally:
    os.unlink(temp_file_name_right)
    os.unlink(temp_file_name_left)
    os.unlink(temp_subtitles_right)
    os.unlink(temp_subtitles_left)

videoToSpeedUp = ffmpeg.input(f'{folderDir}video.mp4')
output = (
    videoToSpeedUp
    .setpts(f'PTS/{framerate}')
    .output(f'{folderDir}video_spedup.mp4', r=framerate)
    .overwrite_output()
)
ffmpeg.run(output)