class Page < ApplicationRecord
	
	belongs_to :subject
	has_and_belongs_to_many :user_names
	has_many :sections
end
