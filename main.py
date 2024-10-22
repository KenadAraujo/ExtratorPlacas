from video.downloadvideo import DownloadVideo
from ia.detect_object import DetectObject

if __name__=="__main__":
    video = DownloadVideo("https://youtu.be/1qmA8UH09PE?si=snhNL309NEXOE3js","assets/downloads")
    video.download()
    arquivos = video.list_files()
    for vi in arquivos:
        path = video.generate_path(vi)
        recording,fps = video.get_video(path)

        ia = DetectObject("safeia.geral.v9.pt")
        plates = ia.extract_plate(video.save_frame, video.save_plate,recording)