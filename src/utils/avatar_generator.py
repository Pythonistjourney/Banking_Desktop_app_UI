from PIL import Image, ImageDraw
import os

class AvatarGenerator:
    def generate_avatar(self, user_id, size=(100, 100)):
        # Simple avatar: First letter of user_id on green background
        img = Image.new('RGB', size, color='#2ECC71')
        draw = ImageDraw.Draw(img)
        text = user_id[0].upper() if user_id else 'U'
        draw.text((size[0]//2-10, size[1]//2-10), text, fill='#FFFFFF')
        
        save_path = f"assets/images/users/{user_id}.png"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path)
        return save_path