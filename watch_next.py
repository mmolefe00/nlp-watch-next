import spacy
nlp = spacy.load('en_core_web_md')

# === FUNCTIONS === #

# read movies.txt file and return dictionary of movies
def read_movies():

    # read movie file
    with open("movies.txt", "r") as file:
        # create empty movie dictionary
        m_dictionary = {}

        # read  file lines
        lines = file.readlines()

        for line in lines:
            # separate line into two parts: title and description
            parts = line.strip("\n").split(" :")

            if len(parts) == 2:
                m_title = parts[0].strip()
                m_desc = parts[1].strip()

                # append to movie dictionary
                m_dictionary[m_title] = m_desc

    # return movie list
    return m_dictionary


# use convert dictionary values to nlp and compare similarity to Hulk Description
# then return the most similar movie title.
def compare_movies(movies):
    max_similarity = 0  # start at 0 (no similarity) so that it keeps updating with the next greatest similarity

    watch_next = ""

    description_to_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
    the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

    # convert hulk description
    comp_desc = nlp(description_to_compare)

    # iterate through dictionary
    for title, description in movies.items():
        # convert dictionary description to nlp
        doc = nlp(description)

        # now compare comp_desc to doc
        similarity = comp_desc.similarity(doc)


        # print(f'{title} - {similarity}')  # -- view each title with its respective similarity


        if similarity > max_similarity:     # if calculated similarity is bigger than max similarity
            max_similarity = similarity     # update the max similarity
            watch_next = title              # update the watch_next title

            # this updates with each iteration so the outputted title is the most similar.

    return watch_next       # return most similar title


# === PROCESSING === #

# give variable to returned 'read_movies' dictionary
movie_dict = read_movies()

# run dictionary through compare_movies function and assign variable 'next_watch'
next_watch = compare_movies(movie_dict)

# assign variable to 'next_watch' movie description
nw_desc = movie_dict[next_watch]

# === OUTPUT === #
# output suggestion title as well as formatted description using dictionary
greeting = "\nWelcome to Stream Streaks! \nFor a world-class curated viewing experience...\n"

prompt = f"""Looking for more? We've got you! ;) 
Since you enjoyed 'Planet Hulk', we think you'd like:

\tTITLE: {next_watch.title()}
\tDescription: {nw_desc}

<< CLICK HERE >> to watch now!"""

# print output
print(greeting)
print(prompt)
