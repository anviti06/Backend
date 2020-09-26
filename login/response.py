from .constant import Text, Heading, Button, Link, Page, Type, Id, ResponseStruct, TextInput

def response_login_intro(s):
    if(s == Page.pg1.value):
        return [
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value : Heading.hd1.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value : Heading.hd2.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value  : Button.bt1.value, ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id4.value, ResponseStruct.val.value  : Link.ln1.value,   ResponseStruct.type.value : Type.ty5.value} , 
            { ResponseStruct.id.value : Id.id5.value, ResponseStruct.val.value  : Text.tx1.value,   ResponseStruct.type.value : Type.ty2.value} 
        ]
    elif (s == Page.pg2.value):
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value : Heading.hd1.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value : Heading.hd3.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value  : Button.bt1.value, ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id4.value, ResponseStruct.val.value  : Link.ln1.value,   ResponseStruct.type.value : Type.ty5.value} , 
            { ResponseStruct.id.value : Id.id5.value, ResponseStruct.val.value  : Text.tx1.value,   ResponseStruct.type.value : Type.ty2.value} 
        ]
    elif (s == Page.pg3.value):
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value : Heading.hd1.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value : Heading.hd4.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value  : Button.bt1.value, ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id4.value, ResponseStruct.val.value  : Link.ln1.value,   ResponseStruct.type.value : Type.ty5.value} , 
            { ResponseStruct.id.value : Id.id5.value, ResponseStruct.val.value  : Text.tx1.value,   ResponseStruct.type.value : Type.ty2.value} 
        ]

def response_login_options(s):
    if(s == Page.pg4.value):
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value  : Heading.hd5.value,    ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value  : Text.tx3.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value  : Text.tx4.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value, ResponseStruct.val.value  : TextInput.ti1.value,  ResponseStruct.type.value : Type.ty3.value} ,
            { ResponseStruct.id.value : Id.id5.value, ResponseStruct.val.value  : Text.tx5.value,       ResponseStruct.type.value : Type.ty2.value} , 
            { ResponseStruct.id.value : Id.id6.value, ResponseStruct.val.value  : Button.bt2.value,     ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id7.value, ResponseStruct.val.value  : Button.bt4.value,     ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id8.value, ResponseStruct.val.value  : Button.bt3.value,     ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id9.value, ResponseStruct.val.value  : Button.bt5.value,     ResponseStruct.type.value : Type.ty4.value}              
        ]

def response_login_with_num(s):
    if(s == Page.pg5.value):
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value  : Heading.hd5.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value  : Text.tx3.value,    ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value  : Text.tx4.value,    ResponseStruct.type.value : Type.ty2.value} ,
        ]

def response_login_otp_verify(s):
    if(s == Page.pg6.value):
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value  : Heading.hd6.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value  : Text.tx6.value,    ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value  : Text.tx7.value,    ResponseStruct.type.value : Type.ty2.value} ,
        ]

def response_login_otp_error(s):
    if(s == Page.pg7.value):
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value  : Heading.hd7.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value  : Heading.hd8.value, ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value  : Text.tx8.value,    ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value, ResponseStruct.val.value  : Button.bt2.value,  ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id5.value, ResponseStruct.val.value  : Button.bt4.value,  ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id6.value, ResponseStruct.val.value  : Button.bt3.value,  ResponseStruct.type.value : Type.ty4.value}              
        ]


def response_login_location(s):
    if(s == Page.pg8.value):
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value  : Text.tx9.value,    ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value  : Button.bt6.value,  ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value  : Text.tx10.value,    ResponseStruct.type.value : Type.ty2.value} ,
        ]
