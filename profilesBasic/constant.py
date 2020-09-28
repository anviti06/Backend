from enum import Enum 


class Page(Enum):
    pg1 = "complete_profile_basic"
    pg2 = "complete_profile_advanced"
    pg3 = "manage_photos"
    pg4 = "select_source"
    pg5 = "tell_us_about_you"

class ResponseStruct(Enum):
    id = "ph"
    type = "type"
    val = "value"
    multival = "multipleValue"
    title = "title"
    desc = "description"
    switch = "switch"
    min_max_range = "range"
    

class Type(Enum):
    ty1 = "heading"
    ty2 = "text"
    ty3 = "textBox"
    ty4 = "button"
    ty5 = "link"
    ty6 = "multi_select"
    ty7 = "dropdown"
    ty8 = "switch"


class Id(Enum):
    id1 = "ph1"
    id2 = "ph2"
    id3 = "ph3"
    id4 = "ph4"
    id5 = "ph5"
    id6 = "ph6"
    id7 = "ph7"
    id8 = "ph8"
    id9 = "ph9"
    id10 = "ph10"
    id11 = "ph11"
    id12 = "ph12"
    id13 = "ph13"
    id14 = "ph14"
    id15 = "ph15"
    id16 = "ph16"

class Heading(Enum):
    hd1 = "Complete Profile"
    hd2 = "Enter your basic info"
    hd3 = "Enter your advanced info"
    hd4 = "Manage Photos"

class Text(Enum):
    tx1 = "By continuing you agree to our Terms and Privacy policy"
    tx2 = "*You need to uload atleast 1 photo"

class TextBox(Enum):
    tb1 = {ResponseStruct.title.value : "Name" ,      ResponseStruct.desc.value : "What's your name?"}
    tb2 = {ResponseStruct.title.value : "Age" ,       ResponseStruct.desc.value : "When were you born?"}
    tb3 = {ResponseStruct.title.value : "Philosofy" , ResponseStruct.desc.value : "Describe your story in 80 caracters. Be crispy, choosy or classy"}
    

class Dropdown(Enum):
    #contains both range and multival attributes
    dd1 = {ResponseStruct.title.value : "Height" ,        ResponseStruct.desc.value : "Select", ResponseStruct.min_max_range.value : ['120' , '190', 'cm'] }
    dd2 = {ResponseStruct.title.value : "Complexion",     ResponseStruct.desc.value : "Select", ResponseStruct.multival.value : ['Fair']}
    dd3 = {ResponseStruct.title.value : "Diet" ,          ResponseStruct.desc.value : "Select", ResponseStruct.multival.value : ['']}
    dd4 = {ResponseStruct.title.value : "Marital status" ,ResponseStruct.desc.value : "Select", ResponseStruct.multival.value : ['Single' , 'Married', 'Separated']}
    dd5 = {ResponseStruct.title.value : "Religion" ,      ResponseStruct.desc.value : "Select", ResponseStruct.multival.value : ['Hindu', 'Sikh']}
    dd6 = {ResponseStruct.title.value : "Occupation" ,    ResponseStruct.desc.value : "Select", ResponseStruct.multival.value : ['Self-Employment', 'Doctor']}

class Switch(Enum):
    s1 = {ResponseStruct.title.value : "Do you drink?" ,     ResponseStruct.switch.value : ['Yes' , 'No']}
    s2 = {ResponseStruct.title.value : "Do you smoke?" ,     ResponseStruct.switch.value : ['Yes' , 'No']}
    s3 = {ResponseStruct.title.value : "Do you like pets?" , ResponseStruct.switch.value : ['Yes' , 'No']}


class MultiSelect(Enum):
    ms1 = {ResponseStruct.title.value : "Name" ,                        ResponseStruct.multival.value : ['Men', 'Women', 'More'] }
    ms2 = {ResponseStruct.title.value : "What are you looking for?" ,   ResponseStruct.multival.value : ['Friend', 'Fling', 'Date'] }
    ms3 = {ResponseStruct.title.value : "What is your political view" , ResponseStruct.multival.value : ['Apolitical', 'Moderate', 'Liberal', 'Conservative'] }
    ms4 = {ResponseStruct.title.value : "Body Type" ,                   ResponseStruct.multival.value : ['Athletic', 'Slim', 'Moderate'] }
    ms5 = {ResponseStruct.title.value : "" ,                            ResponseStruct.multival.value : ['Early Bird', 'Night Owl']},
    ms6 = {ResponseStruct.title.value : "" ,                            ResponseStruct.multival.value : ['Optimistic', 'Realistic'] },
    ms7 = {ResponseStruct.title.value : "" ,                            ResponseStruct.multival.value : ['Introvert', 'Extrovert', ] },
    ms8 = {ResponseStruct.title.value : "" ,                            ResponseStruct.multival.value : ['Quite', 'Loud'] },
    ms9 = {ResponseStruct.title.value : "" ,                            ResponseStruct.multival.value : ['Planner', 'Spontaneour'] },
    ms10 ={ResponseStruct.title.value : "" ,                            ResponseStruct.multival.value : ['Always late', 'Always early'] }


class Button(Enum):
    bt1 = "Next"
    bt2 = "Save changes"
    bt3 = "Save"

class Link(Enum):
    l1 = "SKIP"
    l2 = "Take photo"
    l3 = "Select from Gallery"
    l4 = "Select from Instagram"
    l5 = "Select from Facebook"
    

