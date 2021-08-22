

def apple_collision(self):
		collision = False
		center = [16, 16]
		apple_center_pos = (self.apple.x + center[0], self.apple.y + center[1])
		box_pos = (self.box.x[0]+center[0], self.box.y[0] + center[1])

		if box_pos[0] == apple_center_pos[0] and box_pos[1] == apple_center_pos[1]:
			collision = True
			print('Collision') 

		return collision

def wall_collision(self, window_size):
	collision = False
	box_pos = (self.box.x[0], self.box.y[0])

	if box_pos[0] < 0 or box_pos[0] >= window_size[0]:
		print('wall collision')
		collision = True

	if box_pos[1] < 0 or box_pos[1] >= window_size[1]:
		print('wall collision')
		collision = True

	return collision

def self_collision(self):
	collision = False
	center = [16, 16]
	head_centre = (self.box.x[0] + center[0] , self.box.y[0] + center[1])
	for i in range(2, len(self.box.x)):
		current_box_centre = (self.box.x[i] + center[0], self.box.y[i] + center[1])
		
		if(head_centre[0] == current_box_centre[0] and head_centre[1] == current_box_centre[1]):
			collision = True
			print('Self Collision')
			break
	return collision






