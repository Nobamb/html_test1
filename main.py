# 태그 값들 지정

tag_name = "h1"

angle_bracket = ["<", ">"]

content = "공욱재"


# 태그 조립

tag_jolib = angle_bracket[0] + tag_name + angle_bracket[1] + content + angle_bracket[0] + "/" + tag_name + angle_bracket[1]




result = tag_jolib

# 결과 출력
print(result)