''' program desined create and use a function to return
which movies a user would watch next,if they have watched Planet Hulk
its description based on the highest description similarity match'''


# creating the funcyion to use the description and tile as parameters to suggest another movie.
def movie_selection(watched_movie_title, watched_movie_description):
    import spacy
    nlp = spacy.load("en_core_web_md")
    watched_movie_description = nlp(watched_movie_description)
    movie_list = []
    similarity_list = []
    with open('movies.txt','r') as movies:
        for lines in movies:
            lines = lines.split(":")
            movie_list.append(lines[0])         
            similarity_list.append(watched_movie_description.similarity(nlp(lines[1])))
        # Finding th ehighest similarity and match to the movie to be suggested.
        max_similarity = max(similarity_list)
        max_similarity_index = similarity_list.index(max_similarity) 
        matching_movie = movie_list[max_similarity_index]
        print(f"Since you watched {watched_movie_title}, you should enjoy watching {matching_movie}.")
# Testing the function use
watched_movie_title = "Planet Hulk"
watched_movie_description ='''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator'''

movie_selection(watched_movie_title,watched_movie_description)

