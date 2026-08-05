import wikipedia

def search_wikipedia(topic):
    try:
        result = wikipedia.summary(topic, sentences=2)
        return result

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Please be more specific."

    except wikipedia.exceptions.PageError:
        return "I couldn't find that topic on Wikipedia."

    except Exception:
        return "Something went wrong while searching Wikipedia."


