from collections import deque

maze = [
     "S..#.",
     "##.#.",
     ".....",
     ".####",
     "....G",

  ]
  
  
start = (0,0)
goal = (4,4)

q = deque([(start, [start])])
visited = {start}

while q:
	(r, c), path = q.popleft()
	
	if(r, c) == goal:
		for x, y in path:
			if maze[x][y] not in "SG":
				maze[x] = maze[x][:y] + "*" + maze[x][y+1:]
				
				print("path found!")z
				break
				
	for dr, dc in [(1, 0), (-1,0), (0,1), (0,-1)]:
		nr, nc = r + dr, c + dc
		
		if (0 <= nr < 5 and 0<= nc < 5 and 
			maze[nr][nc] != '#' and (nr, nc) not in visited):
			
			visited.add((nr, nc))
			q.append(((nr, nc), path + [(nr, nc)]))
