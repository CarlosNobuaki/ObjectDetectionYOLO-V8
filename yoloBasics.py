from PIL import Image
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Run inference on 'bus.jpg'
results = model('/home/carlos/Área de Trabalho/Workspace/ObjDetection/inference/images/cat.jpeg')  # results list

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('/home/carlos/Área de Trabalho/Workspace/ObjDetection/runs/classify/predict/results.jpg')  # save image
