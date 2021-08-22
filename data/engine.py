

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




