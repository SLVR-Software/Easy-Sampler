from pytube import YouTube, Playlist
from moviepy.editor import *
import ffmpeg
# misc
import os, sys, re
import shutil

def downloadVideo(url, FILE_PATH):
    print(url)
    video = YouTube(url)
    print(video.title)
    #cleans up video titles of charcters that can't be used in file/directory names
    videoTitle = re.sub('[^A-Za-z0-9 ()]+', '', video.title)
    print(videoTitle)
    STREAMS = video.streams
    SAVE_PATH = os.path.join(FILE_PATH, videoTitle)
    MP3_PATH = os.path.join(FILE_PATH, "AudioFiles")
    MP4_PATH = os.path.join(FILE_PATH, "VideoFiles")
    print(MP3_PATH)
    print(SAVE_PATH)
    print(url)
    highestResolution = findHighestResolution(STREAMS)
    isVideoDownloaded = False
    isAudioDownloaded = False
    videoFileName = ""
    audioFileName = ""
    amountOfStreams = len(STREAMS)
    countedStreams = 0
    for stream in STREAMS:
        countedStreams += 1
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print("Downloading... " + videoTitle)
        print("Length: "+ str(video.length))
        print("Details:")
        print(stream)
        if (stream.type == "video"):
            if (stream.resolution == highestResolution and stream.mime_type == "video/mp4" and isVideoDownloaded == False):
                print("Downloading...." + highestResolution)
                videoFileName = stream.resolution+"-"+stream.type+"_"+videoTitle+".mp4"
                video.streams.get_by_itag(stream.itag).download(output_path=SAVE_PATH,filename=videoFileName)
                isVideoDownloaded = True
        elif (stream.type == "audio" and stream.mime_type == "audio/mp4" and isAudioDownloaded == False):
            print("Downloading..." + stream.type)
            audioFileName = stream.type+"_"+videoTitle+".mp4"
            video.streams.get_by_itag(stream.itag).download(output_path=SAVE_PATH,filename=audioFileName)
            isAudioDownloaded = True
        if (isAudioDownloaded == True and isVideoDownloaded == True):
            #Adaptive Video path
            #combine audio and video streams into single audio/video file
            videoFilePath = os.path.join(SAVE_PATH, videoFileName)
            audioFilePath = os.path.join(SAVE_PATH, audioFileName)

            input_video = ffmpeg.input(videoFilePath)
            input_audio = ffmpeg.input(audioFilePath)
            OUTPUT_PATH = os.path.join(SAVE_PATH, "processed_", videoTitle + ".mp4")

            ffmpeg.output( input_audio,input_video, videoTitle+".mp4").run()
            shutil.move((videoTitle+".mp4"),SAVE_PATH)

            mp3_file = os.path.join(SAVE_PATH, videoTitle+".mp3")

            mp4_file = audioFilePath
            audioclip = AudioFileClip(mp4_file)
            audioclip.write_audiofile(mp3_file)

            #close audio file
            audioclip.close()

            #Deletes the original video file/video file to save disk space
            os.remove(videoFilePath)
            os.remove(audioFilePath)

            break
        elif (isAudioDownloaded == False and isVideoDownloaded == True and countedStreams == amountOfStreams):
            #Progressive video path
            videoFilePath = os.path.join(SAVE_PATH, videoFileName)
            mp3_file = os.path.join(SAVE_PATH, videoTitle+".mp3")

            #creates MP3
            video = VideoFileClip(videoFilePath)
            video.audio.write_audiofile(mp3_file)

            #close the file
            video.close()
            break

    #Move mp3 file to the given MP3_PATH
    shutil.move(mp3_file,MP3_PATH)

    #TODO create csv within each video folder with meta data, youtube link to find it on youtube if needed

    #zip up the folder into zip file
    shutil.make_archive(SAVE_PATH, 'zip', FILE_PATH, videoTitle)

    #move zipped folder to VideoFolder
    shutil.move((SAVE_PATH+".zip"),MP4_PATH)

    #delete original folder
    shutil.rmtree(SAVE_PATH)

def findHighestResolution(STREAMS):
    highestResolution = 0
    for stream in STREAMS:
        if (stream.type == "video"):
            rawResolution = stream.resolution
            print(rawResolution)
            resolution = int(rawResolution.replace("p",""))
            if (resolution >= highestResolution):
                highestResolution = resolution
    highestResolutionString = str(highestResolution) + "p"
    return highestResolutionString

def cleanVideoTitle(videoTitle):
    cleanVideoTitle = videoTitle
    invalidCharacters = ["\\", "/", ":", "*", "?", '"',"<",">","|"]
    for character in invalidCharacters:
        cleanVideoTitle.replace(character,"")
        print(cleanVideoTitle)
    return cleanVideoTitle
