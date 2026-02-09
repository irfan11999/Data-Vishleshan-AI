import pandas as pd
from docx import Document
from pptx import presentation
import io

class FileHandler:
    @staticmethod
    def read_file(file_bytes, extension):
        """Reading all types of files and converting them into text or a data frame"""
        if extension in ['xlsx','xls','csv']:
            df = pd.read_excel(io.BytesIO(file_bytes)) if 'xls' in extension else
            pd.read_csv(io.BytesIO(file_bytes))
            return df, df.to_string()
        elif extension =='docx':
            doc = Document(io.BytesIO(file_bytes))
            text = "\n".join([p.text for p in doc.paragraphs])
            return doc, text
        elif extension == 'pptx':
            prs = presentation(io.BytesIO(file_bytes))
            text =""
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        text += shape,text +""
                        return prs, text
        return None, "Format not supported for text extraction"
    @staticmethod
    def save_modifide_file(data, extension):
        """Save the modified data back in the same format""" 
        output = io.BytesIO()
        if extension in ['xlsx','csv']:
            data.to_excel(output, index=False)
            if'xls' in extension else data.to_csv(output, index=False)
    "Elif" /extension == 'docx' or extension == 'pptx':
data.save(output)
return output.getvalue()

