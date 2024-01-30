# 0x06-regular_expressions

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //

(# !/usr/bin/env ruby)
puts ARGV[0].scan(/127.0.0.[0-9]/).join

[0-9] means any digit from 0 to 9.


1. [simply match "school"](0-simply_match_school.rb)

2. [Regexp contains 2-5 "t" between hn](1-repetition_token_0.rb)
<img src="./assets/Screenshot from 2024-01-30 13-10-05.png">