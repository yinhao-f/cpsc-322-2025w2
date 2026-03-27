# Sample solution:

connected_to(laser,door) <- circuit_ok(c1).
connected_to(window,laser) <- circuit_ok(c2).
connected_to(door,power).
live(X) <- connected_to(X,Y) & live(Y).
live(power).
circuit_ok(c1).
circuit_ok(c2).
triggered(window) <- window_broken(window) & live(window).
triggered(door) <- door_open(door) & live(door).
triggered(laser) <- laser_interrupted(laser) & live(laser).
alarm_triggered(M) <- system(M) & hasSensor(M,X) & triggered(X).
system(s).
hasSensor(s,laser).
hasSensor(s,window).
hasSensor(s,door).