def generateBinaryVals(uniques_list, values_list):
    binaryVals = []
    for item in uniques_list:
        if item in values_list:
            binaryVals.append(1)
        else:
            binaryVals.append(0)

    return binaryVals

def generateSimilarityScore(selected_game, comparison_game, search_options):
    import pandas as pd
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    
    scores = []
    if search_options[0] == 1: # Developers
        scores.append(cosine_similarity([selected_game['Developers_Binary'].values[0]], [comparison_game['Developers_Binary']]).item())
    if search_options[1] == 1: # Platforms
        scores.append(cosine_similarity([selected_game['Platforms_Binary'].values[0]], [comparison_game['Platforms_Binary']]).item())
    if search_options[2] == 1: # Genres
        scores.append(cosine_similarity([selected_game['Genres_Binary'].values[0]], [comparison_game['Genres_Binary']]).item())
    if search_options[3] == 1: # Ratings
        scores.append(comparison_game['Rating_Scaled'])
    if search_options[4] == 1: # Popularity
        scores.append(comparison_game['Plays_Scaled'])

    return scores