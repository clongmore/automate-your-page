def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>'''
  
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', 
            next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
     
TEST_TEXT = """TITLE: Structured Data
DESCRIPTION: Structured data includes Strings and Lists. 
A string is a sequence of characters such as S = 'yabba!' 
A list, however, is a sequence of anything. For example: p=['y','a','b','c','!']. 
A nested list is a list within a list. It can be strings, or numbers, or both. 
Nested lists can be two lines but you have to be sure to separate the lines 
after a comma so that the interpreter will know it is one list and not two. 
The first element of a nested list starts at 0. 
TITLE:  Mutability
DESCRIPTION:  Lists support mutation. Mutation means we can change the value of a 
list after we have created it.   
TITLE: Aliasing
DESCRIPTION: Aliasing is when we have two different ways to refer to the same object. 
If we have two variable names that refer to the same object, any changes we make 
to one of the objects that the variable refers to will also affect the value 
of the object that the second variable refers to. 
TITLE:  The Difference Between Append and Plus (+)
DESCRIPTION:  Append is another List Operation. It is a method similar to the 
find procedure. It is mutating the old list and adding a new element object 
to the end of a list. This adding is not the arithmetic plus (+). This adding 
can actually be rlated to affixing because we are affixing an element at 
the end of a list to store complex data. 
Len is another List Operation that is short for length. """

def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html
  

print generate_all_html(TEST_TEXT)
