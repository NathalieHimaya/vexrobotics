def when_started1():
    while True:
        drivetrain.drive(FORWARD)
        if front_distance.found_object():
            drivetrain.stop()

vr_thread(when_started1)