#로그인 애플리케이션에 입력 기능 추가하기
puts("아이디를 입력해주세요")
input = gets.chomp()
real_egoing = "11"
real_k8805 = "ab"
if real_egoing == input
  puts("Hello!, egoing")
elsif real_k8805 == input
  puts("Hello!, k8805")
else
  puts("Who are you?")
end
