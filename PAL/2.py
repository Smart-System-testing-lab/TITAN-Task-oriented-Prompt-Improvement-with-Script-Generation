def solution():
    # Define a dictionary to map letters to their corresponding sounds
    sounds = {'k': '/k/', 'l': '/l/'}

    # Get the sounds of the letters k and l
    k_sound = sounds[k]
    l_sound = sounds[l]

    # Check if the sounds are the same
    if k_sound == l_sound:
        # If they are the same, substitute k for l in kike
        kike_with_l = 'kike'.replace(k, l)

        # Check if the resulting word is equal to like
        if kike_with_l == like:
            print("target : 0")
            return

    # If the sounds are not the same, print a message indicating that there is a spelling difference
    print("target : 1")
solution()