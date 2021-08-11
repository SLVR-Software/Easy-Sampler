from pytube import YouTube, Playlist
import ffmpeg
# misc
import os, sys, re
import shutil


def downloadVideo(url, FILE_PATH):
    print(url)
    video = YouTube(url)
    print(video.title)
    videoTitle = re.sub('[^A-Za-z0-9 ()]+', '', video.title)
    print(videoTitle)
    STREAMS = video.streams
    SAVE_PATH = os.path.join(FILE_PATH, videoTitle)
    print(SAVE_PATH)
    print(url)
    highestResolution = findHighestResolution(STREAMS)
    isVideoDownloaded = False
    isAudioDownloaded = False
    videoFileName = ""
    audioFileName = ""
    for stream in STREAMS:
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print("Downloading... " + videoTitle)
        print("Length: "+ str(video.length))
        print("Details:")
        print(stream)
        if (stream.type == "video"):
            if (stream.resolution == highestResolution and stream.mime_type == "video/mp4" and isVideoDownloaded == False):
                print("Downloading...." + highestResolution)
                video.streams.get_by_itag(stream.itag).download(output_path=SAVE_PATH,filename_prefix=(stream.resolution+"-"+stream.type+"_"))
                isVideoDownloaded = True
                videoFileName = stream.resolution+"-"+stream.type+"_"+videoTitle+".mp4"
        elif (stream.type == "audio" and stream.mime_type == "audio/mp4" and isAudioDownloaded == False):
            print("Downloading..." + stream.type)
            video.streams.get_by_itag(stream.itag).download(output_path=SAVE_PATH,filename_prefix=(stream.type+"_"))
            isAudioDownloaded = True
            audioFileName = stream.type+"_"+videoTitle+".mp4"
        if (isAudioDownloaded == True and isVideoDownloaded == True):
            videoFilePath = os.path.join(SAVE_PATH, videoFileName)
            audioFilePath = os.path.join(SAVE_PATH, audioFileName)
            print(videoFilePath)
            print(audioFilePath)
            input_video = ffmpeg.input(videoFilePath)
            input_audio = ffmpeg.input(audioFilePath)
            OUTPUT_PATH = os.path.join(SAVE_PATH, "processed", videoTitle + ".mp4")

            #ffmpeg.concat(input_video, input_audio, v=1, a=1).output(SAVE_PATH+"/processed/"+videoTitle+".mp4").run()

            ffmpeg.output( input_audio,input_video, videoTitle+".mp4").run()
            shutil.move((videoTitle+".mp4"),SAVE_PATH)
            
            break

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
