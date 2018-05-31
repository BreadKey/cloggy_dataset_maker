# cloggy_dataset_maker
<div>
<image src = "https://github.com/WikiCloggy/cloggy_dataset_maker/blob/master/cdm.JPG?raw=true">
</div>
강아지 사진을 데이터로 변환해주는 툴

## Requirements
Python3 later  
opencv  
numpy  
scikit-image  
PyQt5

## Usage
python cloggy_dataset_maker.py

## How to use it
1. Select the cloggy image you want to get a data.  
2. Holding down the **Shift key**, **click and drag** to draw a rectangle containing the cloggy. Or draw a rectangle by **left-click and left-click** holding down **control key**.  
3. To get a **silhouette**, press the Get button under the silhouette box. (**The rectangle must exist before getting a silhouette.**)  
4. If you want to get a more **accurate** silhouette, mark the **foreground** of the object with mouse **left click** and mark the **background** of the object with mouse **right click**.  
5. To get a **skeleton**, press the Get button under the silhouette box. (**The Silhouette must exist before getting a skeleton.**)  
6. Select a **keyword** to the cloggy image  
7. Press the save buttons to save the results  
