class Thing 
	attr_accessor :name
	A = 10
end

class Animal < Thing
	def initialize name
		@name = name
	end
end

a = Animal.new 'cat'
puts a.inspect

class X 
	A = 10
	class Y

	end
end

puts X::A