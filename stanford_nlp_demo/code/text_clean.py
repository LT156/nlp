import re

sentence_spelling_dictionary = {
    'thewaytheshapeschangethespace': 'the way the shapes change the space',
    'brightcolorsandanimals': 'bright colors and animals',
    'calmweatherandpeopleworkingtogether': 'calm weather and people working together',
    'thesoftcolors': 'the soft colors',
    'itlookslikeapeacefullocation': 'it looks like a peaceful location',
    'Iliketoplayinthesnow': 'I like to play in the snow',
    'thecalmwaters': 'the calm waters',
    'itseemsincompletesomehow': 'it seems incomplete somehow',
    'thefiguresseemsomehowawkward': 'the figures seem somehow awkward',
    'thegreenandlackofpeople': 'the green and lack of people',
    'boatingisanadventure': 'boating is an adventure',
    'thereseemstobetoomuchsky': 'there seems to be too much sky',
    'onthewholeitlookslikeawallpaperswatch': 'on the whole it looks like a wallpapers watch',
    'thecolorofthewater': 'the color of the water',
    'alloftheplantsandthewatershowingthroughthem': 'all of the plants and the water showing through them',
    'thecolorcombination': 'the color combination',
    'theslashesacrosstheworkandthedarkcolors': 'the slashes across the work and the dark colors',
    'thesimplicityandopenness': 'the simplicity and openness',
    'theproportionbetweenheadandbody': 'the proportion between head and body',
    'thebrightcolorsandthefeelingofmotion': 'the bright colors and the feeling of motion',
    'thedetailinthehands': 'the detail in the hands',
    'thelengthofthewoman\'sneck': 'the length of the woman\'s neck',
    'thedifferentflocksofbirdsinthesky': 'the different flocks of birds in the sky',
    'theskillshownindrawingthefigures': 'the skill shown in drawing the figures',
    'thenaturallookingskintone': 'the natural looking skin tone',
    'theyeadsthatdon\'tseemtobeattatchedtoanything': 'the yeads that don\'t seem to be attatched to anything',
    'themasksheisholding': 'the mask she is holding',
    'theapparantageofthepiece': 'the apparent age of the piece',
    'thepinkbows': 'the pink bows',
    'theintensityonthefaceofthemaninfrontofthewoman.': 'the intensity on the face of the man in front of the woman',
    'theshapesandcolors-itlookshard,painful':  'the shapes and colors - it looks hard, painful',
    'thewaytheguitarisbrokenupandmagnifiedbutstillidentifiable.': 'the way the guitar is broken up and magnified but still identifiable',
    'veryimpressedwiththewaytheartistcreatedlight': 'very impressed with the way the artist created light',
    'itlookslikepeoplearewaitingforsomeeventtohappenlikeaboatraceorsomething': 'it looks like people are waiting for some event to happen like a boat race or something',
    'wonderingifthisisapaintingoratextile': 'wondering if this is a painting or a textile',
    'itseemstoodarkfortheactivity': 'it seems too dark for the activity',
    'Ithinkitskindofweirdhowherhipsmakealmostacircle': 'I think its kind of weird how her hips make almost a circle',
    'thesoftnessofthefiguremakesitfeellikeiamintrudingonanintimatemoment': 'the softness of the figure makes it feel like i am intruding on an intimate moment',
    'Idon\'tseepieceslikethisas\'art\'itcouldbethewallinsomeone\'shouse': 'I don\'t see pieces like this as \'art\' it could be the wall in someone\'s house',
    'thereflectionofthetreesinthepool': 'the reflection of the trees in the pool',
    'thepainonhisface': 'the pain on his face',
    'itremindsmeofastringofbeadsasmallchildwouldmake': 'it reminds me of a string of beads a small child would make',
    'thefigurebeneaththetreeappearsveryrelaxed': 'the figure beneath the tree appears very relaxed',
    'thefacialexpressionisveryloving': 'the facial expression is very loving',
    'thecolorsandactivitymakeitlooklikeafunplacetobe': 'the colors and activity make it look like a fun place to be',
    'itlookslikeaniceareatogoforawalk': 'it looks like an ice area to go for a walk',
    'theyappeartobeayoungcoupleinlove': 'they appear to be a young couple in love',
    'allofthelittledetailsareamazing': 'all of the little details are amazing',
    'knowledgeofthehistoryassociatedwiththeperson': 'knowledge of the history associated with the person',
    'itlookslikeaveryoldpaintedtextile': 'it looks like a very old painted textile',
    'allofthebrightcolorsjustmakemehappy': 'all of the bright colors just make me happy',
    'dificultysortingoutwhetherthefigureismaleorfemale': 'dificulty sorting out whether the figure is male or female',
    'Itseemskindoflikeaposteryou\'dputinaclassroom.': 'It seems kind of like a poster you\'d put in a classroom',
    'Theexpressionontheman\'sfaceappearsangry.': 'The expression on the man\'s face appears angry.',
    'it\'d dark and creepy and weirdly sexual in a bad way.': 'it\'s dark and creepy and weirdly sexual in a bad way.',
    'looks disgusting looks like a cross desser disgusting': 'looks disgusting looks like a cross dresser disgusting',
    'Big skirts and bloomers on dancing ladies definitelymake the mood excitement.': 'big skirts and bloomers on dancing ladies definitely make an exciting mood',
    'The rays eminntating from sum over the town os exhilarating': 'the rays emanating from sun over the town are exhilarating',
    'the way the artist uses black and white really gives this a different feel tp the painting': 'the way the artist uses black and white really gives this a different feel to the painting',
    'This reminds me of jumbled graffiti I saw and had tp clean up every once in a while when I was younger': 'This reminds me of jumbled graffiti I saw and had to clean up every once in a while when I was younger',
    'looks like the cabins i stayed in on my trip tp a dude ranch': 'looks like the cabins i stayed in on my trip to a dude ranch',
    'A young woman applies make-up tp her face as she sits in a pretty robe. A pleasant but unfished work of art.': 'A young woman applies make-up to her face as she sits in a pretty robe. A pleasant but unfinished work of art.',
    'old and not kept up well, bug nice scene of a man at work': 'old and not kept up well, but nice scene of a man at work',
    'Again this painting is dill its lifeless and no color.': 'Again this painting is dull, it is lifeless and has no color.',
    'she smile smartly': 'she smiles smartly',
    'The mountain makes me think of a strong safehold, and a feeling of shelter.': 'The mountain makes me think of a stronghold giving me a feeling of shelter',
    'The detail in the surundsing like the clock tower and statue make it more inspiering': 'The detail in the surroundings like the clock tower and statue make it more inspiring',
    'The man is chained down and left to be attacked by a bird of prey while another man non chalantly watches what is taking place.': 'The man is chained down and left to be attacked by a bird of prey while another man nonchalantly watches what is taking place.',
    'This is a beautiful scene with the mosques in the background and the vegetation in the front.': 'This is a beautiful scene with the onion dome churches in the background and the vegetation in the front.',
    'The colors make me feel like I\'m looking at someone important. I feel a since of awe over them because of their attire.': 'The colors make me feel like I\'m looking at someone important. I feel a sense of awe over them because of their attire.',
    'the detective ihas found the diar everyone knew she kept and now hopefully he wi findout what led up to her breakdown ': 'the detective has found the diary everyone knew she kept and now hopefully he will find out what led up to her breakdown',
    'The VanGoghishness of this makes me smile and wonder how they do it.': 'The Van Gogh like quality of this makes me smile and wonder how they do it.',
    'The colors and shapes compliment each otherakes look like a adult childs painting.': 'The colors and shapes compliment each other and looks like an adult child\'s painting.',
    'I prefer more realistic still ifes.': 'I prefer more realistic still lifes.'
}

def manual_sentence_spelling(x, spelling_dictionary):
    """
    Applies spelling on an entire string, if x is a key of the spelling_dictionary.
    :param x: (string) sentence to potentially be corrected
    :param spelling_dictionary: correction map
    :return: the sentence corrected
    """
    if x in spelling_dictionary:
        return spelling_dictionary[x]
    else:
        return x

QUOTES_RE_STR = r"""(?:['|"][\w]+['|"])"""    # Words encapsulated in apostrophes.
QUOTES_RE = re.compile(r"(%s)" % QUOTES_RE_STR, flags=re.VERBOSE | re.IGNORECASE | re.UNICODE)
def unquote_words(s):
    """ 'king' - > king, "queen" -> queen """
    iterator = QUOTES_RE.finditer(s)
    new_sentence = list(s)
    for match in iterator:
        start, end = match.span()
        new_sentence[start] = ' '
        new_sentence[end-1] = ' '
    new_sentence = "".join(new_sentence)
    return new_sentence

contractions_dict = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "i'd": "I had",
    "i'd've": "I would have",
    "i'll": "I will",
    "i'll've": "I will have",
    "i'm": "I am",
    "i've": "I have",
    "isn't": "is not",
    "it'd": "it had",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "iit will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she had",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "that'd": "that had",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there had",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they had",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have",
    "do'nt": "do not",
    "does\'nt": "does not"
}

CONTRACTION_RE = re.compile('({})'.format('|'.join(contractions_dict.keys())),
                            flags=re.IGNORECASE | re.DOTALL)

def expand_contractions(text, contractions=None, lower_i=True):
    """ Expand the contractions of the text (if any).
    Example: You're a good father. -> you are a good father.
    :param text: (string)
    :param contractions: (dict)
    :param lower_i: boolean, if True (I'm -> 'i am' not 'I am')
    :return: (string)

    Note:
        Side-effect: lower-casing. E.g., You're -> you are.
    """
    if contractions is None:
        contractions = contractions_dict  # Use one define in this .py

    def expand_match(contraction):
        match = contraction.group(0)
        expanded_contraction = contractions.get(match)
        if expanded_contraction is None:
            expanded_contraction = contractions.get(match.lower())
        if lower_i:
            expanded_contraction = expanded_contraction.lower()
        return expanded_contraction

    expanded_text = CONTRACTION_RE.sub(expand_match, text)
    return expanded_text

def artemis_text_clean(text):
    text = manual_sentence_spelling(text, sentence_spelling_dictionary)
    text = unquote_words(text)
    text = expand_contractions(text)
    basic_punct = '/\-~*_=[–]{}$^@|%#<—>'#.?!,:;
    punct_to_space = str.maketrans(basic_punct, ' ' * len(basic_punct))  # map punctuation to space
    clean_text = text.translate(punct_to_space)
    return clean_text
 
text_raw = "When looking at this woman I am filled with curiosity about what she is thinking about with her elbow on the table."
print(artemis_text_clean(text_raw))