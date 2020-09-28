from enum import Enum 


class Page(Enum):
    pg1 = "login_intro1"
    pg2 = "login_intro2"
    pg3 = "login_intro3"
    pg4 = "login_options"
    pg5 = "login_with_number"
    pg6 = "login_otp_verify"
    pg7 = "login_otp_error"
    pg8 = "location"


class ResponseStruct(Enum):
    id = "ph"
    type = "type"
    val = "value"


class Type(Enum):
    ty1 = "heading"
    ty2 = "text"
    ty3 = "textInput"
    ty4 = "button"
    ty5 = "link"

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


class Heading(Enum):
    hd1 = "Bond for Happiness"
    hd2 = "Find your right partner"
    hd3 = "Engage in endless conversations"
    hd4 = "Meet & Date"
    hd5 = "Get started"
    hd6 = "Enter OTP"
    hd7 = "Login with others"
    hd8 = "Your OTP retry has been exhausted."

class Text(Enum):
    tx1 = "By continuing you agree to our Terms and Privacy policy"
    tx2 = "Made in India"
    tx3 = "Enter your mobile number and we will send an OTP to continue"
    tx4 = "+91"
    tx5 = "OR"
    tx6 = "Please Enter the 6 digit OTP we have sent on mobile number"
    tx7 = "Didn't receive the code? Resend OTP in 20s"
    tx8 = "Please login using other options"
    tx9 = "Enable location to start exploring people around you"
    tx10 = "We access your loaction to show potential matches near you. To learn more, check our Privacy Policy"


class TextInput(Enum):
    ti1 = "Enter mobile number"


class Button(Enum):
    bt1 = "Sign in using facebook"
    bt2 = "Sign in with Apple"
    bt3 = "Sign in with facebook"
    bt4 = "Sign in with Instagram"
    bt5 = "Sign in with Google"
    bt6 = "Enable location"


class Link(Enum):
    ln1 = "Other sign in options"


