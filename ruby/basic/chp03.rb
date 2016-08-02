# class Thing 
# 	def initialize(aa, bb)
# 		@name = aa
# 		@b = bb
# 	end

# 	attr_accessor :name
# end

# class A < Thing 
# 	def initialize(aa, bb) 
# 		super aa,'18'
# 	end
# end

# a = A.new 'Howard', '34'
# puts a.inspect

# s4 = 'abcdefghijklmn'

# puts s4
# puts s4[2..4]

# s = gets() # Had we but world enough and time...
# s = s.chomp
# print s + '.'

# a = (1..10)
# b = (-10..-1)
# c = (-10..10)
# d = ('a'..'z')
# e = ('a'...'z')
# str_range = ('abc'..'def')

# for i in a do
# 	puts i
# end

hdoc1 = <<EOF
I want to do it.
	I want to do it again.
		I want to finish it. #{"cloud".upcase}
		Alright, I'm done
EOF

puts hdoc1