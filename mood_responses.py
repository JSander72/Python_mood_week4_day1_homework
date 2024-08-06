
def mood_responses(mood):
    if mood == "happy".lower():
        return "Oh snap, I am happy as well!"
    elif mood == "sad".lower():
        return "Dont worry... hard work spotlights the charecter. Some turn up their noses, some turn up their sleeves, but others don't turn up at all. I have the feeling your are not the latter. #LetsGo"
    elif mood == "excited".lower():
        return "That's what I'm talking bout! I'm exited for you!!!"
    else:
        return "I'm not sure what you mean. Can you please enter: happy, sad, or excited."
    
    