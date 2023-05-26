# first line: 22
@memory.cache
def predict(model: Pipeline, text: str) -> int:
    prediction = model.predict([text])
    return prediction[0]
