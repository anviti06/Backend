from enum import Enum 


class Page(Enum):
    pg1 = "advance_filter"
    pg2 = "filters"
    pg3 = "become_elite_member"

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
    id17 = "ph17"
    id18 = "ph18"
    

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
    ty8 = "switch_type1"
    ty9 = "slide_bar"
    ty10= "switch_type2"

class Heading(Enum):
    hd1 = "Advance Filters"
    hd2 = "Filters"
    hd3 = "Become Elite Member"
    

class Text(Enum):
    tx1 = "Check your elite eligibility now or upgrade your account & unlock interesting features that are designed only for you."
    tx2 = "Connect"
    tx3 = "Send instant chat message without a match"
    tx4 = "Elite"
    tx5 = "Feature in the elite category & select elite people"
    tx6 = "Free"
    tx7 = "No upgrade required"
    
class TextBox(Enum):
    tb1 = {ResponseStruct.title.value : "Crossover" ,      ResponseStruct.desc.value : "Those hwo have crossed your paths"}


class Dropdown(Enum):
    dd1 = {ResponseStruct.title.value : "Height" ,        ResponseStruct.desc.value : "Min: 0'0", ResponseStruct.min_max_range.value : ['120' , '200', 'cm']}
    dd2 = {ResponseStruct.title.value : "" ,              ResponseStruct.desc.value : "Max: 0'0", ResponseStruct.min_max_range.value : ['120' , '200', 'cm']}
    dd3 = {ResponseStruct.title.value : "Marital Status", ResponseStruct.desc.value : "Select",   ResponseStruct.multival.value : ['Separated' , 'Married']}
    dd4 = {ResponseStruct.title.value : "Religion",       ResponseStruct.desc.value : "Select",   ResponseStruct.multival.value : ['' , '']}
    dd5 = {ResponseStruct.title.value : "Occupation",     ResponseStruct.desc.value : "Select",   ResponseStruct.multival.value : ['', '' ]}
    

class Switch_type1(Enum):
    s1 = {ResponseStruct.title.value : "" ,     ResponseStruct.switch.value : ['On' , 'off']}
    s5 = {ResponseStruct.title.value : "Hide Social Media Friends" ,   ResponseStruct.switch.value : ['Show' , 'Hide']}


class Switch_type2(Enum):
    s2 = {ResponseStruct.title.value : "Drink?",ResponseStruct.switch.value : ['Yes' , 'No'], ResponseStruct.desc.value : "Does it matter if the other person drinks?"}
    s3 = {ResponseStruct.title.value : "Smoke?",ResponseStruct.switch.value : ['Yes' , 'No'], ResponseStruct.desc.value : "Does it matter if the other person smokes?"}
    s4 = {ResponseStruct.title.value : "Like Pets?",ResponseStruct.switch.value : ['Yes' , 'No'], ResponseStruct.desc.value : "Does it matter if the other person pets?"}
    

class SlideBar(Enum):
    sb1 = {ResponseStruct.title.value : "Age" , ResponseStruct.range.value : ['22' , '32' , 'Yrs']}    
    sb2 = {ResponseStruct.title.value : "Distance" , ResponseStruct.range.value : ['Nearby' , '3' , 'Kms']}    
    

class MultiSelect(Enum):
    ms1 = {ResponseStruct.title.value : "I'm interested in " ,                        ResponseStruct.multival.value : ['Men', 'Women', 'More' : {'Agender', 'Androgyne', 'Androgynuous'}] }
    ms2 = {ResponseStruct.title.value : "Political View" ,                            ResponseStruct.multival.value : ['Apolitical', 'Moderate', 'Liberal' , 'Conservative'] }
    ms3 = {ResponseStruct.title.value : "Body Type" ,                                 ResponseStruct.multival.value : ['Athletic', 'Slim', 'Moderate'] }
    

class Button(Enum):
    bt1 = "Next"
    bt2 = "Save changes"
    bt3 = "Save"
    bt4 = "Subscribe"
    bt5 = "Check Eligibility"

class Link(Enum):
    l1 = "SKIP"
    l2 = "Take photo"
    l3 = "Select from Gallery"
    l4 = "Select from Instagram"
    l5 = "Select from Facebook"
    l6 = "Set advance features"    

