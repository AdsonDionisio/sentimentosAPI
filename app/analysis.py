result = {}


def analyze_sentiment(text: str):
    if "feliz" in text:
        result["sentiment"] = "Feliz"
    elif "triste" in text:
        result["sentiment"] = "Triste"
    else:
        result["sentiment"] = "Neutro"

def get_result():
    return result
