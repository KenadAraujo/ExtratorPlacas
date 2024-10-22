from yt_dlp import YoutubeDL
import os
import cv2

class DownloadVideo:
    
    def __init__(self, url, output_path='.'):
        self.url = url
        self.output_path = output_path

    def download(self):
        ydl_opts = {
            'format': 'bestvideo+bestaudio',  # Melhor vídeo e áudio disponíveis
            'outtmpl': f'{self.output_path}/%(title)s.%(ext)s',  # Nome do arquivo baseado no título
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                print(f"Baixando o vídeo de: {self.url}")
                ydl.download([self.url])
                print("Download concluído!")
        except Exception as e:
            print(f"Ocorreu um erro durante o download: {e}")
    
    def list_files(self):
        return [f for f in os.listdir(self.output_path) if f.endswith('.webm')]
    
    def generate_path(self, filename):
        return f"{self.output_path}/{filename}"
    
    def save_frame(self, frame, frame_count):
        dir = "assets/frames_detected"
        self._verify_path(dir)
        cv2.imwrite(f"{dir}/frame_{frame_count:04d}.jpg", frame)
    
    def save_plate(self, frame, frame_count,plate_count):
        dir = "assets/plates_detected"
        self._verify_path(dir)
        cv2.imwrite(f"{dir}/frame_{frame_count:04d}_{plate_count:04d}.jpg", frame)
        
    def get_video(self, path):
        video = cv2.VideoCapture(path)
        if not video.isOpened():
            print("Erro ao abrir o vídeo")
            return None
        fps = video.get(cv2.CAP_PROP_FPS)
        return video, fps
    
    def _verify_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)