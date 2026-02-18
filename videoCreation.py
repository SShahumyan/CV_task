# from ultralytics import YOLO
# import cv2
# import os

# model = YOLO("models/yolo_construction.pt")

# # Input video path
# input_video = "videos/1.mp4"
# # Output video path
# output_video = "videos/video1_detected.mp4"

# # OpenCV video reader/writer
# cap = cv2.VideoCapture(input_video)
# width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps    = int(cap.get(cv2.CAP_PROP_FPS))

# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))


# # Process frame by frame
# frame_id = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Run YOLO inference on the frame
#     results = model(frame)

#     # Draw boxes + labels + confidence
#     for r in results:
#         boxes = r.boxes  # Boxes object
#         for box in boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             conf = float(box.conf[0])
#             cls = int(box.cls[0])
#             label = f"{model.names[cls]} {conf:.2f}"

#             # Draw rectangle and label
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, label, (x1, y1-10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            
#     # Convert RGB → BGR for OpenCV
#     frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#     out.write(frame_bgr)
#     frame_id += 1

# cap.release()
# out.release()
# print("Video processed and saved at:", output_video)


from ultralytics import YOLO

model = YOLO("models/yolo_construction_finetuned.pt")

# model.predict(
#     source="videos/1.mp4",     # input video
#     save=True,                  # save annotated video
#     conf=0.3,                   # confidence threshold
#     show=False                  # do not display frames live
# )

model.track(
    source="videos/3u.mp4",
    save=True,
    tracker="botsort.yaml",  # default tracker
    conf=0.2,
    show=True
)
