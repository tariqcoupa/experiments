#!/usr/bin/ruby

class Thing
	def initialize(name, description)
		@name = name
		@description = description
	end

	def getName
		return @name
	end
	
	def setName(name)
		@name = name
	end

	def getDescription
		return @description
	end

	def setDescription(description)
		@description = description
	end
end

class Treasure < Thing
	def initialize(name, description, value)
		super(name, description)
		@value = value
	end

	def getValue
		return @value
	end

	def setValue(value)
		@value = value
	end
end

t = Thing.new("tariq", "is an amazing man", "Awesome")
t.setName("Tariq")
t.setDescription("is wonderful")
t.setValue("Awesome")

puts t.getValue
puts t.getName
