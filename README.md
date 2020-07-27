## BBL588_Project
# Instance Sky Segmentation with Mask R-CNN


- Presentation, result video, Dataset, project files are too big to upload Github. Link to this project is my google drive at link:

https://drive.google.com/drive/folders/1UrjTmZgnyIPfTvaOakZI8PsqaIFe_N3M?usp=sharing


- Anyone can re-train from this drive. Training steps at BBL_588_Sky_Train.ipynb.


- For use the currect weights at Sky detection, weights file is "Mask_RCNN\log\sky20200727T1152\mask_rcnn_sky_0025.h5"  Use this file directly with model with command
'python3 balloon.py splash --weights= /Weightspath --video=/videopath/'  

Example:
'python3 balloon.py splash --weights=/Users/ahmedbingol/Desktop/BBL_588_Project/Mask_RCNN/mask_rcnn_sky_0025.h5 --video=/Users/ahmedbingol/Downloads/Blacksburg_Encounter12.MP4'




- Or anyone can use Detection.ipynb for observe result of frame in model. 

- For Video 2 Frame Conversion, i wrote a script that is Video2Image.py . Some of the frames unrelevant to project, therefore i use more small subset of frames. Dataset path in drive is 'Mask_RCNN\datasets\Sky" folder. Also, Other Bee folder was used in Final exam of that course too. 


- The Result video with above script is uploaded to bbl588_final\Result\ folder. Sadly, it tooks too around 15-20 sec to detect and predict any frame, therefore it is behaving like 0.05 fps. 
