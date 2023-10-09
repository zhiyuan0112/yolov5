# sudo apt install ffmpeg
mkdir data/test/ffmpeg
ffmpeg -i "data/test/video/smoke3.mp4" -r 5 -f image2 data/test/ffmpeg/%d.jpg
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.1 --source data/test/ffmpeg
ffmpeg -f image2 -i runs/detect/exp10/%d.jpg -vcodec libx264 -r 5 runs/detect/exp10/smoke3.mp4

# -r frame rate, need to be changed in real cases.