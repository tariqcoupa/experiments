class CreateUserNames < ActiveRecord::Migration[5.0]
  def change
    create_table :admin_user do |t|
    	t.column "first_name", :string
    	t.column "last_name", :string
    	t.column "email", :string, :default => '', :null => false
    	t.string "password", :limit => 40
      t.timestamps
    end
  end
end
