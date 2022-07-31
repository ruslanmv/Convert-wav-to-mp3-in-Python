from os import path
from pydub import AudioSegment
from pathlib import Path
from gooey import Gooey, GooeyParser
import subprocess
import platform



@Gooey(dump_build_config=False, program_name="wav to mp3 Conversion Tool - ruslanmv.com")
def main():
    desc = "A Python GUI App to convert a .wav and  into a .mp3"
    wav_select_help_msg = "Select a .wav audio file to process"

    my_parser = GooeyParser(description=desc)
    my_parser.add_argument(
        "wav_to_convert", help=wav_select_help_msg, widget="FileChooser"
    )

    my_parser.add_argument(
        "output_dir", help="Directory to save output mp3", widget="DirChooser"
    )

    args = my_parser.parse_args()

    # construct the .wav input audio file path
    wav_to_convert_Path = Path(args.wav_to_convert)

    mp3_outfile_name = str(wav_to_convert_Path.stem) + ".mp3"
    mp3_outfile_Path = Path(args.output_dir, mp3_outfile_name)
    mp3_outfile_Path.unlink(missing_ok=True) # delete the .mp4 file if it's there


    print(f"input .wav file \n {wav_to_convert_Path}")
    print()
    print(f"output .mp3 file \n {mp3_outfile_Path}")
    print()
    
    
    #read wav file to an audio-segment
    #song = AudioSegment.from_wav(wav_to_convert_Path) #your_wave_file.wav

    #export audio segment to mp3
    #song.export(mp3_outfile_Path, format="mp3")  #your_wave_file.mp3

    #play audio-segment
    #play(song)
    
    
    # Determine ffmpeg executable file path
    """
    where ffmpeg
    """
    if platform.system() == 'Windows':

        ffmpeg_path_bytes = subprocess.check_output("where ffmpeg", shell=True) 
        
    elif platform.system() == 'Linux':
        ffmpeg_path_bytes = subprocess.check_output("which ffmpeg", shell=True) 

    ffmpeg_executable_path = ffmpeg_path_bytes.decode().strip()
    print("ffmpeg_executable_path: ", ffmpeg_executable_path)
    
    '''
    ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3
    '''
    
    # create the ffmpeg command
 
    aux = '-vn -ar 44100 -ac 2 -b:a 192k'
    
    ffmpeg_command = f"-i {wav_to_convert_Path} {aux} {mp3_outfile_Path}"
    cmd_command = f"{ffmpeg_executable_path} {ffmpeg_command}"
    
    
    # call ffmpeg
    returned_value = subprocess.call(cmd_command, shell=True)# returns the exit code in unix
    
    print("returned value:", returned_value)
    
    
    



if __name__ == "__main__":
      main()
