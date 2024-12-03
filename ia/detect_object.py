import cv2
from ultralytics import YOLO

class DetectObject:
    def __init__(self, model_path_plate, model_path_char):
        self.path_model_plate = f'assets/models/{model_path_plate}'
        self.path_model_char = f'assets/models/{model_path_char}'
    
    def detect_plate(self, frame):
        plates=[]
        model = YOLO(self.path_model_plate)
        results = model.predict(frame)
        for result in results:
            if len(result.boxes)>0:
                for box in result.boxes:
                    x1, y1, x2, y2 = box.xyxy.numpy()[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    plates.append(frame[y1:y2, x1:x2])
        return frame,plates
    
    def detect_letter_of_plate(self,frame):
        model = YOLO(self.path_model_char)
        results = model.predict(frame)
        class_names = model.names
        detections = []
        plates_char = ""
        for result in results:
            if len(result.boxes) > 0:
                for box in result.boxes:
                    x1, y1, x2, y2 = box.xyxy.numpy()[0]
                    class_id = int(box.cls.numpy()[0])
                    label = class_names[class_id]
                    detections.append((int(x1), int(y1), label))
        detections.sort(key=lambda det: (det[1], det[0]))
        for d in detections:
            plates_char += d[2]
        return plates_char

    def extract_plate(self,function_work_frame,function_work_plates,video:cv2.VideoCapture,frames_per_second=1):
        if not video.isOpened():
            print("Erro ao abrir o vídeo")
            return None
        fps = video.get(cv2.CAP_PROP_FPS)
        frame_count = 0
        frame_interval = int(fps / frames_per_second)
        print(f'Frames por segundo: {fps}, Frame interval: {frame_interval}')

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            if frame_count % frame_interval == 0:
                print(f'Processando frame {frame_count:04d}')
                _,plates = self.detect_plate(frame)
                if len(plates)>0:
                    function_work_frame(frame,frame_count)
                    plate_count=0
                    for plate in plates:
                        function_work_plates(plate,frame_count,plate_count)
                        char_plate = self.detect_letter_of_plate(plate)
                        print(f'Placa detectada: {char_plate}')
                        plate_count += 1
            frame_count += 1
        pass
        
