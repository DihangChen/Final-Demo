from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data='data.yaml',workers=0,epochs=2,batch=16)