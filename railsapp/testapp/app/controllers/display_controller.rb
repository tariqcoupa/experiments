class DisplayController < ApplicationController


	def index	
		render('index')
	end

	def show
		@array = [1,2,3,4,5,6]
		@id = params['id']
		@page = params['page']
		render('show')
	end

	def other_show
		redirect_to(:action => 'index')
	end
end
