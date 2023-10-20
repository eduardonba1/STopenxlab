import os
os.chdir(f"/home/xlab-app-center")
os.system(f"apt update")
os.system(f"pip install -q TTS==0.17.8")
os.system(f"git clone -b v1.1 https://github.com/camenduru/SadTalker")
os.system(f"pip install -q gradio safetensors kornia facexlib yacs gfpgan")
os.chdir(f"/home/xlab-app-center/SadTalker")

os.system(f"apt -y install -qq aria2")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/checkpoints/SadTalker_V0.0.2_256.safetensors -d /home/xlab-app-center/SadTalker/checkpoints -o SadTalker_V0.0.2_256.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/checkpoints/SadTalker_V0.0.2_512.safetensors -d /home/xlab-app-center/SadTalker/checkpoints -o SadTalker_V0.0.2_512.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/checkpoints/mapping_00109-model.pth.tar -d /home/xlab-app-center/SadTalker/checkpoints -o mapping_00109-model.pth.tar")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/checkpoints/mapping_00229-model.pth.tar -d /home/xlab-app-center/SadTalker/checkpoints -o mapping_00229-model.pth.tar")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/gfpgan/weights/GFPGANv1.4.pth -d /home/xlab-app-center/SadTalker/gfpgan/weights -o GFPGANv1.4.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/gfpgan/weights/alignment_WFLW_4HG.pth -d /home/xlab-app-center/SadTalker/gfpgan/weights -o alignment_WFLW_4HG.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/gfpgan/weights/detection_Resnet50_Final.pth -d /home/xlab-app-center/SadTalker/gfpgan/weights -o detection_Resnet50_Final.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/SadTalker/resolve/main/new/gfpgan/weights/parsing_parsenet.pth -d /home/xlab-app-center/SadTalker/gfpgan/weights -o parsing_parsenet.pth")

os.system(f"python app_sadtalker.py --theme dark")
