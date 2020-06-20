# Image_Manipulation

## For watermarking with image and text (text is optional)  :

  Open a `python` terminal then use below commands
  
```
from Main import watermark 
watermark(input_image_path, output_image_path,watermark_image_path,position_logo,text,color,text_size,text_position) 
```
   
ex- 
   
```
watermark(   'gcs-banner.png',                     # Base Image      
             'watermarked_image_output.jpg',       # Output Image    
             'invide.png',                         # Watermark Image     
             'tr',                                 # Watermark Image Position       
             text='Invide',                        # Warermark Text (optional)     
             color ='white',                       # Watermark Text Color (optional)    
             text_size=55,                         # Watermark Text Size (optional)          
             text_position='b'                     # Watermark Text Position with respect to Watermark Image (optional)    
             ) 
             
```

## For watermarking with text only  :

Open a `python` terminal then below commands
  
```
from Main import watermark 
watermark_with_text(input_image_path,output_image_path,text,text_position,color',text_size) 
``` 
 ex-
  
 ``` 
 watermark_with_text('gcs-banner.png',                  # Base Image
                     'watermarked_text_output.png',     # Output Image
                     'Invide',                          # Warermark Text
                     'bc',                              # Watermark Text Position
                     text_size=200,                     # Warermark Text Size (optional)
                     color='white') 
  ```
                       
## Positioning parameter for watermark function :

<pre>For Watermark                                                For Watermark Text </pre>
  
``` 
    tl - Top Left Corner                                          b - Below Watermark Image
    tc - Top Center                                               r - On Right Of Watermark Image
    tr - Top Right
    cl - Center Left
    c  - Center 
    cr - Center Right
    bl - Bottom Left
    bc - Bottom Center
    br - Bottom Right 
    bcl- Bottom Center Left
 ```
    
 
## Positioning parameter for watermark_with_text function :

``` 
    tl - Top Left Corner      
    tc - Top Center
    tr - Top Right
    cl - Center Left
    c  - Center
    cr - Center Right
    bl - Bottom Left
    bc - Bottom Center
    br - Bottom Right 
 ```
   


