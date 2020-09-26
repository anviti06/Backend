from .constant import (
    Page, ResponseStruct, Type, Id, Heading, 
    Text, TextBox, MultiSelect, Button, 
    Switch, Link, Dropdown
)

def response_profile_basic(s):
    if(s == Page.pg1.value):
        return [
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value : Heading.hd1.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value : Heading.hd2.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value : TextBox.tb1.value,     ResponseStruct.type.value : Type.ty3.value} , 
            { ResponseStruct.id.value : Id.id4.value, ResponseStruct.val.value : TextBox.tb2.value,     ResponseStruct.type.value : Type.ty3.value} , 
            { ResponseStruct.id.value : Id.id5.value, ResponseStruct.val.value : MultiSelect.ms1.value, ResponseStruct.type.value : Type.ty6.value} , 
            { ResponseStruct.id.value : Id.id6.value, ResponseStruct.val.value : MultiSelect.ms2.value, ResponseStruct.type.value : Type.ty6.value} , 
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value : Button.bt1.value,      ResponseStruct.type.value : Type.ty4.value} 
        ]

def response_profile_advanced(s):
    if(s == Page.pg2.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd1.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Heading.hd3.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : TextBox.tb3.value,     ResponseStruct.type.value : Type.ty3.value} , 
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : Dropdown.dd1.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id5.value,   ResponseStruct.val.value : MultiSelect.ms3.value, ResponseStruct.type.value : Type.ty6.value} , 
            { ResponseStruct.id.value : Id.id6.value,   ResponseStruct.val.value : MultiSelect.ms4.value, ResponseStruct.type.value : Type.ty6.value} , 
            { ResponseStruct.id.value : Id.id7.value,   ResponseStruct.val.value : Dropdown.dd2.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id8.value,   ResponseStruct.val.value : Dropdown.dd3.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id9.value,   ResponseStruct.val.value : Dropdown.dd4.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id10.value,  ResponseStruct.val.value : Dropdown.dd5.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id11.value,  ResponseStruct.val.value : Dropdown.dd6.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id12.value,  ResponseStruct.val.value : Switch.s1.value,       ResponseStruct.type.value : Type.ty8.value} , 
            { ResponseStruct.id.value : Id.id13.value,  ResponseStruct.val.value : Switch.s2.value,       ResponseStruct.type.value : Type.ty8.value} , 
            { ResponseStruct.id.value : Id.id14.value,  ResponseStruct.val.value : Switch.s3.value,       ResponseStruct.type.value : Type.ty8.value} , 
            { ResponseStruct.id.value : Id.id15.value,  ResponseStruct.val.value : Button.bt2.value,      ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id15.value,  ResponseStruct.val.value : Link.l1.value,         ResponseStruct.type.value : Type.ty5.value}  

        ]


def response_manage_photos(s):
    if(s == Page.pg3.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd4.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Text.tx2.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Button.bt3.value,      ResponseStruct.type.value : Type.ty4.value}             
        ]


def response_select_source(s):
    if(s == Page.pg4.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Link.l2.value,         ResponseStruct.type.value : Type.ty5.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Link.l3.value,         ResponseStruct.type.value : Type.ty5.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Link.l4.value,         ResponseStruct.type.value : Type.ty5.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : Link.l5.value,         ResponseStruct.type.value : Type.ty5.value}    
        ]

def response_about_you(s):
    if(s == Page.pg5.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : MultiSelect.ms5.value, ResponseStruct.type.value : Type.ty6.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : MultiSelect.ms6.value, ResponseStruct.type.value : Type.ty6.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : MultiSelect.ms7.value, ResponseStruct.type.value : Type.ty6.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : MultiSelect.ms8.value, ResponseStruct.type.value : Type.ty6.value} ,    
            { ResponseStruct.id.value : Id.id5.value,   ResponseStruct.val.value : MultiSelect.ms9.value, ResponseStruct.type.value : Type.ty6.value} ,
            { ResponseStruct.id.value : Id.id6.value,   ResponseStruct.val.value : MultiSelect.ms10.value, ResponseStruct.type.value : Type.ty6.value},    
            { ResponseStruct.id.value : Id.id15.value,  ResponseStruct.val.value : Button.bt3.value,      ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id15.value,  ResponseStruct.val.value : Link.l1.value,         ResponseStruct.type.value : Type.ty5.value}  
        
        ]