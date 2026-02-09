from fastapi import FastAPI, UploadFile, File, Form
from core.animator import Animator
from core.file_handler import FileHandler

@app.post("/animate")
async def animate_file(
    file: UploadFile = File(...),
    style: str = Form("FADE"), # User ki choice: FADE, ZOOM, FLY
    text_overlay: str = Form("") 
):
    extension = file.filename.split('.')[-1].lower()
    content = await file.read()
    
    if extension == 'pptx':
        animated_content = Animator.apply_ppt_animation(content, style)
        return {"status": "PPT Animated", "style": style}
        
    elif extension == 'mp4':
        # Video animation logic
        return {"status": "Video Processing Started"}