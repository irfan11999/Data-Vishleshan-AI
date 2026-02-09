import google.generativeai as genai

class AIEngine:
    def _init_(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def analyze_command(self, user_voice_text, data_context, language="Hindi"):
        """Aam bhasha command ko samajhna aur data analyze karna"""
        prompt = f"""
        User Language: {language}
        Context: Aap ek expert Data Assistant hain. 
        User ne aam bhasha mein ye kaha hai: "{user_voice_text}"
        Data Content: {data_context[:5000]}
        
        Instructions:
        1. Agar user modify karne bole to batayein kya badalna hai.
        2. Agar vishleshan (analysis) maange to detail report dein.
        3. Response hamesha {language} mein dein.
        """
        response = self.model.generate_content(prompt)
        return response.text